# Cinnamon prelanders written to Compliance Guide v1.2 (Nov 24, 2026). Template = compliant C2b build.
import os,base64,html as H
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'../../..'))
TPL=open(os.path.join(ROOT,'handoff/compliance-builds/C2b.html'),encoding='utf8').read()
HEAD=TPL[:TPL.find('<div class="pl-g">')]
PDP='https://resilia.shop/products/resilia-ceylon-cinnamon'
CLAIM='Supports healthy blood sugar already within a normal range.†'
GUAR='30-Day Money-Back Guarantee. Request a refund within 30 days of delivery. Shipping is not refundable. No need to send it back.'
ADV='Consult your healthcare provider before use if you are pregnant, nursing, taking medication or have a medical condition.'
RES='Consistent daily use matters most. Individual results may vary.'
DRAM='This story is a dramatization based on composite characters.'
FDA='†These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.'
TRUST='<p class="trust">30-Day Money-Back Guarantee · Ceylon Cinnamon · Two capsules a day</p>'
IMG={'BREAKFAST':('CG_BREAKFAST','cg-cin-breakfast'),'CAFE':('CG_CAFE','cg-cin-cafe'),'CAKE':('CG_CAKE','cg-cin-cake'),'CELL':('CG_CELL','cg-cin-cell'),
 'COUCH':('CG_COUCH','cg-cin-couch'),'PALM':('CG_PALM','cg-cin-palm'),'PHARM':('CG_PHARM','cg-cin-pharm'),'WALK':('CG_WALK','cg-cin-walk'),
 'TUB':('CG_TUB','cg-cin-tub'),'POUCH':('PDP_POUCH','pdp-cin-pouch'),'POUR':('PDP_POUR','pdp-cin-pour'),'FACTS':('PDP_FACTS','pdp-cin-facts')}
_c={}
def uri(f):
    if f not in _c: _c[f]='data:image/jpeg;base64,'+base64.b64encode(open(os.path.join(ROOT,'assets/cinnamon',f+'.jpg'),'rb').read()).decode()
    return _c[f]
def img(k,alt,ratio='4/3',fit='cover',slot=None):
    f,name=IMG[k]; name=slot or name
    return f'<img class="media" src="{uri(f)}" alt="{H.escape(alt)}" data-asset="{name}.jpg" style="aspect-ratio:{ratio};object-fit:{fit}">'
def btn(t): return f'<a class="btn" href="{PDP}">{t}</a>'
BEN=lambda pic: f'''<section class="ben"><p class="tag">WHAT’S IN THE POUCH</p><h2 class="h2">Two ingredients, every dose on the label.</h2><p class="t">Resilia pairs Ceylon cinnamon extract with berberine HCl, in two capsules a day.</p><div class="hvs"><div class="hv"><p class="tag">INGREDIENT 1 · CEYLON CINNAMON, 1,000 MG</p><h3>Ceylon cinnamon extract</h3><p>1,000 mg of Ceylon cinnamon extract per serving.</p><p class="feel"><b>What it does:</b> {CLAIM}</p></div><div class="hv"><p class="tag">INGREDIENT 2 · BERBERINE HCl, 500 MG</p><h3>Berberine HCl</h3><p>500 mg of berberine HCl per serving.</p><p class="feel"><b>How to take it:</b> two capsules daily, with breakfast.</p></div></div>{pic}<div class="bfs"><div class="bf"><span class="bfi">🩸</span><div><b>Healthy blood sugar</b><p>{CLAIM}</p></div></div><div class="bf"><span class="bfi">🌿</span><div><b>Ceylon Cinnamon</b><p>1,000 mg of Ceylon cinnamon extract per serving.</p></div></div><div class="bf"><span class="bfi">💊</span><div><b>Berberine HCl</b><p>500 mg of berberine HCl per serving.</p></div></div><div class="bf"><span class="bfi">☕</span><div><b>Two capsules a day</b><p>With breakfast. That’s the whole routine.</p></div></div><div class="bf"><span class="bfi">🔬</span><div><b>Third-party tested</b><p>Made in GMP certified facilities.</p></div></div><div class="bf"><span class="bfi">✅</span><div><b>30-Day Money-Back Guarantee</b><p>Request a refund within 30 days of delivery. Shipping is not refundable. No need to send it back.</p></div></div></div>{btn('See today’s price →')}<p class="fine">{FDA}</p></section>'''
def card(n,sym,title,main,body,res,pill='',lab='What changes:'):
    p=f'<div class="pill">{pill}</div>' if pill else ''
    bs=''.join(f'<p>{b}</p>' for b in ([body] if isinstance(body,str) else body))
    return f'<div class="r card"><p class="sym">{sym}</p><div class="rh"><div class="num">{n}</div><h3>{title}</h3></div>{main}<div class="body">{p}{bs}<p class="res"><b>{lab}</b> {res}</p></div></div>'

