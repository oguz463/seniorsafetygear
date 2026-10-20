"""Does Medicare Pay for Mobility Equipment, checked 2026-10-20.

Sources read that day: Medicare.gov "Durable medical equipment (DME) coverage" (after the deductible you pay 20% of the
Medicare-approved amount if your supplier accepts assignment; "Make sure your doctors and DME suppliers are enrolled in Medicare";
Medicare will only pay for DME items from suppliers enrolled in Medicare; Part B covers equipment if your doctor or other health care
provider orders it for use in your home; the page does not mention lift chairs or seat lifts, and its list of covered DME "isn't
limited to" the items named). University of Utah Health "Adaptive Equipment Following Joint Replacement" (adaptive equipment such as
sock aids "is not typically covered by insurance"). No Medicare page on scooters, wheelchairs or walkers was read, and secondary
sites on lift chair coverage were not used. Hero photo: Pexels 18681259 by Momo.
"""
import datetime

SLUG = 'does-medicare-pay-for-mobility-equipment'
TOPIC = 'Costs'
TITLE = 'Does Medicare Pay for Mobility Equipment? What Medicare.gov Says'
SEO_TITLE = 'Does Medicare Pay for Mobility Equipment? Medicare.gov Rules'
DESCRIPTION = 'What Medicare.gov says about durable medical equipment: the 20% share, enrolled suppliers and a provider\'s order, and what it does not say about lift chairs.'
PUBLISHED = datetime.date(2026, 10, 20)
UPDATED = datetime.date(2026, 10, 20)
PHOTO = 'mobility-scooters'
PHOTO_ALT = 'person riding a four-wheel mobility scooter away along a gravel path with a flag on the back and tail lights on'
PHOTO_CREDIT = 'Momo (Pexels)'
RELATED = ['best-mobility-scooters', 'best-lift-chairs']

TAKEAWAYS = [
    'Medicare.gov says that after the deductible you pay <strong>20% of the Medicare-approved amount</strong> if the supplier accepts assignment.',
    'The supplier must be <strong>enrolled in Medicare</strong>, and your provider must <strong>order the equipment</strong> for use at home.',
    'Medicare.gov\'s DME page <strong>does not mention lift chairs or seat lifts</strong>.',
    'University of Utah Health says dressing aids like sock aids are <strong>not typically covered by insurance</strong>.',
    'Ask <strong>before you buy</strong>, and keep the provider\'s order.',
]

BODY = '''<p>Mobility equipment can cost hundreds of dollars, and the first question is who pays. Medicare.gov has a page on durable medical equipment, or DME, that sets out the basic rules. It is short, and it leaves out several products people ask about. This article says what the page says, and what it does not.</p>

<h2>What Medicare.gov Says About DME</h2>
<p>Medicare.gov's "Durable medical equipment (DME) coverage" page makes three points that matter before you buy anything.</p>
<ul>
<li><strong>Your share.</strong> After the Part B deductible, you pay 20% of the Medicare-approved amount if your supplier accepts assignment.</li>
<li><strong>The supplier.</strong> The page tells you to make sure your doctors and DME suppliers are enrolled in Medicare, and says Medicare will only pay for DME items from suppliers who are enrolled.</li>
<li><strong>The order.</strong> Part B covers the equipment if your doctor or other health care provider orders it for use in your home.</li>
</ul>
<p>The page says its list of covered equipment "isn't limited to" the items it names. It does not say which products a given beneficiary will get, and it does not set out medical conditions.</p>

<h2>What the Page Does Not Say</h2>
<p>Medicare.gov's DME page does not mention lift chairs or seat lifts, so we could not confirm any coverage from it. Several websites offer opinions on lift chair coverage, but we did not use them, because they are not Medicare's own guidance. The page also does not discuss scooters, transport chairs or the other products in our guides. If you are buying one of them, ask Medicare directly.</p>
<p class="note"><strong>Ask before you buy.</strong> Call 1-800-MEDICARE or your plan, and ask your doctor whether the equipment can be ordered. Buying first and asking later can leave you paying the full amount.</p>

<h2>Things Insurance Usually Does Not Cover</h2>
<p>University of Utah Health says adaptive equipment after joint replacement, such as a sock aid or a reacher, is not typically covered by insurance, so you buy it yourself. That likely applies to many small aids, and it is a reason to check before you spend. Grab bars, shower chairs and raised toilet seats are in the same category in practice, because our guides found no Medicare page about them.</p>

<h2>A Short Checklist</h2>
<ol class="steps">
<li><strong>Ask your doctor</strong> whether the equipment can be ordered for use in your home.</li>
<li><strong>Check the supplier</strong> is enrolled in Medicare and accepts assignment.</li>
<li><strong>Ask what the cost will be</strong> after the deductible, and in writing if you can.</li>
<li><strong>Keep the order and receipts</strong> in case you are asked for them.</li>
<li><strong>Compare with the products in our guides</strong> if you decide to buy on your own.</li>
</ol>

<h2>Where to Look Next</h2>
<p>If you are comparing products, see our guides to <a href="/best-mobility-scooters/">mobility scooters</a> and <a href="/best-lift-chairs/">lift chairs</a>. They compare size, weight and features, and say plainly that they rest on Amazon listings and that Medicare.gov does not mention lift chairs.</p>'''

SOURCES = [
    ('Medicare.gov: Durable medical equipment (DME) coverage', 'https://www.medicare.gov/coverage/durable-medical-equipment-dme-coverage'),
    ('University of Utah Health: Adaptive Equipment Following Joint Replacement', 'https://healthcare.utah.edu/orthopaedics/specialties/joint-replacement/patient-guide/adaptive-equipment'),
]
