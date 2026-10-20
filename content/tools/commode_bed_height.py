"""Bedside commode height finder, checked 2026-10-20.

Height ranges are from the buying guide: Drive Folding Steel Commode RTL11158KDR 17 to 23 in (Drive's page), Medline Drop Arm
Commode 18 to 22 in (Amazon listing), DMI Drop Arm Extra-Wide Commode 20 to 24 in (Amazon listing). The Drive 11148-1 and the Medline
3-in-1 list no seat-height range in the text we read and are left out. We found no agency rule for commode seat height; setting the
seat level with the bed edge or slightly above is our fitting advice for sliding across. CDC "Check for Safety" 2017 checklist
(bedrooms: a lamp close to the bed, a nightlight on the path to the bathroom). MedlinePlus "Bathroom safety for adults" (review date
2026-04-09) names a commode chair as one way to raise the toilet seat height.
"""
import datetime
import json

SLUG = 'bedside-commode-height-finder'
NAME = 'Bedside Commode Height Finder'
TITLE = 'Bedside Commode Height Finder: Match the Seat to Your Bed'
SEO_TITLE = 'Bedside Commode Height Finder: Match a Commode to Your Bed'
DESCRIPTION = 'Enter your bed height to see which bedside commodes in our guide have a seat-height range that reaches it.'
UPDATED = datetime.date(2026, 10, 20)
RELATED = ['best-bedside-commodes', 'best-bed-assist-rails']
PICK_GUIDES = ['best-bedside-commodes']

COMMODES = [
    ['Drive Folding Steel Commode RTL11158KDR', 17, 23, 'best-bedside-commodes/drive-folding-steel-3-in-1-commode'],
    ['Medline Drop Arm Commode', 18, 22, 'best-bedside-commodes/medline-drop-arm-commode'],
    ['DMI Drop Arm Extra-Wide Commode', 20, 24, 'best-bedside-commodes/dmi-drop-arm-extra-wide-commode'],
]

INTRO = '''<p>A bedside commode is easiest to use when its seat sits level with the edge of the bed, or a little above it, so you slide across and stand without a drop. Measure the height of your mattress from the floor, enter it below, and the finder lists the commodes in our guide whose seat-height range reaches it.</p>'''

WIDGET = '''<form id="cb" onsubmit="return false">
<div class="row">
<div><label for="bh">Bed height in inches (floor to the top of the mattress, uncompressed)</label><input id="bh" type="number" min="12" max="40" step="0.25" inputmode="decimal" value="21"></div>
</div>
<div class="result" id="cbo" aria-live="polite"></div>
</form>'''

SCRIPT = 'var COMMODES = ' + json.dumps(COMMODES) + ''';
(function () {
  var h = document.getElementById('bh'), out = document.getElementById('cbo');
  function update() {
    var v = parseFloat(h.value);
    if (!(v > 0)) { out.innerHTML = 'Enter the bed height in inches.'; return; }
    var ok = COMMODES.filter(function (c) { return v >= c[1] && v <= c[2]; });
    var msg = '<span class="big">Seat level with a ' + v + ' in bed</span>';
    if (ok.length) msg += renderPicks(ok.map(function (c) { return c[3]; }), 'Commodes in our guide whose seat can reach ' + v + ' in:') + '<a href="/best-bedside-commodes/">See the full guide</a>.';
    else msg += 'None of the three commodes with a listed range reaches ' + v + ' in. The Drive 11148-1 and the Medline 3-in-1 list no range, so ask the maker. <a href="/best-bedside-commodes/">See the guide</a>.';
    msg += '<br>Set all four legs to the same hole, and check the push pins are locked.';
    out.innerHTML = msg;
  }
  h.addEventListener('input', update); update();
})();'''

BODY = '''<h2>How to Measure Your Bed</h2>
<p>Measure from the floor to the top of the mattress at the edge where you get out. If the mattress is soft, measure with your weight off it. Enter the number above and compare it with the seat-height ranges.</p>
<p>The ranges come from Drive's page for the RTL11158KDR, 17 to 23 inches, and from the Medline drop arm and DMI listings, 18 to 22 and 20 to 24 inches. The Drive 11148-1 and the Medline 3-in-1 list no range in the text we read, so they are left out of the results.</p>
<p>We found no agency rule for commode seat height. Setting the seat level with the bed edge or a little above is our fitting advice. If standing is difficult, a therapist can say whether a higher seat or a different transfer suits you.</p>
<h2>Making the Night Walk Safer</h2>
<p>The CDC's "Check for Safety" checklist suggests a lamp close to the bed, so you do not have to reach for the light, and a nightlight on the path from the bed to the bathroom. MedlinePlus names a commode chair as one way to raise the toilet seat height, which it says can help prevent falls.</p>
<p class="note"><strong>Check the bed too.</strong> A commode next to a bed that moves or slides is a hazard. If you use a bed rail, our <a href="/best-bed-assist-rails/">bed assist rail guide</a> explains the CPSC rule for adult portable bed rails.</p>
<h2>Commode Height Questions</h2>
<h3>What if my bed is higher than every commode's range?</h3>
<p>The highest range in our guide is 24 inches, on the DMI. Ask a therapist about a lower bed or a different transfer, or look at commodes with a higher range.</p>
<h3>Do drop arms change the height I need?</h3>
<p>Not the seat height, but they let you slide across without lifting over an arm. The Medline drop arm and the DMI have them.</p>'''

SOURCES = [
    ('Drive Medical: Folding Steel Commode RTL11158KDR', 'https://shop.drivemedical.com/us/en/p/rtl11158kdr'),
    ('CDC: Check for Safety, A Home Fall Prevention Checklist for Older Adults (2017)', 'https://www.cdc.gov/steadi/pdf/STEADI-Brochure-CheckForSafety-508.pdf'),
    ('MedlinePlus: Bathroom safety for adults (reviewed 2026-04-09)', 'https://medlineplus.gov/ency/patientinstructions/000021.htm'),
]
