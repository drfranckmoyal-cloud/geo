// Captures d'écran du golden master (verrous V16 et V17), avec le Chrome installé sur le Mac.
//   Pages entières aux 6 largeurs du pack : 1440, 1280, 1024, 768, 430, 390 px.
//   Détails pour le contrôle de ChatGPT (08 G) : ouvertures ordinateur et mobile, une section,
//   le pied de page.
// Lancer (site servi en local) : BASE_URL=http://localhost:4322 npm run captures
// Série courte d'un tour de correction (D28) : SET=cible OUT=livrables/golden-master-r2/captures
// Micro-tour avant gel (P0.5) : SET=p05 OUT=livrables/golden-master-r3/captures
import { chromium } from "playwright-core";
import { mkdir } from "node:fs/promises";

const BASE = process.env.BASE_URL ?? "http://localhost:4322";
const OUT = process.env.OUT ?? "livrables/golden-master-r1/captures";
const ONLY = process.env.WIDTHS?.split(",").map(Number);
const SET = process.env.SET ?? "complet";
const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

const pages = [
  ["accueil", "/"],
  ["franck-moyal", "/franck-moyal/"],
  ["usures-dentaires", "/usures-dentaires/"],
];
const widths = ONLY ?? [1440, 1280, 1024, 768, 430, 390];
const height = (w) => (w >= 1024 ? 900 : 932);

const browser = await chromium.launch({ executablePath: CHROME, headless: true });

async function open(ctx, path) {
  const page = await ctx.newPage();
  await page.goto(BASE + path, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  // Faire défiler toute la page pour charger les images différées (portrait du bloc auteur…),
  // puis revenir en haut.
  await page.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 600) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 40));
    }
    window.scrollTo(0, 0);
    await Promise.all([...document.images].map((img) => (img.complete ? null : new Promise((r) => (img.onload = img.onerror = r)))));
  });
  await page.waitForTimeout(250);
  return page;
}

// Micro-tour P0.5 avant gel (D31 à D35) : méthode, phrase clé, auteur, en-tête mobile
if (SET === "p05") {
  await mkdir(OUT, { recursive: true });
  const ctx = (w, h) => browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2, reducedMotion: "reduce", locale: "fr-FR" });
  const desk = await ctx(1440, 900), mob = await ctx(430, 932), small = await ctx(390, 844);
  const noSticky = (page) => page.addStyleTag({ content: ".site-header { position: static !important; }" });
  let n = 0;
  const file = (name) => `${OUT}/${String(++n).padStart(2, "0")}_${name}.png`;
  const region = async (page, selectors, name, pad = 32) => {
    const boxes = [];
    for (const sel of selectors) boxes.push(await page.locator(sel).first().boundingBox());
    const top = Math.min(...boxes.map((b) => b.y)) - pad, bottom = Math.max(...boxes.map((b) => b.y + b.height)) + pad;
    const width = page.viewportSize().width;
    await page.screenshot({ path: file(name), fullPage: true, clip: { x: 0, y: Math.max(0, top), width, height: bottom - Math.max(0, top) } });
  };
  for (const [c, label] of [[desk, "ordinateur"], [mob, "mobile"]]) {
    const p = await open(c, "/"); await noSticky(p);
    await p.locator("#methode").screenshot({ path: file(`methode-${label}`) });
    await p.close();
  }
  for (const [c, label] of [[desk, "ordinateur"], [mob, "mobile"]]) {
    const p = await open(c, "/usures-dentaires/"); await noSticky(p);
    await region(p, [".u-quote", ".u-link"], `phrase-cle-${label}`);
    await region(p, [".u-author"], `auteur-${label}`);
    await p.close();
  }
  for (const [c, w, label] of [[small, 390, "390"], [mob, 430, "430"]]) {
    const p = await open(c, "/"); await p.screenshot({ path: file(`en-tete-mobile-${label}`), clip: { x: 0, y: 0, width: w, height: 150 } }); await p.close();
  }
  await Promise.all([desk.close(), mob.close(), small.close()]);
  await browser.close();
  console.log(`micro-tour P0.5 : ${n} captures dans ${OUT}`);
  process.exit(0);
}

