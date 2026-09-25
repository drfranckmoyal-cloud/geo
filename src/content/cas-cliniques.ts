// Cas cliniques du Dr Franck Moyal : photographies réelles de sa pratique, fournies par lui dans
// « icono GEO » et documentées dans sa fiche de renseignements. Consentements de publication web
// confirmés par Franck, transmis par ChatGPT le 24/09/2026.
//
// Les versions publiées sont fabriquées par `npm run photos` (src/assets/photos/cas/) : allégées,
// sans métadonnées, sans aucune retouche de couleur, de luminosité ni de netteté.
//
// Ce fichier est le registre des cas. Il est prévu pour être enrichi plus tard (POINT 3 :
// preuve clinique) — un cas pourra recevoir demande, diagnostic, options envisagées, traitement
// retenu, suivi et liens, sans qu'il faille déplacer les photographies ni retoucher les pages.
//
// Règles de légende (ChatGPT, §11, §25, §31) : court, factuel, clinique ; aucune information
// personnelle ; aucune pathologie rattachée publiquement au patient photographié ; rien d'inventé
// sur la technique, la durée, le matériau ou le nombre de séances quand ce n'est pas documenté.

import compositeSix from "../assets/photos/cas/composite-bonding-six-dents-anterieures.jpg";
import compositeQuatre from "../assets/photos/cas/composite-bonding-quatre-dents-anterieures.jpg";
import compositeStratifie from "../assets/photos/cas/composite-stratifie-dyschromie.jpg";
import facettesInitial from "../assets/photos/cas/facettes-planification-initial.jpg";
import facettesProjet from "../assets/photos/cas/facettes-planification-projet.jpg";
import facettesResultat from "../assets/photos/cas/facettes-planification-resultat.jpg";
import facettesAvant from "../assets/photos/cas/facettes-ceramique-avant.jpg";
import facettesApres from "../assets/photos/cas/facettes-ceramique-apres.jpg";
import eclaircissementAvant from "../assets/photos/cas/eclaircissement-ambulatoire-avant.jpg";
import eclaircissementApres from "../assets/photos/cas/eclaircissement-ambulatoire-apres.jpg";
import mihAvant from "../assets/photos/cas/mih-erosion-infiltration-avant.jpg";
import mihApres from "../assets/photos/cas/mih-erosion-infiltration-apres.jpg";
import dyschromieAvant from "../assets/photos/cas/dyschromie-erosion-infiltration-avant.jpg";
import dyschromieApres from "../assets/photos/cas/dyschromie-erosion-infiltration-apres.jpg";
import erosionExogene from "../assets/photos/cas/usure-erosive-exogene.jpg";
import erosionRaccourcissement from "../assets/photos/cas/usure-erosive-raccourcissement.jpg";
import bilanInitial from "../assets/photos/cas/bilan-esthetique-initial.jpg";
import bilanProjet from "../assets/photos/cas/bilan-esthetique-projet.jpg";
import bilanResultat from "../assets/photos/cas/bilan-esthetique-resultat.jpg";
import usureReconstruction from "../assets/photos/cas/usure-anterieure-reconstruction.jpg";
import rehabilitationAvant from "../assets/photos/cas/rehabilitation-usure-avant.jpg";
import rehabilitationApres from "../assets/photos/cas/rehabilitation-usure-apres.jpg";

export interface CasImage {
  src: ImageMetadata;
  alt: string;
  /** Étiquette affichée au-dessus de l'image : « Avant », « Projet »… */
  etiquette?: string;
  /** Légende employée lorsque cette photographie est affichée seule, dans sa propre section
   *  d'une page de cas clinique (POINT 3, phase B) */
  legende?: string;
}

export interface CasClinique {
  /** Identifiant stable, réutilisable (POINT 3) */
  id: string;
  /** une photographie ; deux photographies comparées ; une séquence de trois */
  type: "image" | "avant-apres" | "sequence";
  /** Légende du cas, affichée sous la ou les photographies */
  legende: string;
  /** « Cas clinique — Dr Franck Moyal », une seule fois par cas */
  attribution?: boolean;
  images: CasImage[];
}

const ATTRIBUTION = "Cas clinique — Dr Franck Moyal";

