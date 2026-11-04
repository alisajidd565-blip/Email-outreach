# Usage: python3 tools/probe_domains.py brand1.com brand2.co.uk ...
# Skips domains in known_domains.txt, scrapes home + contact pages for emails, checks MX via dns.google.
import sys,re,subprocess,json,concurrent.futures as cf
known=set(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','known_domains.txt')).read().split())
PATHS=['','/policies/contact-information','/pages/contact','/pages/contact-us','/contact','/contact-us','/en/contact','/pages/about-us','/about']
BAD=re.compile(r'sentry|wixpress|example|domain\.com|email\.address|\.(png|jpg|jpeg|gif|webp|svg)$|shopify|godaddy|your@|name@|@sentry|wix\.com|squarespace|jquery|bootstrap',re.I)
def get(u):
    try: return subprocess.run(['curl','-sL','-m','15','-A','Mozilla/5.0',u],capture_output=True,text=True,errors='ignore').stdout
    except Exception: return ''
def mx(d):
    try:
        j=json.loads(get(f'https://dns.google/resolve?name={d}&type=MX'))
        return bool(j.get('Answer'))
    except Exception: return False
def probe(dom):
    if any(k==dom or k.endswith('.'+dom) or dom.endswith('.'+k) for k in known): return dom,'KNOWN',[]
    emails=set(); title=''
    for p in PATHS:
        h=get(f'https://{dom}{p}')
        if p=='' :
            if not h: return dom,'DEAD',[]
            m=re.search(r'<title[^>]*>(.*?)</title>',h,re.S|re.I); title=(m.group(1).strip()[:60] if m else '')
        for e in re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',h):
            if not BAD.search(e): emails.add(e.lower())
        if emails and p!='': break
    out=[(e,mx(e.split('@')[1])) for e in sorted(emails)]
    return dom,title,out
doms=[d.strip() for d in sys.argv[1:]]
with cf.ThreadPoolExecutor(8) as ex:
    for dom,t,o in ex.map(probe,doms): print(dom,'|',t,'|',o)
