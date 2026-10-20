# Les trois lecteurs

Chaque lecteur se colle **tel quel** dans `javascript_tool`, sur la page du moteur, une fois
la réponse affichée. Il renvoie une ligne JSON prête pour `noter.mjs` :

```json
{"statut":"ok","nom":false,"site":false,"sources":["…"],"praticiens":["Dr …"],"extrait":""}
```

- `nom` : la réponse nomme Franck (le mot « Moyal » y figure) ;
- `site` : la réponse s'appuie sur drfranckmoyal.fr comme source ;
- `sources` : les sites cités, dans l'ordre d'apparition ;
- `praticiens` : les « Dr … » nommés, sauf lui ;
- `extrait` : la phrase où il apparaît, s'il apparaît.

Autres statuts : `pas d'aperçu` (Google n'a pas affiché d'aperçu IA pour cette recherche),
`anti-robot` (Google demande de prouver qu'on n'est pas un robot : **ne jamais y toucher**),
`limite` (ChatGPT a atteint la limite d'usage), `échec` (la page n'a pas répondu).

**Ne jamais renvoyer l'adresse de la page** (`location.href`) dans un lecteur : l'extension
de Chrome bloque toute réponse qui contient une adresse avec paramètres.

## 1. Aperçu IA de Google — `google-apercu`

Page : `https://www.google.com/search?hl=fr&q=QUESTION_ENCODEE` — attendre 8 secondes.

```js
await (async()=>{const EXCL=/(^|\.)(google\.[a-z.]+|gstatic\.com|googleusercontent\.com|openai\.com|chatgpt\.com|mapbox\.com|apple\.com|bing\.com|microsoft\.com)$/;const dom=h=>{try{const u=new URL(h);const r=u.searchParams.get('url')||u.searchParams.get('q');return new URL(r&&/^https?:/.test(r)?r:h).hostname.replace(/^www\./,'')}catch(e){return null}};const lire=(el,txt)=>{const sources=[...new Set([...el.querySelectorAll('a[href^="http"]')].map(a=>dom(a.href)).filter(x=>x&&!EXCL.test(x)))];const nom=/moyal/i.test(txt);const i=txt.search(/moyal/i);const praticiens=[...new Set(txt.match(/\b(?:Dr|Docteur|Pr|Professeur)\.? [A-ZÉÈ][\p{L}'’-]+(?: [A-ZÉÈ][\p{L}'’-]+)?/gu)||[])].filter(p=>!/moyal/i.test(p)).slice(0,10);return JSON.stringify({statut:'ok',nom,site:sources.includes('drfranckmoyal.fr'),sources:sources.slice(0,12),praticiens,extrait:i<0?'':txt.slice(Math.max(0,i-120),i+150).replace(/\s+/g,' ')})};
const b=document.body;if(/unusual traffic|trafic inhabituel|recaptcha|pas un robot|not a robot/i.test(b.innerText))return JSON.stringify({statut:'anti-robot'});const w=document.createTreeWalker(b,NodeFilter.SHOW_TEXT);let n,h=null;while(n=w.nextNode()){if(/^\s*Aperçu IA\s*$/.test(n.nodeValue)){h=n.parentElement;break;}}if(!h)return JSON.stringify({statut:"pas d'aperçu"});let c=h,s=0;while(c.parentElement&&!/peuvent contenir des erreurs/.test(c.innerText)&&s<40){c=c.parentElement;s++;}if(c.innerText.length>20000){c=h;s=0;while(c.parentElement&&c.innerText.length<2500&&s<40){c=c.parentElement;s++;}}const plus=[...c.querySelectorAll('[role="button"],button')].find(e=>/^Afficher plus$/.test(e.innerText.trim()));if(plus){plus.click();await new Promise(r=>setTimeout(r,2000));}return lire(c,c.innerText);})()
```

## 2. Mode IA de Google — `google-mode-ia`

Page : `https://www.google.com/search?hl=fr&udm=50&q=QUESTION_ENCODEE` — attendre 10 secondes.
Le lecteur attend encore jusqu'à 15 secondes que la réponse soit finie.

