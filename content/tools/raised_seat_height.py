"""Raised toilet seat height calculator, checked 2026-10-20.

Sources read that day: Joint Replacement Resource Centre (E. Katz), hosted by the Winnipeg Regional Health Authority, "How to
Measure for a Raised Toilet Seat" (feet on the floor, hips ideally higher than knees on a slope of about 2 inches; if knees
are higher than hips it is much harder to get off the toilet; measure the height of the toilet from the floor to the top of
the bowl without the seat or lid; find a seated surface where feet are flat and hips are about 2 inches above knees and measure
it; the height of the raised seat is that total minus the toilet height, for example 19 in minus 15 in is a 4 in seat; if hips
and knees are level a 2 to 3 inch seat may work; note round or elongated; allow for footwear height). MedlinePlus "Bathroom
safety for adults" (review date 2026-04-09: raising the toilet seat height can help prevent falls). Seat heights are from the
Amazon listings in the raised toilet seat guide, checked 2026-10-20.
"""
import datetime
import json

SLUG = 'raised-toilet-seat-height-calculator'
NAME = 'Raised Toilet Seat Height Calculator'
TITLE = 'Raised Toilet Seat Height Calculator: How Many Inches Do You Need?'
SEO_TITLE = 'Raised Toilet Seat Height Calculator: Find Your Rise in Inches'
DESCRIPTION = 'Enter your toilet height and your ideal seated height to see how many inches a raised toilet seat should add, and which seats in our guide come closest.'
UPDATED = datetime.date(2026, 10, 21)
UPDATES = [(datetime.date(2026, 10, 21), 'Added a worked example table based on the Joint Replacement Resource Centre measuring method.')]
RELATED = ['best-raised-toilet-seats', 'best-bedside-commodes', 'best-grab-bars']
PICK_GUIDES = ['best-raised-toilet-seats']

SEATS = [
    ['Bemis Assurance 3 in', 3, 'elongated', 'best-raised-toilet-seats/bemis-assurance-3-inch'],
    ['Vive with handles 3.5 in', 3.5, 'elongated', 'best-raised-toilet-seats/vive-raised-toilet-seat-with-handles'],
    ['Carex with arms 3.5 in', 3.5, 'elongated', 'best-raised-toilet-seats/carex-raised-toilet-seat-with-arms'],
    ['AquaSense 4 in', 4, 'round', 'best-raised-toilet-seats/aquasense-4-inch-riser'],
    ['HealthSmart 5 in', 5, 'round', 'best-raised-toilet-seats/healthsmart-5-inch-padded-riser'],
]

INTRO = '''<p>A raised toilet seat should add enough height that your feet are flat on the floor and your hips sit a little higher than your knees. The Joint Replacement Resource Centre gives a two-measurement method, and this calculator does the subtraction. Measure your toilet, find a seat where you sit comfortably, measure that, and enter both below.</p>'''

WIDGET = '''<form id="rs" onsubmit="return false">
<div class="row">
<div><label for="rt">Toilet height in inches (floor to top of the bowl, without the seat or lid)</label><input id="rt" type="number" min="8" max="30" step="0.25" inputmode="decimal" value="15"></div>
<div><label for="ri">Your ideal seated height in inches (floor to the top of a seat where your feet are flat and your hips are about 2 in above your knees)</label><input id="ri" type="number" min="8" max="34" step="0.25" inputmode="decimal" value="19"></div>
</div>
<div class="result" id="rso" aria-live="polite"></div>
</form>'''

