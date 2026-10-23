"""How Steep Is Too Steep for a Home Ramp, checked 2026-10-20.

Sources read that day: U.S. Access Board, 2010 ADA Standards for Accessible Design, section 405 Ramps (403.3 running slope of walking surfaces not steeper than 1:20 and the definition of a ramp as steeper than 1:20; 405.2 running slope not
steeper than 1:12; Table 405.2 allows slopes up to 1:8 in existing sites where space is limited, with a rise limit of 6 in for
slopes steeper than 1:12 up to 1:10 and 3 in for steeper than 1:10 up to 1:8, and prohibits slopes steeper than 1:8; 405.3 cross
slope not steeper than 1:48; 405.5 clear width 36 in; 405.6 rise 30 in maximum per run; 405.7 landings 60 in long, 60 by 60 in
where the ramp turns; 405.8 handrails on runs with a rise over 6 in; 405.9 edge protection on each side; the ADA Standards govern
public and commercial buildings, not private homes). Listed step heights and prices (checked 2026-10-20) are from the Amazon listings in the ramp guide; the Access Board page was re-read 2026-10-23. Hero photo: Pexels 35831406 by DΛVΞ GΛRCIΛ.
Pexels 37043590 by Eugene Lee.
"""
import datetime

SLUG = 'how-steep-is-too-steep-for-a-home-ramp'
TOPIC = 'Ramps'
TITLE = 'How Steep Is Too Steep for a Home Ramp? The ADA 1:12 Rule Explained'
SEO_TITLE = 'Wheelchair Ramp Slope Chart and the ADA 1:12 Rule'
DESCRIPTION = 'A slope chart in ratio, percent and degrees, what a 1:12 slope means in inches, the steeper slopes the ADA allows for small rises, the 30-inch limit per run and the handrail and landing rules.'
PUBLISHED = datetime.date(2026, 10, 20)
UPDATED = datetime.date(2026, 10, 23)
UPDATES = [(datetime.date(2026, 10, 23), 'Added a slope chart in ratio, percent and degrees, the ramp length for a 12-inch or 12-foot rise, and portable ramp price per foot.'), (datetime.date(2026, 10, 21), 'Added a worked table from step height to ramp length and answers on slope, landings and home use.')]
PHOTO = 'ramp-slope'
PHOTO_ALT = 'wheelchair-accessible white van with its side doors open, traffic cones on the road and a driver standing nearby'
PHOTO_CREDIT = 'DΛVΞ GΛRCIΛ (Pexels)'
RELATED = ['best-wheelchair-ramps']

TAKEAWAYS = [
    'The ADA Standards set the limit at a slope of <strong>1:12</strong>: 12 inches of ramp for every 1 inch of rise.',
    'A <strong>3-inch step needs 36 inches</strong> of ramp, and a 6-inch step needs 72.',
    'Steeper slopes, up to 1:8, are allowed only for <strong>small rises in existing sites</strong>, and nothing steeper than 1:8.',
    'The ADA asks for <strong>handrails</strong> when the rise is over 6 inches, and a <strong>36-inch</strong> clear width.',
    'Portable ramp listings often claim <strong>steeper slopes</strong> than the ADA rule allows.',
]

