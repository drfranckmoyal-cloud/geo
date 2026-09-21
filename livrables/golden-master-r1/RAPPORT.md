# Golden master drfranckmoyal.fr — rapport de fin de phase, tour 1

*Claude Code, 21 septembre 2026. À lire avec les captures du dossier `captures/`.*
*Référence : pack V1.3.1 (V1.3 + fichier Usures corrigé par Franck) et réponse de ChatGPT
du 21/09/2026 (menu, intertitres et textes de la page Usures — décisions D10 à D13).*

Les trois pages demandées sont construites : `/`, `/franck-moyal/`, `/usures-dentaires/`.
Aucune autre page. Aucun texte inventé, contrôlé automatiquement (§3).

---

## 1. Captures (08 G)

| Fichier | Contenu |
|---|---|
| `captures/pages/<page>-1440.png`, `-430.png` | Chaque page en entier, ordinateur (1440 px) et mobile (430 px) |
| `captures/pages/<page>-1280/1024/768/390.png` | Les autres largeurs demandées (08 A) |
| `captures/details/ouverture-ordinateur-<page>.png` | Section d'ouverture (hero), ordinateur, haute définition |
| `captures/details/ouverture-mobile-<page>.png` | Section d'ouverture (hero), mobile, haute définition |
| `captures/details/section-usures-pourquoi-les-dents-s-usent.png` | Une section de contenu |
| `captures/details/pied-de-page.png` | Pied de page |

26 captures au total (18 pages entières + 8 détails). Elles se régénèrent à l'identique avec
`npm run captures`.

---

## 2. Design

### Composants — les 30 du pack, plus 2 éléments techniques

