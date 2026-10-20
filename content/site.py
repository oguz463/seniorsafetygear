"""Site-wide settings and the simple pages for SeniorSafetyGear."""

import datetime

BASE_URL = 'https://www.seniorsafetygear.com'
AMAZON_TAG = 'seniorsafetygear-20'
AUTHOR = 'Oğuz Tokatlı'
AUTHOR_URL = BASE_URL + '/about/#author'
AUTHOR_SAME_AS = ['https://www.linkedin.com/in/oguz-tokatli/', 'https://github.com/oguz463']
CONTACT_EMAIL = 'hello@seniorsafetygear.com'
DISCLOSURE = 'As an Amazon Associate, SeniorSafetyGear earns from qualifying purchases.'
UPDATED = datetime.date(2026, 10, 20)

NAV = [('Guides', '/guides/'), ('Articles', '/articles/'), ('Tools', '/tools/'), ('How we research', '/how-we-research/'), ('About', '/about/')]

HOME_TITLE = 'SeniorSafetyGear: Mobility and Bathroom Safety Buying Guides Built on Maker Specs and Safety Guidance'
HOME_DESCRIPTION = 'Research-based buying guides for rollators, shower chairs, bedside commodes, canes and more, compared on weight limits, dimensions and public safety guidance.'
HOME_EYEBROW = 'Mobility and bathroom safety, researched'
HOME_H1 = 'Equipment that keeps you safe and moving, chosen on the facts'
HOME_LEAD = 'We compare rollators, shower chairs, raised toilet seats, canes and more on the numbers that decide whether they work: the weight limit, the dimensions, the fit, and what the CDC, MedlinePlus and the CPSC say.'
HOME_STEPS = [
    ('Guidance first', 'Every guide starts with what the CDC, MedlinePlus, OrthoInfo or the CPSC say about that kind of equipment.'),
    ('The maker\'s own numbers', 'Limits and sizes come from maker pages where we could read them, and we flag where a listing disagrees.'),
    ('Named sources', 'Each guide lists the pages it relies on, and says plainly which figures rest only on an Amazon listing.'),
]

