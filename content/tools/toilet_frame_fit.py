"""Toilet safety frame fit checker, checked 2026-10-20.

Fit rules are from the Amazon listings in the toilet safety frame guide: HOMLAND B0DK97XB99 fits two-hole toilets with 5.5 in bolt
spacing and a base at least 3 in deep, width 24 to 25.6 in; Vive B0DXNBZQ7C needs at least 2 in between the seat bolt holes and the
tank, is for flat-tank toilets with a fixed bolted seat and excludes curved tanks, smart and bidet toilets and quick-release hinges;
Vaunn B0FP3N943S is free-standing, width 19 to 24 in, and the listing says it fits round, elongated and one-piece toilets; Carex
B00354B818 width 16 to 18 in; Medline B000BJBH48 lists no width and is left out of the width test. The checker treats a frame as
wide enough when the top of its width range is at least the outside width of the seat. That rule is our own reading of the
listings, not a maker rule. We found no standard for toilet safety frames.
"""
import datetime
import json

SLUG = 'toilet-safety-frame-fit-checker'
NAME = 'Toilet Safety Frame Fit Checker'
TITLE = 'Toilet Safety Frame Fit Checker: Will It Fit Your Toilet?'
SEO_TITLE = 'Toilet Safety Frame Fit Checker: Which Frames Fit?'
DESCRIPTION = 'Enter your toilet\'s width, bolt spacing, tank gap and seat type to see which toilet safety frames in our guide the listings say will fit.'
UPDATED = datetime.date(2026, 10, 20)
RELATED = ['best-toilet-safety-frames', 'best-raised-toilet-seats']
PICK_GUIDES = ['best-toilet-safety-frames']

INTRO = '''<p>Toilet safety frames fail for dull reasons: the bolts are the wrong distance apart, the tank is too close or the arms do not open wide enough. Measure four things on your toilet, enter them below, and the checker lists the frames in our guide whose Amazon listings say they fit.</p>'''

WIDGET = '''<form id="tf" onsubmit="return false">
<div class="row">
<div><label for="tw">Outside width of the seat in inches</label><input id="tw" type="number" min="10" max="30" step="0.25" inputmode="decimal" value="15"></div>
<div><label for="tg">Gap from the seat bolt holes to the tank in inches</label><input id="tg" type="number" min="0" max="12" step="0.25" inputmode="decimal" value="2.5"></div>
</div>
<div class="row">
<div><label for="tb">Bolt spacing</label><select id="tb"><option value="55">5.5 in, two holes</option><option value="other">Something else or not sure</option></select></div>
<div><label for="tt">Toilet type</label><select id="tt"><option value="plain">Flat tank, fixed bolted seat</option><option value="odd">Curved tank, bidet seat or quick-release hinge</option></select></div>
</div>
<div class="result" id="tfo" aria-live="polite"></div>
</form>'''

SCRIPT = '''(function () {
  var w = document.getElementById('tw'), g = document.getElementById('tg'), b = document.getElementById('tb'), t = document.getElementById('tt'), out = document.getElementById('tfo');
  function update() {
    var wv = parseFloat(w.value), gv = parseFloat(g.value);
    if (!(wv > 0) || isNaN(gv)) { out.innerHTML = 'Enter the width and the gap in inches.'; return; }
    var keys = [], notes = [];
    if (wv <= 24) keys.push('best-toilet-safety-frames/vaunn-folding-toilet-safety-frame'); else notes.push('The Vaunn opens to 24 in, narrower than your seat.');
    if (wv <= 18) keys.push('best-toilet-safety-frames/carex-toilet-safety-frame'); else notes.push('The Carex opens to 18 in, narrower than your seat.');
    if (wv <= 25.6 && b.value === '55') keys.push('best-toilet-safety-frames/homland-aluminum-toilet-safety-rail');
    else notes.push(b.value === '55' ? 'The HOMLAND opens to 25.6 in, narrower than your seat.' : 'The HOMLAND listing asks for 5.5 in bolt spacing.');
    if (gv >= 2 && t.value === 'plain') keys.push('best-toilet-safety-frames/vive-flip-up-toilet-safety-rail');
    else notes.push(t.value === 'plain' ? 'The Vive listing asks for at least 2 in between the bolt holes and the tank.' : 'The Vive listing excludes curved tanks, bidet seats and quick-release hinges.');
    keys.push('best-toilet-safety-frames/medline-toilet-safety-rail');
    var msg = '<span class="big">' + keys.length + ' frame' + (keys.length === 1 ? '' : 's') + ' to check for your toilet</span>';
    msg += renderPicks(keys, 'Frames whose listings fit these measurements:');
    msg += '<br>The Medline lists no width, so confirm it with the seller. ' + notes.join(' ');
    out.innerHTML = msg;
  }
  [w, g, b, t].forEach(function (e) { e.addEventListener('input', update); e.addEventListener('change', update); }); update();
})();'''

BODY = '''<h2>What to Measure</h2>
<ul>
<li><strong>Outside width of the seat.</strong> Measure the widest point of the seat from side to side. The arms must sit outside it.</li>
<li><strong>Gap to the tank.</strong> Measure from the seat bolt holes to the front of the tank. The Vive listing asks for at least 2 inches.</li>
<li><strong>Bolt spacing.</strong> Most toilets have two bolt holes. The HOMLAND listing asks for 5.5 inches between them and a base at least 3 inches deep.</li>
<li><strong>Toilet type.</strong> The Vive listing excludes curved or irregular tanks, smart and bidet toilets and seats with quick-release hinges.</li>
</ul>
<h2>How the Checker Decides</h2>
<p>It follows the listings on Amazon. A free-standing frame is shown when the top of its width range is at least the width of your seat, and a bolted frame is shown only when your toilet meets the conditions in its listing. That width rule is our own reading, and we found no standard for toilet safety frames. The Medline listing gives no width, so it is always shown with a note to check with the seller.</p>
<p class="note"><strong>Check before you rely on it.</strong> Weight ratings are the sellers' figures. Push on each arm and check that the frame does not move before you use it, and ask a therapist if you are unsure whether a frame is the right aid. Our <a href="/best-toilet-safety-frames/">toilet safety frame guide</a> compares all five.</p>
<h2>Fit Questions</h2>
<h3>What if my toilet has a quick-release seat?</h3>
<p>The Vive listing excludes seats with quick-release hinges, and the HOMLAND frame uses the seat screws. A free-standing frame needs no fitting, so start with the Vaunn if the width suits.</p>
<h3>Does a raised seat change the fit?</h3>
<p>It can. A raised seat changes the seat height and may change the gap to the tank, so measure again with the raised seat on. See our <a href="/tools/raised-toilet-seat-height-calculator/">raised toilet seat calculator</a>.</p>'''

SOURCES = [
    ('MedlinePlus: Bathroom safety for adults (reviewed 2026-04-09)', 'https://medlineplus.gov/ency/patientinstructions/000021.htm'),
]