BODY = '''<p>A ramp is a trade between how high you must climb and how far you must travel to climb it. The 2010 ADA Standards, published by the U.S. Access Board, pin that trade down with a number: a ramp run should have a running slope not steeper than 1:12. The ADA covers public and commercial buildings and does not bind a private home, but it is the clearest published rule for how steep a ramp should be.</p>

<h2>What 1:12 Means in Inches</h2>
<p>A slope of 1:12 means that for every 1 inch of rise, the ramp is 12 inches long. Multiply the rise by 12 to get the length.</p>
<table class="art-table"><thead><tr><th>Step height</th><th>Ramp length at 1:12</th></tr></thead><tbody>
<tr><td>2 inches</td><td>24 inches (2 feet)</td></tr>
<tr><td>3 inches</td><td>36 inches (3 feet)</td></tr>
<tr><td>6 inches</td><td>72 inches (6 feet)</td></tr>
<tr><td>8 inches</td><td>96 inches (8 feet)</td></tr>
<tr><td>12 inches</td><td>144 inches (12 feet)</td></tr>
</tbody></table>
<p>Our <a href="/tools/wheelchair-ramp-length-calculator/">ramp length calculator</a> does the multiplication and lists the portable ramps in our guide that are long enough.</p>

<h2>Ramp Slope Chart: Ratio, Percent, Degrees</h2>
<p>Ramp slopes are written three ways: as a ratio (1:12), as a percent grade (rise divided by run, times 100) and as an angle in degrees. This chart converts the slopes you will see in listings and codes. The percent and degree values are our own arithmetic from the ratio.</p>
<table class="art-table"><thead><tr><th>Ratio</th><th>Percent grade</th><th>Angle</th><th>Rise per foot of ramp</th><th>ADA status</th></tr></thead><tbody>
<tr><td>1:20</td><td>5%</td><td>2.9&deg;</td><td>0.6 in</td><td>Not a ramp: the ADA treats a walking surface at 1:20 or flatter as level ground</td></tr>
<tr><td>1:16</td><td>6.25%</td><td>3.6&deg;</td><td>0.75 in</td><td>Steeper than 1:20, so it counts as a ramp, and gentler than the 1:12 limit</td></tr>
<tr><td>1:12</td><td>8.33%</td><td>4.8&deg;</td><td>1 in</td><td>The ADA maximum for a ramp run</td></tr>
<tr><td>1:10</td><td>10%</td><td>5.7&deg;</td><td>1.2 in</td><td>Existing sites only, for a rise of 6 in or less</td></tr>
<tr><td>1:8</td><td>12.5%</td><td>7.1&deg;</td><td>1.5 in</td><td>Existing sites only, for a rise of 3 in or less. Nothing steeper is allowed</td></tr>
<tr><td>1:6</td><td>16.67%</td><td>9.5&deg;</td><td>2 in</td><td>Steeper than the ADA allows</td></tr>
<tr><td>1:4</td><td>25%</td><td>14.0&deg;</td><td>3 in</td><td>Steeper than the ADA allows. About the slope of a short portable ramp on a 9 in step</td></tr>
</tbody></table>
<p>The ADA defines a ramp as a walking surface with a running slope steeper than 1:20, and its advisory text encourages the least possible running slope. The 1:12 line is the limit, not the target: a gentler slope is easier for a person pushing a chair up it.</p>

<h2>When Steeper Is Allowed</h2>
<p>For existing sites where space is limited, the ADA allows steeper slopes, but only for small rises. A slope steeper than 1:12 up to 1:10 is allowed for a rise of 6 inches or less, and a slope steeper than 1:10 up to 1:8 for a rise of 3 inches or less. Anything steeper than 1:8 is prohibited. The cross slope, the tilt from side to side, should not be steeper than 1:48.</p>

<h2>The Other ADA Numbers</h2>
<ul>
<li><strong>Rise per run:</strong> 30 inches at most. A higher step needs landings and more than one run.</li>
<li><strong>Landings:</strong> 60 inches long at the top and bottom, and 60 by 60 inches where the ramp changes direction.</li>
<li><strong>Clear width:</strong> 36 inches minimum. The portable ramps in our guide are about 29 inches wide.</li>
<li><strong>Handrails:</strong> required on ramp runs with a rise greater than 6 inches.</li>
<li><strong>Edges:</strong> edge protection on each side of the ramp and landings.</li>
</ul>

<h2>What the Listings Say</h2>
<p>The Amazon listings for portable ramps give step heights that are much steeper than 1:12. The VNN 3-foot ramp lists 3 to 9 inches, which at its 36-inch length is as steep as 1:4. The VNN 6-foot lists 6 to 18 inches and the WHALEMOTOR 8-foot lists 8 to 24 inches, also reaching 1:4. A ramp that steep is hard to push a chair up and easy to tip, and it is outside what the ADA allows. Use the 1:12 rule to choose the length, and treat the listing's range as an outer limit.</p>
<p class="note"><strong>Check your chair too.</strong> A ramp that is steeper than you can push is not a solution, even if the listing says it will take the load. A physical therapist or occupational therapist can say how steep a slope you or a helper can manage.</p>

<h2>Which Ramp for Which Step</h2>
<p>For a 2 or 3 inch threshold, a 2 or 3 foot portable ramp matches the rule. For a 6-inch porch step, you need about 6 feet, and for 8 inches about 8 feet. Above 6 inches, the ADA also asks for handrails, which portable ramps do not have. Our <a href="/best-wheelchair-ramps/">wheelchair ramp guide</a> compares five ramps from 2 to 8 feet.</p>

<h2>Worked Examples: From Step Height to Ramp Length</h2>
<p>At a slope of 1:12 the ramp length is the rise times 12. The ADA allows a rise of up to 30 inches in a single run, so longer steps need landings and more than one run.</p>
<table class="art-table"><thead><tr><th>Rise</th><th>Ramp length at 1:12</th><th>What else applies</th></tr></thead><tbody>
<tr><td>4 inches</td><td>48 inches (4 feet)</td><td>No handrail needed, since the rise is 6 inches or less</td></tr>
<tr><td>10 inches</td><td>120 inches (10 feet)</td><td>Handrails, since the rise is over 6 inches</td></tr>
<tr><td>18 inches</td><td>216 inches (18 feet)</td><td>Handrails, edge protection and a 60-inch landing at each end</td></tr>
<tr><td>30 inches</td><td>360 inches (30 feet)</td><td>The longest single run the ADA allows</td></tr>
<tr><td>40 inches</td><td>Two runs: 30 feet and 10 feet</td><td>A 60 by 60 inch landing where the ramp turns</td></tr>
</tbody></table>
<p>The 40-inch row shows how it works: the first run takes the maximum 30 inches of rise over 30 feet, a landing follows, and the second run covers the last 10 inches over 10 feet. The table is our own arithmetic from the ADA numbers, and it assumes you can fit the run.</p>

<h2>Ramp Questions</h2>
<h3>Does the ADA apply to my home?</h3>
<p>No. The ADA Standards govern public and commercial buildings. They are still the clearest published rule on slope, and they are a sensible target for a home ramp.</p>
<h3>Can a 3-foot ramp handle a 6-inch step?</h3>
<p>Not at the ADA's slope. A 6-inch rise needs 72 inches, or 6 feet. A 3-foot ramp over a 6-inch step would be 1:6, steeper than the ADA allows.</p>
<h3>What about the steeper slopes the ADA allows?</h3>
<p>Only in existing sites with limited space, and only for small rises: up to 1:10 for a rise of 6 inches or less, and up to 1:8 for a rise of 3 inches or less. A 3-inch rise at 1:8 is 24 inches of ramp, against 36 inches at 1:12.</p>
<h3>What ramp length do I need for a 12-foot height?</h3>
<p>It depends on whether you mean 12 inches or 12 feet. A rise of 12 inches needs 144 inches, or 12 feet, of ramp at 1:12. A rise of 12 feet is 144 inches, which at 1:12 needs 1,728 inches, or 144 feet, of ramp. The ADA allows a rise of 30 inches per run, so 144 inches of rise takes five runs with landings between them, and the landings add length. Few homes have the room for that, so a lift or a different entrance is the usual alternative, and a contractor or an occupational therapist can say which fits.</p>
<h3>How much does a ramp cost?</h3>
<p>For a portable ramp, multiply the length you need by the price per foot. On the Amazon listings in our ramp guide, checked on 2026-10-20, the price per foot of ramp ranged from about $25 to about $44:</p>
<table class="art-table"><thead><tr><th>Ramp</th><th>Listed price</th><th>Length</th><th>Price per foot</th></tr></thead><tbody>
<tr><td>VEVOR 3FT</td><td>$73.63</td><td>3 ft</td><td>$24.54</td></tr>
<tr><td>VNN 3FT</td><td>$115.99</td><td>3 ft</td><td>$38.66</td></tr>
<tr><td>VNN 6FT</td><td>$249.99</td><td>6 ft</td><td>$41.67</td></tr>
<tr><td>FACHNUO 2FT</td><td>$86.98</td><td>2 ft</td><td>$43.49</td></tr>
<tr><td>WHALEMOTOR 8FT</td><td>$349.99</td><td>8 ft</td><td>$43.75</td></tr>
</tbody></table>
<p>Prices change, so check the listing. We do not quote a cost for a permanent ramp built at a house, because the price depends on materials, the rise and local labor, and we found no published figure we trust. Ask for written quotes. Our <a href="/articles/does-medicare-pay-for-mobility-equipment/">Medicare article</a> covers what insurance does and does not pay for.</p>
<h3>Who can check the slope for my chair?</h3>
<p>A physical or occupational therapist can say how steep a slope you or a helper can manage, which can be gentler than the ADA limit.</p>'''

SOURCES = [
    ('U.S. Access Board: 2010 ADA Standards for Accessible Design, section 405 Ramps', 'https://www.access-board.gov/ada/'),
]