PAGES = {
    'about': (
        'About SeniorSafetyGear | SeniorSafetyGear',
        'Who writes SeniorSafetyGear and how the site is funded.',
        '''<p>SeniorSafetyGear is written by Oğuz Tokatlı. The guides are research-based: we read the makers' manuals and spec pages, the guidance that the CDC, FDA and U.S. Consumer Product Safety Commission publish for each kind of equipment, then compare the products on those facts. We don't claim to have tested products in a lab, and we are not a medical practice.</p>
<h2>What makes these guides different</h2>
<p>Most buying guides tell you which product won. We try to show you why, and where the evidence is thin. Each guide opens with what the official guidance says about that kind of equipment. The cards then give the maker's own numbers, and a short "best for, skip if" line says who each pick suits. When a retailer listing and the maker disagree, we say which one we trust and why.</p>
<h2>What we don't do</h2>
<p>We don't run lab tests, and we don't pretend to have used every product. We don't let commission rates choose the winners, and we don't use the words "medically reviewed" for text a clinician hasn't reviewed. A guide that can't source a claim leaves it out. Nothing here replaces advice from a doctor, physical therapist or occupational therapist, who can measure the right height and fit for one person.</p>
<h2>How to read a guide</h2>
<p>Each guide opens with the official guidance for its category. Then there is one card per pick: the maker's figures in a spec table, why we picked it, what to know before you buy, and who it suits or doesn't. Near the end, an "Our Take" section compares the picks against each other. The sources are listed at the bottom, and every page shows the date it was last updated.</p>
<p>The site is funded by the Amazon Associates program. When you buy through a link here, SeniorSafetyGear may earn a commission at no extra cost to you. That never decides which products we include; stock, safety guidance and the makers' published specs do.</p>
<h2 id="author">About the author</h2>
<p>Oğuz Tokatlı is a full-stack developer who has been researching and writing buying guides since 2018, across kids and baby gear, electronics, outdoor gear, home and garden, and health. Oğuz built SeniorSafetyGear, researches the products and edits every guide before it goes live.</p>
<p>The method is the same on every page: read the maker's specs and manuals and the public safety guidance for the product, check that each pick is in stock in the US, and update guides when products or guidance change. Every fact names its source, listed at the bottom of each page.</p>
<p><a href="https://www.linkedin.com/in/oguz-tokatli/" rel="me noopener" target="_blank">LinkedIn</a> · <a href="https://github.com/oguz463" rel="me noopener" target="_blank">GitHub</a></p>
<h2 id="contact">Contact</h2>
<p>Questions, corrections or a product you'd like us to look at? Email <a href="mailto:hello@seniorsafetygear.com">hello@seniorsafetygear.com</a>. More on our <a href="/contact/">contact page</a>.</p>''',
    ),
    'contact': (
        'Contact SeniorSafetyGear | SeniorSafetyGear',
        'How to reach SeniorSafetyGear with questions, corrections or product suggestions.',
        '''<p>You can reach SeniorSafetyGear by email at <a href="mailto:hello@seniorsafetygear.com">hello@seniorsafetygear.com</a>. Messages go to Oğuz Tokatlı, who writes and edits the site.</p>
<h2>Corrections</h2>
<p>If you spot a mistake, such as a wrong weight limit, an outdated rule or a broken link, please send the page address, what looks wrong and, if you have one, a source. We check corrections against the maker's specs and the official guidance and update the page.</p>
<h2>Product questions and orders</h2>
<p>We don't sell products. Orders, shipping and returns for anything bought through our links are handled by Amazon or the seller named on the listing. For a recall or a safety problem with a product, contact its maker and report it to the U.S. Consumer Product Safety Commission at SaferProducts.gov. We can't give medical advice or choose equipment for a particular person; for that, ask a doctor, physical therapist or occupational therapist.</p>
<h2>Suggestions</h2>
<p>Tell us which equipment you'd like to see compared next.</p>''',
    ),
    'how-we-research': (
        'How We Research | SeniorSafetyGear',
        'How SeniorSafetyGear picks and compares mobility and safety equipment: official guidance, maker pages, stock checks and what we do when sources disagree.',
        '''<p>SeniorSafetyGear guides are desk research, not lab tests. We don't have a testing lab, and we don't claim a product "performed" a certain way. What we do is read the documents that decide whether a product is safe and what it can do, compare them side by side, and tell you where they disagree. Here is the process, step by step.</p>
<h2>1. Start with the guidance, not the product</h2>
<p>Before we look at a single product, we read what public agencies say about that kind of equipment: the CDC's older adult fall prevention pages, the FDA's rules and safety communications for devices such as bed rails, and the CPSC's guidance. The first section of each guide says what that guidance covers and what it doesn't, before any picks appear.</p>
<h2>2. Read the maker's own page</h2>
<p>For each pick we open the maker's product page and manual and take weight limits, dimensions, seat and handle heights, materials and care instructions from there. Retailer listings are written for search, and they are sometimes wrong or out of date. The maker's page is the better source, and each guide lists the pages it used under Sources.</p>
<h2>3. Check the stock</h2>
<p>Every pick was in stock on Amazon for a US delivery address on the day we checked, with delivery to ZIP 10001. Product pages carry an updated date; when a product goes out of stock or guidance changes, the guide is revisited.</p>
<h2>4. Compare the numbers, then say what they mean</h2>
<p>Once the facts are in one place, we compare picks on the numbers that change how you will use the product: a rollator's weight limit and folded width, a shower chair's seat height range, a toilet seat's added height. "Best overall" is our judgment of which pick suits the most households on those facts. It is not an average of star ratings, and it is not the product that pays the highest commission.</p>
<h2>What we do when sources disagree</h2>
<p>We use the maker's number and say so on the card. When the maker is silent on a point, or a model is no longer on the maker's site, the card says so, and we would rather replace a pick than fill the gap with a guess.</p>
<h2>What we leave out</h2>
<ul>
<li><strong>Claims we can't source.</strong> If a figure has no named source, it doesn't go in the guide.</li>
<li><strong>"Medically reviewed" labels.</strong> We don't use them unless a clinician has actually reviewed the text.</li>
<li><strong>Safety promises.</strong> No product prevents falls or injuries by itself. Where a feature is marketed that way, we tell you what the CDC or FDA says instead.</li>
</ul>
<h2>How the site is funded</h2>
<p>SeniorSafetyGear earns a commission through the Amazon Associates program when you buy through our links, at no extra cost to you. That is the only revenue. Our <a href="/disclosure/">affiliate disclosure</a> has the details. Because Amazon is the only retailer we link to, we only include products that Amazon actually has in stock.</p>
<h2>Spot a mistake?</h2>
<p>Email <a href="mailto:hello@seniorsafetygear.com">hello@seniorsafetygear.com</a> with the page, what looks wrong and a source if you have one. We check it against the maker's page or the official guidance and fix the page.</p>''',
    ),
    'privacy': (
        'Privacy Policy | SeniorSafetyGear',
        'SeniorSafetyGear privacy policy.',
        '''<p>SeniorSafetyGear is a static website. It has no accounts, no comments and no forms, and it sets no cookies of its own. We do not run advertising or tracking scripts.</p>
<h2>What we collect</h2>
<p>We do not ask you for any personal information to read the site. If you email <a href="mailto:hello@seniorsafetygear.com">hello@seniorsafetygear.com</a>, we receive your email address and whatever you write, and we use it only to reply. We do not add it to a mailing list or share it.</p>
<h2>Who delivers the site</h2>
<p>The site is delivered through Cloudflare. Like any web host, Cloudflare handles the IP address and browser details of each visit in order to serve pages and block abuse. See <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Cloudflare's privacy policy</a> for how it treats that data.</p>
<h2>Amazon links</h2>
<p>Product links go to Amazon and carry our Associates tag, so Amazon can credit us for a purchase. When you follow one, Amazon may set its own cookies and collects data under <a href="https://www.amazon.com/privacy" rel="noopener">Amazon's privacy notice</a>. We do not see what you do on Amazon. Other outside links, such as manufacturer and government pages, are governed by those sites' own policies.</p>
<h2>Children</h2>
<p>The site is written for adults and caregivers and is not directed at children. We do not knowingly collect information from children.</p>
<h2>Changes</h2>
<p>If we add analytics or any other tool that handles visitor data, we will update this page first.</p>''',
    ),
    'disclosure': (
        'Affiliate Disclosure | SeniorSafetyGear',
        'How SeniorSafetyGear earns money.',
        f'<p>{DISCLOSURE} Links to Amazon on this site are affiliate links. The price you pay is the same.</p>',
    ),
}


