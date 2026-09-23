# Audit après POINT 1 — photographies, assets et contrôle éditorial

*Claude Code, 24 septembre 2026. Contrôles menés sur le dépôt, sur le site fabriqué et sur le site
en ligne. Les corrections autorisées ont été appliquées et déployées ; tout le reste est signalé
sans modification.*

---

# PARTIE A — PHOTOGRAPHIES ET ASSETS

## Document de référence : RETROUVÉ

**OUI.** C'est la fiche de renseignements en ligne que Franck a remplie le 22/09/2026 (page privée
`https://claude.ai/artifact/1sKz2QAnH3sbxvqixANouD`, base de données `infos/franck`). Elle contient
une note par thème de photographies, écrite par lui. Il y précise :

> « toutes les photos sont triées dans un dossier sur mon bureau appelé Icono GEO (les légendes sont
> en remarque) »

Les « remarques » sont les champs de notes de cette même fiche, reproduits ci-dessous. Les fichiers
eux-mêmes ne portent **aucun commentaire Finder ni étiquette** : je les ai tous vérifiés. Un résumé
de ces notes figure aussi dans `livrables/pre-lancement/POINTS-PRE-LANCEMENT.md` (§2 e).

## Pourquoi les photographies n'apparaissent pas

**Aucune photographie clinique n'a jamais été intégrée au site, et aucune n'est dans le dépôt.**
Ce n'est pas une régression ni un fichier cassé :

1. les photos sont restées dans `~/Desktop/icono GEO`, hors du dépôt — règle du projet : aucune
   photo de patient dans le dépôt GitHub ;
2. leur répartition page par page et leurs légendes n'ont jamais été arrêtées : c'est le point 4 du
   rapport du correctif V1.3, toujours ouvert, qui t'attend ;
3. trois confirmations manquent encore, par cas : consentement couvrant la publication web, cas
   d'érosion liée à un TCA, âge du patient MIH lors de l'éclaircissement ;
4. depuis le correctif V1.3 (§7, ta consigne), **un emplacement d'image sans visuel validé
   disparaît du site public** : les pages ne montrent donc plus de cadres gris, elles montrent du
   texte seul.

## Inventaire complet des assets du dépôt

7 fichiers, aucun autre format image (ni WebP, ni AVIF, ni HEIC en source).

| Fichier | Catégorie | Dimensions / poids | Utilisé | Appelé par | Pages |
|---|---|---|---|---|---|
| `src/assets/photos/portrait-franck.jpg` | B — portrait | 277 Ko | **oui** | `index.astro`, `franck-moyal.astro`, `[slug].astro` (bloc auteur) | 18 pages + accueil et page Franck en ouverture |
| `src/assets/photos/portrait-franck-source.png` | B — portrait, original | 6,0 Mo | non (source) | — | — |
| `src/assets/brand/logo-fm.svg` | F — logo | 4,1 Ko | **oui** | `Logo.astro` (en-tête, pied de page) | les 23 pages |
| `src/assets/brand/logo-fm-source.png` | F — logo, original | 849 Ko | non (source) | — | — |
| `public/favicon.svg` | F — icône | 4,1 Ko | **oui** | `BaseLayout.astro` | les 23 pages |
| `public/favicon-48.png` | F — icône | 1,2 Ko | **oui** | `BaseLayout.astro` | les 23 pages |
| `public/apple-touch-icon.png` | F — icône | 5,7 Ko | **oui** | `BaseLayout.astro` | les 23 pages |

Dans le site fabriqué, Astro produit 18 déclinaisons du portrait (JPG, WebP, AVIF, plusieurs
largeurs) : c'est normal, c'est l'image responsive.

**Aucun asset orphelin, aucune image cassée, aucun appel vers un fichier absent.** Les deux fichiers
« source » sont les originaux conservés volontairement (D4, D5) ; ils ne sont pas publiés.

## Les 22 photographies documentées, et leur état

Dossier `~/Desktop/icono GEO`, 22 fichiers, 8 sous-dossiers. Aucune n'est dans le dépôt ni en
production : statut **PRÉSENTE MAIS NON INTÉGRÉE** pour toutes.

