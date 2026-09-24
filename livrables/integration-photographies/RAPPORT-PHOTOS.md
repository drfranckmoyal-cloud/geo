# Intégration définitive des photographies cliniques — rapport final

*Claude Code, 24 septembre 2026. Consigne archivée telle quelle dans
`docs/echanges/2026-09-24-chatgpt-integration-photographies-cliniques.md` (52 points).
Site contrôlé **en production** après déploiement : https://drfranckmoyal.fr*

---

## A — INTÉGRATION

**Photos source retrouvées :** 22, dans `~/Desktop/icono GEO` (112 Mo), réparties en 7 dossiers —
Composite bonding (3), Facettes (5, dont un sous-dossier « facettes cas 2 »), Éclaircissement (2),
Icon (4), Erosion (2), Bilan esthetique (3), Usures (3). Aucune photographie de cabinet, aucun scan
de suivi : rien n'a été inventé pour combler ces manques, aucune image n'a été générée.
**Les originaux n'ont pas été touchés** (aucun fichier modifié le 24/09/2026, dossier intact).

**Photos préparées pour le web :** 22, dans `src/assets/photos/cas/` (4,5 Mo), fabriquées par
`npm run photos` (`scripts/prepare-photos.mjs`).

**Photos intégrées :** **22 sur 22**, regroupées en **13 cas cliniques** sur **8 pages**.

**Photos volontairement non intégrées :** aucune. Deux précisions :

- les trois images du dossier « Bilan esthetique » forment une seule séquence (initial → projet →
  résultat) : un cas, trois photographies ;
- deux photographies du dossier « Composite bonding » et une du dossier « Usures » sont des montages
  avant/après réalisés par Franck lui-même (les deux états dans une même image). Elles sont donc
  posées en photographie seule, avec une légende qui dit « avant, puis après », et non en composant
  avant/après — poser un montage dans un cadre « Avant » aurait été faux.

---

## B — RÉPARTITION

### Composite bonding — `/composite-bonding-paris/`

**Photos :** 3. **Composants :** 3 × `ClinicalImage`.
**Emplacements :**

| Cas | Après la section |
|---|---|
| `composite-stratifie` | « Construire une dent couche après couche » |
| `composite-six-dents` | « Ce que je recherche avec un composite antérieur » |
| `composite-quatre-dents` | « Ce que je recherche avec un composite antérieur » |

### Facettes — `/facettes-dentaires-paris/`

**Photos :** 5. **Composants :** `ClinicalSequence` (3 images) + `ClinicalBeforeAfter` (2 images).
**Emplacements :**

| Cas | Après la section |
|---|---|
| `facettes-planification` (initial → projet → résultat) | « Sublimer un sourire plutôt que remplacer des dents » |
| `facettes-ceramique` (avant / après) | « La céramique : lumière, profondeur et finesse » |

### Éclaircissement — `/eclaircissement-dentaire-paris/`

**Photos :** 2. **Composant :** `ClinicalBeforeAfter` (« Avant » / « Après 4 semaines »).
**Emplacement :** après « Est-ce que le résultat est visible ? ».

### Taches / ICON — `/taches-dentaires-dyschromies-icon/`

**Photos :** 4. **Composants :** 2 × `ClinicalBeforeAfter`.
**Emplacements :**

| Cas | Après la section |
|---|---|
| `mih-erosion-infiltration` | « Oui, lorsqu'une opacité d'une incisive permanente est gênante » |
| `dyschromie-erosion-infiltration` | « Une technique très conservatrice pour certaines taches blanches » |

### Érosion — `/erosion-dentaire/`

**Photos :** 2. **Composants :** 2 × `ClinicalImage`.
**Emplacements :**

| Cas | Après la section |
|---|---|
| `erosion-exogene` | « Quels sont les premiers signes ? » |
| `erosion-raccourcissement` | « Quand faut-il restaurer ? » |

### Bilan esthétique — `/bilan-esthetique-personnalise/`

**Photos :** 3. **Composant :** `ClinicalSequence` (situation initiale → projet → résultat).
**Emplacement :** après « Qu'apporte le smile design ? ».

