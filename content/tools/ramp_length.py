"""Wheelchair ramp length calculator, checked 2026-10-20.

Sources read that day: U.S. Access Board, 2010 ADA Standards for Accessible Design, section 405 Ramps (405.2 running slope not
steeper than 1:12; Table 405.2 allows steeper slopes up to 1:8 in existing sites where space is limited, with a rise limit of
6 in for slopes steeper than 1:12 up to 1:10 and 3 in for steeper than 1:10 up to 1:8, and prohibits slopes steeper than 1:8;
405.6 rise 30 in maximum per run; 405.7 landings 60 in long; 405.8 handrails on runs with a rise over 6 in; 405.5 clear width
36 in minimum). The ADA Standards govern public and commercial buildings, not private homes. Section 504.2 Treads and Risers (read 2026-11-08: risers 4 in minimum and 7 in maximum, treads 11 in minimum). Ramp lengths and listed step
heights are from the Amazon listings used in the wheelchair ramp guide, checked 2026-10-20.
"""
import datetime
import json

SLUG = 'wheelchair-ramp-length-calculator'
NAME = 'Wheelchair Ramp Length Calculator'
TITLE = 'Wheelchair Ramp Length Calculator: How Long a Ramp for Your Step?'
SEO_TITLE = 'Wheelchair Ramp Length Calculator: 1:12 Slope by Step Height'
DESCRIPTION = 'Enter your step height, or see the table by number of steps, for the ramp length the ADA 1:12 slope needs and which portable ramps in our guide are long enough.'
UPDATED = datetime.date(2026, 11, 8)
UPDATES = [(datetime.date(2026, 11, 8), 'Added a table of ramp length by number of steps and answers for 2, 3, 4 and 5 steps and a 4-foot height.'), (datetime.date(2026, 10, 23), 'Added the number of runs and landings for rises over 30 inches, and answers on a 12-foot height and cost per foot.'), (datetime.date(2026, 10, 21), 'Added a worked table of step heights against the portable ramps in our guide.')]
RELATED = ['best-wheelchair-ramps', 'best-transport-wheelchairs', 'best-mobility-scooters']
PICK_GUIDES = ['best-wheelchair-ramps']

# (name, length in inches, listed step heights) from the wheelchair ramp guide
RAMPS = [
    ['FACHNUO 2FT', 24, '2 to 6 in', 'best-wheelchair-ramps/fachnuo-2ft-portable-ramp'],
    ['VNN 3FT', 36, '3 to 9 in', 'best-wheelchair-ramps/vnn-3ft-portable-ramp'],
    ['VEVOR 3FT', 36, '3 to 6 in', 'best-wheelchair-ramps/vevor-3ft-portable-ramp'],
    ['VNN 6FT', 72, '6 to 18 in', 'best-wheelchair-ramps/vnn-6ft-portable-ramp'],
    ['WHALEMOTOR 8FT', 96, '8 to 24 in', 'best-wheelchair-ramps/whalemotor-8ft-portable-ramp'],
]

INTRO = '''<p>A ramp has to be long enough for the height of the step. The ADA Standards set the limit at a slope of 1:12, which means 12 inches of ramp for every 1 inch of rise. Enter your step height below and the calculator gives the length that slope needs, plus the portable ramps in our guide that are long enough.</p>'''

WIDGET = '''<form id="rl" onsubmit="return false">
<div class="row">
<div><label for="rr">Step height in inches (ground to top of step)</label><input id="rr" type="number" min="0.5" max="60" step="0.25" inputmode="decimal" value="4"></div>
</div>
<div class="result" id="rlo" aria-live="polite"></div>
</form>'''

