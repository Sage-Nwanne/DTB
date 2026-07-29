function redirectTo(request, path, params = {}) {
  const url = new URL(path, request.url);

  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== null && value !== "") {
      url.searchParams.set(key, value);
    }
  }

  return Response.redirect(url.toString(), 303);
}

async function readForm(request) {
  const contentType = request.headers.get("content-type") || "";

  if (contentType.includes("application/json")) {
    return await request.json();
  }

  const formData = await request.formData();
  return Object.fromEntries(formData.entries());
}

function clean(value) {
  return String(value || "").trim();
}

function isValidEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

function looksAutomated(body) {
  const honeypot = clean(body.website);
  const startedAt = Number(body.started_at);

  if (honeypot) return true;
  if (Number.isFinite(startedAt) && Date.now() - startedAt < 1200) return true;
  return false;
}

function normalizePath(pathname) {
  if (!pathname || pathname === "/") {
    return "/";
  }

  return pathname.replace(/\/+$/, "");
}

async function handleContact(request, env) {
  try {
    const body = await readForm(request);

    const name = clean(body.name);
    const email = clean(body.email);
    const company = clean(body.company);
    const phone = clean(body.phone);
    const service = clean(body.service);
    const budget = clean(body.budget);
    const timeline = clean(body.timeline);
    const message = clean(body.message);

    if (looksAutomated(body)) {
      return redirectTo(request, "/contact/", { sent: "1" });
    }

    if (!name || !email || !message || !isValidEmail(email)) {
      return redirectTo(request, "/contact/", {
        error: "A valid name, email, and message are required.",
      });
    }

    if (name.length > 100 || email.length > 254 || company.length > 120 || message.length > 4000) {
      return redirectTo(request, "/contact/", {
        error: "One or more fields are longer than allowed.",
      });
    }

    if (!env.RESEND_API_KEY) {
      return redirectTo(request, "/contact/", {
        error: "Email service is not configured yet. Add RESEND_API_KEY in Cloudflare settings.",
      });
    }

    const toEmail = env.CONTACT_TO_EMAIL || "inquire@dtbsolutions.tech";
    const fromEmail = env.CONTACT_FROM_EMAIL || "Website Contact <inquire@dtbsolutions.tech>";

    const emailText = [
      "New DTB contact form submission",
      "",
      `Name: ${name}`,
      `Email: ${email}`,
      `Phone: ${phone || "N/A"}`,
      `Company: ${company || "N/A"}`,
      `Service: ${service || "N/A"}`,
      `Budget: ${budget || "N/A"}`,
      `Timeline: ${timeline || "N/A"}`,
      "",
      "Message:",
      message,
    ].join("\n");

    const resendResponse = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [toEmail],
        subject: `New DTB inquiry from ${name}`,
        reply_to: email,
        text: emailText,
      }),
    });

    if (!resendResponse.ok) {
      return redirectTo(request, "/contact/", {
        error: "Message could not be sent. Please check the email configuration.",
      });
    }

    return redirectTo(request, "/contact/", { sent: "1" });
  } catch (error) {
    return redirectTo(request, "/contact/", {
      error: "Invalid form submission.",
    });
  }
}

async function handleNewsletter(request, env) {
  try {
    const body = await readForm(request);
    const email = clean(body.email);

    if (looksAutomated(body)) {
      return redirectTo(request, "/blog/", { subscribed: "1" });
    }

    if (!email || !isValidEmail(email) || email.length > 254) {
      return redirectTo(request, "/blog/", { error: "A valid email is required." });
    }

    if (!env.RESEND_API_KEY) {
      return redirectTo(request, "/blog/", {
        error: "Newsletter service is not configured yet. Add RESEND_API_KEY in Cloudflare settings.",
      });
    }

    if (env.RESEND_AUDIENCE_ID) {
      const audienceResponse = await fetch(
        `https://api.resend.com/audiences/${env.RESEND_AUDIENCE_ID}/contacts`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${env.RESEND_API_KEY}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, unsubscribed: false }),
        },
      );

      if (!audienceResponse.ok) {
        return redirectTo(request, "/blog/", {
          error: "Newsletter signup could not be saved. Please try again.",
        });
      }

      return redirectTo(request, "/blog/", { subscribed: "1" });
    }

    const toEmail = env.CONTACT_TO_EMAIL || "inquire@dtbsolutions.tech";
    const fromEmail = env.CONTACT_FROM_EMAIL || "Website Contact <inquire@dtbsolutions.tech>";

    const resendResponse = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [toEmail],
        subject: "New DTB newsletter signup",
        text: `New newsletter signup: ${email}`,
      }),
    });

    if (!resendResponse.ok) {
      return redirectTo(request, "/blog/", {
        error: "Newsletter signup could not be sent. Please try again.",
      });
    }

    return redirectTo(request, "/blog/", { subscribed: "1" });
  } catch (error) {
    return redirectTo(request, "/blog/", {
      error: "Invalid newsletter submission.",
    });
  }
}

async function serveAsset(request, env) {
  const url = new URL(request.url);
  const pathname = url.pathname;

  if (
    (request.method === "GET" || request.method === "HEAD") &&
    pathname !== "/" &&
    !pathname.includes(".")
  ) {
    const normalized = pathname.endsWith("/") ? pathname : `${pathname}/`;
    const indexUrl = new URL(request.url);
    indexUrl.pathname = `${normalized}index.html`;

    const indexResponse = await env.ASSETS.fetch(new Request(indexUrl, request));

    if (indexResponse.status !== 404) {
      return indexResponse;
    }
  }

  return env.ASSETS.fetch(request);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = normalizePath(url.pathname);

    if (request.method === "GET" && pathname === "/api/contact") {
      return redirectTo(request, "/contact/");
    }

    if (request.method === "GET" && pathname === "/api/newsletter") {
      return redirectTo(request, "/blog/");
    }

    if (
      request.method === "POST" &&
      ["/api/contact", "/contact"].includes(pathname)
    ) {
      return handleContact(request, env);
    }

    if (
      request.method === "POST" &&
      ["/api/newsletter", "/newsletter", "/blog"].includes(pathname)
    ) {
      return handleNewsletter(request, env);
    }

    return serveAsset(request, env);
  },
};
