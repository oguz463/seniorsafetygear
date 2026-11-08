"""Shower seat height finder, checked 2026-10-20.

Height ranges are from the buying guide: HOMLAND shower stool 14 to 19 in (Amazon listing), Medline backless shower chair with
arms 16 to 21 in (Amazon listing), Drive Medical transfer tub bench 17.5 to 22.5 in (Drive's page). The Medline chair with arms and
back and the Drive bath bench with back adjust in 1 in steps but their listings and pages give no full range in the text we read, so
they are left out. The ADA range is the only published seat height we found, and it covers public buildings; the home check used is feet flat on the tub floor with knees about
level with hips, which is our fitting advice and not a published standard. U.S. Access Board 2010 ADA Standards read
2026-11-08: 610.2 the top of bathtub seats 17 in minimum and 19 in maximum above the bathroom finish floor, a removable in-tub seat 15 to
16 in deep; 610.3 the top of a shower compartment seat the same 17 to 19 in; 610.4 250 lb of force at any point; the ADA governs public
and commercial buildings, not private homes. MedlinePlus "Bathroom safety for adults" (review date
2026-04-09) advises sitting on a bath chair or bench when taking a shower.
"""
import datetime
import json

SLUG = 'shower-seat-height-finder'
NAME = 'Shower Seat Height Finder'
TITLE = 'Shower Seat Height Finder: Which Chair Adjusts to Your Leg?'
SEO_TITLE = 'Shower Seat Height Finder: Match a Chair to Your Leg Length'
DESCRIPTION = 'The ADA puts bathtub and shower seats 17 to 19 inches high. Enter your floor-to-knee height to see which shower chairs in our guide adjust to it.'
UPDATED = datetime.date(2026, 11, 8)
UPDATES = [(datetime.date(2026, 11, 8), 'Added the ADA Standards range of 17 to 19 inches for bathtub and shower seats, and which listed seats reach it.'), (datetime.date(2026, 10, 21), 'Added a worked table of seat heights against the shower seats with a listed range.')]
RELATED = ['best-shower-chairs', 'best-grab-bars']
PICK_GUIDES = ['best-shower-chairs']

SEATS = [
    ['HOMLAND stool', 14, 19, 'best-shower-chairs/homland-adjustable-shower-stool'],
    ['Medline backless chair with arms', 16, 21, 'best-shower-chairs/medline-backless-shower-chair-with-arms'],
    ['Drive transfer bench', 17.5, 22.5, 'best-shower-chairs/drive-tub-transfer-bench'],
]

INTRO = '''<p><strong>The standard height for a shower seat is 17 to 19 inches</strong> above the floor, measured to the top of the seat. That is the range in the ADA Standards for bathtub seats (section 610.2) and shower compartment seats (section 610.3). The ADA covers public and commercial buildings, not private homes, so for your own bathroom treat it as a reference point.</p>
<p>A shower seat that is too low makes standing harder, and one that is too high leaves your feet dangling. The usual fitting check is a seat that puts your feet flat on the tub floor with your knees about level with your hips. That check is our practical advice, not a published standard. Measure from the floor to the back of your knee while you sit with your feet flat, enter it below, and the finder lists the seats in our guide that adjust to that height.</p>'''

WIDGET = '''<form id="sh" onsubmit="return false">
<div class="row">
<div><label for="sk">Floor to the back of your knee, in inches (sitting, feet flat, bare feet)</label><input id="sk" type="number" min="10" max="30" step="0.25" inputmode="decimal" value="17"></div>
</div>
<div class="result" id="sho" aria-live="polite"></div>
</form>'''

SCRIPT = 'var SEATS = ' + json.dumps(SEATS) + ''';
(function () {
  var k = document.getElementById('sk'), out = document.getElementById('sho');
  function update() {
    var v = parseFloat(k.value);
    if (!(v > 0)) { out.innerHTML = 'Enter the height in inches.'; return; }
    var ok = SEATS.filter(function (s) { return v >= s[1] && v <= s[2]; });
    var msg = '<span class="big">Aim for a seat about ' + v + ' in high</span>';
    if (ok.length) msg += renderPicks(ok.map(function (s) { return s[3]; }), 'Seats in our guide whose listed range reaches ' + v + ' in:') + '<a href="/best-shower-chairs/">See the full guide</a>.';
    else msg += 'None of the three seats with a listed range reaches ' + v + ' in. The Medline chair with arms and back and the Drive bath bench with back adjust in 1 in steps but list no full range, so check their boxes. <a href="/best-shower-chairs/">See the guide</a>.';
    msg += '<br>Set the height before you get wet, and check the leg pins are locked.';
    out.innerHTML = msg;
  }
  k.addEventListener('input', update); update();
})();'''