export const casCliniques: Record<string, CasClinique> = {
  "composite-six-dents": {
    id: "composite-six-dents",
    type: "image",
    legende: "Reconstruction esthétique additive de six dents antérieures en composite : avant, puis après.",
    attribution: true,
    images: [{ src: compositeSix, alt: "Six dents antérieures avant, puis après reconstruction additive en composite" }],
  },
  "composite-quatre-dents": {
    id: "composite-quatre-dents",
    type: "image",
    legende: "Reconstruction esthétique additive de quatre dents antérieures en composite : avant, puis après.",
    attribution: true,
    images: [{ src: compositeQuatre, alt: "Quatre dents antérieures avant, puis après reconstruction additive en composite" }],
  },
  "composite-stratifie": {
    id: "composite-stratifie",
    type: "image",
    legende: "Composite stratifié sur une dent antérieure présentant une dyschromie : avant, puis après.",
    attribution: true,
    images: [{ src: compositeStratifie, alt: "Dent antérieure dyschromiée avant, puis après composite stratifié" }],
  },
  "facettes-planification": {
    id: "facettes-planification",
    type: "sequence",
    legende: "Exemple de planification d’un traitement par facettes : situation initiale, projet esthétique et résultat clinique.",
    attribution: true,
    images: [
      {
        src: facettesInitial,
        alt: "Situation initiale avant traitement par facettes",
        etiquette: "Situation initiale",
        legende: "Situation initiale, avant toute intervention.",
      },
      {
        src: facettesProjet,
        alt: "Projet esthétique numérique avant réalisation des facettes",
        etiquette: "Projet",
        legende: "Projet esthétique numérique réalisé avec SmileCloud. L’appareil orthodontique en place fait partie du traitement.",
      },
      {
        src: facettesResultat,
        alt: "Résultat clinique après traitement par facettes",
        etiquette: "Résultat",
        legende: "Résultat après la pose de quatre facettes en céramique.",
      },
    ],
  },
  "facettes-ceramique": {
    id: "facettes-ceramique",
    type: "avant-apres",
    legende: "Exemple clinique d’un traitement par facettes en céramique.",
    attribution: true,
    images: [
      { src: facettesAvant, alt: "Dents antérieures avant traitement par facettes en céramique", etiquette: "Avant" },
      { src: facettesApres, alt: "Dents antérieures après traitement par facettes en céramique", etiquette: "Après" },
    ],
  },
  "eclaircissement-ambulatoire": {
    id: "eclaircissement-ambulatoire",
    type: "avant-apres",
    legende: "Évolution de la teinte après 4 semaines d’éclaircissement ambulatoire.",
    attribution: true,
    images: [
      { src: eclaircissementAvant, alt: "Situation avant éclaircissement dentaire", etiquette: "Avant" },
      { src: eclaircissementApres, alt: "Résultat après quatre semaines d’éclaircissement ambulatoire", etiquette: "Après 4 semaines" },
    ],
  },
  "mih-erosion-infiltration": {
    id: "mih-erosion-infiltration",
    type: "avant-apres",
    legende: "Tache de MIH sur une incisive — prise en charge associant éclaircissement et érosion-infiltration.",
    attribution: true,
    images: [
      { src: mihAvant, alt: "Tache blanche de MIH visible sur une incisive avant traitement", etiquette: "Avant" },
      { src: mihApres, alt: "Incisive après éclaircissement et érosion-infiltration de résine", etiquette: "Après" },
    ],
  },
  "dyschromie-erosion-infiltration": {
    id: "dyschromie-erosion-infiltration",
    type: "avant-apres",
    legende: "Dyschromie unitaire associée à une tache blanche — prise en charge par éclaircissement puis érosion-infiltration.",
    attribution: true,
    images: [
      { src: dyschromieAvant, alt: "Dyschromie et tache blanche sur une incisive avant traitement", etiquette: "Avant" },
      { src: dyschromieApres, alt: "Incisive après éclaircissement et érosion-infiltration de résine", etiquette: "Après" },
    ],
  },
  "erosion-exogene": {
    id: "erosion-exogene",
    type: "image",
    legende: "Exemple d’usure dentaire érosive associée à une exposition acide exogène.",
    attribution: true,
    images: [{ src: erosionExogene, alt: "Usure dentaire érosive visible sur les dents antérieures" }],
  },
  "erosion-raccourcissement": {
    id: "erosion-raccourcissement",
    type: "image",
    legende: "Usure dentaire érosive avec raccourcissement des dents.",
    attribution: true,
    images: [{ src: erosionRaccourcissement, alt: "Dents antérieures raccourcies par une usure dentaire érosive" }],
  },
  "bilan-esthetique": {
    id: "bilan-esthetique",
    type: "sequence",
    legende: "De la situation initiale au projet esthétique puis au résultat clinique.",
    attribution: true,
    images: [
      {
        src: bilanInitial,
        alt: "Situation initiale avant projet esthétique",
        etiquette: "Situation initiale",
        legende: "Situation initiale : usures importantes et déficit esthétique majeur.",
      },
      {
        src: bilanProjet,
        alt: "Projet esthétique numérique construit à partir des photographies du patient",
        etiquette: "Projet",
        legende: "Simulation numérique du projet esthétique, réalisée avec SmileCloud.",
      },
      {
        src: bilanResultat,
        alt: "Résultat clinique après réalisation du projet esthétique",
        etiquette: "Résultat",
        legende: "Résultat après la pose de vingt facettes en céramique.",
      },
    ],
  },
  "usure-reconstruction": {
    id: "usure-reconstruction",
    type: "image",
    legende: "Dents antérieures usées, avant et après reconstruction.",
    attribution: true,
    images: [{ src: usureReconstruction, alt: "Dents antérieures usées, puis reconstruites" }],
  },
  "rehabilitation-usure": {
    id: "rehabilitation-usure",
    type: "avant-apres",
    legende: "Dents usées avant et après reconstruction.",
    attribution: true,
    images: [
      { src: rehabilitationAvant, alt: "Dents antérieures usées avant reconstruction", etiquette: "Avant" },
      { src: rehabilitationApres, alt: "Dents antérieures après reconstruction", etiquette: "Après" },
    ],
  },
};

export const attributionCas = ATTRIBUTION;
