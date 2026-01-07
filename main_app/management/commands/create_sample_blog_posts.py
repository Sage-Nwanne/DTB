from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from main_app.models import BlogPost, Category, Tag
from datetime import timedelta

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample blog posts for testing'

    def handle(self, *args, **kwargs):
        # Get or create admin user
        admin_user = User.objects.filter(is_superuser=True).first()
        if not admin_user:
            self.stdout.write(self.style.ERROR('No admin user found. Please create one first.'))
            return

        # Create categories
        web_design_cat, _ = Category.objects.get_or_create(
            name='Web Design',
            defaults={'slug': 'web-design', 'description': 'Tips and insights on modern web design'}
        )
        
        automation_cat, _ = Category.objects.get_or_create(
            name='AI & Automation',
            defaults={'slug': 'ai-automation', 'description': 'Automation strategies for business growth'}
        )
        
        business_cat, _ = Category.objects.get_or_create(
            name='Business Growth',
            defaults={'slug': 'business-growth', 'description': 'Strategies for scaling your business'}
        )
        
        marketing_cat, _ = Category.objects.get_or_create(
            name='Digital Marketing',
            defaults={'slug': 'digital-marketing', 'description': 'Marketing tips and strategies'}
        )

        # Create tags
        seo_tag, _ = Tag.objects.get_or_create(name='SEO', defaults={'slug': 'seo'})
        tips_tag, _ = Tag.objects.get_or_create(name='Tips', defaults={'slug': 'tips'})
        case_study_tag, _ = Tag.objects.get_or_create(name='Case Study', defaults={'slug': 'case-study'})
        tutorial_tag, _ = Tag.objects.get_or_create(name='Tutorial', defaults={'slug': 'tutorial'})
        ai_tag, _ = Tag.objects.get_or_create(name='AI', defaults={'slug': 'ai'})
        small_business_tag, _ = Tag.objects.get_or_create(name='Small Business', defaults={'slug': 'small-business'})

        # Sample blog posts
        posts_data = [
            {
                'title': '5 Web Design Mistakes That Are Costing You Customers',
                'slug': '5-web-design-mistakes-costing-customers',
                'category': web_design_cat,
                'tags': [tips_tag, small_business_tag],
                'excerpt': 'Your website should be your best salesperson. Here are 5 common mistakes that are driving potential customers away.',
                'content': '''
<p>Your website is often the first impression potential customers have of your business. Unfortunately, many small businesses make critical design mistakes that cost them sales. Here are the top 5 mistakes we see—and how to fix them.</p>

<h2>1. Slow Loading Speed</h2>
<p>If your website takes more than 3 seconds to load, you're losing customers. Studies show that 53% of mobile users abandon sites that take longer than 3 seconds to load.</p>
<p><strong>The Fix:</strong> Optimize images, use a CDN, and choose quality hosting. We've helped clients reduce load times from 8 seconds to under 2 seconds, resulting in a 40% decrease in bounce rate.</p>

<h2>2. Not Mobile-Friendly</h2>
<p>Over 60% of web traffic comes from mobile devices. If your site doesn't work well on phones and tablets, you're turning away the majority of your potential customers.</p>
<p><strong>The Fix:</strong> Use responsive design that adapts to any screen size. Test your site on multiple devices before launching.</p>

<h2>3. Unclear Call-to-Action</h2>
<p>Visitors should know exactly what action to take within seconds of landing on your page. If they have to hunt for your contact button or don't know what to do next, they'll leave.</p>
<p><strong>The Fix:</strong> Make your primary CTA prominent, clear, and action-oriented. Use contrasting colors and place it above the fold.</p>

<h2>4. Too Much Text, Not Enough Visuals</h2>
<p>Walls of text are overwhelming. People scan websites—they don't read every word. If your site looks like a novel, visitors will bounce.</p>
<p><strong>The Fix:</strong> Break up text with headings, bullet points, and images. Use white space strategically. Show, don't just tell.</p>

<h2>5. Outdated Design</h2>
<p>If your website looks like it's from 2010, visitors will assume your business is outdated too. First impressions matter.</p>
<p><strong>The Fix:</strong> Modern design doesn't have to be expensive. Clean layouts, modern fonts, and updated imagery can transform your site.</p>

<h2>Ready to Fix Your Website?</h2>
<p>We've helped 50+ small businesses transform their websites into customer-generating machines. Want to see what we can do for you? <a href="/contact/">Get a free website audit</a>.</p>
                ''',
                'days_ago': 2,
            },
            {
                'title': 'How AI Chatbots Saved This Business 15 Hours Per Week',
                'slug': 'ai-chatbots-saved-15-hours-per-week',
                'category': automation_cat,
                'tags': [case_study_tag, ai_tag, small_business_tag],
                'excerpt': 'A real case study of how we implemented an AI chatbot that handles customer inquiries 24/7 and freed up 15 hours of manual work per week.',
                'content': '''
<p>Meet Sarah, owner of a growing e-commerce business selling handmade jewelry. She was spending 15+ hours per week answering the same customer questions: "Do you ship internationally?" "What's your return policy?" "Is this item in stock?"</p>

<p>Sound familiar? Here's how we solved it.</p>

<h2>The Problem</h2>
<p>Sarah's business was growing, but she was drowning in customer service. She couldn't afford to hire someone full-time, but she also couldn't keep up with the volume of inquiries. Worse, she was missing messages that came in after hours, losing potential sales.</p>

<h2>The Solution: AI Chatbot</h2>
<p>We implemented a custom AI chatbot on her website that:</p>
<ul>
<li>Answers common questions instantly (24/7)</li>
<li>Captures leads when she's offline</li>
<li>Qualifies customers before they reach her</li>
<li>Integrates with her CRM</li>
</ul>

<h2>The Results (After 30 Days)</h2>
<ul>
<li><strong>15 hours saved per week</strong> - No more answering the same questions</li>
<li><strong>40% increase in after-hours inquiries</strong> - Customers get instant responses anytime</li>
<li><strong>25% boost in conversions</strong> - Faster responses = more sales</li>
<li><strong>Zero missed leads</strong> - Every inquiry is captured and followed up</li>
</ul>

<h2>What It Cost</h2>
<p>Total investment: $400 for setup + $50/month for maintenance. Sarah calculated she was spending $600/month worth of her time on customer service. The ROI was immediate.</p>

<h2>Could This Work for Your Business?</h2>
<p>If you're spending hours answering repetitive questions, an AI chatbot could be your solution. We offer a free consultation to see if it's right for your business. <a href="/contact/">Schedule your free call</a>.</p>
                ''',
                'days_ago': 5,
            },
            {
                'title': 'The Ultimate SEO Checklist for Small Business Websites',
                'slug': 'ultimate-seo-checklist-small-business',
                'category': marketing_cat,
                'tags': [seo_tag, tutorial_tag, small_business_tag],
                'excerpt': 'A step-by-step SEO checklist that will help your small business website rank higher on Google and get more organic traffic.',
                'content': '''
<p>Want to rank higher on Google without paying for ads? This SEO checklist covers everything you need to optimize your small business website for search engines.</p>

<h2>On-Page SEO Essentials</h2>

<h3>1. Title Tags</h3>
<ul>
<li>Include your primary keyword</li>
<li>Keep it under 60 characters</li>
<li>Make it compelling (people need to want to click)</li>
</ul>

<h3>2. Meta Descriptions</h3>
<ul>
<li>Summarize the page in 150-160 characters</li>
<li>Include a call-to-action</li>
<li>Use your target keyword naturally</li>
</ul>

<h3>3. Header Tags (H1, H2, H3)</h3>
<ul>
<li>One H1 per page (your main headline)</li>
<li>Use H2s for main sections</li>
<li>Include keywords in headers naturally</li>
</ul>

<h3>4. Content Quality</h3>
<ul>
<li>Write for humans first, search engines second</li>
<li>Aim for 1000+ words for important pages</li>
<li>Answer the questions your customers are asking</li>
<li>Update content regularly</li>
</ul>

<h2>Technical SEO</h2>

<h3>5. Site Speed</h3>
<ul>
<li>Aim for under 3 seconds load time</li>
<li>Compress images</li>
<li>Use browser caching</li>
<li>Minimize CSS and JavaScript</li>
</ul>

<h3>6. Mobile Optimization</h3>
<ul>
<li>Use responsive design</li>
<li>Test on multiple devices</li>
<li>Ensure buttons are easy to tap</li>
</ul>

<h3>7. SSL Certificate</h3>
<ul>
<li>Your site should use HTTPS (not HTTP)</li>
<li>Google prioritizes secure sites</li>
</ul>

<h2>Local SEO (For Local Businesses)</h2>

<h3>8. Google Business Profile</h3>
<ul>
<li>Claim and verify your listing</li>
<li>Complete all information</li>
<li>Add photos regularly</li>
<li>Respond to reviews</li>
</ul>

<h3>9. Local Keywords</h3>
<ul>
<li>Include your city/region in content</li>
<li>Create location-specific pages if you serve multiple areas</li>
</ul>

<h2>Off-Page SEO</h2>

<h3>10. Backlinks</h3>
<ul>
<li>Get listed in local directories</li>
<li>Partner with complementary businesses</li>
<li>Create shareable content</li>
</ul>

<h2>Need Help with SEO?</h2>
<p>SEO can be overwhelming, but it's one of the best long-term investments for your business. We offer complete SEO services for small businesses. <a href="/contact/">Get a free SEO audit</a>.</p>
                ''',
                'days_ago': 7,
            },
            {
                'title': '10 Ways to Automate Your Small Business (Without Coding)',
                'slug': '10-ways-automate-small-business',
                'category': automation_cat,
                'tags': [tips_tag, tutorial_tag, small_business_tag],
                'excerpt': 'Automation isn\'t just for big companies. Here are 10 practical ways small businesses can automate tasks and save time.',
                'content': '''
<p>Think automation is only for enterprise companies with big budgets? Think again. Here are 10 ways any small business can automate tasks and save hours every week—no coding required.</p>

<h2>1. Email Marketing Automation</h2>
<p>Set up welcome sequences, abandoned cart emails, and follow-ups that run on autopilot. Tools like Mailchimp or ConvertKit make this easy.</p>

<h2>2. Social Media Scheduling</h2>
<p>Stop posting manually every day. Use tools like Buffer or Hootsuite to schedule a week's worth of posts in one sitting.</p>

<h2>3. Appointment Booking</h2>
<p>Let customers book appointments online 24/7. Tools like Calendly sync with your calendar and send automatic reminders.</p>

<h2>4. Invoice Generation</h2>
<p>Automatically generate and send invoices when a project is completed. QuickBooks and FreshBooks can handle this.</p>

<h2>5. Customer Onboarding</h2>
<p>Create automated welcome emails, setup guides, and check-in sequences for new customers.</p>

<h2>6. Lead Capture</h2>
<p>Automatically add form submissions to your CRM and trigger follow-up sequences.</p>

<h2>7. Review Requests</h2>
<p>Automatically ask happy customers for reviews after a purchase or project completion.</p>

<h2>8. Data Backup</h2>
<p>Set up automatic backups of your important files and databases. Never lose data again.</p>

<h2>9. Report Generation</h2>
<p>Automatically generate and email weekly/monthly reports on sales, traffic, or other key metrics.</p>

<h2>10. Customer Support</h2>
<p>Use chatbots to handle common questions and route complex issues to the right person.</p>

<h2>Ready to Automate?</h2>
<p>We help small businesses implement these automations and more. <a href="/contact/">Schedule a free automation consultation</a>.</p>
                ''',
                'days_ago': 10,
            },
            {
                'title': 'Why Your Business Needs a Website (Even If You Have Social Media)',
                'slug': 'why-business-needs-website',
                'category': web_design_cat,
                'tags': [small_business_tag, tips_tag],
                'excerpt': 'Social media is great, but it\'s not enough. Here\'s why every business needs a professional website.',
                'content': '''
<p>"I have Instagram and Facebook. Do I really need a website?" We hear this question all the time. The short answer: Yes. Here's why.</p>

<h2>1. You Don't Own Social Media</h2>
<p>Instagram, Facebook, TikTok—they can change their algorithms, shut down your account, or disappear entirely. Your website is yours. You control it.</p>

<h2>2. Credibility and Trust</h2>
<p>When people search for your business, they expect to find a website. No website = less credible in many customers' eyes.</p>

<h2>3. Better for SEO</h2>
<p>Social media posts don't rank well on Google. Your website does. If you want to be found in search, you need a website.</p>

<h2>4. Complete Control</h2>
<p>On social media, you're limited by their templates and features. On your website, you can design the exact experience you want.</p>

<h2>5. Capture Leads</h2>
<p>Social media makes it hard to capture email addresses and build your own audience. Your website makes it easy.</p>

<h2>6. Professional Email</h2>
<p>With a website, you get a professional email (you@yourbusiness.com) instead of yourbusiness123@gmail.com.</p>

<h2>7. E-commerce Capabilities</h2>
<p>While you can sell on social media, your own e-commerce site gives you more control and lower fees.</p>

<h2>The Bottom Line</h2>
<p>Use social media to drive traffic to your website—not as a replacement for it. Your website is your digital home base.</p>

<h2>Ready to Build Your Website?</h2>
<p>We create professional, affordable websites for small businesses. <a href="/contact/">Get a free quote</a>.</p>
                ''',
                'days_ago': 14,
            },
            {
                'title': 'How We Increased a Client\'s Website Traffic by 300% in 90 Days',
                'slug': 'increased-website-traffic-300-percent',
                'category': marketing_cat,
                'tags': [case_study_tag, seo_tag],
                'excerpt': 'A detailed case study of how we tripled a client\'s organic traffic in just 3 months using SEO and content strategy.',
                'content': '''
<p>When a local HVAC company came to us, they were getting about 200 website visitors per month. Three months later, they were getting over 600. Here's exactly what we did.</p>

<h2>The Starting Point</h2>
<ul>
<li>200 monthly visitors</li>
<li>Ranking on page 3-5 for target keywords</li>
<li>Outdated website design</li>
<li>No blog or content strategy</li>
<li>Slow loading speed (7+ seconds)</li>
</ul>

<h2>What We Did</h2>

<h3>Month 1: Technical Foundation</h3>
<ul>
<li>Redesigned website with modern, mobile-friendly layout</li>
<li>Improved site speed from 7 seconds to 1.8 seconds</li>
<li>Fixed broken links and 404 errors</li>
<li>Optimized all images</li>
<li>Set up Google Analytics and Search Console</li>
</ul>

<h3>Month 2: On-Page SEO</h3>
<ul>
<li>Keyword research for HVAC services in their area</li>
<li>Optimized all page titles and meta descriptions</li>
<li>Rewrote service pages with target keywords</li>
<li>Added location-specific content</li>
<li>Created FAQ section answering common questions</li>
</ul>

<h3>Month 3: Content Strategy</h3>
<ul>
<li>Published 8 blog posts targeting long-tail keywords</li>
<li>Created service area pages for nearby cities</li>
<li>Added customer testimonials and case studies</li>
<li>Built local citations and directory listings</li>
</ul>

<h2>The Results</h2>
<ul>
<li><strong>300% increase in organic traffic</strong> (200 → 600+ visitors/month)</li>
<li><strong>Page 1 rankings</strong> for 12 target keywords</li>
<li><strong>50% increase in phone calls</strong> from the website</li>
<li><strong>35% increase in quote requests</strong></li>
</ul>

<h2>The ROI</h2>
<p>Total investment: $3,500 over 3 months. The client estimates the increased traffic generated an additional $15,000 in revenue in month 3 alone.</p>

<h2>Want Similar Results?</h2>
<p>Every business is different, but the fundamentals are the same. <a href="/contact/">Let's talk about your SEO strategy</a>.</p>
                ''',
                'days_ago': 21,
            },
        ]

        # Create the posts
        for post_data in posts_data:
            tags = post_data.pop('tags')
            days_ago = post_data.pop('days_ago')
            
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults={
                    **post_data,
                    'author': admin_user,
                    'status': 'published',
                    'published_at': timezone.now() - timedelta(days=days_ago),
                }
            )
            
            if created:
                post.tags.set(tags)
                self.stdout.write(self.style.SUCCESS(f'Created blog post: {post.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Blog post already exists: {post.title}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Sample blog posts created successfully!'))