| Dossier / fichier | Description documentée (fiche de Franck) | Emplacement prévu | Dépôt | Code | Production | Statut |
|---|---|---|---|---|---|---|
| `Composite bonding/1.png`, `2.png`, `3.jpg` | 1 — composite 6 dents antérieures ; 2 — composite 4 dents antérieures ; 3 — composite stratifié sur une dent dyschromiée | page Composite bonding (2 emplacements) | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Facettes /1.png`, `2.png`, `3.png` | 1 — initial ; 2 — projet ; 3 — final (un cas en trois temps) | page Facettes (2 emplacements) | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Facettes /facettes cas 2 /avant.JPG`, `apres.jpg` | second cas de facettes, avant / après | page Facettes | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Eclaircissement/1.jpg`, `2.jpg` | 1 — avant ; 2 — après 4 semaines d'éclaircissement ambulatoire | page Éclaircissement (2 emplacements) | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Icon/1.jpg`, `1bis.jpg` | cas 1 : tache de MIH sur une incisive, traitée par éclaircissement puis érosion-infiltration (ICON) | page Taches (priorité MIH, V1.3) | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Icon/2.jpg`, `2bis.jpg` | cas 2 : dyschromie unitaire et tache blanche, traitées par éclaircissement puis érosion-infiltration | page Taches | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Erosion /1.JPG` | érosion d'origine exogène | page Érosion (prioritaire selon V1.3 §7) | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Erosion /2.jpg` | érosion avec raccourcissement, due à un TCA (boulimie) | à trancher : pas de légende nommant la maladie (V1.3 §7) | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE — décision éditoriale en attente |
| `Bilan esthetique /initial .jpg`, `Projet.png`, `final .jpg` | « légendes dans le dossier » : initial, projet, final | page Bilan esthétique (2 emplacements) | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Usures /cas 1.jpg` | « légendes dans le dossier » | pages Usures / Réhabilitation | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| `Usures /cas 2 /avant .jpg`, `après.jpg` | cas 2, avant / après | pages Usures / Réhabilitation | non | non | non | PRÉSENTE MAIS NON INTÉGRÉE |
| *Cabinet / environnement* | Franck : « j'ai pas » | — | — | — | — | DOCUMENTATION SANS FICHIER |
| *Scans de suivi* | Franck : « j'ai pas » | — | — | — | — | DOCUMENTATION SANS FICHIER |

Poids des fichiers : de 421 Ko à 13 Mo, en 1080×1080 à 6048×4024. Ils devront être recadrés et
allégés avant publication — le site charge aujourd'hui 190 à 213 Ko par page.

**Aucune photo n'a été déplacée, renommée ni supprimée.**

## Images réellement affichées, page par page

| Pages | Images visibles | Asset | Texte de remplacement |
|---|---|---|---|
| Accueil et Dr Franck Moyal | 1 | portrait (ouverture) | « Portrait du Dr Franck Moyal » |
| 16 pages cliniques et Paris 9 | 1 | portrait (bloc auteur) | vide, image décorative : le nom figure à côté en texte |
| Publications, Conférences, Activité hospitalière, Médias, Contact, Mentions légales | 0 | — | — |

Images cassées : **0**. Images masquées par CSS : **0**. Emplacements réservés visibles : **0**.

## Open Graph

| | |
|---|---|
| `og:image` | `https://drfranckmoyal.fr/_astro/portrait-franck.…jpg` — identique sur les 23 pages |
| `twitter:card` | `summary` |
| `twitter:image` | **absent** — avec une carte `summary`, X et LinkedIn retombent sur `og:image` : l'aperçu fonctionne, mais une image sociale dédiée (1200 × 630) donnerait un meilleur rendu. À décider |

---

# PARTIE B — AUDIT ÉDITORIAL

## « Erosive tooth wear » : corrigé

**19 occurrences trouvées** dans les pages en ligne : **7 dans le texte patient** (corrigées) et
**12 dans les titres de publications scientifiques** (conservées, l'anglais y est l'original).

### Les 7 corrections, déployées

