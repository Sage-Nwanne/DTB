# DTB Website Complete Overhaul Plan

## 🎯 Overview

Complete redesign of DTB website with modern design system, new pages, and interactive features. Inspired by DevSec's design language but tailored for DTB's services (web + agentic automation).

---

## 🎨 Design System

### Color Palette
- **Charcoal**: `#0c0c0c` (background)
- **Slate**: `#141414` (secondary bg)
- **Text**: `#e9e9e9` (primary text)
- **Accent**: `#ff9f1a` → `#b35400` (gradient)
- **Graphite**: `#1a1a1a` (card base)

### Typography
- **Headings**: Poppins or Inter (600–700 weight)
- **Body**: Inter (400–500 weight)
- **Mono**: For code snippets

### Components
- **Buttons**: Rounded-md, bold label, outer glow on hover
  - Primary: Orange solid
  - Secondary: Outline with subtle glow
- **Cards**: Graphite base with hover lift
- **Sections**: Hero band, stat bar, trust-strip, card grid, split sections

---

## 📄 Pages to Build/Redesign

### 1. Home (Landing)
- Hero band: "Design. Automate. Breakthrough."
- 4 service cards (Web, Automation, Marketing, Consulting)
- Proof strip: "12+ launches · 100% on-time · 30-day support"
- Featured work (2 tiles with metrics)
- Why DTB section (3 bullets)
- Testimonial slider (1–3)
- CTA band: "Let's map your breakthrough in 20 minutes"

### 2. Services (New)
- Intro blurb
- 4 service blocks (each links to section)
- Packages table (Basic/Standard/Premium)
- Bottom CTA

### 3. Portfolio (Redesign)
- Filter chips: All / Web / AI / Marketing
- Project cards: thumbnail, title, stack tags, outcome
- Detail modal: image + 3 bullets (Goal, Built, Result)

### 4. About (New)
- Mission statement
- Values (Innovation, Precision, Partnership, Integrity)
- Timeline/credibility row
- Meet the Devs mini grid
- Wire grid background with subtle animation

### 5. Reviews (Redesign)
- 6 review cards (quote, client, service, logo)
- "What we delivered" badges
- CTA: "Join our success stories"

### 6. Meet the Devs (New)
- Individual developer cards (photo, role, stack)
- "Recent work" link to filtered portfolio
- Mini paragraph about team

### 7. Contact (Redesign)
- Simple form (Name, Email, Project Type, Budget, Message)
- Reassurance copy
- Email button + calendar link

---

## 🧩 Reusable Components to Build

```
<Hero /> - gradient bg + two CTAs
<ServiceCard /> - icon, title, 2 bullets, link
<StatStrip /> - 3 stats
<ProjectCard /> - image, tags, result
<Testimonial /> - slider
<CTASection /> - gradient band
<Footer /> - 2-col sitemap + socials
<Button /> - primary/secondary with glow
<Card /> - base card with hover effects
```

---

## 🚀 Implementation Phases

### Phase 1: Design System & Foundation
- [ ] Set up Tailwind CSS with custom colors
- [ ] Create button styles (primary, secondary, glow)
- [ ] Import fonts (Poppins, Inter)
- [ ] Build SVG wire grid background
- [ ] Create base component library

### Phase 2: Page Structure & Layout
- [ ] Redesign Home page
- [ ] Create Services page
- [ ] Redesign Portfolio page
- [ ] Create About page
- [ ] Redesign Reviews page
- [ ] Create Meet the Devs page
- [ ] Redesign Contact page

### Phase 3: Navigation & Global Components
- [ ] Build sticky top nav
- [ ] Create footer
- [ ] Implement responsive design

### Phase 4: Interactive Features & Animation
- [ ] Hover effects (buttons, cards)
- [ ] Testimonial slider
- [ ] Portfolio filter + modal
- [ ] Background animations
- [ ] Developer card hover effects

### Phase 5: Content & Polish
- [ ] Add all copy
- [ ] Optimize images
- [ ] SEO optimization
- [ ] Performance testing

### Phase 6: Deployment
- [ ] Local testing
- [ ] Deploy to Railway
- [ ] Verify all pages

---

## 📋 Current Stack

- **Backend**: Django 5.2.1
- **Frontend**: Django Templates + Tailwind CSS + htmx (Phase 1)
- **Interactivity**: htmx for dynamic interactions (no page reloads)
- **Deployment**: Railway
- **Database**: PostgreSQL (production)

### Future Roadmap (Phase 2+)
- Expose DRF endpoints for specific features
- Drop in React/Vue "islands" only where needed
- Client dashboard (progress tracker)
- Membership system (agentic services)
- Marketing/Training courses & guides
- CMS functionality
- Chatbot integration

---

## 🎯 Frontend Architecture (Option C → B Migration Path)

### Phase 1: Django Templates + Tailwind + htmx
- Server-rendered HTML with Tailwind CSS
- htmx for dynamic interactions (no page reloads)
- SEO-friendly, fast initial load
- Easy to build and iterate

### Phase 2: Expose DRF Endpoints
- Create REST API endpoints for complex features
- Keep existing Django templates for marketing pages
- Drop in React/Vue "islands" only where needed

### Phase 3: Full SPA (Optional)
- Migrate to full React/Vue if needed
- Keep Django as pure API backend

---

## 🎯 Next Steps

1. **Set up Tailwind CSS** in Django project
2. **Install htmx** for dynamic interactions
3. **Create design system** (colors, typography, components)
4. **Build Home page** as proof of concept
5. **Start Phase 1**: Build all marketing pages
6. **Plan Phase 2**: Identify which features need React/Vue islands

---

## 📝 Content Kit (Ready to Use)

### Service One-Liners
- **Web Services**: "Conversion-first websites with SEO, analytics, and maintenance baked in."
- **Agentic Automation**: "AI agents and workflows that replace busywork with results."
- **Marketing & Growth**: "Content systems that compound attention into revenue."
- **Consulting & Partnerships**: "Strategy, audits, and white-label delivery you can trust."

### Proof Bar
"12+ launches • 100% on-time handoffs • 30-day post-launch support"

### Hero CTA Labels
- Primary: "Explore Services"
- Secondary: "Start a Project"

---

## 🎬 Animation Guidelines

- **Global background**: Continuous, extremely slow motion
- **Interactive elements**: Micro-motion on hover
- **Hero/CTA**: One intentional focal animation
- **Rule**: "Motion should exist but user shouldn't notice until they stop scrolling"

---

## ✅ Success Criteria

- [ ] All 7 pages built and functional
- [ ] Design system consistent across all pages
- [ ] Responsive on mobile, tablet, desktop
- [ ] Performance: LCP < 2.5s
- [ ] SEO optimized
- [ ] Deployed to Railway
- [ ] All interactive features working

---

## 📞 Questions to Answer

1. **Frontend approach**: Keep Django templates or build SPA?
2. **Developer photos**: Use new headshots or placeholders?
3. **Portfolio items**: How many projects to showcase initially?
4. **Services page**: Include or fold into Home?
5. **Testimonials**: Do you have 1–3 ready?

---

**Status**: Ready to start Phase 1 ✨

