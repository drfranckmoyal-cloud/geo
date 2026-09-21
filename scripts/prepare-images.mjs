// Prépare les images du site à partir des originaux fournis par Franck.
//  1. Logo : le monogramme « Fm » (PNG) est vectorisé en SVG, en deux couches —
//     l'encre en noir doux de la palette, l'arc dans le vert sauge d'origine du logo.
//  2. Portrait : recadré en 4:5, contraste local légèrement renforcé, noir et blanc purs
//     remplacés par le noir doux et le blanc cassé de la palette.
//  3. Icônes de navigateur (favicon) tirées du logo.
// Lancer : npm run images
import sharp from "sharp";
import potrace from "potrace";
import { mkdir, writeFile } from "node:fs/promises";
import { promisify } from "node:util";

const trace = promisify(potrace.trace);
const INK = "#171715";
const PAPER = "#FAF8F3";
const ARC = "#848C73"; // vert de l'arc, mesuré sur le logo d'origine

const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));

// Deux cartes d'intensité (0 = fond, 255 = trait) : l'encre (gris sombre neutre) et l'arc
// (seul élément verdâtre). Lissées puis seuillées à mi-hauteur, elles donnent des contours
// propres au traçage.
async function masks(src) {
  const { data, info } = await sharp(src).removeAlpha().raw().toBuffer({ resolveWithObject: true });
  const { width, height } = info;
  const ink = Buffer.alloc(width * height, 0);
  const arc = Buffer.alloc(width * height, 0);
  const clamp = (v) => Math.max(0, Math.min(255, Math.round(v)));
  for (let i = 0; i < width * height; i++) {
    const r = data[i * 3], g = data[i * 3 + 1], b = data[i * 3 + 2];
    const lum = 0.299 * r + 0.587 * g + 0.114 * b;
    const green = g - (r + b) / 2; // ≈ 0,5 pour le fond, ≈ 17 au cœur de l'arc, ≈ 1,5 pour l'encre
    if (green > 5 && lum > 95) arc[i] = clamp((green / 17) * 255);
    else ink[i] = clamp(((250 - lum) / (250 - 45)) * 255);
  }
  const toPng = (buf, sigma) =>
    sharp(buf, { raw: { width, height, channels: 1 } }).blur(sigma).threshold(118).negate().png().toBuffer();
  return { ink: await toPng(ink, 0.8), arc: await toPng(arc, 1.6), width, height };
}

const pathsOf = (svg) => [...svg.matchAll(/<path[^>]*\sd="([^"]+)"/g)].map((m) => m[1]).join(" ");

async function logo() {
  const src = "src/assets/brand/logo-fm-source.png";
  const m = await masks(src);
  const opts = { threshold: 128, turdSize: 6, optTolerance: 0.25, alphaMax: 1.0, color: "#000", background: "transparent" };
  const inkD = pathsOf(await trace(m.ink, opts));
  const arcD = pathsOf(await trace(m.arc, opts));
  // Cadre serré autour du dessin (mesuré : x 313–945, y 426–826), avec une petite marge.
  const vb = [300, 412, 660, 428];
  const body = (inkFill, arcFill) =>
    `<path fill="${arcFill}" fill-rule="evenodd" d="${arcD}"/><path fill="${inkFill}" fill-rule="evenodd" d="${inkD}"/>`;
  const svg = (inkFill, arcFill, extra = "") =>
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb.join(" ")}" role="img" aria-label="Dr Franck Moyal">${extra}${body(inkFill, arcFill)}</svg>\n`;
  await mkdir("src/assets/brand", { recursive: true });
  await writeFile("src/assets/brand/logo-fm.svg", svg(INK, ARC));
  // Icône carrée : monogramme centré sur fond blanc cassé.
  const side = 700, x0 = vb[0] + vb[2] / 2 - side / 2, y0 = vb[1] + vb[3] / 2 - side / 2 + 20;
  const icon = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${x0} ${y0} ${side} ${side}"><rect x="${x0}" y="${y0}" width="${side}" height="${side}" fill="${PAPER}"/>${body(INK, ARC)}</svg>\n`;
  await mkdir("public", { recursive: true });
  await writeFile("public/favicon.svg", icon);
  await sharp(Buffer.from(icon)).resize(180, 180).png().toFile("public/apple-touch-icon.png");
  await sharp(Buffer.from(icon)).resize(48, 48).png().toFile("public/favicon-48.png");
  // Aperçu de contrôle (non publié)
  await sharp(Buffer.from(svg(INK, ARC, `<rect x="${vb[0]}" y="${vb[1]}" width="${vb[2]}" height="${vb[3]}" fill="${PAPER}"/>`)))
    .resize(1320).png().toFile("scripts/.apercu-logo.png");
  console.log("logo : SVG et icônes écrits");
}

// Portrait HD (D26) : original du Nikon D780, 6048 × 4024 px, fourni par Franck le 21/09/2026.
async function portrait() {
  const src = "src/assets/photos/portrait-franck-source.png";
  const meta = await sharp(src).metadata();
  // Recadrage vertical 4:5 sur toute la hauteur, centré sur le visage (centre mesuré : 45,7 %
  // de la largeur) ; il reste 10 % d'air au-dessus des cheveux.
  const cropH = meta.height;
  const cropW = Math.round((cropH * 4) / 5);
  const cx = Math.round(meta.width * 0.457);
  const left = Math.max(0, Math.min(meta.width - cropW, cx - Math.round(cropW / 2)));
  const W = 1600, H = 2000;
  const base = () =>
    sharp(src).extract({ left, top: 0, width: cropW, height: cropH }).resize(W, H, { kernel: "lanczos3" }).greyscale();
  const plainImg = await base().sharpen({ sigma: 0.6 }).raw().toBuffer({ resolveWithObject: true });
  // Contraste local du visage légèrement renforcé, comme demandé pour la version HD (D26) :
  // 60 % d'une égalisation locale douce, 40 % de l'image d'origine.
  const boosted = await base().clahe({ width: 400, height: 400, maxSlope: 2 }).sharpen({ sigma: 0.6 }).raw().toBuffer();
  const info = plainImg.info;
  const data = Buffer.alloc(plainImg.data.length);
  for (let i = 0; i < data.length; i++) data[i] = Math.round(plainImg.data[i] * 0.4 + boosted[i] * 0.6);
  const [a, b] = [hex(INK), hex(PAPER)];
  // Point noir = gris moyen du fond, mesuré dans les deux coins hauts : le fond de la photo tombe
  // exactement sur le noir doux et se fond dans un aplat de même couleur.
  const C = info.channels;
  let sum = 0, n = 0;
  for (const [x0, y0] of [[0, 0], [W - 120, 0]])
    for (let y = y0; y < y0 + 120; y++) for (let x = x0; x < x0 + 120; x++) { sum += data[(y * W + x) * C]; n++; }
  const black = Math.round(sum / n) + 3;
  const out = Buffer.alloc(W * H * 3);
  for (let i = 0; i < W * H; i++) {
    const t = Math.max(0, (data[i * C] - black) / (255 - black));
    for (let c = 0; c < 3; c++) out[i * 3 + c] = Math.round(a[c] + (b[c] - a[c]) * t);
  }
  await sharp(out, { raw: { width: W, height: H, channels: 3 } })
    .jpeg({ quality: 92, mozjpeg: true })
    .toFile("src/assets/photos/portrait-franck.jpg");
  console.log(`portrait : ${meta.width}×${meta.height} → ${W}×${H}, point noir ${black}, harmonisé noir doux / blanc cassé`);
}

await logo();
await portrait();