| URL | Avant | Après |
|---|---|---|
| `/diagnostic-usures-dentaires/` | Il est recommandé dans les documents de consensus sur l'erosive tooth wear. | …sur l'**usure dentaire érosive**. |
| `/diagnostic-usures-dentaires/` (FAQ) | …peuvent participer à l'erosive tooth wear, parfois même… | …participer à l'**usure dentaire érosive**, parfois même… |
| `/bruxisme-usure-dentaire/` | Les consensus sur l'erosive tooth wear décrivent… | Les consensus sur l'**usure dentaire érosive** décrivent… |
| `/erosion-dentaire/` (réponse directe) | L'erosive tooth wear est un processus chimico-mécanique différent de la carie. | L'**usure dentaire érosive** est un processus chimico-mécanique différent de la carie. |
| `/erosion-dentaire/` | L'**erosive tooth wear** correspond à une perte progressive… | L'**usure dentaire érosive** correspond à une perte progressive… |
| `/anorexie-erosion-dentaire-sans-vomissements/` | L'erosive tooth wear est aujourd'hui **défini** comme un processus chimico-mécanique… | L'**usure dentaire érosive** est aujourd'hui **définie** comme un processus chimico-mécanique… |
| `/anorexie-erosion-dentaire-sans-vomissements/` | …la progression réelle de l'erosive tooth wear restent limitées. | …la progression réelle de l'**usure dentaire érosive** restent limitées. |

Une seule adaptation grammaticale : « défini » → « définie », le mot « usure » étant féminin.
Aucune autre modification de phrase.

Ces corrections sont appliquées par le mécanisme habituel des décisions de ChatGPT : les fichiers
du pack ne sont pas modifiés, le remplacement est déclaré dans `src/content/pages-suivantes.ts` et
listé par le contrôle des textes. **Un contrôle automatique interdit désormais le retour de
l'expression dans le texte patient** (`node scripts/check-html.mjs`).

## Autres termes anglais : aucun résidu accidentel

| Terme | Où | Décision |
|---|---|---|
| `composite bonding` | pages Composite, Esthétique, menu | **volontaire** — terminologie retenue du site |
| `smile design`, `Digital Smile Design` | Bilan, Esthétique, Facettes (9 occurrences) | **volontaire** — terme professionnel, employé dans tes textes validés |
| `Basic Erosive Wear Examination (BEWE)` | Diagnostic des usures | **nom propre** d'un indice clinique international : à conserver |
| `mock-up` | page pilier (critère 04) | **volontaire** — terme professionnel |
| `umbrella review` | Érosion (2 fois), Anorexie (1 fois) | terme méthodologique anglais dans du texte patient. **Signalé, non modifié** : « revue générale » ou « méta-revue » seraient possibles, c'est un choix éditorial |
| `workflow` | Réhabilitation des dents usées : « Le workflow peut comprendre : … » | anglicisme dans du texte patient. **Signalé, non modifié** : « déroulé » ou « démarche » seraient possibles |
| `SmileCloud`, `ICON`, `PubMed`, `DOI` | partout | noms de produits, d'outils et de bases : normaux |

Aucun mot de la liste de contrôle (`before`, `after`, `learn more`, `read more`, `contact us`,
`booking`, `appointment`, `discover`, `next`, `previous`, `home`, `about`, `services`, `expertise`,
`treatments`, `patient journey`, `case`, `whitening`, `veneers`, `teeth`) n'apparaît dans le texte
patient, les titres, les descriptions, les textes de remplacement ni les libellés d'interface.

Les libellés d'interface sont tous français : Menu, Fermer, Aller au contenu, Accueil, Prendre
rendez-vous, Rendez-vous, À lire aussi, Auteur, Fil d'Ariane, Navigation principale, Pied de page,
Mentions légales, Voir les N sources scientifiques, Mis à jour le…

## Textes d'attente et textes techniques : aucun

`Lorem ipsum`, `placeholder`, `TODO`, `TBD`, `à fournir`, `à compléter`, `test`, `sample`,
`example`, `dummy`, `temp`, `undefined`, `null` : **0 occurrence visible** sur les 23 pages.