WHY=f"""<section class="ben"><p class="tag">WHY RESILIA</p><h2 class="h2">Why people choose Resilia Ceylon Cinnamon</h2><p class="t">The real cost of a supplement isn’t the price of the pouch. It’s another bottle you don’t trust, don’t finish and never reorder.</p><div class="bfs"><div class="bf"><span class="bfi">🏷️</span><div><b>Both doses, printed</b><p>1,000 mg Ceylon cinnamon extract and 500 mg berberine HCl: the actual amounts in every two-capsule serving. No blend hiding the amounts.</p></div></div><div class="bf"><span class="bfi">📦</span><div><b>One pouch, not two bottles</b><p>Ceylon cinnamon extract and berberine HCl together, so there’s one thing to take, one thing to reorder and one delivery.</p></div></div><div class="bf"><span class="bfi">☕</span><div><b>A routine you’ll actually keep</b><p>Two capsules with breakfast. If a routine is complicated, you stop doing it. This one takes ten seconds.</p></div></div><div class="bf"><span class="bfi">🩸</span><div><b>One clear claim</b><p>{CLAIM}</p></div></div><div class="bf"><span class="bfi">🔬</span><div><b>Made with care</b><p>Third-party tested. Made in GMP certified facilities. Gluten free, non-GMO, no artificial additives.</p></div></div><div class="bf"><span class="bfi">✅</span><div><b>30 days to decide</b><p>{GUAR}</p></div></div></div>{btn('Get Resilia Ceylon Cinnamon →')}</section>"""
REVS=[('Debra M.','I was already looking into berberine when I came across this. Figured getting cinnamon and berberine together made more sense than buying two different bottles. Price was decent too. No complaints so far.'),
 ('John S.','I take mine with breakfast, right after my coffee. Been doing it for about six weeks now and haven\'t missed many days. I\'m usually terrible at keeping up with supplements lol, but this one\'s easy.')]
def reviews():
    c=''.join(f'<div class="r card"><p style="color:#C8871E;font-size:18px;letter-spacing:2px">★★★★★</p><div class="body"><p>“{t}”</p><p style="font-size:14px;color:#7A6558"><b>{n}</b> · Resilia Ceylon Cinnamon · <span data-review-date="TODO">[date from review platform]</span></p></div></div>' for n,t in REVS)
    return f'<section style="display:flex;flex-direction:column;gap:10px"><!-- DEV: real customer reviews; add each review date from Resilia\'s review platform before launch. Compliance approval required (Rule 12). --><p class="tag">WHAT CUSTOMERS SAY</p><h2 class="h2">“This one’s easy.”</h2>{c}<p class="fine">Individual results may vary.</p></section>'

