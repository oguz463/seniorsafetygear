"""What Kind of Exercise Prevents Falls, checked 2026-10-20.

Source read in full (abstract) that day: Sherrington C, Fairhall NJ, Wallbank GK, et al. "Exercise for preventing falls in older
people living in the community." Cochrane Database Syst Rev 2019 (PubMed 30703272): 108 RCTs, 23,407 participants in 25 countries,
average age 76, 77% women; exercise of all types versus control RaR 0.77 (95% CI 0.71 to 0.83; 59 studies, 12,981 participants,
high certainty), 195 fewer falls per 1000 people per year from 850; fallers RR 0.85 (0.81 to 0.89; 63 studies, high certainty), 72
fewer fallers per 1000 from 480; balance and functional exercise RaR 0.76 (0.70 to 0.81; 39 studies, 7,920, high certainty);
multiple types RaR 0.66 (0.50 to 0.88; 11 studies, 1,374, moderate); Tai Chi RaR 0.81 (0.67 to 0.99; 7 studies, 2,655, low
certainty) and fallers RR 0.80 (0.70 to 0.91; high); resistance-only, dance and walking uncertain; fall-related fractures RR 0.73
(0.56 to 0.95, low certainty); adverse events mostly non-serious musculoskeletal. USPSTF 2024 (JAMA, June 4 2024) was read only
through news coverage (Healio, MDedge), not the statement itself, so it is described as reported and not quoted: grade B for exercise
interventions in community-dwelling adults 65 and older at increased risk of falls. Hero photo: Pexels 8940488 by Vlada Karpovich.
"""
import datetime

SLUG = 'what-exercise-prevents-falls-cochrane-review'
TOPIC = 'Research'
TITLE = 'What Kind of Exercise Prevents Falls? What the Cochrane Review Found'
SEO_TITLE = 'Exercise to Prevent Falls: What the Cochrane Review Found'
DESCRIPTION = 'A 2019 Cochrane review of 108 trials found exercise cuts the rate of falls by 23%. Which types worked, which are uncertain and what the evidence does not show.'
PUBLISHED = datetime.date(2026, 10, 20)
UPDATED = datetime.date(2026, 10, 20)
PHOTO = 'exercise-and-falls'
PHOTO_ALT = 'older man and woman standing in a park with their arms stretched out in front of them doing slow balance exercises'
PHOTO_CREDIT = 'Vlada Karpovich (Pexels)'
RELATED = ['best-rollators', 'best-canes']

TAKEAWAYS = [
    'A 2019 Cochrane review of <strong>108 trials and 23,407 people</strong> found exercise reduces the <strong>rate of falls by 23%</strong> (high certainty).',
    '<strong>Balance and functional exercise</strong> cut falls by 24%. Programs that <strong>add resistance exercise</strong> probably cut them by 34%.',
    '<strong>Tai Chi</strong> may reduce falls by 19%, with low certainty on the rate and high certainty on the number of fallers.',
    'The review was <strong>uncertain about resistance-only training, dance and walking</strong>.',
    'It tested exercise, <strong>not walkers or other equipment</strong>.',
]

BODY = '''<p>Most of what you can buy for a safer home, from grab bars to rollators, has no trial behind it. Exercise does. The best evidence is a Cochrane review by Cathie Sherrington and colleagues, published in 2019, which pooled 108 randomized trials with 23,407 people living in the community. The average age was 76, and 77% were women. Here is what it found.</p>

<h2>Exercise Cuts the Rate of Falls</h2>
<p>Across 59 studies and 12,981 people, exercise of all types reduced the rate of falls by 23% compared with a control that was not expected to reduce falls (rate ratio 0.77, 95% confidence interval 0.71 to 0.83). The authors rated the evidence high certainty. They give an example: out of 1,000 people followed for a year, with 850 falls expected, exercise meant about 195 fewer falls.</p>
<p>Exercise also reduced the number of people who fell at least once by 15% (risk ratio 0.85). Of 1,000 people, with 480 expected to fall, that is about 72 fewer fallers. The effect did not differ between trials that picked people at higher risk of falling and those that did not.</p>

<h2>Which Types Worked</h2>
<table class="art-table"><thead><tr><th>Type of exercise</th><th>Rate of falls</th><th>Certainty</th></tr></thead><tbody>
<tr><td>Balance and functional exercise (39 studies)</td><td>24% lower</td><td>High</td></tr>
<tr><td>Multiple types, usually balance and functional plus resistance (11 studies)</td><td>34% lower</td><td>Moderate</td></tr>
<tr><td>Tai Chi (7 studies)</td><td>19% lower</td><td>Low</td></tr>
<tr><td>Resistance training only, dance or walking</td><td>Uncertain</td><td>Not enough evidence</td></tr>
</tbody></table>
<p>The authors say the effect differed by type of exercise. Programs that reduce falls mainly involve balance and functional exercises, which challenge standing balance and everyday movements. Tai Chi also reduced the number of people who fell by 20%, and the certainty for that measure was high, while the certainty for its effect on the rate of falls was low. The review found no trials of flexibility or endurance exercise against a control.</p>

<h2>Other Outcomes Are Less Certain</h2>
<p>Exercise may reduce fall-related fractures (risk ratio 0.73) and falls needing medical attention (risk ratio 0.61), but the certainty was low. The effect on falls needing a hospital stay was unclear. Adverse events were reported in 27 trials and were mostly minor and in the muscles and joints. Only one trial monitored them closely in both groups.</p>

<h2>What the Review Does Not Say</h2>
<ul>
<li><strong>It does not test equipment.</strong> No part of the review compares walking aids, grab bars or shower chairs with nothing. That does not mean they do not help, but this evidence does not show it.</li>
<li><strong>It does not say which program suits you.</strong> The trials covered many programs, and the review's conclusions are about groups of people.</li>
<li><strong>It excluded some groups.</strong> Trials focused on conditions such as stroke were left out.</li>
</ul>
<p class="note"><strong>The USPSTF agrees on exercise.</strong> We read news coverage of the U.S. Preventive Services Task Force's June 2024 recommendation, not the statement itself. As reported, it advises clinicians to offer exercise programs to adults aged 65 and over who are at increased risk of falling, at grade B.</p>

<h2>What to Do With This</h2>
<p>Ask your doctor or a physical therapist about a balance and strength program before you spend on equipment, and use equipment for the tasks where you need it. A cane or rollator can make a walk safer while you build strength, and our <a href="/articles/cane-walker-or-rollator/">cane, walker or rollator article</a> helps you choose. For the home itself, see what the same research group found in <a href="/articles/do-home-safety-changes-prevent-falls/">the evidence on home safety changes</a>.</p>'''

SOURCES = [
    ('Sherrington C, et al.: Exercise for preventing falls in older people living in the community. Cochrane Database Syst Rev 2019', 'https://pubmed.ncbi.nlm.nih.gov/30703272/'),
    ('Healio: USPSTF finalizes recommendation on exercise for fall prevention among older adults (June 2024)', 'https://healio.com/news/primary-care/20240604/uspstf-finalizes-recommendation-on-exercise-for-fall-prevention-among-older-adults'),
]