SCRIPT = 'var RAMPS = ' + json.dumps(RAMPS) + ''';
(function () {
  var r = document.getElementById('rr'), out = document.getElementById('rlo');
  function ft(inches) { var f = Math.floor(inches / 12), i = Math.round(inches - f * 12); return (f ? f + ' ft ' : '') + (i || !f ? i + ' in' : '').trim(); }
  function update() {
    var rise = parseFloat(r.value);
    if (!(rise > 0)) { out.innerHTML = 'Enter the step height in inches.'; return; }
    var len = rise * 12, msg = '<span class="big">' + ft(len) + ' of ramp</span>At the ADA slope of 1:12, a ' + rise + ' in step needs ' + len + ' in (' + (len / 12).toFixed(1) + ' ft) of ramp.';
    if (rise > 30) msg += ' <strong>The ADA allows a rise of 30 in at most for one ramp run,</strong> so this step needs ' + Math.ceil(rise / 30) + ' runs with ' + (Math.ceil(rise / 30) - 1) + ' landing' + (Math.ceil(rise / 30) > 2 ? 's' : '') + ' between them, and the landings add length.';
    if (rise > 6) msg += ' The ADA also asks for handrails on ramp runs with a rise over 6 in, and portable ramps do not have them.';
    var fit = RAMPS.filter(function (x) { return x[1] >= len; });
    if (fit.length) { msg += '<br>' + renderPicks(fit.map(function (x) { return x[3]; }), 'Ramps in our guide that are long enough at 1:12:') + '<a href="/best-wheelchair-ramps/">See the full ramp guide</a>.'; }
    else { msg += '<br>None of the portable ramps in our guide is long enough. The longest, the 8 ft WHALEMOTOR (96 in), suits a rise up to 8 in at 1:12.'; }
    if (rise <= 3) msg += '<br>For an existing site with no room, the ADA allows steeper slopes only for small rises: up to 1:10 for 6 in or less, and up to 1:8 for 3 in or less.';
    out.innerHTML = msg;
  }
  r.addEventListener('input', update); update();
})();'''