TOOLS_NOTES = '''<h2>Which Tool to Use When</h2>
<ul>
<li><strong>Buying a ramp for a step?</strong> Use the <a href="/tools/wheelchair-ramp-length-calculator/">ramp length calculator</a>. It turns the step height into the length the ADA's 1:12 slope needs.</li>
<li><strong>Choosing a raised toilet seat?</strong> Measure your toilet and your ideal seated height, then use the <a href="/tools/raised-toilet-seat-height-calculator/">raised toilet seat height calculator</a>.</li>
<li><strong>Fitting a cane or rollator?</strong> Use the <a href="/tools/cane-and-walker-height-checker/">cane and walker height checker</a> with the height of your wrist crease.</li>
</ul>
<h2>How They Work</h2>
<p>Each calculation runs in your browser, and we do not store what you type. Each tool reads its numbers from a named source: the ADA Standards for ramps, the Joint Replacement Resource Centre's method for raised seats and OrthoInfo's wrist crease rule for canes and walkers. Every tool page lists its sources.</p>
<h2>What They Cannot Tell You</h2>
<p>A calculator gives a starting number from a measurement. It does not know your balance, strength or home. A physical therapist or occupational therapist can fit equipment to you, and the tools here are meant to help you ask the right questions.</p>'''
ARTICLES_NOTES = '''<h2>Where to Start</h2>
<ul>
<li><strong>The bathroom:</strong> the <a href="/articles/bathroom-fall-prevention-checklist/">bathroom fall prevention checklist</a> turns MedlinePlus and CDC advice into seven checks, and <a href="/articles/shower-chair-or-transfer-bench/">shower chair or transfer bench</a> helps you choose between two seats.</li>
<li><strong>Walking aids:</strong> <a href="/articles/cane-walker-or-rollator/">cane, walker or rollator</a> explains the three and gives OrthoInfo's fit and safety rules.</li>
</ul>
<p>Every article names its sources at the bottom and links to the buying guides that compare products.</p>'''
