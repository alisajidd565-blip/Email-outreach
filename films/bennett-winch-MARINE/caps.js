const { chromium } = require('playwright'); const fs=require('fs'); const D=process.argv[2];
const b64=f=>fs.readFileSync(f).toString('base64');
const fontCSS=`@font-face{font-family:M;src:url(data:font/ttf;base64,${b64(D+'/fonts/Montserrat.ttf')})} @font-face{font-family:CI;src:url(data:font/ttf;base64,${b64(D+'/fonts/CormorantGaramond-Italic.ttf')})}
body{margin:0;width:1920px;height:1080px;background:transparent;position:relative;overflow:hidden;-webkit-font-smoothing:antialiased}
.sup{position:absolute;left:110px;bottom:104px;font-family:M;font-weight:500;font-size:31px;letter-spacing:.40em;color:#F7F2EA;text-shadow:0 0 2px rgba(0,0,0,.35),0 2px 22px rgba(0,0,0,.85)}
.sup .rule{display:block;width:44px;height:2px;background:#F7F2EA;opacity:.9;margin-bottom:20px}
.mid{position:absolute;left:0;right:0;bottom:96px;text-align:center;font-family:M;font-weight:500;font-size:28px;letter-spacing:.42em;line-height:2.0;color:#F4EFE6;text-shadow:0 1px 14px rgba(0,0,0,.6)}
.tag{position:absolute;left:150px;top:350px;width:640px;color:#F4EFE6;text-shadow:0 2px 24px rgba(0,0,0,.6)}
.tag .t1{font-family:M;font-weight:500;font-size:44px;letter-spacing:.38em}
.tag .t2{font-family:CI;font-weight:400;font-size:50px;line-height:1.25;margin-top:26px;opacity:.95}
.logo{position:absolute;left:150px;top:700px;width:430px}`;
const cards={
 cap_london:`<div class="sup"><span class="rule"></span>LONDON &nbsp;·&nbsp; 06:14</div>`,
 cap_road:`<div class="sup"><span class="rule"></span>THE ROAD NORTH</div>`,
 cap_coast:`<div class="sup"><span class="rule"></span>THE ATLANTIC COAST &nbsp;·&nbsp; 16:52</div>`,
 cap_suede:`<div class="mid">MOSS-BACKED ITALIAN SUEDE<br>IMPERMEABLE TO MOISTURE</div>`,
 end_tag:`<div class="tag"><div class="t1">MARINE BLUE</div><div class="t2">Named for the sea.<br>Built to meet it.</div></div>`,
 end_logo:`<img class="logo" src="data:image/png;base64,${b64(D+'/logo_white.png')}">`
};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
 for(const [k,v] of Object.entries(cards)){await p.setContent(`<html><head><style>${fontCSS}</style></head><body>${v}</body></html>`,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);await p.screenshot({path:`${D}/${k}.png`,omitBackground:true});}
 await b.close();})();