### Usures / Réhabilitation

**Photos :** 3. **Composants :** `ClinicalImage` sur `/usures-dentaires/`, `ClinicalBeforeAfter` sur
`/rehabilitation-dents-usees/`.
**Emplacements :**

| Page | Cas | Après la section |
|---|---|---|
| `/usures-dentaires/` | `usure-reconstruction` | « Restaurer l'esthétique et la fonction ensemble » |
| `/rehabilitation-dents-usees/` | `rehabilitation-usure` | « Réhabiliter une dentition usée ne signifie plus automatiquement poser des couronnes » |

Sur `/usures-dentaires/`, la photographie remplace l'emplacement réservé qui était prévu à cet
endroit : il n'y a plus d'emplacement vide sur cette page.

---

## C — FICHIERS

| | |
|---|---|
| **Originaux** | `~/Desktop/icono GEO` — 22 fichiers, 112 Mo, JPEG et PNG, jusqu'à 4032 px de large. **Jamais modifiés, jamais déplacés, jamais recopiés dans le dépôt.** |
| **Versions web** | `src/assets/photos/cas/` — 22 fichiers, 4,5 Mo, dans le dépôt GitHub privé avec le site (arbitrage de Franck du 24/09/2026). |
| **Fabrication** | `npm run photos` (`scripts/prepare-photos.mjs`, sharp) : largeur ramenée à 2000 px au maximum, orientation de l'appareil appliquée puis **métadonnées supprimées** (EXIF, IPTC, GPS), JPEG qualité 84 **sans sous-échantillonnage de la couleur** (4:4:4, le détail dentaire est préservé). **Aucune retouche** : ni luminosité, ni contraste, ni saturation, ni balance des blancs, ni netteté, ni recadrage. Le programme est rejouable : il refabrique les 22 fichiers à l'identique. |
| **Stratégie de formats** | Le site fabrique lui-même, à la construction, les versions réellement servies : **WebP**, en 3 largeurs par image (600 / 900 / 1400 px pour une photographie seule, 500 / 800 / 1200 px pour un avant/après, 400 / 700 / 1000 px pour une séquence de trois). Le navigateur choisit la largeur qui correspond à l'écran (`srcset` + `sizes`). Le JPEG reste la source ; il n'est pas servi. |
| **Tailles finales servies** | 32 à 146 Ko par photographie, **1,86 Mo pour les 22**. Mise en cache par le serveur : 7 jours. |
| **Registre des cas** | `src/content/cas-cliniques.ts` : identifiant stable, type d'affichage, légende, attribution, `alt` de chaque image. Prévu pour le POINT 3 — un cas pourra recevoir demande, diagnostic, options, traitement, suivi et liens **sans déplacer une seule photographie ni retoucher une page**. |
| **Composants** | `src/components/clinical/ClinicalImage.astro`, `ClinicalBeforeAfter.astro`, `ClinicalSequence.astro`, et `CasClinique.astro` qui choisit le bon composant à partir du registre. Composants gelés du golden master non modifiés (verrou V24). |

---

## D — ÉDITORIAL

Mesuré sur les 22 pages **en production**, texte patient et bibliographies comptés séparément :

| | |
|---|---|
| `erosive tooth wear` visible patient | **0** — 12 occurrences subsistent, toutes dans les titres de publications scientifiques (5 pages), comme demandé |
| `umbrella review` visible patient | **0** — 3 occurrences subsistent, toutes dans les titres de publications (`/anorexie-erosion-dentaire-sans-vomissements/`, `/erosion-dentaire/`, `/taches-dentaires-dyschromies-icon/`) |
| `workflow` dans la phrase concernée | remplacé par **« démarche »** ; le mot `workflow` n'apparaît plus **nulle part** sur le site |
| Bibliographies | intactes : aucune référence, aucun DOI, aucun titre modifié |

Autres anomalies découvertes : aucune nouvelle. Les points déjà signalés dans l'audit du 24/09/2026
restent traités ou en attente de ta décision (voir G).

---

## E — RESPONSIVE

