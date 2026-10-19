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
// Depuis le 19/10/2026, Franck dépose aussi des photographies par thème de carte :
const SOURCE_THEMES = `${homedir()}/Desktop/PHOTOS SITE - par theme`;
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
// Les quatre étapes du bilan esthétique (dossier « 01 Bilan esthetique », 19/10/2026).
// Les noms de fichiers sont ceux de Franck, qui y a écrit les légendes et l'ordre.
const photosThemes = {
  "01 Bilan esthetique/Un bilan photographique est réalisé à chaque premiere consultation (photo a placer avant 1).png":
    "bilan-parcours-1-photographies.jpg",
  "01 Bilan esthetique/1 - La forme des dents du futur sourire est determinée grace aux logiciels de planification .png":
    "bilan-parcours-2-planification.jpg",
  "01 Bilan esthetique/2 - une modélisation 3D du projet esthétique est ensuite réalisée .png":
    "bilan-parcours-3-modelisation-3d.jpg",
  "01 Bilan esthetique/3 - une simulation en situation réele eest générée en fonction du projet pour donner une idée du resultat final à atteindre.jpg":
    "bilan-parcours-4-simulation.jpg",
  // Éclaircissement : deux images générées (Canva, 19/10/2026), pas des photographies de patients.
  "02 Eclaircissement/gouttieres-de-blanchiment (image generee).jpg":
    "eclaircissement-gouttieres.jpg",
  "02 Eclaircissement/colorants vin rouge cafe the cigarette (image generee).jpg":
    "eclaircissement-colorants.jpg",
  "02 Eclaircissement/sensibilites eau glacee (image generee).jpg":
    "eclaircissement-sensibilites.jpg",
  // Trois cas d'éclaircissement, montages avant/après fabriqués sur le Mac (19/10/2026).
  "02 Eclaircissement/_montages/eclaircissement-cas-1-avant-apres.jpg": "eclaircissement-cas-1-avant-apres.jpg",
  "02 Eclaircissement/_montages/eclaircissement-cas-2-avant-apres.jpg": "eclaircissement-cas-2-avant-apres.jpg",
  "02 Eclaircissement/_montages/eclaircissement-cas-3-avant-apres.jpg": "eclaircissement-cas-3-avant-apres.jpg",
  "02 Eclaircissement/_montages/eclaircissement-cas-1-couverture.jpg": "eclaircissement-cas-1-couverture.jpg",
  // Infiltration ICON (19/10/2026) : deux cas détourés sur fond noir (Canva), montés sur le Mac ;
  // un cas en trois temps (tache, traitement, résultat) et un exemple de fluorose. Noms neutres.
  "03 Infiltration ICON/_montages/icon-cas-1-avant-apres.jpg": "icon-cas-1-avant-apres.jpg",
  "03 Infiltration ICON/_montages/icon-cas-2-avant-apres.jpg": "icon-cas-2-avant-apres.jpg",
  "03 Infiltration ICON/_montages/icon-cas-1-couverture.jpg": "icon-cas-1-couverture.jpg",
  "03 Infiltration ICON/_montages/icon-fluorose.jpg": "icon-fluorose.jpg",
  "03 Infiltration ICON/_montages/icon-mih-tache.jpg": "icon-mih-tache.jpg",
  "03 Infiltration ICON/_montages/icon-traitement-21.jpg": "icon-traitement-21.jpg",
  "03 Infiltration ICON/_montages/icon-resultat-associe.jpg": "icon-resultat-associe.jpg",
};

await mkdir(CIBLE, { recursive: true });
const existants = new Set(await readdir(CIBLE).catch(() => []));
let total = 0;
const lots = [
  ...Object.entries(photos).map(([o, n]) => [`${SOURCE}/${o}`, n]),
  ...Object.entries(photosThemes).map(([o, n]) => [`${SOURCE_THEMES}/${o}`, n]),
];
for (const [src, nom] of lots) {
  // Un original absent (dossier déplacé, rangé) n'arrête pas tout : la version web
  // déjà publiée dans le dépôt reste telle quelle, on le signale et on continue.
  let entree;
  try {
    entree = await sharp(src).metadata();
  } catch {
    console.log(`${nom.padEnd(46)} original introuvable — version publiée conservée`);
    existants.delete(nom);
    continue;
  }
  await sharp(src)
    .rotate() // respecte l'orientation enregistrée par l'appareil avant de retirer les métadonnées
    .flatten({ background: "#ffffff" }) // un PNG avec transparence s'aplatit sur blanc
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
