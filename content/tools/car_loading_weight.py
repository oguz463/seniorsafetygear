"""Car loading weight checker, checked 2026-10-20.

Weights are from the buying guides: rollators (Drive aluminum 13 lb and Drive 7.5 in wheels 18.5 lb from Drive's pages; Medline
steel 16.5 lb, HOMLAND 20.4 lb and VOCIC about 22.85 lb from Amazon listings), transport wheelchairs (Medline Ultra Lightweight 15
lb listing; Drive Fly-Lite 18.9 lb with footrests, Drive page; Drive ATC19 21 lb, the details-table figure; Drive economy 26 lb,
Drive page; Medline with 12 in wheels 26 lb listing) and mobility scooters (heaviest piece or lift weight: SuperHandy Passport frame
27 lb, Vive rear section 29 lb, Rascal Venture heaviest piece 29.5 lb, Iris 3 lift weight 30 lb with seat and batteries removed;
listings). The Hoverfly T3 is left out because its listing gives no piece weight. These are product-listing and maker figures, not
tested weights.
"""
import datetime
import json

SLUG = 'car-loading-weight-checker'
NAME = 'Car Loading Weight Checker'
TITLE = 'Car Loading Weight Checker: Can You Lift It Into the Trunk?'
SEO_TITLE = 'Car Loading Weight Checker: Rollators, Chairs and Scooters'
DESCRIPTION = 'Enter the most you can lift to see which rollators, transport wheelchairs and scooter pieces in our guides weigh that much or less.'
UPDATED = datetime.date(2026, 10, 20)
RELATED = ['best-rollators', 'best-transport-wheelchairs', 'best-mobility-scooters']
PICK_GUIDES = ['best-rollators', 'best-transport-wheelchairs', 'best-mobility-scooters']

WEIGHTS = {
    'rollator': ['Rollators', '/best-rollators/', 'total weight', [[13, 'best-rollators/drive-aluminum-rollator'], [16.5, 'best-rollators/medline-steel-rollator'], [18.5, 'best-rollators/drive-rollator-7-5-inch-wheels'], [20.4, 'best-rollators/homland-extra-wide-rollator'], [22.85, 'best-rollators/vocic-z21-all-terrain-rollator']]],
    'transport': ['Transport wheelchairs', '/best-transport-wheelchairs/', 'weight with footrests', [[15, 'best-transport-wheelchairs/medline-ultra-lightweight-transport-chair'], [18.9, 'best-transport-wheelchairs/drive-fly-lite-transport-chair'], [21, 'best-transport-wheelchairs/drive-atc19-transport-chair'], [26, 'best-transport-wheelchairs/drive-economy-transport-chair'], [26, 'best-transport-wheelchairs/medline-transport-chair-12-inch-wheels']]],
    'scooter': ['Mobility scooters', '/best-mobility-scooters/', 'heaviest piece', [[27, 'best-mobility-scooters/superhandy-passport-mobility-scooter'], [29, 'best-mobility-scooters/vive-3-wheel-mobility-scooter'], [29.5, 'best-mobility-scooters/rascal-venture-3-wheel-scooter'], [30, 'best-mobility-scooters/iris-3-lightweight-mobility-scooter']]],
}

INTRO = '''<p>A walking aid or scooter that you cannot lift into a car is no use outside the house. Enter the most you or your helper can lift comfortably, choose the kind of product, and the checker lists the picks in our guides that weigh that much or less. For scooters it uses the heaviest single piece, since that is what you lift.</p>'''

_opts = ''.join(f'<option value="{k}">{v[0]}</option>' for k, v in WEIGHTS.items())
WIDGET = f'''<form id="cl" onsubmit="return false">
<div class="row">
<div><label for="ck">Product type</label><select id="ck">{_opts}</select></div>
<div><label for="cw">The most you can lift, in pounds</label><input id="cw" type="number" min="5" max="100" step="0.5" inputmode="decimal" value="20"></div>
</div>
<div class="result" id="clo" aria-live="polite"></div>
</form>'''

SCRIPT = 'var WEIGHTS = ' + json.dumps(WEIGHTS) + ''';
(function () {
  var k = document.getElementById('ck'), w = document.getElementById('cw'), out = document.getElementById('clo');
  function update() {
    var cat = WEIGHTS[k.value], lim = parseFloat(w.value);
    if (!(lim > 0)) { out.innerHTML = 'Enter a weight in pounds.'; return; }
    var ok = cat[3].filter(function (p) { return p[0] <= lim; });
    var msg = '<span class="big">' + lim + ' lb limit</span>';
    if (ok.length) msg += renderPicks(ok.map(function (p) { return p[1]; }), cat[0] + ' in our guide with a ' + cat[2] + ' of ' + lim + ' lb or less:') + '<a href="' + cat[1] + '">See the full guide</a>.';
    else msg += 'None of the ' + cat[0].toLowerCase() + ' in our guide has a ' + cat[2] + ' of ' + lim + ' lb or less. The lightest is ' + Math.min.apply(null, cat[3].map(function (p) { return p[0]; })) + ' lb. <a href="' + cat[1] + '">See the guide</a>.';
    msg += '<br>Weights are the makers\\' or listings\\' figures. Try lifting before you buy.';
    out.innerHTML = msg;
  }
  [k, w].forEach(function (el) { el.addEventListener('input', update); el.addEventListener('change', update); });
  update();
})();'''

BODY = '''<h2>What the Weights Mean</h2>
<p>For a rollator, the figure is the whole rollator. For a transport wheelchair, it includes the footrests, which swing away or come off, so you can lift the frame and the footrests separately. For a scooter, it is the heaviest piece after the scooter comes apart or folds: the SuperHandy Passport's frame is 27 pounds, the Vive's rear section 29, the Rascal Venture's heaviest piece 29.5 and the Iris 3 lifts at 30 pounds with the seat and batteries removed.</p>
<p>The weights come from the makers' pages where we could read them, such as Drive's 13 pounds for its aluminum rollator and 18.9 pounds with footrests for the Fly-Lite, and from Amazon listings otherwise. The Hoverfly scooter is left out because its listing gives no piece weight.</p>
<p class="note"><strong>Lift it before you buy if you can.</strong> A number in pounds does not tell you how the weight is shaped, how high you must lift it or how awkward the handle is. Ask a physical therapist if lifting is a concern for you, and remember that a helper can lift it for you.</p>
<h2>Car Loading Questions</h2>
<h3>What if every product is too heavy?</h3>
<p>Look at the lighter classes. The lightest rollator in our guide is 13 pounds, the lightest transport chair 15 pounds and the lightest scooter piece 27 pounds. A cane weighs about a pound, so it may do the job if you need only a little support.</p>
<h3>Does the folded size matter too?</h3>
<p>Yes. A trunk has a width and a depth. Our guides give folded sizes where the maker or listing gives them, such as 33 by 9 by 28 inches for the Fly-Lite with its riggings.</p>'''

SOURCES = [
    ('Drive Medical: Aluminum Rollator R726BL', 'https://shop.drivemedical.com/us/en/p/r726bl'),
    ('Drive Medical: 4 Wheel Rollator with 7.5 in Casters 10257BL-1', 'https://shop.drivemedical.com/us/en/p/10257bl-1'),
    ('Drive Medical: Fly-Lite Aluminum Transport Chair DFL19-BLK', 'https://shop.drivemedical.com/us/en/p/dfl19-blk'),
    ('Drive Medical: Trans Chair Econ 17 in TR37E-SV', 'https://shop.drivemedical.com/us/en/p/tr37e-sv'),
]
