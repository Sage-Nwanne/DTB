# Designed to Breakthrough Website

The DTB website presents web, automation, infrastructure and growth strategy as one connected digital-systems offering for small teams and growing organizations.

## Brand direction

- Signature: **Design. Transform. Breakthrough.**
- Campaign line: **From foundation to flow.**
- Visual language: black and charcoal foundations, dominant DTB orange, metallic-gold depth, restrained purple system signals, smoked glass and circuit traces
- Content standard: public projects and attributable evidence without unsupported metrics or anonymous testimonials

## Routes

- `/` — homepage
- `/services/` — four connected service pillars, transparent pricing and engagement paths
- `/works/` — public work, system concepts and clearly labeled capability examples
- `/about/` — mission, operating principles and team
- `/reviews/` — reviews, proof and delivery standards
- `/blog/` — honest pre-launch blog and notification form
- `/contact/` — project intake and FAQ
- `/shawn/` — published team profile
- `/privacy/` and `/terms/` — legal pages
- `/sage/` and `/devs/` — no-index redirects to the team page until confirmed profile content is available

## Architecture

Source pages live in `public/`. The build copies them into `dist/` and injects the shared header and footer from `scripts/templates.js`.

```text
public/
  assets/
    icons.svg
    site.js
  static/css/
    site.css
  */index.html
scripts/
  build.js
  templates.js
  validate.js
src/
  worker.js
```

The shared shell is represented in source HTML with:

```html
<!-- DTB_HEADER -->
<!-- DTB_FOOTER -->
```

Do not hand-copy the navigation or footer into individual pages.

## Local development

```bash
npm install
npm run dev
```

Useful commands:

```bash
npm run build
npm run check
npm run preview
npm run deploy
```

`npm run check` builds the site and validates:

- all expected routes and shared assets
- shared header, footer and stylesheet usage
- local links, assets and fragment targets
- absence of known legacy placeholders and dead-link patterns

## Contact and Insights forms

The Cloudflare Worker handles:

- `POST /api/contact`
- `POST /contact`
- `POST /api/newsletter`
- `POST /newsletter`
- `POST /blog`

The forms include honeypot and submission-timing checks. The Worker also validates email format and field lengths.

Cloudflare environment variables:

```text
RESEND_API_KEY
CONTACT_TO_EMAIL
CONTACT_FROM_EMAIL
RESEND_AUDIENCE_ID
```

`RESEND_AUDIENCE_ID` is optional. When configured, Insights signups are saved to the Resend audience. Otherwise DTB receives an internal signup notification.

## Deployment

The site is deployed as a Cloudflare Worker with static assets from `dist/`.

```bash
npm run check
npm run deploy
```

Oversized source assets are excluded by the build when they exceed Cloudflare Workers' asset limit.

## Content safeguards

- Publish testimonials only after the client approves the quote and attribution.
- Label client work, system concepts and capability examples distinctly.
- Do not add performance percentages or client counts without supporting records.
- Keep unpublished team profiles no-indexed until the biography and public links are confirmed.
- Have legal pages reviewed before production use when business terms change.
