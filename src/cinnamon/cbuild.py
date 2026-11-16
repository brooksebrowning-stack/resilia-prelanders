import sys,os,inspect,base64,html
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'../../g24')); import build as B
# --- cinnamon palette from the PDP: rust #9B470D, cream #F6EDE7, Clash Grotesk ---
css=B.CSS
for a,b in [('#8A2B1F','#9B470D'),('#2A1E1A','#1F1A17'),('#3B2F2A','#2E2622'),('#4A3D37','#3D332D'),('#FAF5EF','#F6EDE7'),('#EADFD3','#E8D6C8'),('#F4EEE6','#F3E9E1'),('#EADFD6','#F6EDE7'),('#7A6A62','#7A6558')]:
    css=css.replace(a,b)
css=css.replace("family=Figtree","family=Space+Grotesk:wght@500;600;700&family=Figtree")
css=css.replace(".pl-g h1{font-family:'Source Serif 4',Georgia,serif;font-weight:800",".pl-g h1{font-family:'Clash Grotesk','Space Grotesk',system-ui,sans-serif;font-weight:700;letter-spacing:-.01em")
css=css.replace(".pl-g .h2{font-family:'Source Serif 4',Georgia,serif;font-weight:800",".pl-g .h2{font-family:'Clash Grotesk','Space Grotesk',system-ui,sans-serif;font-weight:700")
css=css.replace(".pl-g .btn{",".pl-g .btn{font-family:'Clash Grotesk','Space Grotesk',sans-serif;text-transform:uppercase;letter-spacing:.04em;")
B.CSS=css
B.PDP='https://resilia.shop/products/resilia-ceylon-cinnamon'
def img(f): return 'data:image/jpeg;base64,'+base64.b64encode(open(os.path.join(HERE,'img',f+'.jpg'),'rb').read()).decode()
CM={}
def cmedia(k, ratio='4/3', fit='cover'):
    if k in CM:
        f,alt,name=CM[k]
        return f'<img class="media" src="{img(f)}" alt="{html.escape(alt)}" data-asset="{name}.jpg" style="aspect-ratio:{ratio};object-fit:{fit}">'
    return OLD_MEDIA(k,ratio,fit)
OLD_MEDIA=B.media; B.media=cmedia
def reg(k,f,alt,name): CM[k]=(f,alt,name)
reg('POUCH','PDP_POUCH','Resilia Ceylon Cinnamon with Berberine HCl pouch, 60 capsules','pdp-cin-pouch')
reg('C_POUR','PDP_POUR','Resilia Ceylon Cinnamon capsules poured from the pouch into a glass jar','pdp-cin-pour')
reg('C_FACTS','PDP_FACTS','Supplement Facts: Ceylon cinnamon bark extract 1,000 mg, berberine HCl 500 mg','pdp-cin-facts')
B.FAQ=[('What’s in Resilia Ceylon Cinnamon?','Two ingredients, with the doses on the label: Ceylon cinnamon (Cinnamomum verum) bark extract, 1,000 mg, standardized to cinnamaldehyde and polyphenols, and berberine HCl, 500 mg. Two vegetable capsules per serving, 30 servings per pouch. Gluten free, non-GMO, no artificial additives.'),
 ('Is it the cassia cinnamon from the grocery store?','No. Resilia uses true Ceylon cinnamon (Cinnamomum verum), not cassia.'),
 ('How do I take it?','Two capsules, once a day, with your favorite drink. Most people take them with breakfast.'),
 ('Can I take it with my medication?','Talk to your doctor before starting any supplement, especially if you take prescription medication, including for blood sugar or blood pressure. Keep taking what your doctor prescribed and tell them you’ve added it. Resilia is a dietary supplement, not a replacement for anything your doctor prescribes.'),
 ('When will I notice anything?','Some people notice steadier energy in the first few weeks. Give it 2 to 3 months of daily use. Individual results vary.'),
 ('What if it’s not for me?','Every order comes with a 30-day money-back guarantee.')]
def faq():
    q=''.join(f'<details><summary>{a}</summary><p>{b}</p></details>' for a,b in B.FAQ)
    return f'''<section style="display:flex;flex-direction:column;gap:4px"><h2 class="h2" style="margin-bottom:6px">Questions people ask</h2>{q}</section>
<a class="btn" href="{B.PDP}">See if Resilia is right for you →</a>
<div class="fine" style="display:flex;flex-direction:column;gap:8px;margin-top:8px">
<p>ADVERTORIAL. This page is an advertisement for Resilia. Stories are dramatizations adapted from Resilia’s videos; characters are portrayed by actors or illustrated.</p>
<p>†These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.</p>
<p>*Individual results vary. Research referenced was conducted on ingredients, not on Resilia products. Resilia is a dietary supplement and is not a substitute for medical care or prescribed medication. Talk to your doctor before starting any supplement.</p></div>'''
B.faq=faq
def product(cta):
    return f'''<section class="box"><div style="display:flex;flex-wrap:wrap;gap:18px;align-items:center">
<div style="flex:0 0 150px;width:150px">{B.media('POUCH','1/1','contain')}</div>
<div style="flex:1 1 240px;display:flex;flex-direction:column;gap:8px"><h3 style="font-family:'Clash Grotesk','Space Grotesk',sans-serif;font-size:23px;font-weight:700;line-height:1.2">Resilia Ceylon Cinnamon + Berberine HCl</h3>
<p style="font-size:16px;line-height:1.5">Ceylon cinnamon bark extract 1,000 mg · Berberine HCl 500 mg. Two capsules a day. True Ceylon, not cassia. 30-day money-back guarantee.</p></div></div>
<a class="btn" href="{B.PDP}">{cta}</a><p style="font-size:13px;color:#7A6558;text-align:center"><span class="stars">★★★★☆</span> 4.2 on Trustpilot · 1,665 reviews · See today’s price at the official shop.</p></section>'''
B.product=product
src=inspect.getsource(B.page)
src=src.replace("30-day money-back guarantee · Third-party tested · No garlic breath","30-day money-back guarantee · True Ceylon, not cassia · Two capsules a day")
src=src.replace("quote='<blockquote","quote=P.get('quote') or ''\n    _old='<blockquote")
src=src.replace("got=['Aged Garlic Blend","got=P.get('got') or ['Aged Garlic Blend")
src=src.replace("What men notice","{P.get('notice_h','What men notice')}")
src=src.replace("Take two softgels every morning","Take two capsules every morning")
exec(src,B.__dict__)
GOT=['Ceylon cinnamon (Cinnamomum verum) bark extract, standardized to cinnamaldehyde & polyphenols (1,000 mg)','Berberine HCl (500 mg)','True Ceylon, not cassia','Two vegetable capsules, once a day','Gluten free, non-GMO, no artificial additives','30-day money-back guarantee']
def build(P):
    P.setdefault('got',GOT)
    h=B.page(P); open(os.path.join(HERE,'out',P['id']+'.html'),'w').write(h); print(P['id'],len(h)//1024,'KB')