SCRIPT = 'var SEATS = ' + json.dumps(SEATS) + ''';
(function () {
  var t = document.getElementById('rt'), i = document.getElementById('ri'), out = document.getElementById('rso');
  function update() {
    var toilet = parseFloat(t.value), ideal = parseFloat(i.value);
    if (!(toilet > 0) || !(ideal > 0)) { out.innerHTML = 'Enter both measurements in inches.'; return; }
    var need = ideal - toilet, msg;
    if (need <= 0) { out.innerHTML = '<span class="big">No raised seat needed</span>Your toilet is already as high as your ideal seated height. A raised seat would put your hips well above your knees.'; return; }
    msg = '<span class="big">' + need.toFixed(2).replace(/\\.?0+$/, '') + ' inches</span>Seat height needed: your ideal seated height of ' + ideal + ' in minus your toilet height of ' + toilet + ' in.';
    var near = SEATS.map(function (s) { return [s, Math.abs(s[1] - need)]; }).sort(function (a, b) { return a[1] - b[1]; }).slice(0, 3);
    msg += '<br>' + renderPicks(near.map(function (x) { return x[0][3]; }), 'Closest seats in our guide (' + near.map(function (x) { return x[0][1] + ' in, ' + x[0][2]; }).join('; ') + '):') + '<a href="/best-raised-toilet-seats/">See the full guide</a>.';
    if (need < 2) msg += '<br>The Joint Replacement Resource Centre says a 2 to 3 inch seat may work if your hips and knees are level when seated. Under 2 inches, check with a therapist.';
    if (need > 5) msg += '<br>Our picks add at most 5 inches. A bedside commode over the toilet can add more, so see our <a href="/best-bedside-commodes/">bedside commode guide</a>.';
    msg += '<br>Wear the shoes you use when you measure, and check whether your bowl is round or elongated.';
    out.innerHTML = msg;
  }
  [t, i].forEach(function (el) { el.addEventListener('input', update); }); update();
})();'''

BODY = '''<h2>How to Take the Two Measurements</h2>
<ol>
<li><strong>Toilet height.</strong> Measure from the floor to the top of the toilet bowl, not the seat or lid.</li>
<li><strong>Ideal seated height.</strong> Sit on a bed or chair where your feet are flat on the floor and your hips are about 2 inches above your knees, wearing the shoes you wear to the bathroom. Measure from the floor to the top of the seat.</li>
<li><strong>Subtract.</strong> The raised seat's height is your ideal seated height minus the toilet height. The handout's example is 19 inches minus 15 inches, which means a 4-inch seat.</li>
</ol>
<p>The Joint Replacement Resource Centre says that if your knees are higher than your hips it is much harder to get off the toilet, and that if your hips and knees are level, a 2 to 3 inch seat may work. MedlinePlus says raising the toilet seat height can help prevent falls.</p>
<p class="note"><strong>Check the bowl shape too.</strong> Round and elongated bowls need different seats. Ask a doctor, physical therapist or occupational therapist if you are unsure, especially after a hip or knee replacement.</p>
<h2>Raised Seat Height Questions</h2>
<h3>What height do the seats in your guide add?</h3>
<p>The Bemis Assurance adds 3 inches, the Vive and Carex 3.5, the AquaSense 4 and the HealthSmart 5, according to the makers' pages and listings.</p>
<h3>What if I need more than 5 inches?</h3>
<p>A bedside commode used over the toilet is higher. See our <a href="/best-bedside-commodes/">bedside commode guide</a>, and ask a therapist.</p>

<h2>Worked Examples</h2>
<p>The method from the Joint Replacement Resource Centre is to find a seat height where your feet are flat and your hips sit about 2 inches above your knees, then subtract the toilet's height.</p>
<table class="art-table"><thead><tr><th>Comfortable seat height</th><th>Toilet height</th><th>Raised seat needed</th></tr></thead><tbody>
<tr><td>17 in</td><td>15 in</td><td>2 in</td></tr>
<tr><td>19 in</td><td>15 in</td><td>4 in</td></tr>
<tr><td>21 in</td><td>15 in</td><td>6 in</td></tr>
</tbody></table>
<p>The seats in our guide rise 3 to 5 inches. The 19-inch case needs 4 inches, which the AquaSense matches. The 17-inch case needs a 2-inch rise, below the lowest seat in the guide. The same source says that if your hips and knees are level, a 2 to 3 inch seat may work. The 21-inch case needs more than 5 inches, which is why a bedside commode or a different aid may suit better.</p>
<h2>More Seat Questions</h2>
<h3>Does footwear change the number?</h3>
<p>The source suggests allowing for the height of the footwear you wear when you measure.</p>
<h3>Round or elongated?</h3>
<p>Check your bowl and note whether it is round or elongated, since our guide lists the shape of each seat.</p>'''

SOURCES = [
    ('Joint Replacement Resource Centre (Winnipeg Regional Health Authority): How to Measure for a Raised Toilet Seat', 'https://wrha.mb.ca/files/joint-replacement-how-to-measure-rts.pdf'),
    ('MedlinePlus: Bathroom safety for adults (reviewed 2026-04-09)', 'https://medlineplus.gov/ency/patientinstructions/000021.htm'),
    ('Vive Health: Toilet Seat Riser with Arms', 'https://www.vivehealth.com/products/raised-toilet-seat-with-handles'),
]