| Famille | Composants (05) | Où |
|---|---|---|
| Global | `SiteHeader`, `SiteFooter`, `Container`, `Section`, `SectionEyebrow`, `EditorialH1`, `EditorialH2`, `LeadText`, `BodyText`, `PrimaryButton`, `TextLink`, `Breadcrumbs` | Les trois pages |
| Accueil | `HeroSplit`, `PillarPair`, `PhilosophyStatement`, `MethodSteps`, `AuthorityStrip`, `FinalCTA` | Accueil (`FinalCTA` sert aux trois pages) |
| Éditorial / profil | `EditorialHero`, `TextImageSection`, `PullStatement`, `InlineEvidenceLinks`, `AuthorBlock` | Page Franck ; `TextImageSection`, `PullStatement` et `AuthorBlock` aussi sur Usures, `TextImageSection` sur l'accueil (bloc TCA) |
| Clinique | `ClinicalHero`, `DirectAnswer`, `SymptomList`, `ClinicalPathway`, `FAQAccordion`, `SourceList`, `RelatedPages` | Page Usures |
| Techniques (hors liste) | `Logo` (monogramme vectoriel), `MediaFrame` (emplacement réservé d'image) | Partout |

Déclinaisons prévues pour l'extensibilité (08 F, critère 8), sans variante arbitraire :

- `TextImageSection` a six compositions : image à droite, image à gauche, texte décalé, colonne de lecture, texte et colonne latérale, bloc « domaine spécifique » sur fond vert sauge. C'est ce qui évite les sections identiques répétées (07 §6).
- `PullStatement` a deux usages : titre-manifeste (« Traiter juste ») et phrase clé en exergue (page Usures).
- `PrimaryButton` a une taille « en-tête » de 42 px, **à valider** : l'en-tête doit rester fin (07 §12), alors que la hauteur de référence est de 52 px.

### Réglages de design (tokens) — `src/styles/tokens.css`

| Réglage | Valeurs |
|---|---|
| Couleurs | Les 6 du pack (`#171715`, `#FAF8F3`, `#F4F0E8`, `#D8D3CA`, `#5E685D`, `#B9C1B5`). Deux transparences, sans teinte nouvelle : texte secondaire = noir doux à 74 % (contraste ≈ 7:1) ; micro-zones vert sauge = sauge clair à 30 %. |
| Titres | Cormorant Garamond 500 (et italique 500). H1 44 → 72 px, H2 34 → 48 px (52 px pour les phrases manifestes), H3 24 → 32 px. |
| Texte | Inter (variable). Chapeau 20 → 24 px, texte 17 → 18 px, petit texte 14–15 px. |
| Grille | Conteneur 1240 px, 12 colonnes, texte éditorial 736 px, marges 20 → 40 px. |
| Respiration | Sections 72 → 136 px ; titre → texte 24 → 32 px ; texte → bouton 32 → 40 px. |
| Boutons | Fond `#171715`, texte `#FAF8F3`, 52 px, coins 3 px, survol vert sauge en 200 ms. |
| Mouvement | Fondu + 10 px, 420 ms, au défilement ; rien si le visiteur a demandé moins d'animations. |

Les tailles sont fluides entre 390 et 1440 px et restent dans les fourchettes du pack aux deux bouts.

### Choix typographiques

- **Titres : Cormorant Garamond**, la solution gratuite désignée par le pack (01, 07 §4). Ses accents sont hauts et étroits, et cela se voit dans des titres en français (« hôpital », « même »). Ce n'est pas un défaut technique : c'est le dessin de la police. Comparaison jointe : `comparaison-polices-titres.png` (question 1, §5).
- **Texte : Inter.**
- **Hébergement des polices** : sur le site lui-même, préchargées ; aucune requête vers Google (RGPD).
- **Typographie française** : espaces insécables devant « : ; ? ! » et dans les guillemets, pour qu'aucun signe ne commence une ligne. « Chirurgien-dentiste » ne se coupe jamais au trait d'union. Les mots ne changent pas.

### Adaptation mobile (V16)

- **Menu** : le menu complet s'affiche à partir de 1240 px (1280 et 1440). En dessous, le bouton « Prendre rendez-vous » reste visible, à côté d'un simple « Menu » qui déplie la liste, sans animation.
- **Ouvertures** : sur l'accueil, le texte vient d'abord et le portrait ensuite. Sur la page Franck, le portrait vient d'abord (« portrait dominant »).
- **Colonnes** : les compositions en colonnes se replient en une colonne sous 1024 px, les listes à deux colonnes sous 768 px.
- **H1** : au plus 4 lignes à toutes les largeurs testées (accueil : 4 lignes à 1024 px, 3 ailleurs).

### Images

- **Logo** : le monogramme « Fm » (D4) est redessiné en vectoriel à partir du PNG, fidèle à l'original. L'encre est en noir doux, l'arc dans son vert d'origine (`#848C73`). Il sert aussi d'icône de navigateur.
- **Portrait** (D5) : trois réglages, rien d'autre.
  - Le point noir est ajusté pour que le fond de la photo tombe exactement sur le noir doux du site.
  - Les tons vont du noir doux au blanc cassé, au lieu du noir et du blanc purs.
  - Les bords latéraux sont adoucis pour que les épaules se fondent dans l'aplat.

  La photo est posée en bas d'un aplat noir doux : elle garde sa taille réelle et aucun bord n'est visible.
- **Limite** : l'original ne fait que 480 × 480 px et paraît doux sur les écrans haute définition. Un original plus grand est nécessaire (§5).

---

## 3. Technique

| Point | État |
|---|---|
| Construction | Astro 7.3.3, pages HTML statiques, lisibles sans JavaScript. `npm run build` sans erreur. |
| Adresses | `/`, `/franck-moyal/`, `/usures-dentaires/` (terminées par « / », comme l'arborescence V4). |
| Informations pour les moteurs | Titre, description, adresse de référence (canonical), aperçus de partage (Open Graph) sur chaque page. |
| Données structurées | Accueil : `WebSite` + `Person`. Franck : `ProfilePage` + `Person` complet (lieu d'exercice, domaines, établissements) + `EducationalOrganization` (Smileclub Formation, fondateur). Usures : `MedicalWebPage` (auteur, 7 citations avec DOI) + `BreadcrumbList`. Identifiant unique `https://drfranckmoyal.fr/#franck-moyal` partout. |
| Plan du site, robots | `sitemap-index.xml` (les 3 pages, elles seules) ; `robots.txt` ouvert à tous les moteurs, IA comprises. |
| Mesure d'audience | Aucune (§6, point 16 du fichier maître) : pas de traceur, pas de bandeau cookies. |
| JavaScript | Deux petits scripts : l'en-tête qui se compacte au défilement, et les apparitions discrètes. Aucune bibliothèque. |

### Rapidité et qualité — Lighthouse 13.5 (outil de Google), build final servi en local

| Page | Rapidité | Accessibilité | Bonnes pratiques | Référencement | Affichage principal (LCP) | Poids total |
|---|---|---|---|---|---|---|
| Accueil — mobile | 100 | 100 | 100 | 100 | 1,7 s | 115 Ko |
| Accueil — ordinateur | 100 | 100 | 100 | 100 | 0,4 s | 115 Ko |
| Franck — mobile | 100 | 100 | 100 | 100 | 1,4 s | 92 Ko |
| Franck — ordinateur | 100 | 100 | 100 | 100 | 0,4 s | 92 Ko |
| Usures — mobile | 100 | 100 | 100 | 100 | 1,7 s | 117 Ko |
| Usures — ordinateur | 100 | 100 | 100 | 100 | 0,4 s | 117 Ko |

Aucun décalage de mise en page pendant le chargement (CLS 0) sur les trois pages.

### Contrôle du HTML — `node scripts/check-html.mjs` : réussi

- **Titres** : un seul H1 par page, aucun saut de niveau d'intertitre.
- **Structure** : langue `fr`, une zone principale, toutes les images décrites.
- **Données structurées** : conformes aux types imposés par le pack.
- **Liens** : les 14 liens externes (sources) sont en `rel="noopener noreferrer"`.

### Contrôle des textes — `npm run verify` : réussi, aucun écart

1. **Rien d'inventé** : les 208 textes des pages existent mot pour mot dans le pack ou la réponse de ChatGPT.
2. **Rien de perdu** : tous les textes préparés sont dans les pages.
3. **Rien d'oublié** : chaque passage affichable du pack se retrouve dans sa page.

Seules différences, toutes décidées :

- **D6** : « Dentiste esthétique » → « Dentisterie esthétique » dans le titre Google de l'accueil.
- **D11** : section 5 de la page Usures, nouvelle étiquette et nouveau titre.
- **D12** : « Attrition / contraintes mécaniques » → « Attrition et contraintes mécaniques ».

Enfin, « dentiste esthétique » est absent partout (V21).

---

## 4. Emplacements réservés

### Photos et schémas manquants

| Emplacement | Page |
|---|---|
| Portrait en haute définition, pour remplacer le 480 px | Accueil, Franck, bloc auteur |
| Visuel « dentisterie esthétique et adhésive » | Accueil (pilier A) |
| Visuel « usures dentaires » | Accueil (pilier B) |
| Visuel « pratique esthétique » | Franck (section 1) |
| Photographie clinique | Usures (section 1) |
| Schéma des mécanismes d'usure (contenu à définir) | Usures (section 2) |
| Cas clinique avant / après, avec consentement documenté | Usures (section 6) |

**Vidéos** : aucune prévue par le pack.

### Liens non finalisés

- **« Prendre rendez-vous »** (en-tête, ouvertures, blocs finaux, pied de page) : ancre provisoire vers le bloc final de la page, en attendant la décision de Franck (D8).
- **Mentions légales** : aucune adresse dans l'arborescence (`#`).
- **Pages à venir** : 11 adresses définitives, qui renvoient pour l'instant à une page introuvable. `/dentisterie-esthetique-paris/`, `/bilan-esthetique-personnalise/`, `/tca-dents/`, `/erosion-dentaire/`, `/diagnostic-usures-dentaires/`, `/rehabilitation-dents-usees/`, `/bruxisme-usure-dentaire/`, `/dents-courtes-usees/`, `/publications/`, `/conferences-formations/`, `/activite-hospitaliere/`.
- **Profils externes de Franck** (LinkedIn…) pour les données structurées (`sameAs`), et adresses des preuves d'autorité (00 §7) : à fournir.
- **Adresse et téléphone du cabinet** : à fournir (pied de page).

### Libellés d'interface ajoutés (hors contenu éditorial)

- Visibles : « Menu », « Fermer », « Accueil » (fil d'Ariane), « Auteur », « © 2026 Dr Franck Moyal ».
- Invisibles à l'écran : « Aller au contenu » (accessibilité), le texte de remplacement « Portrait du Dr Franck Moyal », les intitulés des zones de navigation.

---

## 5. Questions — uniquement celles qui bloquent la validation

1. **Police des titres.** Faut-il garder Cormorant Garamond, dont les accents hauts et étroits se voient en français (comparaison jointe) ? Deux alternatives, gratuites aussi :
   - Newsreader, de Production Type (Paris), dans l'esprit « Tiempos » que cite le pack ;
   - EB Garamond, plus classique.

   Changer ne touche qu'un seul réglage.
2. **Portrait en haute définition.** L'original de la photo, idéalement 2 000 px de large ou plus, est indispensable pour que le portrait reste net en grand.

---

## 6. Points d'interprétation à confirmer (non bloquants)

- **Répartition des couleurs** : j'ai appliqué celle de 07 plutôt que celle de 01 (§6, point 6 du fichier maître).
- **Méthode** : 6 étapes sur l'accueil, comme dans 02 ; « Simuler » est compris dans « Planifier ».
- **« Découvrir ma démarche »** mène à la section Méthode de l'accueil.
- **Menu** : « Érosion & TCA » → `/tca-dents/` ; « Publications & enseignement » → `/publications/`.
- **Page Usures, libellés** : les libellés de section du pack servent de petite étiquette au-dessus des titres (D11). Les légendes « Signes possibles », « Axes », « Outils » sont affichées ; les consignes de rédaction (« Texte : », « Lien : »…) ne le sont pas.
- **Page Usures, parcours clinique** (`ClinicalPathway`) : c'est le sommaire des 8 étapes de la page, dans l'ordre du pack.
- **Page Usures, pages liées** (`RelatedPages`) : un bloc final titré « Usures dentaires » regroupe les 6 pages filles, avec les libellés de liens du pack.
- **Sources** : les notes « Soutient : » sont affichées en petit sous chaque référence.
- **Auteur** : l'auteur de la page Usures est présenté par le nom, le titre et la phrase d'introduction de la page Franck. Aucun texte nouveau, pas de date de mise à jour.
- **FAQ** : réponses affichées ouvertes, sans accordéon (07 §17 : accordéons seulement si réellement utiles).
- **En-tête sur ordinateur** : le monogramme seul à gauche, puisque « Dr Franck Moyal » figure déjà dans le menu (et que tout ne tient pas sur une ligne sinon). Le nom reste lu par les lecteurs d'écran.
- **Bloc TCA de l'accueil** : pas de composant dédié dans 05 ; j'ai réutilisé `TextImageSection`, avec la même composition que sur la page Franck et la page Usures.

---

## 7. Auto-contrôle (listes 08 C, D, E — à confirmer par ChatGPT)

- **Accueil** : H1 visible d'emblée, ouverture aérée, deux piliers identifiables, bloc Esthétique / Fonction / Préservation fort, méthode en liste éditoriale, TCA présent mais secondaire, autorité discrète, appel final net, aucune carte répétée.
- **Franck** : portrait dominant, page incarnée, pas de CV, l'esthétique avant l'hospitalier, usures présentes, TCA en expertise spécifique, enseignement valorisé, hospitalier plus bas, phrases fortes en grand (intro, « Traiter juste »), aucun logo.
- **Usures** : H1 très lisible, réponse directe immédiatement sous le titre, causes et diagnostic avant le traitement, prévention visible, réhabilitation esthétique et fonctionnelle, liens érosion / TCA / réhabilitation, fond clair, aucune dent générique, FAQ lisible, sources et auteur présents.
- **Limite honnête** : tant que les photos manquent, les emplacements réservés pèsent sur le critère « niveau de gamme ». La mise en page est faite pour de vraies photos.
