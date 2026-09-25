// Versions web des photographies du cas « usures antérieures et facettes minimalement invasives »
// (POINT 3.5, 25/09/2026). Leur original est le document que Franck a préparé lui-même :
//   ~/Desktop/Cas_clinique_usure_3Step_Page_GEO_site_V2_facettes_minimalement_invasives.docx
// Les photographies y sont incorporées, chacune accompagnée de sa légende : c'est cette
// correspondance, écrite par Franck, qui les rattache à ce cas — jamais une ressemblance visuelle.
//
// Deux d'entre elles sont déjà publiées sur la page Réhabilitation (`rehabilitation-usure-avant`
// et `-apres`) : comparaison faite fichier par fichier, ce sont les mêmes photographies, donc le
// même patient. Elles ne sont pas recopiées ; le registre réutilise les fichiers existants.
//
// Mêmes règles que `npm run photos` : largeur maximale 2000 px, JPEG qualité 84 sans
// sous-échantillonnage de la couleur, aucune retouche, métadonnées supprimées.
// Lancer : npm run photos-usure
import sharp from "sharp";
import { stat } from "node:fs/promises";
import { homedir } from "node:os";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);

const DOC = `${homedir()}/Desktop/Cas_clinique_usure_3Step_Page_GEO_site_V2_facettes_minimalement_invasives.docx`;
const CIBLE = "src/assets/photos/cas";
const LARGEUR_MAX = 2000;

// image du document → nom publié (l'ordre est celui du document, légendes de Franck en commentaire)
const photos = {
  "image1.png": "usure-3step-sourire-avant.jpg", // Avant traitement
  "image2.png": "usure-3step-sourire-apres.jpg", // Après réhabilitation
  // image3.jpg — Vue initiale : déjà publiée sous rehabilitation-usure-avant.jpg
  "image4.jpg": "usure-3step-palatin-initial.jpg", // Vue palatine : perte de longueur et de substance
  "image5.png": "usure-3step-planification.jpg", // Planification numérique du sourire
  "image6.jpg": "usure-3step-ceramiques-taco.jpg", // Restaurations céramiques antérieures de type TACO
  "image7.jpg": "usure-3step-controle-projet.jpg", // Contrôle du projet restaurateur avant finalisation
  "image8.jpg": "usure-3step-gouttiere-composite.jpg", // Gouttière de composite injecté, secteur mandibulaire
  "image9.jpg": "usure-3step-resultat-sourire.jpg", // Résultat final du sourire
  // image10.jpg — Vue intra-orale finale : déjà publiée sous rehabilitation-usure-apres.jpg
  "image11.jpg": "usure-3step-palatin-final.jpg", // Vue palatine après réhabilitation
  "image12.jpg": "usure-3step-detail-anterieur.jpg", // Détail du secteur antérieur restauré
};

// Le .docx est une archive zip : `unzip -p` en extrait une image sans rien écrire sur le disque
const { execFileSync } = require("node:child_process");

let total = 0;
for (const [source, nom] of Object.entries(photos)) {
  const brut = execFileSync("unzip", ["-p", DOC, `word/media/${source}`], { maxBuffer: 64 * 1024 * 1024 });
  const entree = await sharp(brut).metadata();
  await sharp(brut)
    .rotate()
    .resize({ width: Math.min(LARGEUR_MAX, entree.width), withoutEnlargement: true })
    .jpeg({ quality: 84, chromaSubsampling: "4:4:4", mozjpeg: true })
    .toFile(`${CIBLE}/${nom}`);
  const { size } = await stat(`${CIBLE}/${nom}`);
  total += size;
  console.log(`${nom.padEnd(38)} ${entree.width}×${entree.height} ${(brut.length / 1e6).toFixed(1)} Mo → ${Math.round(size / 1024)} Ko`);
}
console.log(`\n${Object.keys(photos).length} photographies préparées, ${(total / 1e6).toFixed(1)} Mo au total.`);
console.log("2 photographies du document sont déjà publiées (vue initiale et vue finale) : elles ne sont pas recopiées.");
