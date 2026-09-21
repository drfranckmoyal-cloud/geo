// Captures d'écran du golden master (verrous V16 et V17), avec le Chrome installé sur le Mac.
//   Pages entières aux 6 largeurs du pack : 1440, 1280, 1024, 768, 430, 390 px.
//   Détails pour le contrôle de ChatGPT (08 G) : ouvertures ordinateur et mobile, une section,
//   le pied de page.
// Lancer (site servi en local) : BASE_URL=http://localhost:4322 npm run captures
// Série courte d'un tour de correction (D28) : SET=cible OUT=livrables/golden-master-r2/captures
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

await mkdir(`${OUT}/pages`, { recursive: true });
await mkdir(`${OUT}/details`, { recursive: true });
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
