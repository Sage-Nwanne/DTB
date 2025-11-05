# 🧪 Testing Guide - DTB Website

## ✅ Quick Testing Checklist

### **1. Page Loading**
- [ ] Home page loads at `http://localhost:8001/`
- [ ] Services page loads at `http://localhost:8001/services`
- [ ] Portfolio page loads at `http://localhost:8001/works`
- [ ] About page loads at `http://localhost:8001/about`
- [ ] Reviews page loads at `http://localhost:8001/reviews`
- [ ] Contact page loads at `http://localhost:8001/contact`

### **2. Navigation**
- [ ] Navbar appears on all pages
- [ ] Logo links to home
- [ ] All nav links work (Home, Services, Portfolio, About, Reviews, Contact)
- [ ] "Start a Project" button works
- [ ] Footer appears on all pages
- [ ] Footer links work

### **3. Design & Styling**
- [ ] Orange accent color (#ff9f1a) visible
- [ ] Dark background (charcoal) applied
- [ ] Fonts load correctly (Poppins, Inter)
- [ ] Buttons have hover effects
- [ ] Cards have hover effects
- [ ] Responsive layout on mobile

### **4. Home Page**
- [ ] Hero section displays
- [ ] 4 service cards visible
- [ ] Proof strip shows 3 metrics
- [ ] CTA buttons work
- [ ] All text readable

### **5. Services Page**
- [ ] 4 service blocks display
- [ ] Pricing table shows 4 tiers
- [ ] Process section shows 4 steps
- [ ] All "Get Started" buttons work
- [ ] Pricing is clear and readable

### **6. Portfolio Page**
- [ ] 6 project cards display
- [ ] Filter buttons work (All, Web, Automation, Marketing)
- [ ] Projects filter correctly
- [ ] Tech stack tags visible
- [ ] Hover effects show "View Project"

### **7. About Page**
- [ ] Mission statement displays
- [ ] 4 values cards visible
- [ ] Timeline shows 4 items
- [ ] Team section shows 3 members
- [ ] All text readable

### **8. Reviews Page**
- [ ] 6 testimonial cards display
- [ ] 5-star ratings visible
- [ ] Client names and titles shown
- [ ] Stats section shows 4 metrics
- [ ] All testimonials readable

### **9. Contact Page**
- [ ] Contact form displays
- [ ] All 7 form fields present:
  - [ ] Name
  - [ ] Email
  - [ ] Company
  - [ ] Service dropdown
  - [ ] Budget dropdown
  - [ ] Message textarea
  - [ ] Submit button
- [ ] Contact info sidebar visible
- [ ] FAQ section shows 5 items
- [ ] Form inputs have focus states

### **10. Responsive Design**
- [ ] Test on mobile (375px width)
- [ ] Test on tablet (768px width)
- [ ] Test on desktop (1024px+ width)
- [ ] All pages responsive
- [ ] No horizontal scrolling
- [ ] Text readable on all sizes

### **11. Performance**
- [ ] Pages load quickly (< 2 seconds)
- [ ] CSS loads properly
- [ ] Images load properly
- [ ] No console errors
- [ ] No 404 errors (except favicon)

### **12. Links & CTAs**
- [ ] All "Get Started" buttons link to `/contact/`
- [ ] All "Learn more" links work
- [ ] All navigation links work
- [ ] All footer links work
- [ ] Social media links present

---

## 🧪 **Manual Testing Steps**

### **Test 1: Full Page Load**
```
1. Open http://localhost:8001/
2. Wait for page to fully load
3. Check browser console for errors
4. Verify all images loaded
```

### **Test 2: Navigation**
```
1. Click each nav link
2. Verify page changes
3. Check URL updates
4. Verify content loads
```

### **Test 3: Responsive Design**
```
1. Open DevTools (F12)
2. Toggle device toolbar
3. Test mobile (375px)
4. Test tablet (768px)
5. Test desktop (1024px)
6. Verify layout adapts
```

### **Test 4: Hover Effects**
```
1. Hover over buttons
2. Verify glow effect
3. Hover over cards
4. Verify lift effect
5. Hover over links
6. Verify color change
```

### **Test 5: Form Interaction**
```
1. Click on form fields
2. Verify focus state
3. Type in fields
4. Verify text appears
5. Try submitting (will fail without backend)
```

### **Test 6: Portfolio Filter**
```
1. Click "All Projects"
2. Verify all 6 projects show
3. Click "Web Design"
4. Verify only web projects show
5. Click "Automation"
6. Verify only automation projects show
7. Click "Marketing"
8. Verify only marketing projects show
```

---

## 🔍 **Browser DevTools Checks**

### **Console Tab**
- [ ] No red errors
- [ ] No warnings about missing resources
- [ ] No CORS errors

### **Network Tab**
- [ ] All CSS files load (200 status)
- [ ] All images load (200 status)
- [ ] No 404 errors (except favicon)
- [ ] Page load time < 2 seconds

### **Elements Tab**
- [ ] Proper HTML structure
- [ ] Tailwind classes applied
- [ ] No inline styles (except necessary)
- [ ] Proper semantic HTML

---

## 📱 **Device Testing**

### **Mobile (iPhone 12)**
- [ ] All pages load
- [ ] Text readable
- [ ] Buttons clickable
- [ ] No horizontal scroll
- [ ] Images scale properly

### **Tablet (iPad)**
- [ ] All pages load
- [ ] Layout adapts
- [ ] Text readable
- [ ] Buttons clickable

### **Desktop (1920x1080)**
- [ ] All pages load
- [ ] Full layout visible
- [ ] Hover effects work
- [ ] Responsive grid shows

---

## ✅ **Final Checklist**

- [ ] All 6 pages load without errors
- [ ] All links work correctly
- [ ] Design system applied consistently
- [ ] Responsive on all devices
- [ ] No console errors
- [ ] No 404 errors (except favicon)
- [ ] Hover effects work
- [ ] Form displays correctly
- [ ] Portfolio filter works
- [ ] Performance is good

---

## 🚀 **Ready for Deployment**

Once all tests pass:
1. Commit changes to git
2. Push to GitHub
3. Deploy to Railway
4. Connect Squarespace domain
5. Go live!

---

**Testing Status**: Ready to test ✅