66 mesures **en production** (11 pages × 6 largeurs), page déroulée jusqu'en bas, photographies
chargées :

| Largeur | Résultat |
|---|---|
| 320 px | photographies à 280 px de large, une par ligne (avant/après et séquences empilés) ; légendes lisibles |
| 375 px | 335 px ; le bouton d'appel final passe désormais à la ligne au lieu de dépasser |
| 390 px | 350 px ; idem |
| 430 px | 390 px ; idem |
| 768 px | avant/après toujours empilés (ils ne passent côte à côte qu'à partir de 48 em) |
| Desktop (1440 px) | photographie seule 602 à 704 px dans la colonne de texte ; avant/après 2 × 602 px ; séquence 3 × 389 px, sur toute la largeur utile (1240 px) |
| **Débordement horizontal** | **0 px sur les 66 mesures.** Le débordement du bouton d'appel signalé dans l'audit (5 px à 375 px sur 4 pages, 1 à 390 px) est corrigé partout. |

Les 22 photographies se chargent réellement à chaque largeur (aucune image cassée, aucun
`naturalWidth` à zéro).

---

## F — PERFORMANCE

Lighthouse mobile, **en production**, avant (audit du 23/09/2026) et après :

| Page | Avant | Après | LCP | CLS | Poids total | Images au chargement |
|---|---|---|---|---|---|---|
| `/` (sans photographie) | 100 / 100 / 100 / 100 | **100 / 100 / 100 / 100** | 1,8 s | 0 | 213 Ko | 22 Ko |
| `/facettes-dentaires-paris/` (5 photos) | 100 / 100 / 100 / 100 | **100 / 100 / 100 / 100** | 1,9 s | 0 | 256 Ko | 60 Ko |
| `/composite-bonding-paris/` (3 photos) | 100 / 100 / 100 / 100 | **100 / 100 / 100 / 100** | 1,8 s | 0 | 228 Ko | 32 Ko |

Le poids au chargement bouge peu parce que **toutes les photographies cliniques sont en chargement
différé** : elles sont toutes sous la ligne de flottaison, aucune n'est l'élément LCP. Ce que
télécharge un lecteur qui va jusqu'au bas de la page :

| Page | Photos | Poids des photographies |
|---|---|---|
| `/facettes-dentaires-paris/` | 5 | 174 Ko |
| `/taches-dentaires-dyschromies-icon/` | 4 | 159 Ko |
| `/erosion-dentaire/` | 2 | 155 Ko |
| `/composite-bonding-paris/` | 3 | 142 Ko |
| `/bilan-esthetique-personnalise/` | 3 | 111 Ko |
| `/rehabilitation-dents-usees/` | 2 | 87 Ko |
| `/eclaircissement-dentaire-paris/` | 2 | 81 Ko |
| `/usures-dentaires/` | 1 | 44 Ko |

**CLS = 0 partout** : chaque image porte ses dimensions dans le HTML, la place est réservée avant
le chargement. Aucune page ne dépasse 260 Ko au chargement, et 430 Ko une fois entièrement lue.

---

## G — ANOMALIES

**Rien de prévu n'a été laissé de côté.** Les points à connaître :

1. **Trois photographies sont des montages avant/après** (composite × 2, usures × 1) : posées en
   photographie seule, légende « avant, puis après ». Si tu veux le composant avant/après pour ces
   cas, il faudrait les deux états en fichiers séparés — Franck ne les a pas fournis ainsi.
2. **Cas TCA** : la consigne interdit de rattacher publiquement une pathologie au patient
   photographié. Aucune photographie n'a donc été posée sur `/tca-dents/` ni sur
   `/anorexie-erosion-dentaire-sans-vomissements/`, et la légende des cas d'érosion ne nomme aucun
   trouble alimentaire.
3. **Aucune photographie de cabinet, aucun scan de suivi** : les emplacements correspondants restent
   vides et invisibles sur le site public (correctif V1.3), conformément aux §43 et §44.
4. **Images sociales (`og:image`)** : inchangées, comme demandé. Note séparée ci-dessous.
5. **Propreté du serveur** : le dossier `_astro` en ligne contient **exactement les 106 fichiers de
   la version fabriquée aujourd'hui** — listes comparées, empreintes identiques. Aucun résidu
   d'une version précédente, aucun fichier orphelin.
6. **Sauvegarde iCloud, incident évité** : iCloud fabrique parfois des copies « fichier 2.jpg » dans
   le dossier `dist/` du Mac ; le premier paquet préparé ce matin en contenait quinze. Il n'a pas
   été déposé. La fabrication du paquet (`npm run paquet`) les écarte désormais d'office, et le
   serveur n'en porte aucune — vérifié dossier par dossier.

---

## Contrôle après déploiement (§50) — site en production

Les 22 pages répondent en `200` et sont **identiques, octet pour octet, à la version fabriquée
localement**. Les 8 pages qui portent des photographies :

| URL | Photos intégrées | Type de composant | Alt | Légende | Chargement | Mobile |
|---|---|---|---|---|---|---|
| `/composite-bonding-paris/` | 3 | 3 × ClinicalImage | 3/3, descriptifs | 3 légendes + attribution | différé, 3 largeurs, dimensions posées | 350 px, aucun débordement |
| `/facettes-dentaires-paris/` | 5 | ClinicalSequence + ClinicalBeforeAfter | 5/5 | 2 légendes + attribution ; étiquettes « Situation initiale / Projet / Résultat » et « Avant / Après » en texte HTML | différé, 3 largeurs, dimensions posées | 350 px, empilé, aucun débordement |
| `/eclaircissement-dentaire-paris/` | 2 | ClinicalBeforeAfter | 2/2 | 1 légende + attribution ; « Avant » / « Après 4 semaines » en texte | différé | 350 px, empilé |
| `/taches-dentaires-dyschromies-icon/` | 4 | 2 × ClinicalBeforeAfter | 4/4 | 2 légendes + attribution ; « Avant » / « Après » en texte | différé | 350 px, empilé |
| `/erosion-dentaire/` | 2 | 2 × ClinicalImage | 2/2 | 2 légendes + attribution | différé | 350 px |
| `/bilan-esthetique-personnalise/` | 3 | ClinicalSequence | 3/3 | 1 légende + attribution ; « Situation initiale / Projet / Résultat » en texte | différé | 350 px, empilé |
| `/rehabilitation-dents-usees/` | 2 | ClinicalBeforeAfter | 2/2 | 1 légende + attribution ; « Avant » / « Après » en texte | différé | 350 px, empilé |
| `/usures-dentaires/` | 1 | ClinicalImage | 1/1 | 1 légende + attribution | différé | 350 px |

**Total : 22 photographies, 13 cas, 8 pages.** Aucune image manquante, aucune 404, aucun
`alt` vide, aucune légende absente, aucune mention « Avant / Projet / Résultat » portée uniquement
par l'image.

---

## Note séparée — images sociales (`og:image`), §42

**Rien n'a été modifié.** État actuel : les 23 pages partagent la même image sociale, le portrait de
Franck ; `twitter:card` vaut `summary` (petite vignette carrée) et `twitter:image` est absent — les
réseaux retombent alors sur `og:image`, donc le portrait.

Ce qui me paraît juste, à ta décision :

1. **Ne pas utiliser d'avant/après patient comme image sociale.** Une photographie clinique sortie
   de sa page perd son contexte, sa légende et sa nuance ; elle devient une promesse de résultat.
   C'est exactement ce que le reste du site refuse de faire. Cela vaut aussi pour les séquences.
2. **Pages qui gagneraient le plus à une image dédiée**, dans cet ordre : la page pilier
   `/dentisterie-esthetique-paris/`, `/contact/`, `/franck-moyal/`, puis les quatre pages de
   traitement (`/composite-bonding-paris/`, `/facettes-dentaires-paris/`,
   `/eclaircissement-dentaire-paris/`, `/taches-dentaires-dyschromies-icon/`). Ce sont les adresses
   qu'un patient partage ou qu'un confrère envoie.
3. **Forme à envisager** : des visuels sociaux dédiés 1200 × 630, sobres, du même système que le
   site — fond ivoire, titre de la page en Fraunces, filet vert sauge, nom du praticien — sans
   photographie de patient. Ils se fabriquent automatiquement à la construction, un par page, sans
   travail manuel ni nouvelle décision éditoriale à chaque page.
4. **Un ajout gratuit, quand tu voudras** : `twitter:card` en `summary_large_image`, pour que la
   vignette occupe toute la largeur au lieu d'un carré de 120 px.

Je n'ai touché à rien de tout cela : c'est un chantier à ouvrir séparément.

---

*Prochaine étape : ta revue. Conformément au §51, je n'ai commencé ni le POINT 2 ni le POINT 3.*

---

## Ajout du soir — un cas sur les deux pages d'entrée (24/09/2026)

Franck a constaté qu'en arrivant sur le site par une recherche Google, il ne voyait aucune
photographie : le lien de Google mène à l'accueil, et **ni l'accueil ni la page pilier ne
montraient de cas** — ce sont pourtant les deux pages sur lesquelles un patient arrive. Il a
demandé d'en poser un sur chacune. C'est fait, en ligne et contrôlé :

| Page | Cas | Emplacement | Composant |
|---|---|---|---|
| `/` | `composite-six-dents` — reconstruction additive de six dents antérieures | sous le bloc « Esthétique. Fonction. Préservation. », aligné sur sa colonne de texte, même fond ivoire | ClinicalImage |
| `/dentisterie-esthetique-paris/` | `eclaircissement-ambulatoire` — avant / après 4 semaines | après « Qu'est-ce que le gradient thérapeutique ? » | ClinicalBeforeAfter |

Le choix des deux cas suit l'argument de chaque page : sur l'accueil, une transformation obtenue
**sans retirer de tissu dentaire**, ce que la phrase manifeste affirme ; sur la page pilier, le
traitement **le moins invasif** produisant un résultat visible, ce que défend le gradient
thérapeutique. Les cas « projet numérique » (séquences de planification) ont été écartés à ces
deux endroits : ce sont des captures de logiciel, avec appareil orthodontique visible sur l'une.

**À savoir :** les 13 cas étant déjà tous employés sur les pages de soins, ces deux-là
réapparaissent (pages Composite bonding et Éclaircissement). Franck l'a accepté en connaissance de
cause et fournira, si possible, un cas inédit — ainsi que des photographies de cabinet, qui
manquent toujours (§43).

**Contrôles après ce second déploiement :** les 23 pages en ligne sont identiques à la version
fabriquée ; les deux nouvelles photographies se chargent à 390 px comme à 1440 px, aucun
débordement horizontal ; le dossier `_astro` du serveur contient exactement les 106 fichiers de la
version fabriquée.

**Incident rattrapé au passage :** iCloud avait de nouveau fabriqué des copies dans le dossier de
travail — cette fois suffixées « 3 » —, et trois d'entre elles sont parties sur le serveur avec le
paquet (`index 3.html`, `favicon-48 3.png`, une image de portrait). Elles n'étaient appelées par
aucune page. Elles ont été mises à la corbeille du serveur, et la fabrication du paquet écarte
désormais **toute** copie de ce type, quel que soit son numéro.

**Rapidité, après cet ajout :** Lighthouse mobile en production, accueil **100 / 100 / 100 / 100**,
LCP 1,8 s, CLS 0, 263 Ko (contre 213 Ko avant : la photographie de l'accueil est assez haut dans la page pour que
le navigateur la télécharge dès l'ouverture, alors que toutes les autres attendent le défilement ;
son attribut reste « chargement différé ») ; page pilier
**100 / 100 / 100 / 100**, LCP 1,0 s, CLS 0, 198 Ko.

**Emplacements réservés encore vides sur la page pilier :** le pack y prévoit deux visuels —
« 3 à 5 cas cliniques réels » sous « Quelles solutions en dentisterie esthétique ? » et une
« photographie réelle de planification esthétique » sous « Quelle place pour le smile design ? ».
Ils restent masqués, faute d'instruction sur ce qu'il faut y mettre. Dis-le si tu veux les remplir
avec les cas existants.

