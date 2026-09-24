// Versions web des photographies cliniques (intégration du 24/09/2026).
// Les originaux de Franck (~/Desktop/icono GEO) ne sont jamais modifiés ni déplacés : ce programme
// en fabrique une copie allégée dans src/assets/photos/cas/, que le site publie.
//  - largeur maximale 2000 px, suffisant pour un affichage net en haute densité ;
//  - JPEG qualité 84, sans sous-échantillonnage de la couleur (détail dentaire préservé) ;
//  - aucune retouche : ni luminosité, ni saturation, ni balance des blancs, ni netteté ;
//  - métadonnées (EXIF, IPTC, GPS) supprimées — sharp ne les recopie pas par défaut.
// Lancer : npm run photos
import sharp from "sharp";
import { mkdir, readdir, stat } from "node:fs/promises";
import { homedir } from "node:os";

const SOURCE = `${homedir()}/Desktop/icono GEO`;
const CIBLE = "src/assets/photos/cas";
const LARGEUR_MAX = 2000;

// original (dans le dossier de Franck) → nom publié
const photos = {
  "Composite bonding/1.png": "composite-bonding-six-dents-anterieures.jpg",
  "Composite bonding/2.png": "composite-bonding-quatre-dents-anterieures.jpg",
  "Composite bonding/3.jpg": "composite-stratifie-dyschromie.jpg",
  "Facettes /1.png": "facettes-planification-initial.jpg",
  "Facettes /2.png": "facettes-planification-projet.jpg",
  "Facettes /3.png": "facettes-planification-resultat.jpg",
  "Facettes /facettes cas 2 /avant.JPG": "facettes-ceramique-avant.jpg",
  "Facettes /facettes cas 2 /apres.jpg": "facettes-ceramique-apres.jpg",
  "Eclaircissement/1.jpg": "eclaircissement-ambulatoire-avant.jpg",
  "Eclaircissement/2.jpg": "eclaircissement-ambulatoire-apres.jpg",
  "Icon/1.jpg": "mih-erosion-infiltration-avant.jpg",
  "Icon/1bis.jpg": "mih-erosion-infiltration-apres.jpg",
  "Icon/2.jpg": "dyschromie-erosion-infiltration-avant.jpg",
  "Icon/2bis.jpg": "dyschromie-erosion-infiltration-apres.jpg",
  "Erosion /1.JPG": "usure-erosive-exogene.jpg",
  "Erosion /2.jpg": "usure-erosive-raccourcissement.jpg",
  "Bilan esthetique /initial .jpg": "bilan-esthetique-initial.jpg",
  "Bilan esthetique /Projet.png": "bilan-esthetique-projet.jpg",
  "Bilan esthetique /final .jpg": "bilan-esthetique-resultat.jpg",
  "Usures /cas 1.jpg": "usure-anterieure-reconstruction.jpg",
  "Usures /cas 2 /avant .jpg": "rehabilitation-usure-avant.jpg",
  "Usures /cas 2 /après.jpg": "rehabilitation-usure-apres.jpg",
};

await mkdir(CIBLE, { recursive: true });
const existants = new Set(await readdir(CIBLE).catch(() => []));
let total = 0;
for (const [origine, nom] of Object.entries(photos)) {
  const src = `${SOURCE}/${origine}`;
  const entree = await sharp(src).metadata();
  await sharp(src)
    .rotate() // respecte l'orientation enregistrée par l'appareil avant de retirer les métadonnées
    .resize({ width: Math.min(LARGEUR_MAX, entree.width), withoutEnlargement: true })
    .jpeg({ quality: 84, chromaSubsampling: "4:4:4", mozjpeg: true })
    .toFile(`${CIBLE}/${nom}`);
  const apres = await stat(`${CIBLE}/${nom}`);
  const avant = await stat(src);
  total += apres.size;
  console.log(
    `${nom.padEnd(46)} ${String(entree.width).padStart(4)}×${String(entree.height).padEnd(4)} ${(avant.size / 1e6).toFixed(1)} Mo → ${Math.round(apres.size / 1024)} Ko`,
  );
  existants.delete(nom);
}
console.log(`\n${Object.keys(photos).length} photographies préparées, ${(total / 1e6).toFixed(1)} Mo au total.`);
if (existants.size) console.log(`Fichiers présents dans ${CIBLE} et absents de cette liste : ${[...existants].join(", ")}`);
