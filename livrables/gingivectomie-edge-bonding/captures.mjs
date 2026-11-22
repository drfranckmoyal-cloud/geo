// Captures des deux pages écrites le 22/11/2026 (Gingivectomie, Edge bonding), pour que Franck les voie
// en maquette avant toute mise en ligne. La maquette doit être servie en local (port 4330).
//   node livrables/gingivectomie-edge-bonding/captures.mjs
import { chromium } from "playwright-core";

const BASE = "http://localhost:4330/docs/refonte/maquettes/site/";
const OUT = "livrables/gingivectomie-edge-bonding/maquettes/";
const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
// sans l'option, chaque lancement laisse un clone de Chrome de 2 Go apparents (voir scripts/captures.mjs)
const browser = await chromium.launch({
  executablePath: CHROME, headless: true, args: ["--disable-features=MacAppCodeSignClone"],
});
const pages = [["01-gingivectomie", "gingivectomie-paris.html"], ["02-edge-bonding", "edge-bonding-paris.html"]];
for (const [largeur, hauteur, suffixe, echelle] of [[1440, 900, "ordinateur", 1], [390, 844, "telephone", 2]]) {
  const ctx = await browser.newContext({ viewport: { width: largeur, height: hauteur }, deviceScaleFactor: echelle,
    reducedMotion: "reduce", locale: "fr-FR" });
  for (const [nom, fichier] of pages) {
    const page = await ctx.newPage();
    await page.goto(BASE + fichier, { waitUntil: "networkidle" });
    await page.evaluate(() => document.fonts.ready);
    await page.addStyleTag({ content: ".entete{position:static !important} .barre-mobile{display:none !important}" });
    await page.evaluate(async () => {
      for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 40)); }
      window.scrollTo(0, 0);
    });
    await page.waitForTimeout(250);
    await page.screenshot({ path: `${OUT}${nom}-${suffixe}.jpg`, fullPage: true, type: "jpeg", quality: 82 });
    const debord = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    console.log(nom, suffixe, "hauteur", await page.evaluate(() => document.body.scrollHeight), "débordement", debord);
    await page.close();
  }
  await ctx.close();
}
await browser.close();