BODY = '''<h2>How the Calculation Works</h2>
<p>The ADA Standards say a ramp run should have a running slope not steeper than 1:12. That means the ramp length in inches is the rise in inches times 12. A 2-inch step needs 24 inches, a 3-inch step 36 inches, a 6-inch step 72 inches and an 8-inch step 96 inches.</p>
<p>In an existing site where space is limited, the ADA allows steeper slopes, up to 1:8, but only for small rises. A slope steeper than 1:12 up to 1:10 is allowed for a rise of 6 inches or less, and a slope steeper than 1:10 up to 1:8 for a rise of 3 inches or less. Anything steeper than 1:8 is prohibited.</p>
<h2>Other ADA Ramp Numbers</h2>
<ul>
<li><strong>Rise:</strong> 30 inches at most for one run.</li>
<li><strong>Clear width:</strong> 36 inches minimum. Portable ramps in our guide are about 29 inches wide.</li>
<li><strong>Landings:</strong> 60 inches long at the top and bottom, and 60 by 60 inches where the ramp turns.</li>
<li><strong>Handrails:</strong> required on ramp runs with a rise over 6 inches.</li>
<li><strong>Edges:</strong> edge protection on both sides.</li>
</ul>
<p class="note"><strong>The ADA covers public and commercial buildings.</strong> A private home does not have to follow it, but the 1:12 rule is the clearest published guide to a slope a chair user and a helper can manage. The listings for portable ramps say they work at steeper slopes, so use this calculator to choose the length, not the listing's step height range.</p>
<h2>Ramp Length Questions</h2>
<h3>How long a ramp do I need for a 4-inch step?</h3>
<p>48 inches, or 4 feet, at 1:12. Our guide's 3-foot ramps are too short for 4 inches at that slope, and the 6-foot ramp is longer than needed.</p>
<h3>Can I use a shorter ramp?</h3>
<p>The ADA allows steeper slopes only for small rises in existing sites, and prohibits anything steeper than 1:8. A steeper ramp is harder to push up and easier to tip on.</p>
<h3>Do I need a handrail?</h3>
<p>The ADA asks for handrails on ramp runs with a rise over 6 inches. The portable ramps in our guide have side baffles, not handrails.</p>

<h2>Ramp Length by Number of Steps</h2>
<p>If you only know how many steps there are, multiply the steps by the height of one riser to get the rise, then by 12. The ADA Standards (section 504.2) set stair risers at 4 inches minimum and 7 inches maximum, so a flight of ADA stairs rises at most 7 inches a step. The table uses 6 and 7 inches as two examples, with the ramp length at 1:12 (1 foot of ramp per inch of rise). Measure your own risers, since yours may fall outside that range.</p>
<table class="art-table"><thead><tr><th>Steps</th><th>Ramp with 6 in risers</th><th>Ramp with 7 in risers</th><th>Runs at 7 in</th></tr></thead><tbody><tr><td>1</td><td>6 ft (6 in rise)</td><td>7 ft (7 in rise)</td><td>1</td></tr><tr><td>2</td><td>12 ft (12 in rise)</td><td>14 ft (14 in rise)</td><td>1</td></tr><tr><td>3</td><td>18 ft (18 in rise)</td><td>21 ft (21 in rise)</td><td>1</td></tr><tr><td>4</td><td>24 ft (24 in rise)</td><td>28 ft (28 in rise)</td><td>1</td></tr><tr><td>5</td><td>30 ft (30 in rise)</td><td>35 ft (35 in rise)</td><td>2</td></tr><tr><td>6</td><td>36 ft (36 in rise)</td><td>42 ft (42 in rise)</td><td>2</td></tr></tbody></table>
<p>A rise of more than 30 inches needs more than one run, with a 60-inch landing between runs (ADA sections 405.6 and 405.7). The landings add to the lengths above. Measuring the total height from the ground to the door threshold is more accurate than counting steps, so enter that in the calculator.</p>

<h2>Worked Examples</h2>
<table class="art-table"><thead><tr><th>Step height</th><th>Length at 1:12</th><th>Portable ramps in our guide that are long enough</th></tr></thead><tbody><tr><td>2 in</td><td>24 in (2 ft)</td><td>FACHNUO 2FT, VNN 3FT, VEVOR 3FT, VNN 6FT, WHALEMOTOR 8FT</td></tr><tr><td>3 in</td><td>36 in (3 ft)</td><td>VNN 3FT, VEVOR 3FT, VNN 6FT, WHALEMOTOR 8FT</td></tr><tr><td>4 in</td><td>48 in (4 ft)</td><td>VNN 6FT, WHALEMOTOR 8FT</td></tr><tr><td>6 in</td><td>72 in (6 ft)</td><td>VNN 6FT, WHALEMOTOR 8FT</td></tr><tr><td>8 in</td><td>96 in (8 ft)</td><td>WHALEMOTOR 8FT</td></tr></tbody></table>
<p>The 12-inches-per-inch rule is the ADA's, and portable ramp listings often claim steeper slopes. Our article on <a href="/articles/how-steep-is-too-steep-for-a-home-ramp/">ramp slope</a> explains the ADA numbers and how longer rises need landings.</p>
<h2>More Ramp Questions</h2>
<h3>How long should a ramp be for 2 steps?</h3>
<p>With 7-inch risers, 2 steps rise 14 inches, which needs 168 inches, or 14 feet, of ramp at 1:12. With 6-inch risers it is 12 inches of rise and 12 feet of ramp.</p>
<h3>How long should a ramp be for 3 steps?</h3>
<p>3 steps of 7 inches rise 21 inches and need 252 inches, or 21 feet. With 6-inch risers it is 18 feet.</p>
<h3>How long should a ramp be for 4 steps?</h3>
<p>4 steps of 7 inches rise 28 inches and need 336 inches, or 28 feet, in one run. With 6-inch risers it is 24 feet.</p>
<h3>How long should a ramp be for 5 steps?</h3>
<p>5 steps of 7 inches rise 35 inches, which is over the 30-inch limit for one run, so it needs two runs with a landing between them. The ramp is 420 inches, or 35 feet, plus the landing. With 6-inch risers the rise is exactly 30 inches, so 30 feet in one run.</p>
<h3>How long a ramp for a 4-foot height?</h3>
<p>4 feet is 48 inches of rise, which at 1:12 needs 576 inches, or 48 feet, of ramp, in two runs with a landing between them. If you mean a 4-inch rise, it needs 48 inches, or 4 feet.</p>
<h3>What ramp length do I need for a 12-foot height?</h3>
<p>A rise of 12 feet is 144 inches, which at 1:12 needs 1,728 inches, or 144 feet, of ramp, in five runs with landings between them. If you mean a 12-inch rise, it needs 144 inches, or 12 feet. Enter the height in inches above to see either.</p>
<h3>How much does a portable ramp cost per foot?</h3>
<p>On the Amazon listings in our ramp guide, checked on 2026-10-20, between about $25 and $44 per foot of ramp. Multiply the length you need by that to estimate a portable ramp. The <a href="/articles/how-steep-is-too-steep-for-a-home-ramp/">ramp slope article</a> has the per-foot table.</p>
<h3>Does the ADA apply to a home ramp?</h3>
<p>No, the ADA Standards govern public and commercial buildings, but they are a clear target for a home.</p>'''

SOURCES = [
    ('U.S. Access Board: 2010 ADA Standards for Accessible Design, sections 405 Ramps and 504 Stairways', 'https://www.access-board.gov/ada/'),
]