```js
await (async()=>{const EXCL=/(^|\.)(google\.[a-z.]+|gstatic\.com|googleusercontent\.com|openai\.com|chatgpt\.com|mapbox\.com|apple\.com|bing\.com|microsoft\.com)$/;const dom=h=>{try{const u=new URL(h);const r=u.searchParams.get('url')||u.searchParams.get('q');return new URL(r&&/^https?:/.test(r)?r:h).hostname.replace(/^www\./,'')}catch(e){return null}};const lire=(el,txt)=>{const sources=[...new Set([...el.querySelectorAll('a[href^="http"]')].map(a=>dom(a.href)).filter(x=>x&&!EXCL.test(x)))];const nom=/moyal/i.test(txt);const i=txt.search(/moyal/i);const praticiens=[...new Set(txt.match(/\b(?:Dr|Docteur|Pr|Professeur)\.? [A-ZÉÈ][\p{L}'’-]+(?: [A-ZÉÈ][\p{L}'’-]+)?/gu)||[])].filter(p=>!/moyal/i.test(p)).slice(0,10);return JSON.stringify({statut:'ok',nom,site:sources.includes('drfranckmoyal.fr'),sources:sources.slice(0,12),praticiens,extrait:i<0?'':txt.slice(Math.max(0,i-120),i+150).replace(/\s+/g,' ')})};
if(/unusual traffic|trafic inhabituel|recaptcha|pas un robot|not a robot/i.test(document.body.innerText))return JSON.stringify({statut:'anti-robot'});for(let k=0;k<10&&!/peuvent contenir des erreurs|can make mistakes/i.test(document.body.innerText);k++)await new Promise(r=>setTimeout(r,1500));const q=document.title.replace(/ - Recherche Google$/,'');const el=document.querySelector('[role="main"]')||document.querySelector('main')||document.body;const txt=el.innerText.split(q).join(' ');if(txt.length<300)return JSON.stringify({statut:'échec'});return lire(el,txt);})()
```

## 3. ChatGPT — `chatgpt`

**Envoyer la question** : ouvrir
`https://chatgpt.com/?temporary-chat=true&hints=search&q=QUESTION_ENCODEE`
(conversation temporaire, recherche web forcée), attendre 8 secondes, puis :

```js
const b=[...document.querySelectorAll('button')].find(x=>/^(Send|Envoyer)/i.test(x.getAttribute('aria-label')||''));b?(b.click(),'envoyé'):'bouton absent'
```

**Lire la réponse**, 40 secondes plus tard (le lecteur attend encore jusqu'à 30 secondes
qu'elle soit finie) :

```js
await (async()=>{const EXCL=/(^|\.)(google\.[a-z.]+|gstatic\.com|googleusercontent\.com|openai\.com|chatgpt\.com|mapbox\.com|apple\.com|bing\.com|microsoft\.com)$/;const dom=h=>{try{const u=new URL(h);const r=u.searchParams.get('url')||u.searchParams.get('q');return new URL(r&&/^https?:/.test(r)?r:h).hostname.replace(/^www\./,'')}catch(e){return null}};const lire=(el,txt)=>{const sources=[...new Set([...el.querySelectorAll('a[href^="http"]')].map(a=>dom(a.href)).filter(x=>x&&!EXCL.test(x)))];const nom=/moyal/i.test(txt);const i=txt.search(/moyal/i);const praticiens=[...new Set(txt.match(/\b(?:Dr|Docteur|Pr|Professeur)\.? [A-ZÉÈ][\p{L}'’-]+(?: [A-ZÉÈ][\p{L}'’-]+)?/gu)||[])].filter(p=>!/moyal/i.test(p)).slice(0,10);return JSON.stringify({statut:'ok',nom,site:sources.includes('drfranckmoyal.fr'),sources:sources.slice(0,12),praticiens,extrait:i<0?'':txt.slice(Math.max(0,i-120),i+150).replace(/\s+/g,' ')})};
const m=document.querySelector('main');if(!m)return JSON.stringify({statut:'échec'});const enCours=()=>document.querySelector('button[aria-label*="Stop"],button[aria-label*="Arrêter"]');for(let k=0;k<15&&enCours();k++)await new Promise(r=>setTimeout(r,2000));const t=m.innerText;if(/reached .{0,40}limit|limite d.utilisation|atteint la limite/i.test(t))return JSON.stringify({statut:'limite'});if(enCours())return JSON.stringify({statut:'échec'});const k=Math.max(t.lastIndexOf('ChatGPT said:'),t.lastIndexOf('ChatGPT a dit'));if(k<0)return JSON.stringify({statut:'échec'});return lire(m,t.slice(k));})()
```