EXPECT=f'''<section class="r"><h2>What to expect</h2><div class="wk"><b>EVERY MORNING</b><p class="t" style="font-size:17px">Two capsules with breakfast.</p></div><div class="wk"><b>EVERY DAY</b><p class="t" style="font-size:17px">{CLAIM}</p></div><div class="wk"><b>OVER TIME</b><p class="t" style="font-size:17px">{RES}</p></div><p class="fine">Watch the trend, not one day.</p></section>
<section class="box"><p class="tag">30-DAY GUARANTEE</p><h2 class="h2">Try it for 30 days.</h2><p class="t">Take two capsules every morning for a month. Every order comes with a {GUAR} You don’t have to subscribe: buy one pouch or a bundle, whatever fits.</p></section>'''
def fit(a,b): return f'''<section class="r"><h2 class="h2">Is Resilia for someone like me?</h2><p class="t">{a}</p><p class="t">{b}</p><p class="tag" style="margin-top:6px">WHAT’S IN EVERY SERVING</p><ul class="rt"><li>Ceylon cinnamon extract (1,000 mg)</li><li>Berberine HCl (500 mg)</li><li>Ceylon Cinnamon</li><li>Two vegetable capsules, once a day</li><li>Gluten free, non-GMO, no artificial additives</li><li>30-Day Money-Back Guarantee</li></ul></section>'''
def product(cta): return f'''<section class="box"><div style="display:flex;flex-wrap:wrap;gap:18px;align-items:center">
<div style="flex:0 0 150px;width:150px">{img('POUCH','Resilia Ceylon Cinnamon with Berberine HCl pouch, 60 capsules','1/1','contain')}</div>
<div style="flex:1 1 240px;display:flex;flex-direction:column;gap:8px"><h3 style="font-family:'Clash Grotesk','Space Grotesk',sans-serif;font-size:23px;font-weight:700;line-height:1.2">Resilia Ceylon Cinnamon + Berberine HCl</h3>
<p style="font-size:16px;line-height:1.5">Ceylon cinnamon extract 1,000 mg · Berberine HCl 500 mg. Two capsules daily. {GUAR}</p><ul class="rt" style="margin-top:4px"><li>{CLAIM}</li><li>Two capsules daily</li><li>Two capsules daily, 30 servings per pouch</li><li>One pouch or a bundle. No subscription required.</li><li>Third-party tested · GMP certified facilities</li></ul></div></div>
{btn(cta)}<p style="font-size:13px;color:#7A6558;text-align:center">See today’s price at the official shop.</p></section>'''
FAQ=[('What’s in Resilia Ceylon Cinnamon?','Two ingredients, with the doses on the label: Ceylon cinnamon extract, 1,000 mg, and berberine HCl, 500 mg. Two vegetable capsules per serving, 30 servings per pouch. Gluten free, non-GMO, no artificial additives.'),
 ('What kind of cinnamon is it?','Resilia uses Ceylon Cinnamon extract.'),
 ('Why are both ingredients in the same pouch?','So it’s one routine: one pouch, two capsules, one reorder. Every two-capsule serving has 1,000 mg of Ceylon cinnamon extract and 500 mg of berberine HCl.'),
 ('Do I have to subscribe?','No. Buy one pouch or a bundle, whatever fits. One pouch is 30 servings, a month of mornings.'),
 ('How do I take it?','Two capsules, once a day, with your favorite drink. Most people take them with breakfast.'),
 ('Should I check with anyone first?',ADV),('How long should I take it?',RES),('What if it’s not for me?','Every order comes with a '+GUAR)]
def tail(story):
    q=''.join(f'<details><summary>{a}</summary><p>{b}</p></details>' for a,b in FAQ)
    d=(' '+DRAM+' Characters are portrayed by actors or illustrated.') if story else ''
    return f'''<section style="display:flex;flex-direction:column;gap:4px"><h2 class="h2" style="margin-bottom:6px">Questions people ask</h2>{q}</section>
{btn('Get Resilia at today’s price →')}
<div class="fine" style="display:flex;flex-direction:column;gap:8px;margin-top:8px">
<p>ADVERTORIAL. This page is an advertisement for Resilia.{d}</p>
<p>{FDA}</p>
<p>*{RES} {ADV}</p></div>
</main></div></div></body></html>'''
def page(P):
    story=P.get('story',False)
    by='By Resilia · '+DRAM if story else 'By Resilia'
    h=[f'<div class="pl-g"><div class="adv">ADVERTORIAL</div><div class="wrap"><main>',
       f'<p class="eyebrow">{P["eyebrow"]}</p><h1>{P["h1a"]} <span style="color: #8E1B1F">{P["h1b"]}</span></h1><p class="sub">{P["sub"]}</p>',
       f'<p class="by">{by}</p>',P['hero'],f'<p class="t" style="font-size:20px">{P["intro"]}</p>',
       btn('See today’s price at the official shop →')+TRUST, P['edu'], BEN(P['benpic']),
       f'<section style="display:flex;flex-direction:column;gap:6px"><h2 class="h2">{P["list_h"]}</h2></section>']
    for i,c in enumerate(P['cards'],1):
        h.append(card(i,*c,lab=P.get('lab','What changes:')))
        if i==3: h.append(btn('Get Resilia Ceylon Cinnamon →')+TRUST)
        if i==6: h.append(btn('Start my 30-day Resilia routine →')+TRUST)
    h+=[WHY,reviews(),EXPECT,fit(*P['fit']),product('Claim my pouch at today’s price →'),tail(story)]
    out=HEAD.replace('<title>C2B Prelander</title>',f'<title>{P["id"].upper()} Prelander</title>')+'\n'.join(h)
    os.makedirs(os.path.join(HERE,'out'),exist_ok=True)
    fn=os.path.join(HERE,'out',P['id'].upper()+'.html'); open(fn,'w',encoding='utf8').write(out); print(fn,len(out)//1024,'KB')
def edu(*parts): return '<section class="edu">'+''.join(parts)+'</section>'
def tag(t,top=False):
    st=' style="margin-top:8px"' if top else ''
    return f'<p class="tag"{st}>{t}</p>'
def h2(t): return f'<h2 class="h2">{t}</h2>'
def t(x): return f'<p class="t">{x}</p>'
