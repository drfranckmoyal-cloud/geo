// Captures d'écran du golden master (verrous V16 et V17), avec le Chrome installé sur le Mac.
//   Pages entières aux 6 largeurs du pack : 1440, 1280, 1024, 768, 430, 390 px.
//   Détails pour le contrôle de ChatGPT (08 G) : ouvertures ordinateur et mobile, une section,
//   le pied de page.
// Lancer (site servi en local) : BASE_URL=http://localhost:4322 npm run captures
import { chromium } from "playwright-core";
import { mkdir } from "node:fs/promises";

const BASE = process.env.BASE_URL ?? "http://localhost:4322";
const OUT = process.env.OUT ?? "livrables/golden-master-r1/captures";
const ONLY = process.env.WIDTHS?.split(",").map(Number);
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
