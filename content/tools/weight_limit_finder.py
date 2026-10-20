"""Weight limit finder, checked 2026-10-20.

Limits are the figures in the buying guides (maker pages where we could read them, Amazon listings otherwise), and where a
maker page and a listing disagree the lower figure is used: Drive transfer bench 350 lb (the Drive page says 400); HOMLAND
shower stool 300 lb (listing: 400 lb frame, 300 lb recommended user weight); VOCIC Z21 350 lb (listing: recommended user
weight); WHALEMOTOR ramp 606 lb (title says 800); Iris 3 scooter 265 lb including cargo. Products with no stated limit in the
text we read are left out: HOMLAND rollator, HONEYBULL cane, Medline and Medical King bed rails, Hoverfly scooter, the lift
chairs. No agency sets a safe margin above a product's limit, so the finder compares the limit with the weight you enter and
tells you to add what you carry. Sources: the Drive Medical, Vive and HurryCane pages listed below, plus the Amazon listings
named in each guide.
"""
import datetime
import json

SLUG = 'weight-limit-finder'
NAME = 'Weight Limit Finder'
TITLE = 'Weight Limit Finder: Which Mobility Products Hold Your Weight?'
SEO_TITLE = 'Weight Limit Finder: Walkers, Shower Seats, Commodes and More'
DESCRIPTION = 'Enter your weight and what you carry to see which rollators, shower chairs, commodes, scooters, transport chairs, canes, ramps and raised seats in our guides list a high enough limit.'
UPDATED = datetime.date(2026, 10, 20)
RELATED = ['best-rollators', 'best-shower-chairs', 'best-bedside-commodes', 'best-mobility-scooters', 'best-transport-wheelchairs']
PICK_GUIDES = ['best-rollators', 'best-shower-chairs', 'best-bedside-commodes', 'best-mobility-scooters', 'best-transport-wheelchairs',
               'best-raised-toilet-seats', 'best-toilet-safety-frames', 'best-canes', 'best-wheelchair-ramps', 'best-bed-assist-rails']

LIMITS = {
    'rollator': ['Rollators', '/best-rollators/', [[350, 'best-rollators/drive-rollator-7-5-inch-wheels'], [300, 'best-rollators/drive-aluminum-rollator'], [350, 'best-rollators/medline-steel-rollator'], [350, 'best-rollators/vocic-z21-all-terrain-rollator']]],
    'shower': ['Shower chairs and benches', '/best-shower-chairs/', [[350, 'best-shower-chairs/medline-shower-chair-with-arms-and-back'], [350, 'best-shower-chairs/drive-tub-transfer-bench'], [300, 'best-shower-chairs/drive-shower-chair-with-back'], [350, 'best-shower-chairs/medline-backless-shower-chair-with-arms'], [300, 'best-shower-chairs/homland-adjustable-shower-stool']]],
    'commode': ['Bedside commodes', '/best-bedside-commodes/', [[350, 'best-bedside-commodes/drive-folding-bedside-commode'], [350, 'best-bedside-commodes/drive-folding-steel-3-in-1-commode'], [350, 'best-bedside-commodes/medline-3-in-1-folding-commode'], [350, 'best-bedside-commodes/medline-drop-arm-commode'], [500, 'best-bedside-commodes/dmi-drop-arm-extra-wide-commode']]],
    'scooter': ['Mobility scooters', '/best-mobility-scooters/', [[265, 'best-mobility-scooters/vive-3-wheel-mobility-scooter'], [300, 'best-mobility-scooters/rascal-venture-3-wheel-scooter'], [275, 'best-mobility-scooters/superhandy-passport-mobility-scooter'], [265, 'best-mobility-scooters/iris-3-lightweight-mobility-scooter']]],
    'transport': ['Transport wheelchairs', '/best-transport-wheelchairs/', [[300, 'best-transport-wheelchairs/medline-transport-chair-12-inch-wheels'], [300, 'best-transport-wheelchairs/drive-fly-lite-transport-chair'], [300, 'best-transport-wheelchairs/medline-ultra-lightweight-transport-chair'], [300, 'best-transport-wheelchairs/drive-atc19-transport-chair'], [250, 'best-transport-wheelchairs/drive-economy-transport-chair']]],
    'toilet': ['Raised toilet seats', '/best-raised-toilet-seats/', [[1000, 'best-raised-toilet-seats/bemis-assurance-3-inch'], [300, 'best-raised-toilet-seats/vive-raised-toilet-seat-with-handles'], [250, 'best-raised-toilet-seats/carex-raised-toilet-seat-with-arms'], [400, 'best-raised-toilet-seats/aquasense-4-inch-riser'], [300, 'best-raised-toilet-seats/healthsmart-5-inch-padded-riser']]],
    'cane': ['Canes', '/best-canes/', [[350, 'best-canes/hurrycane-freedom-edition'], [300, 'best-canes/kinggear-self-standing-quad-cane'], [250, 'best-canes/dmi-adjustable-walking-cane'], [300, 'best-canes/medline-aluminum-offset-cane']]],
    'frame': ['Toilet safety frames', '/best-toilet-safety-frames/', [[250, 'best-toilet-safety-frames/medline-toilet-safety-rail'], [300, 'best-toilet-safety-frames/carex-toilet-safety-frame'], [300, 'best-toilet-safety-frames/vaunn-folding-toilet-safety-frame'], [350, 'best-toilet-safety-frames/homland-aluminum-toilet-safety-rail'], [450, 'best-toilet-safety-frames/vive-flip-up-toilet-safety-rail']]],
    'ramp': ['Portable ramps', '/best-wheelchair-ramps/', [[800, 'best-wheelchair-ramps/vnn-3ft-portable-ramp'], [800, 'best-wheelchair-ramps/fachnuo-2ft-portable-ramp'], [800, 'best-wheelchair-ramps/vevor-3ft-portable-ramp'], [800, 'best-wheelchair-ramps/vnn-6ft-portable-ramp'], [606, 'best-wheelchair-ramps/whalemotor-8ft-portable-ramp']]],
    'bedrail': ['Bed assist rails', '/best-bed-assist-rails/', [[300, 'best-bed-assist-rails/stander-wonder-pivot-bed-rail'], [300, 'best-bed-assist-rails/lunderg-bed-assist-rail-with-light'], [380, 'best-bed-assist-rails/kingpavonini-bed-assist-rail']]],
}