// Pages suivantes, lot A (D38) : une page entière représentative, puis uniquement les
// compositions nouvelles (21_MANIFESTE_INTEGRATION.md, « Livraison par lot »).
// SET=lotA OUT=livrables/pages-suivantes-lot-a/captures
if (SET === "lotA") {
  await mkdir(OUT, { recursive: true });
  const ctx = (w, h, scale = 2) => browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: scale, reducedMotion: "reduce", locale: "fr-FR" });
  const desk = await ctx(1440, 900), mob = await ctx(390, 844), deskFull = await ctx(1440, 900, 1), mobFull = await ctx(390, 844, 1);
  const noSticky = (page) => page.addStyleTag({ content: ".site-header { position: static !important; }" });
  let n = 0;
  const file = (name) => `${OUT}/${String(++n).padStart(2, "0")}_${name}.png`;
  const region = async (page, from, to, name, pad = 0) => {
    const a = await page.locator(from).first().boundingBox();
    const b = await page.locator(to).first().boundingBox();
    const width = page.viewportSize().width;
    await page.screenshot({ path: file(name), fullPage: true, clip: { x: 0, y: a.y - pad, width, height: b.y + b.height - a.y + 2 * pad } });
  };
  const section = async (c, path, selector, name) => {
    const p = await open(c, path);
    await noSticky(p);
    await p.locator(selector).screenshot({ path: file(name) });
    await p.close();
  };
  // 1-2. Page Dentisterie esthétique entière
  for (const [c, label] of [[deskFull, "ordinateur-1440"], [mobFull, "mobile-390"]]) {
    const p = await open(c, "/dentisterie-esthetique-paris/");
    await p.screenshot({ path: file(`page-dentisterie-esthetique-${label}`), fullPage: true });
    await p.close();
  }
  // 3. Ouverture clinique avec un H1 long, sur mobile (V16)
  const h = await open(mob, "/taches-dentaires-dyschromies-icon/");
  await h.screenshot({ path: file("ouverture-h1-long-mobile-390") });
  await h.close();
  // 4-5. Intertitres en grille, avec liens et emplacement d'image en pleine largeur
  await section(desk, "/dentisterie-esthetique-paris/", "#quels-traitements-peuvent-transformer-un-sourire", "grille-traitements-ordinateur");
  await section(mob, "/dentisterie-esthetique-paris/", "#quels-traitements-peuvent-transformer-un-sourire", "grille-traitements-mobile");
  // 6. Intertitre H3 sous le titre, liste sur deux colonnes
  await section(desk, "/dentisterie-esthetique-paris/", "#comment-debute-un-projet-esthetique", "sous-titre-et-liste-ordinateur");
  // 7. Texte, liste et emplacement d'image côte à côte
  await section(desk, "/dentisterie-esthetique-paris/", "#quelle-place-pour-le-smile-design", "texte-liste-image-ordinateur");
  // 8. Méthode en 7 étapes sur la page Bilan esthétique
  await section(desk, "/bilan-esthetique-personnalise/", "#methode", "methode-page-bilan-ordinateur");
  // 9. Liste en colonne latérale
  await section(desk, "/composite-bonding-paris/", "#dans-quelles-situations-utilise-t-on-le-composite", "liste-laterale-ordinateur");
  // 10-11. Liste numérotée
  await section(desk, "/facettes-dentaires-paris/", "#a-quoi-ressemble-reellement-le-parcours", "liste-numerotee-ordinateur");
  await section(mob, "/facettes-dentaires-paris/", "#a-quoi-ressemble-reellement-le-parcours", "liste-numerotee-mobile");
  // 12. Sources avec note, bloc auteur
  const s = await open(desk, "/composite-bonding-paris/");
  await noSticky(s);
  await region(s, "#sources", ".pack-author", "sources-note-auteur-ordinateur", 8);
  await s.close();
  // 13. Pages liées puis appel final (ordre du contrat de composants)
  const e = await open(desk, "/dentisterie-esthetique-paris/");
  await noSticky(e);
  await region(e, "nav.related", "#rendez-vous", "pages-liees-appel-final-ordinateur");
  await e.close();
  // 14. Page sans appel final (Éclaircissement : pas de CTA dans le pack)
  const f = await open(desk, "/eclaircissement-dentaire-paris/");
  await noSticky(f);
  await region(f, "#sources", ".site-footer", "fin-de-page-sans-appel-final-ordinateur");
  await f.close();
  await Promise.all([desk.close(), mob.close(), deskFull.close(), mobFull.close()]);
  await browser.close();
  console.log(`lot A : ${n} captures dans ${OUT}`);
  process.exit(0);
}

