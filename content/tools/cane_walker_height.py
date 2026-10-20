"""Cane and walker height checker, checked 2026-10-20.

Sources read that day: OrthoInfo (American Academy of Orthopaedic Surgeons) "How To Use Crutches, Canes, and Walkers"
(when standing up straight the top of a cane or walker should reach the crease in your wrist; elbow slightly bent when you hold
the handgrip; the page is about walkers in general). Height ranges are from the makers' pages and Amazon listings in the cane and
rollator guides, checked 2026-10-20: HurryCane 30.5 to 37.5 in (Drive), KINGGEAR 31 to 36 in, DMI 30 to 39 in, Medline offset
29 to 38 in, HONEYBULL 30 to 36 in; rollator handles Drive 7.5 in wheels 30 to 34 in (Drive), Drive aluminum 32 to 37 in
(Drive), Medline steel 31 to 35 in, HOMLAND 33 to 40 in (listing).
"""
import datetime
import json

SLUG = 'cane-and-walker-height-checker'
NAME = 'Cane and Walker Height Checker'
TITLE = 'Cane and Walker Height Checker: Set the Handle to Your Wrist Crease'
SEO_TITLE = 'Cane and Walker Height Checker: Wrist Crease Rule'
DESCRIPTION = 'Enter the height of your wrist crease to see the cane or rollator handle height OrthoInfo advises and which canes and rollators in our guides reach it.'
UPDATED = datetime.date(2026, 10, 20)
RELATED = ['best-canes', 'best-rollators']
PICK_GUIDES = ['best-canes', 'best-rollators']

CANES = [
    ['HurryCane Freedom Edition', 30.5, 37.5, 'best-canes/hurrycane-freedom-edition'],
    ['KINGGEAR quad cane', 31, 36, 'best-canes/kinggear-self-standing-quad-cane'],
    ['DMI adjustable cane', 30, 39, 'best-canes/dmi-adjustable-walking-cane'],
    ['Medline offset cane', 29, 38, 'best-canes/medline-aluminum-offset-cane'],
    ['HONEYBULL folding cane', 30, 36, 'best-canes/honeybull-foldable-free-standing-cane'],
]
ROLLATORS = [
    ['Drive rollator, 7.5 in wheels', 30, 34, 'best-rollators/drive-rollator-7-5-inch-wheels'],
    ['Drive aluminum rollator', 32, 37, 'best-rollators/drive-aluminum-rollator'],
    ['Medline steel rollator', 31, 35, 'best-rollators/medline-steel-rollator'],
    ['HOMLAND extra-wide rollator', 33, 40, 'best-rollators/homland-extra-wide-rollator'],
]

INTRO = '''<p>OrthoInfo, the American Academy of Orthopaedic Surgeons' patient site, gives one rule for fitting a cane or a walker: when you stand up straight, the top of the handle should reach the crease in your wrist, and your elbow should be slightly bent when you hold it. Measure the height of your wrist crease and enter it below to see which products in our guides reach it.</p>'''

WIDGET = '''<form id="cw" onsubmit="return false">
<div class="row">
<div><label for="cwh">Wrist crease height in inches (stand up straight in your usual shoes, let your arm hang, measure from the floor to the crease)</label><input id="cwh" type="number" min="20" max="50" step="0.25" inputmode="decimal" value="33"></div>
</div>
<div class="result" id="cwo" aria-live="polite"></div>
</form>'''

SCRIPT = 'var CANES = ' + json.dumps(CANES) + ', ROLLATORS = ' + json.dumps(ROLLATORS) + ''';
(function () {
  var h = document.getElementById('cwh'), out = document.getElementById('cwo');
  function fits(list, v) { return list.filter(function (x) { return v >= x[1] && v <= x[2]; }); }
  function update() {
    var v = parseFloat(h.value);
    if (!(v > 0)) { out.innerHTML = 'Enter the height in inches.'; return; }
    var c = fits(CANES, v), r = fits(ROLLATORS, v);
    var msg = '<span class="big">Set the handle to about ' + v + ' in</span>OrthoInfo says the top should reach your wrist crease when you stand up straight.';
    msg += '<br>' + (c.length ? renderPicks(c.map(function (x) { return x[3]; }), 'Canes whose height range reaches ' + v + ' in:') : '<strong>No cane in our guide reaches this height.</strong>') + '<a href="/best-canes/">See the cane guide</a>.';
    msg += '<br>' + (r.length ? renderPicks(r.map(function (x) { return x[3]; }), 'Rollators whose handle range reaches ' + v + ' in:') : '<strong>No rollator in our guide reaches this height.</strong>') + '<a href="/best-rollators/">See the rollator guide</a>.';
    msg += '<br>Check that your elbow is slightly bent when you hold the grip, and ask a physical therapist to confirm if it feels wrong.';
    out.innerHTML = msg;
  }
  h.addEventListener('input', update); update();
})();'''

BODY = '''<h2>How to Measure Your Wrist Crease Height</h2>
<ol>
<li>Put on the shoes you wear most.</li>
<li>Stand up straight beside a wall with your arms hanging at your sides.</li>
<li>Have someone measure from the floor to the crease in your wrist, where the hand meets the forearm.</li>
<li>Enter the number above.</li>
</ol>
<p>OrthoInfo says that when you stand up straight, the top of the cane or walker should reach the crease in your wrist, and your elbows should be slightly bent when you hold the handgrips. It tells you to hold a cane in the hand opposite the side that needs support.</p>
<p class="note"><strong>Height ranges are not the whole fit.</strong> The ranges in our guides come from the makers' pages and listings. A cane that reaches your number still has to feel right in your hand, and a rollator should be checked while you walk with it. Ask a physical therapist if you are unsure.</p>
<h2>Cane and Walker Height Questions</h2>
<h3>Does the same rule work for a rollator?</h3>
<p>OrthoInfo's page covers walkers in general and does not name rollators, but the wrist crease check applies to any handle you lean on.</p>
<h3>What if my number is outside every range?</h3>
<p>Look at the cane and rollator guides for taller or shorter products, or ask the maker. Do not use a handle that is set far from your wrist crease.</p>'''

SOURCES = [
    ('OrthoInfo (AAOS): How To Use Crutches, Canes, and Walkers', 'https://www.orthoinfo.org/recovery/how-to-use-crutches-canes-and-walkers'),
    ('Drive Medical at Home: HurryCane Freedom Edition', 'https://drivemedicalathome.com/products/hurrycane-freedom-edition'),
    ('Drive Medical: 4 Wheel Rollator with 7.5 in Casters 10257BL-1', 'https://shop.drivemedical.com/us/en/p/10257bl-1'),
    ('Drive Medical: Aluminum Rollator R726BL', 'https://shop.drivemedical.com/us/en/p/r726bl'),
]