INTRO = '''<p>Every product has a weight limit, and the figure on the page is not always the figure you should use. Enter your weight, add anything you carry or any helper's weight that the product also supports, choose a kind of product, and the finder lists the picks in our guides whose limit is high enough. Where a maker's page and a listing disagree, it uses the lower figure.</p>'''

_opts = ''.join(f'<option value="{k}">{v[0]}</option>' for k, v in LIMITS.items())
WIDGET = f'''<form id="wl" onsubmit="return false">
<div class="row">
<div><label for="wk">Product type</label><select id="wk">{_opts}</select></div>
<div><label for="ww">Your weight in pounds</label><input id="ww" type="number" min="50" max="900" step="1" inputmode="numeric" value="220"></div>
<div><label for="we">Extra load in pounds (bag, cargo, helper)</label><input id="we" type="number" min="0" max="400" step="1" inputmode="numeric" value="0"></div>
</div>
<div class="result" id="wlo" aria-live="polite"></div>
</form>'''

SCRIPT = 'var LIMITS = ' + json.dumps(LIMITS) + ''';
(function () {
  var k = document.getElementById('wk'), w = document.getElementById('ww'), x = document.getElementById('we'), out = document.getElementById('wlo');
  function update() {
    var cat = LIMITS[k.value], wt = parseFloat(w.value), extra = parseFloat(x.value) || 0;
    if (!(wt > 0)) { out.innerHTML = 'Enter your weight in pounds.'; return; }
    var need = wt + extra, ok = cat[2].filter(function (p) { return p[0] >= need; }).sort(function (a, b) { return a[0] - b[0]; });
    var msg = '<span class="big">' + need + ' lb to support</span>';
    if (ok.length) msg += renderPicks(ok.map(function (p) { return p[1]; }), cat[0] + ' in our guide with a listed limit of ' + need + ' lb or more:') + '<a href="' + cat[1] + '">See the full guide</a>.';
    else msg += 'None of the ' + cat[0].toLowerCase() + ' in our guide lists a limit of ' + need + ' lb or more. Look for a bariatric model and ask the maker for its tested limit. <a href="' + cat[1] + '">See the guide</a>.';
    msg += '<br>Limits are the lower of the maker figure and the listing figure where they disagree.';
    out.innerHTML = msg;
  }
  [k, w, x].forEach(function (el) { el.addEventListener('input', update); el.addEventListener('change', update); });
  update();
})();'''

BODY = '''<h2>How to Use the Result</h2>
<p>The finder compares the limit with the weight you enter plus the extra load. For a rollator, the extra load is a bag or shopping. For a scooter, the Iris 3 listing says its 265 pounds includes cargo. For a ramp, add the weight of the chair or scooter, because the ramp carries both. For a shower seat or commode, extra load is usually zero.</p>
<p>No agency sets a safe margin above a product's stated limit, so we do not add one. If you are close to a limit, choose the product with the higher figure, and ask the maker how the limit was tested.</p>
<h2>Where the Limits Come From</h2>
<p>The limits are the ones in our buying guides. Drive Medical's pages give 350 pounds for its rollator and commodes, 300 for its aluminum rollator and bath bench, and 250 for its economy transport chair. Drive's transfer bench page says 400 pounds and its Amazon listing says 350, so the finder uses 350. HOMLAND lists its shower stool at 400 pounds as the frame's maximum and 300 as the recommended user weight, so it uses 300. Products whose listing text gave no limit are left out, because a missing number is not a high one.</p>
<p class="note"><strong>Ask a professional for a fit.</strong> A weight limit is one number. A physical therapist or occupational therapist can check whether a product also suits your height, strength and home.</p>
<h2>Weight Limit Questions</h2>
<h3>Why are some products missing from the results?</h3>
<p>Their listings give no weight limit in the text we read. Our guides flag these, for example the HOMLAND rollator, the HONEYBULL cane and the Hoverfly scooter. Check the product page before buying.</p>
<h3>Does a higher limit mean a better product?</h3>
<p>No. A limit only tells you the most the product is rated for. Size, fit and the features in our guides decide the pick among those that qualify.</p>'''

SOURCES = [
    ('Drive Medical: 4 Wheel Rollator with 7.5 in Casters 10257BL-1', 'https://shop.drivemedical.com/us/en/p/10257bl-1'),
    ('Drive Medical: Aluminum Rollator R726BL', 'https://shop.drivemedical.com/us/en/p/r726bl'),
    ('Drive Medical: Transfer Tub Bench 12011KD-1', 'https://shop.drivemedical.com/us/en/p/12011kd-1'),
    ('Drive Medical: Folding Steel Commode 11148-1', 'https://shop.drivemedical.com/us/en/p/11148-1'),
    ('Drive Medical: Trans Chair Econ 17 in TR37E-SV', 'https://shop.drivemedical.com/us/en/p/tr37e-sv'),
    ('Vive Health: Toilet Seat Riser with Arms', 'https://www.vivehealth.com/products/raised-toilet-seat-with-handles'),
    ('Drive Medical at Home: HurryCane Freedom Edition', 'https://drivemedicalathome.com/products/hurrycane-freedom-edition'),
]