Seule trace, invisible pour le visiteur : le nom de classe CSS `placeholder-text`, hérité du système
de design gelé. Il n'affiche rien.

## Typographie française : une correction

**Corrigé** : dans la liste des sources, « DOI : » s'écrivait avec une espace ordinaire avant les
deux-points. C'est désormais une espace insécable, comme partout ailleurs sur le site.

Contrôlés sans rien trouver : apostrophes droites (le site n'emploie que l'apostrophe typographique
’), doubles espaces, espaces avant `; ? !`, caractères mal encodés, mots collés, répétitions,
guillemets non fermés, textes tronqués.

## Anomalie signalée, non corrigée : débordement horizontal sur mobile

Le bouton d'appel final ne coupe jamais son libellé (`white-space: nowrap`, composant gelé). Quand
le libellé est long, la page déborde latéralement :

| Largeur | Pages concernées | Largeur du bouton |
|---|---|---|
| 390 px | `/bruxisme-usure-dentaire/` — « Faire analyser une usure associée au bruxisme » | 402 px pour 358 px disponibles |
| 375 px | les mêmes, plus `/dentisterie-esthetique-paris/` (« Réaliser un bilan esthétique personnalisé »), `/dents-courtes-usees/` (« Faire analyser des dents courtes ou usées »), `/rehabilitation-dents-usees/` (« Étudier une réhabilitation des dents usées ») | 360 à 402 px |

Le défaut est **antérieur à ce travail** et ne vient pas des corrections. Deux réponses possibles,
à ton choix : raccourcir ces quatre libellés, ou autoriser le bouton à passer sur deux lignes sur
petit écran — ce second point touche le système de design gelé.

---

# RAPPORT FINAL

## Photos

- Assets du dépôt : **7** (3 icônes, 1 logo publié + 1 original, 1 portrait publié + 1 original)
- Photographies fournies par Franck : **22**, dans `~/Desktop/icono GEO`
- Utilisées sur le site : **1** (le portrait) ; **0** photographie clinique
- Non utilisées : **22** photographies cliniques + 2 fichiers originaux conservés
- Cassées : **0**
- Conformes au document de référence : sans objet, aucune n'est intégrée
- Document de référence retrouvé : **OUI** (fiche en ligne de Franck, base `infos/franck`)

## Erreurs éditoriales

- « erosive tooth wear » trouvées : **19** — 7 dans le texte patient, 12 en bibliographie
- Corrigées : **7** (les 12 titres de publications restent en anglais)
- Autres anglicismes accidentels : **0** ; 2 termes signalés pour décision (`umbrella review`,
  `workflow`), 4 termes volontaires confirmés
- Textes d'attente : **0**
- Fautes et erreurs typographiques : **1** corrigée (« DOI : »)
- Erreurs d'encodage : **0**

## Contrôle final

| | |
|---|---|
| « erosive tooth wear » visible | **0** |
| Résidus anglais accidentels | **0** |
| Textes d'attente visibles | **0** |
| Images cassées | **0** |
| Pages sans photographie | 5 sans aucune image (Publications, Conférences, Activité hospitalière, Médias, Contact, Mentions légales) ; 21 sans photographie clinique |
| Open Graph | portrait sur les 23 pages ; `twitter:image` absent (repli sur `og:image`) |
| Débordement mobile | 1 page à 390 px, 4 pages à 375 px — signalé, non corrigé |

Contrôles automatiques après correction : construction, textes (aucun écart), HTML et données
structurées (23 pages), contrôle avant mise en ligne — tous au vert. Les 23 pages en ligne sont
identiques, octet pour octet, à la version fabriquée.

## Ce qu'il faut de toi pour les photographies

1. la répartition page par page et les légendes, selon tes priorités du correctif V1.3 (§8) ;
2. la décision sur le cas d'érosion liée à un TCA (légende sans nommer la maladie, ou cas écarté) ;
3. les trois confirmations de consentement, cas par cas, que Franck doit donner.

Dès que ces points sont réglés, l'intégration technique est prête : les emplacements existent déjà
dans les pages, il suffira d'y placer les images préparées.