BODY = '''<h2>How to Measure</h2>
<ol>
<li>Sit on a firm chair with your bare feet flat on the floor and your knees bent about 90 degrees.</li>
<li>Measure from the floor to the back of your knee, where your thigh meets the seat edge.</li>
<li>Enter the number above. A seat at that height should put your feet flat and your knees about level with your hips.</li>
</ol>
<p>MedlinePlus advises sitting on a bath chair or bench when you take a shower. It does not give a seat height. The ADA Standards do, at 17 to 19 inches, but only for public and commercial buildings, so the fitting check above is our advice for a home. If you have had a hip or knee replacement, ask your surgeon or therapist for the height they want, because some recoveries call for a higher seat.</p>
<h2>What the ADA Standards Say</h2>
<p>The U.S. Access Board's 2010 ADA Standards say the top of a bathtub seat shall be 17 inches minimum and 19 inches maximum above the bathroom finish floor (section 610.2). A removable in-tub seat shall be 15 to 16 inches deep. Section 610.3 gives the same 17 to 19 inches for a seat in a shower compartment, and section 610.4 asks the seat, its fasteners and its mounting to withstand 250 pounds of force at any point. The standards govern public and commercial buildings, so a home seat does not have to meet them.</p>
<h2>Which Seats Have a Listed Range</h2>
<p>The HOMLAND stool is listed at 14 to 19 inches in 1-inch steps. The Medline backless chair with arms is listed at 16 to 21 inches, and Drive's page lists 17.5 to 22.5 inches for its transfer bench. The Medline chair with arms and back and the Drive bath bench with back adjust in 1-inch steps, but the text we read gives no full range, so they are not in the results.</p>
<p class="note"><strong>Set the height before you get wet.</strong> Push the pins through the holes on all four legs and press down on the seat. A seat that shifts on a wet floor is the hazard to avoid.</p>
<h2>Shower Seat Height Questions</h2>
<h3>Should the seat be higher if standing is hard?</h3>
<p>A higher seat shortens the distance you push up, but your feet should still reach the floor. A therapist can set the height that suits your legs and any surgery precautions.</p>
<h3>Does a transfer bench use the same measurement?</h3>
<p>A transfer bench sits across the tub wall, so its height also has to clear the tub edge. Drive's page lists 17.5 to 22.5 inches. See our <a href="/articles/shower-chair-or-transfer-bench/">shower chair or transfer bench article</a>.</p>

<h2>Worked Examples</h2>
<table class="art-table"><thead><tr><th>Seat height</th><th>Fits</th></tr></thead><tbody><tr><td>15 in</td><td>HOMLAND stool</td></tr><tr><td>17 in</td><td>HOMLAND stool, Medline backless chair with arms</td></tr><tr><td>18 in</td><td>HOMLAND stool, Medline backless chair with arms, Drive transfer bench</td></tr><tr><td>20 in</td><td>Medline backless chair with arms, Drive transfer bench</td></tr><tr><td>22 in</td><td>Drive transfer bench</td></tr></tbody></table>
<p>The ADA range of 17 to 19 inches sits inside the listed range of the HOMLAND and the Medline chair, and the Drive transfer bench reaches it from 17.5 inches. At 18 inches all three listed seats can be set to your number. At the ends of the scale the choice narrows to one product, so confirm the adjustment steps in the listing.</p>
<h2>More Shower Seat Questions</h2>
<h3>Where does the guidance come from?</h3>
<p>MedlinePlus advises sitting on a bath chair or bench when you take a shower. The 17 to 19 inch range comes from the ADA Standards, sections 610.2 and 610.3, which govern public and commercial buildings. The height check, feet flat on the tub floor with knees about level with hips, is our fitting advice and not a published standard.</p>
<h3>Why are some seats missing?</h3>
<p>The Medline chair with arms and back and the Drive bath bench with back adjust in 1-inch steps, but their pages give no full range in the text we read, so they are left out.</p>'''

SOURCES = [
    ('U.S. Access Board: 2010 ADA Standards for Accessible Design, section 610 Seats', 'https://www.access-board.gov/ada/'),
    ('MedlinePlus: Bathroom safety for adults (reviewed 2026-04-09)', 'https://medlineplus.gov/ency/patientinstructions/000021.htm'),
    ('Drive Medical: Transfer Tub Bench 12011KD-1', 'https://shop.drivemedical.com/us/en/p/12011kd-1'),
]
