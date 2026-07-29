(function () {
  const replacements = new Map([
    ["DTB brings your website, brand, infrastructure and day-to-day tools together so the business is easier to run, easier to trust and ready to grow.", "We build the brand, website and systems your business needs to grow with confidence."],
    ["Talk Through My Project", "Start a Project"],
    ["Turn the idea into a business ready to operate.", "Launch with a stronger foundation."],
    ["Positioning, identity, infrastructure and a professional launch—designed as one foundation.", "Brand, website and infrastructure built to work together from day one."],
    ["Start with clarity", "Build Your Foundation"],
    ["Remove the bottlenecks holding back your next stage.", "Fix what is slowing the business down."],
    ["Connected tools, sharper workflows and ongoing optimization for businesses ready to scale.", "Better tools, cleaner workflows and less time lost to manual work."],
    ["Find the opportunity", "Improve the Business"],
    ["Your business should work as one system.", "Everything should work together."],
    ["Your website, tools and internal processes should support one another—not create more work for your team.", "We connect the customer experience with the systems behind it."],
    ["Four parts of a stronger business.", "What we build."],
    ["We plan the customer-facing experience and the systems behind it together, so nothing important gets treated as an afterthought.", "From your public brand to the tools your team uses every day."],
    ["Positioning, visual direction and conversion-minded websites that establish trust and create a clear next step.", "Clear branding and websites built to earn trust and drive action."],
    ["Connected intake, follow-up, reporting and intelligent workflows that reduce busywork without losing control.", "Automations that handle repetitive work and keep your team in control."],
    ["Hosting, cloud deployment, security, backups and documented foundations built for reliability and handoff.", "Reliable hosting, security, backups and business infrastructure."],
    ["Offer clarity, analytics, content systems and ongoing improvements grounded in what the business actually needs.", "Practical strategy, analytics and ongoing improvements that support growth."],
    ["Clear starting points, before the sales call.", "Know the starting price."],
    ["Website packages begin at $2.5K, with project, enterprise and ongoing-partner options shown openly.", "Website packages start at $2.5K, with custom and ongoing options available."],
    ["See what the work looks like.", "Work that speaks for itself."],
    ["Explore real client work, the problem each project addressed and what DTB was responsible for delivering.", "See the websites, platforms and systems we have delivered."],
    ["A partner beyond launch day.", "Built to last beyond launch."],
    ["We build, document and support the work so your team understands what it owns and what comes next.", "Every project includes a clear handoff, documentation and support."],
    ["Understand the business, audience, friction and opportunity.", "Define the goal, audience and real business need."],
    ["Map the right strategy, experience and connected system.", "Plan the experience, technology and path forward."],
    ["Build, test, launch, document and hand off with confidence.", "Build, test and launch with a clear handoff."],
    ["Measure performance and evolve the system as the business grows.", "Improve what works as the business grows."],
    ["Let’s talk about what the business needs next.", "Ready to build what comes next?"],
    ["Tell us what is working, where things are getting stuck and what you want the next stage of the business to look like.", "Bring us the goal. We will help you build the right path forward."],

    ["Small team. Connected thinking.", "Proven work. Personal service."],
    ["DTB combines design, technology and operations around one goal: help small teams work with the clarity and capability of a much larger organization.", "We help businesses look sharper, work smarter and grow on a stronger foundation."],
    ["Build systems that fit the business—not the other way around.", "Built around your business."],
    ["Great design should clarify. Technology should reduce friction. A partner should leave the business more capable than when the project began.", "Good design earns trust. Good systems save time. Our work delivers both."],
    ["Make the right thing clear.", "Make the business clear."],
    ["Shape the offer, message and experience so customers and teams know what happens next.", "Clarify the offer, message and customer experience."],
    ["Connect the work behind it.", "Make the work easier."],
    ["Replace disconnected steps and fragile workarounds with intentional systems and documentation.", "Replace manual steps and disconnected tools with reliable systems."],
    ["Create room for the next stage.", "Build for the next stage."],
    ["Remove the constraint that keeps the business from operating, serving or growing with confidence.", "Solve the problems limiting service, efficiency and growth."],
    ["Build capability, not dependence.", "Leave the business stronger."],
    ["Communicate clearly, document decisions and create a system the team can understand and own.", "Clear communication, documented work and a system your team can own."],
    ["These are practical delivery rules—not marketing statistics.", "The standards we bring to every project."],
    ["Different disciplines. One delivery system.", "The team behind the work."],
    ["A small team with different specialties, working from one shared plan.", "Strategy, design, development and delivery under one roof."],
    ["Founded DTB and leads the connection between client strategy, technical delivery, infrastructure and the operating workflows behind each solution.", "Leads business strategy, technical delivery and infrastructure across DTB projects."],
    ["Leads product experience and development across interface, system and AI-focused work.", "Leads product design and development across web, software and automation projects."],
    ["Supports discovery, client coordination and the path from qualified opportunity through delivery.", "Leads client coordination, project planning and sales development."],
    ["From individual projects to connected systems.", "How DTB grew."],
    ["The story is presented without an unverified year-by-year timeline.", "What began with digital projects grew into a full-service technology partnership."],
    ["DTB began around the belief that small teams deserve intentional design and technical foundations—not disposable templates.", "DTB started by helping small businesses get better design and stronger technical foundations."],
    ["Client work exposed the operational friction behind public experiences, expanding the work into automation, infrastructure and process.", "As client needs grew, so did our work across automation, infrastructure and operations."],
    ["DTB now approaches the brand, website and internal operation as parts of the same business system.", "Today we build the brand, website and internal systems as one connected operation."],
    ["The direction is a durable digital-systems partnership: clear strategy, accountable delivery and continuous improvement.", "We continue to grow as a long-term partner for strategy, technology and support."],
    ["Bring the constraint. Build the breakthrough.", "Bring us the goal. We will build the path."],
    ["Start with a focused conversation about the business and the system behind it.", "Tell us what the business needs next."],

    ["Services built around the whole business.", "Everything your business needs to move forward."],
    ["We begin with the bottleneck and design the right combination of identity, technology and operating systems around it.", "From branding and websites to automation and infrastructure, we build what gets results."],
    ["Four connected pillars", "Our services"],
    ["Build what the business needs next.", "Choose the right next move."],
    ["Start with one need or combine several. We shape the scope around the business instead of forcing every project into the same package.", "Start with one service or combine them into a complete solution."],
    ["Turn the business into a clear, credible public experience that gives the right customer a confident next step.", "Build a polished brand and website that turns attention into action."],
    ["Reduce repetitive work and missed follow-up with workflows that remain understandable, reviewable and under your control.", "Automate repetitive work, improve follow-up and keep operations moving."],
    ["Create a reliable technical foundation for the website, team and information the business depends on.", "Protect and support the systems your business depends on."],
    ["Sharpen the offer, identify the next constraint and improve the system based on evidence instead of noise.", "Use clear strategy and real data to make better growth decisions."],
    ["Know the starting point before we talk.", "Straightforward pricing."],
    ["These are clear baseline packages—not teaser prices. Final scope is confirmed in writing before work begins, and every project package includes post-launch support.", "These are real starting prices. Final scope is approved before work begins, and every package includes post-launch support."],
    ["Transparent baseline. Right-sized scope.", "A clear way to work together."],
    ["The public prices establish an honest starting point. Discovery then defines the outcome, boundaries and delivery path before the proposal is approved.", "Choose a starting point. We will confirm the scope, timeline and deliverables before you commit."],
    ["A clear path from friction to flow.", "A simple process. Clear results."],
    ["Bring the problem. DTB will help map the right next move before prescribing technology.", "Tell us the goal and we will recommend the right service."],
    ["Map My Breakthrough", "Talk to DTB"],

    ["Proof should feel personal and verifiable.", "Results you can see. Clients you can hear from."],
    ["Read what clients have said about the work, then explore public projects for yourself.", "See what clients say and review the work for yourself."],
    ["What clients have said about working with DTB.", "What clients say about DTB."],
    ["These reviews cover website development, UX, e-commerce, email, CMS and marketing work across different client needs.", "Feedback from clients across web, UX, e-commerce, email and digital strategy."],
    ["Public projects you can inspect.", "See the work for yourself."],
    ["These links are a stronger starting point than anonymous praise.", "Visit selected projects and experience the work firsthand."],
    ["Evaluate the fit", "Work with DTB"],
    ["Have questions about a project?", "Have a project in mind?"],
    ["Ask about the scope, role, constraints or delivery approach during a focused consultation.", "Let’s talk about the goal, scope and best path forward."],
    ["Talk with DTB", "Start a Project"]
  ]);

  function replaceText(root) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      const trimmed = node.nodeValue.trim();
      if (!replacements.has(trimmed)) return;
      node.nodeValue = node.nodeValue.replace(trimmed, replacements.get(trimmed));
    });
  }

  replaceText(document.body);

  const descriptions = {
    "/": "DTB builds websites, brands, automation and infrastructure that help businesses grow and operate with confidence.",
    "/about/": "Meet the team behind DTB and learn how we combine design, development, automation and infrastructure for growing businesses.",
    "/services/": "Explore DTB services and straightforward pricing for websites, branding, automation, infrastructure and ongoing support.",
    "/reviews/": "Read client reviews and explore selected DTB website, UX, e-commerce and digital systems projects."
  };
  const path = window.location.pathname;
  const description = descriptions[path];
  if (description) {
    const meta = document.querySelector('meta[name="description"]');
    if (meta) meta.setAttribute("content", description);
  }
})();