// Série courte demandée par ChatGPT après le tour 1 (D28)
if (SET === "cible") {
  await mkdir(OUT, { recursive: true });
  const ctx = (w, h) => browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2, reducedMotion: "reduce", locale: "fr-FR" });
  const desk = await ctx(1440, 900), mob = await ctx(430, 932), small = await ctx(390, 844);
  let n = 0;
  const shot = async (page, name, opts = {}) => {
    n++;
    await page.screenshot({ path: `${OUT}/${String(n).padStart(2, "0")}_${name}.png`, ...opts });
  };
  const noSticky = (page) => page.addStyleTag({ content: ".site-header { position: static !important; }" });
  for (const [name, path] of pages) {
    const d = await open(desk, path); await shot(d, `ouverture-ordinateur-${name}`); await d.close();
    const m = await open(mob, path); await shot(m, `ouverture-mobile-${name}`); await m.close();
  }
  // Section Méthode (7 étapes)
  for (const [c, label] of [[desk, "ordinateur"], [mob, "mobile"]]) {
    const p = await open(c, "/"); await noSticky(p);
    await p.locator("#methode").screenshot({ path: `${OUT}/${String(++n).padStart(2, "0")}_methode-${label}.png` });
    await p.close();
  }
  // Sources et auteur (page Usures)
  for (const [c, label] of [[desk, "ordinateur"], [mob, "mobile"]]) {
    const p = await open(c, "/usures-dentaires/"); await noSticky(p);
    const a = await p.locator("#sources").boundingBox();
    const b = await p.locator(".u-author").boundingBox();
    await p.screenshot({ path: `${OUT}/${String(++n).padStart(2, "0")}_sources-auteur-${label}.png`, fullPage: true, clip: { x: 0, y: a.y, width: c === desk ? 1440 : 430, height: b.y + b.height - a.y + 24 } });
    await p.close();
  }
  // En-tête mobile (390 et 430 px)
  for (const [c, w, label] of [[small, 390, "390"], [mob, 430, "430"]]) {
    const p = await open(c, "/"); await shot(p, `en-tete-mobile-${label}`, { clip: { x: 0, y: 0, width: w, height: 150 } }); await p.close();
  }
  // Menu ordinateur, sous-menus ouverts
  for (const [group, label] of [["Érosion & TCA", "erosion-tca"], ["Publications & enseignement", "publications-enseignement"]]) {
    const p = await open(desk, "/"); await p.getByRole("button", { name: group }).click(); await p.waitForTimeout(150);
    await shot(p, `menu-ordinateur-${label}`, { clip: { x: 0, y: 0, width: 1440, height: 420 } }); await p.close();
  }
  // Menu mobile ouvert
  const pm = await open(small, "/"); await pm.locator(".mobile-nav summary").click(); await pm.waitForTimeout(150);
  await shot(pm, "menu-mobile-ouvert"); await pm.close();
  await Promise.all([desk.close(), mob.close(), small.close()]);
  await browser.close();
  console.log(`série courte : ${n} captures dans ${OUT}`);
  process.exit(0);
}

// Pages entières
await mkdir(`${OUT}/pages`, { recursive: true });
await mkdir(`${OUT}/details`, { recursive: true });
for (const w of widths) {
  const ctx = await browser.newContext({
    viewport: { width: w, height: height(w) },
    deviceScaleFactor: 1,
    reducedMotion: "reduce",
    locale: "fr-FR",
  });
  for (const [name, path] of pages) {
    const page = await open(ctx, path);
    await page.screenshot({ path: `${OUT}/pages/${name}-${w}.png`, fullPage: true });
    await page.close();
  }
  await ctx.close();
  console.log(`pages entières : ${w} px`);
}

// Détails, en haute définition (×2)
if (!ONLY) {
  const desk = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, reducedMotion: "reduce", locale: "fr-FR" });
  const mob = await browser.newContext({ viewport: { width: 430, height: 932 }, deviceScaleFactor: 2, reducedMotion: "reduce", locale: "fr-FR" });
  for (const [name, path] of pages) {
    const p1 = await open(desk, path);
    await p1.screenshot({ path: `${OUT}/details/ouverture-ordinateur-${name}.png` });
    await p1.close();
    const p2 = await open(mob, path);
    await p2.screenshot({ path: `${OUT}/details/ouverture-mobile-${name}.png` });
    await p2.close();
  }
  const s = await open(desk, "/usures-dentaires/");
  await s.addStyleTag({ content: ".site-header { position: static !important; }" });
  await s.locator("#causes").screenshot({ path: `${OUT}/details/section-usures-pourquoi-les-dents-s-usent.png` });
  await s.locator(".site-footer").screenshot({ path: `${OUT}/details/pied-de-page.png` });
  await s.close();
  await desk.close();
  await mob.close();
  console.log("détails : ouvertures, section, pied de page");
}

await browser.close();
