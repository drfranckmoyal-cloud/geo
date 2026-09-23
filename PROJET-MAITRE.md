# drfranckmoyal.fr — fichier maître

*(Dépôt `geo` : le site professionnel du Dr Franck Moyal. « GEO » veut dire : être compris,
cité et recommandé par les moteurs génératifs, c'est-à-dire les IA qui répondent aux
questions : ChatGPT, Gemini, Claude, Perplexity, Google AI Overviews / AI Mode, Copilot / Bing.)*

> **Document de référence du projet.** Toute nouvelle conversation sur le sujet commence par
> la lecture de ce fichier, puis du pack de référence en vigueur (§3 ; aujourd'hui
> `docs/golden-master/v1.3.1/`), en commençant par `00_PROJECT_CONTEXT.md`.
>
> Il garde quatre choses : **où on en est** (§0 et §7), **ce qui ne se rediscute plus**
> (les verrous, §4), **ce qui a été décidé** (§5) et **ce qui s'est dit** (le journal, §10).
> Il est mis à jour à chaque étape, puis enregistré et envoyé sur GitHub dans la foulée.
>
> En cas de doute sur un point de design ou de contenu, **le pack fait foi** : ce fichier le
> résume, il ne le remplace pas.

---

## 0. Tableau de bord

| | |
|---|---|
| **Phase en cours** | **Le site est en ligne** sur https://drfranckmoyal.fr (D46), déclaré à Google (D47) et à Bing (D48). **Étape 6 : travail SEO/GEO page par page avec ChatGPT** — POINT 1, la page pilier Dentisterie esthétique, est en ligne (D50). Restent les photos et le suivi d'indexation. |
| **Dernière étape faite** | POINT 1 SEO/GEO appliqué (D50, `livrables/point-1-page-pilier/RAPPORT-POINT-1.md`, copié sur le Bureau) : la page Dentisterie esthétique devient la page pilier du cluster — comment choisir son praticien, six critères, matrice demande → solutions, quatre solutions, bloc usures, approche du Dr Moyal, dix questions de FAQ ; contenu clinique de la V1.2 conservé ; contrôles au vert, page en ligne et identique à la version fabriquée. Avant : audit de production demandé par ChatGPT (23/09/2026, `livrables/audit-production-2026-09-23.md`, copié sur le Bureau) : 15 contrôles sur le site en ligne, une seule anomalie — `/sitemap.xml` en 404 —, corrigée et remise en ligne (D49) ; Lighthouse mobile 100 / 100 / 100 / 100 sur 5 pages, LCP 1,8 s, CLS 0, TBT 0 ms ; données structurées sans erreur au test des résultats enrichis de Google. Avant : contrôle du courriel de Search Console du 23/09/2026 : les motifs « page avec redirection » et « exclue par la balise noindex » correspondent aux choix du site (adresse unique par page, mentions légales hors index) ; rien à corriger. Avant : site déclaré à Bing (D48) : importé depuis Google Search Console dans le compte Bing Webmaster Tools de Franck, plan du site envoyé, les 22 pages indexables soumises. Avant : site déclaré à Google (D47) : propriété « drfranckmoyal.fr » validée dans Google Search Console par un enregistrement TXT chez OVH, plan du site envoyé et lu (« Opération effectuée »), indexation demandée pour l'accueil, la page Franck, Usures dentaires et Dentisterie esthétique. Certificat https de Let's Encrypt, installé par Hostinger à 9 h 04, couvrant `drfranckmoyal.fr` et `www` ; les 23 pages en ligne sont identiques à la version locale. Avant : domaine branché (D46) : chez OVH, `drfranckmoyal.fr` et `www` pointent vers le serveur Hostinger (`91.108.101.161`), courrier OVH inchangé ; les résolveurs de Google et de Cloudflare voient déjà la nouvelle adresse ; `http://` et `www.` sont redirigés vers `https://drfranckmoyal.fr/`. Avant : correctif V1.3 appliqué (D45 ; `livrables/pre-lancement/RAPPORT-CORRECTIF-V1-3.md`, copié sur le Bureau) : page Taches centrée sur la MIH, téléphone et e-mail au même niveau (Contact, Paris 9, pied de page), 6 profils officiels, cabinet décrit aux moteurs (`#practice`, type `Dentist`), DentCA et Smileclub Formation, robots tous autorisés, emplacements d'images vides masqués. Tous les contrôles réussis ; page Taches : Lighthouse 99 / 100 / 100 / 100, H1 en 4 lignes sur mobile, 7 références vérifiées sur PubMed. Cette version est déposée chez Hostinger : à l'adresse provisoire, les 23 pages sont identiques à la version locale. Avant : site créé dans l'espace Hostinger de Franck et fichiers déposés (D43) : à l'adresse provisoire, les 23 pages et tous les fichiers répondent, identiques à la version locale ; hébergeur des mentions légales : Hostinger. Franck confirme les consentements des photos (D44). Avant : fiche de Franck intégrée (D42) : téléphone, e-mail, hébergeur (OVH, remplacé par Hostinger), 4 profils officiels, pas de réservation en ligne ; DOI de la page Facettes rétablis. Le contrôle avant mise en ligne ne relève plus que 3 points (`livrables/pre-lancement/POINTS-PRE-LANCEMENT.md`). Avant : reconstruction depuis la V1.2 finale (`livrables/pages-suivantes-v1-2/RAPPORT-RECONSTRUCTION-V1-2.md`) : textes sans écart et plus aucun écart de renvois, HTML et plan du site réussis, les 20 H1 en 4 lignes au plus sur mobile, 37 références vérifiées sur PubMed, Lighthouse 99–100 ; tous les liens de rendez-vous vers `/contact/#prendre-rendez-vous`. Fiche de renseignements en ligne pour Franck. Avant : validation consolidée (D40) ; lot D construit et contrôlé (`livrables/pages-suivantes-lot-d/RAPPORT-LOT-D.md`, avec le bilan des 20 pages) : Contact et Mentions légales, lien du pied de page raccordé, mentions légales hors du plan du site. Lot C (`livrables/pages-suivantes-lot-c/RAPPORT-LOT-C.md`) : textes sans écart, HTML et manifeste réussis sur 21 pages, Lighthouse page locale 99 / 100 / 100 / 100. Lot B (`livrables/pages-suivantes-lot-b/RAPPORT-LOT-B.md`) : textes sans écart, HTML et manifeste réussis sur 16 pages, Lighthouse page TCA 99 / 100 / 100 / 100 après une optimisation de police (D39). Lot A : `livrables/pages-suivantes-lot-a/RAPPORT-LOT-A.md`, avec les écarts de tout le pack (§6, points 28 à 34). |
| **Prochaine action** | POINT 2 du travail SEO/GEO, annoncé par ChatGPT : la page comparative « Facettes ou composite : comment choisir ? ». En parallèle : réponses de ChatGPT aux points signalés (H1, FAQ à dix questions, débordement du bouton à 375 px) ; photos ; suivi de l'indexation. |
| **La construction est-elle bloquée ?** | Non. Tout élément manquant est remplacé par un emplacement réservé, clairement signalé (verrou V2). |
| **En attente de Franck** | Le renouvellement de l'offre Hostinger Premium avant le 22/10/2026 ; pour chaque photo retenue, trois confirmations (rapport V1.3, §4) ; le nom de sa fiche Google et son adresse publique (point 41) ; la double authentification de son compte OVH, qu'OVH lui recommande. |

---

## 1. Le projet en bref

- Le site professionnel personnel du **Dr Franck Moyal**, chirurgien-dentiste à Paris, à
  l'adresse `drfranckmoyal.fr`.
- Ce n'est ni un site de cabinet généraliste, ni un site vitrine standard, ni une page
  publicitaire, ni un simple portfolio de cas cliniques.
- Il doit devenir, tout à la fois (00 §1) :
  1. la source de référence sur « Dr Franck Moyal » sur le web ;
  2. une vitrine haut de gamme de sa pratique clinique ;
  3. un centre de contenus de référence sur ses domaines d'expertise ;
  4. un atout pour le référencement Google, local et thématique (SEO) ;
  5. un atout GEO, pensé pour être compris, cité et recommandé par les IA.
- Le but concret : que des questions posées **sans son nom** — « quel dentiste esthétique à
  Paris ? », « quel dentiste fait du composite bonding à Paris ? », « qui consulter pour des
  dents usées ? », « quel dentiste prend en charge l'érosion dentaire ? », « quel dentiste
  connaît bien les conséquences dentaires des TCA ? » — mènent peu à peu les moteurs vers lui.
- **Deux piliers de même importance** : la dentisterie esthétique et adhésive ; les usures
  dentaires.
- **Une expertise spécifique**, rattachée au pilier Usures et non pas troisième pilier :
  l'érosion et les troubles des conduites alimentaires (TCA).
- **Le fil rouge** : Esthétique · Fonction · Préservation, reliés par le gradient
  thérapeutique (la solution la plus conservatrice compatible avec l'objectif — sans
  timidité sur l'esthétique : le site doit aussi donner envie).
- **La méthode** : Écouter → Documenter → Analyser → Planifier → Simuler → Décider ensemble →
  Traiter (00 §5 ; la page d'accueil en montre 6, voir §6 point 5).
- **L'identité publique à faire émerger** (00 §6) : chirurgien-dentiste à Paris ; pratique
  privée exclusivement orientée vers la dentisterie esthétique et adhésive ; activité majeure
  autour des usures ; expertise érosion / TCA ; enseignement et formation ; activité
  hospitalière ; publications et conférences. Ces informations sont aujourd'hui dispersées
  sur plusieurs sites tiers : le site doit devenir la source qui les unifie.
- **Les lecteurs** : les patients d'abord (70 à 80 %) ; puis les confrères, les organismes
  de formation, les médias, les partenaires, et les moteurs eux-mêmes.
- **Le critère de réussite** de la première phase : Franck peut dire
  « Oui. C'est exactement l'image que je veux donner de ma pratique. »

---

## 2. Qui fait quoi

| Qui | Rôle | Fait | Ne fait pas |
|---|---|---|---|
| **Franck** | Directeur clinique, décideur final | Valide le ton et la véracité clinique, choisit les cas et les photos, valide le rendu final | Ne rédige pas les pages |
| **ChatGPT** | Chef de projet stratégique | Direction éditoriale et rédaction complète, SEO/GEO, architecture, direction artistique, système de composants, contrôle du rendu de Claude | — |
| **Claude Code** | Développeur exécutant | Technique, composants, adaptation mobile, rapidité, SEO technique, données structurées (les informations cachées destinées aux moteurs), plan du site, intégration des textes | Ne redéfinit ni la stratégie ni le design ; n'invente aucun texte |

**Le circuit de validation** (00_README) :

1. Claude construit.
2. Claude fournit les captures, sur ordinateur et sur mobile, avec le court rapport de fin
   de phase (08 H).
3. ChatGPT contrôle le rendu par rapport au pack.
4. Franck valide, ou demande des modifications.
5. Claude corrige, et l'on recommence jusqu'à ce que le rendu soit validé.
6. Le rendu est validé : les composants sont **gelés**.
7. Le reste du site est décliné à partir de cette base.

**En pratique** : Franck fait le lien entre ChatGPT et Claude. Il transmet les captures et le
rapport à ChatGPT, puis rapporte ici ses retours. Chaque retour est résumé au journal (§10) ;
les retours longs sont archivés tels quels (voir §10). Chaque nouvelle version du pack est
rangée à côté des précédentes (§3).

---

## 3. Le pack de référence

**Version en vigueur : V1.3.1**, dans `docs/golden-master/v1.3.1/` = la V1.3 avec le fichier
`04_USURES_DENTAIRES.md` corrigé par Franck le 21/09/2026. Ce fichier gagne 7 sources
scientifiques, avec leurs renvois `[1]` à `[7]` dans le texte, une règle d'affichage des
sources et une date de vérification bibliographique. Cinq passages sont reformulés pour
coller aux sources : le bloc de réponse directe, les sections 2, 3 et 5, et le second
paragraphe de la section 6. Les 9 autres fichiers sont identiques à la V1.3.

**Compléments en vigueur**, en attendant leur intégration par ChatGPT dans une prochaine
version du pack : `docs/echanges/2026-09-21-chatgpt-reponses-points-17-20.md` (menu de
l'en-tête, intertitres et textes de la section 2 de la page Usures, lien Bruxisme — D10 à D13) et
`docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour1.md` (contrôle du tour 1 — D16 à D28) et
`docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour2.md` (contrôle du tour 2 — D30 à D36) et
`docs/echanges/2026-09-21-decision-gel-golden-master.md` (**gel du golden master** — D37, V24).

**Pages suivantes — version en vigueur : V1.2 finale**, dans `docs/pages-suivantes/v1.2/` (26 fichiers
archivés tels quels : les 20 pages, l'arborescence, le manifeste, les journaux de modifications 22
et 25, la validation 23 et la checklist 24), source unique depuis le 22/09/2026 (D41), avec
`docs/echanges/2026-09-22-chatgpt-message-reconstruction-v1-2.md`. La V1 reste archivée dans
`docs/pages-suivantes/v1/`.

**Correctif pré-lancement V1.3** (22/09/2026, D45), dans `docs/pages-suivantes/v1.3/` (4 fichiers
archivés tels quels) : `06_taches-dentaires-dyschromies-icon_V1_3.md` remplace le seul fichier 06 ;
`DECISIONS_PRE_LANCEMENT_V1_3.md` (rendez-vous, profils, fiche Google, DentCA et Smileclub
Formation, robots d'IA, page 06, visuels) et `04_FICHE_CORRECTIVE_CONTACT_EMAIL_V1_3.md`
(téléphone et e-mail au même niveau ; prime pour les coordonnées), avec
`MESSAGE_CLAUDE_PATCH_V1_3.md`.

**Pour les pages suivantes** : `docs/echanges/2026-09-22-chatgpt-23-validation-consolidee-lots-a-b-c-d.md`
(validation des compositions des 4 lots et précisions — D40) et
`docs/echanges/2026-09-22-chatgpt-24-checklist-avant-mise-en-ligne.md` (checklist avant mise
en ligne). La V1.2 annoncée par la validation est arrivée le 22/09/2026 (D41).

**Pack « pages suivantes » V1** (réponse de ChatGPT à `docs/besoins-pages-suivantes.md`) —
`PACK_PAGES_SUIVANTES_CLAUDE_CODE_V1.zip`, reçu le 21/09/2026 (fichiers datés du 21/09/2026,
21 h 09), 22 fichiers archivés **sans aucune modification** dans `docs/pages-suivantes/v1/`
(copies vérifiées identiques au zip et au dossier du Bureau) : `00_ARBORESCENCE_ET_ORDRE.md`
(20 pages, 4 lots, décisions), un fichier par page (`01` à `20`, au format ROUTING / HERO /
RÉPONSE DIRECTE / CONTRAT DE COMPOSANTS / CONTENU MOT POUR MOT / LIENS / AUTEUR /
RÉFÉRENCEMENT / IMAGES / SOURCES / NOTES NON AFFICHÉES) et `21_MANIFESTE_INTEGRATION.md`
(règles d'intégration, contrôles automatiques à ajouter, livraison par lot). Ses textes sont
lus directement dans ces fichiers au moment de fabriquer le site (`src/lib/pack.ts`) : rien
n'est recopié à la main.

**Historique :** V1.3 — `GOLDEN_MASTER_FRANCK_MOYAL_V1_3.zip`, reçu le 21/09/2026 (fichiers
datés du 21/09/2026, 16 h 22), 10 fichiers, archivés **sans aucune modification** dans
`docs/golden-master/v1.3/` (copies vérifiées identiques aux originaux).

| Fichier | Contenu | Rôle |
|---|---|---|
| `00_README.md` | Ordre de lecture, mission, circuit de validation | — |
| `00_PROJECT_CONTEXT.md` | Vision, positionnement, architecture, rôles — **à lire avant tout** | Stratégie |
| `01_DESIGN_SYSTEM.md` | Couleurs, polices, grille, espacements, boutons, images | Design |
| `02_HOME.md` | Textes de la page d'accueil, titres et descriptions pour Google | Fait foi pour les textes |
| `03_FRANCK_MOYAL.md` | Textes de la page Franck Moyal, titres et descriptions pour Google | Fait foi pour les textes |
| `04_USURES_DENTAIRES.md` | Textes de la page Usures, FAQ, titres et descriptions pour Google | Fait foi pour les textes |
| `05_COMPONENT_MAP.md` | Les 30 composants à construire puis geler | Composants |
| `06_PROMPT_CLAUDE_CODE.md` | Règles d'exécution et livrables | Règles pour Claude |
| `07_ART_DIRECTION.md` | Direction artistique, qui se déclare « verrouillée » (sa version interne : 1.0) | Avec 08, prime sur toute interprétation esthétique personnelle de Claude (06) |
| `08_VISUAL_QA_CLAUDE.md` | Contrôle visuel : obligatoire, interdit, listes de contrôle, 8 critères | Grille de contrôle du rendu |

Ordre de lecture imposé : `00_PROJECT_CONTEXT` → `01` → `02` → `03` → `04` → `05` → `06` →
`07` → `08`.

**Règles :**
- Les fichiers du pack ne sont **jamais modifiés**.
- Une nouvelle version (V1.4…) est rangée dans son propre dossier
  (`docs/golden-master/v1.4/`) ; ses différences avec la précédente sont résumées au journal ;
  la ligne « Version en vigueur » ci-dessus est mise à jour.
- Les empreintes (§11) permettent de reconnaître une version à coup sûr.

---

## 4. Verrous — ce qui ne se rediscute pas

Figés par le pack. Seul Franck peut lever un verrou, par une décision notée au §5.
Entre parenthèses : le fichier et la section d'origine.

| # | Verrou |
|---|---|
| V1 | **Trois pages, pas une de plus, pour la phase 1** : `/`, `/franck-moyal/`, `/usures-dentaires/`. Ni les autres pages, ni le CMS complet (système de gestion de contenu), ni fonction marketing non demandée, ni nouveau gabarit, ni variante esthétique. Rien d'autre avant la validation humaine. (00_README ; 00 §12, §14 ; 06) — *Phase 1 close avec le gel (D37) ; les 20 pages suivantes sont commandées par le pack « pages suivantes » (D38).* |
| V2 | **Les textes ne se touchent pas.** Ni modifiés, ni raccourcis sans validation, ni complétés. Pas de slogan, pas de chiffre marketing, pas de badge « expert », « premium », « leader ». Si une information manque : un emplacement réservé clairement signalé, jamais une invention. (06 ; 08 B) |
| V3 | **La stratégie, l'arborescence, le positionnement, les titres et l'ordre des sections** restent tels quels. (06) |
| V4 | **Les adresses des pages** (00 §11). Accueil `/` · entité `/franck-moyal/` · pilier esthétique `/dentisterie-esthetique-paris/`, avec `/bilan-esthetique-personnalise/`, `/composite-bonding-paris/`, `/facettes-dentaires-paris/`, `/eclaircissement-dentaire-paris/`, `/taches-dentaires-dyschromies-icon/` · pilier usures `/usures-dentaires/`, avec `/diagnostic-usures-dentaires/`, `/rehabilitation-dents-usees/`, `/bruxisme-usure-dentaire/`, `/erosion-dentaire/`, `/dents-courtes-usees/`, `/tca-dents/` · autorité `/publications/`, `/conferences-formations/`, `/activite-hospitaliere/`, `/medias-interviews/`. |
| V5 | **Les couleurs** : noir doux `#171715` · blanc cassé `#FAF8F3` · ivoire `#F4F0E8` · gris chaud `#D8D3CA` · vert sauge sombre `#5E685D` (accent) · vert sauge clair `#B9C1B5` (accent secondaire). Répartition : 70–80 % blanc cassé et ivoire, 10–15 % noir doux, 5–10 % gris chaud, 5 % de vert au maximum. Le vert ponctue (petite étiquette, filet, survol, petite zone de fond, détail typographique), il n'est jamais le thème. Interdits : bleu médical, bleu nuit corporate, turquoise, violet cosmétique, or, beige trop jaune, dégradés, vert saturé. (07 §3 ; 01 ; 08 B) |
| V6 | **Les polices** : titres en serif éditoriale (dans l'esprit de Canela, Editorial New, Tiempos ; Cormorant Garamond si le choix doit être gratuit — **remplacée par Newsreader depuis D16**) ; texte en sans-serif neutre (Inter, Manrope ; Suisse ou Neue Haas si licence). Tailles sur ordinateur : H1 64–76 px, H2 42–52, H3 26–32, chapeau 22–26, texte 17–19, petit texte 14–15. Sur mobile : H1 42–48, H2 32–38, H3 24–28, chapeau 20–22, texte 17–18. Contraste fort entre les niveaux, interlignage confortable. Le contraste serif / sans-serif fait partie de l'identité : la serif pour le désir et la personnalité, la sans-serif pour la précision clinique. (07 §4 ; 01 ; 08 A) |
| V7 | **La grille et la respiration** : largeur maximale 1180–1240 px ; texte éditorial 720–820 px ; 12 colonnes ; marges sur mobile 20–24 px. Espace entre sections : 112–144 px sur ordinateur, 72–88 px sur mobile ; titre → texte 24–32 px ; texte → bouton 32–40 px. Mieux vaut 4 blocs forts bien espacés que 9 petites sections serrées. (07 §5 ; 01) |
| V8 | **La composition** : éditoriale, parfois asymétrique (texte décalé, grands vides, image légèrement hors axe, titres très grands, blocs courts sur fond ivoire). Pas de grille de cartes uniforme, pas de centrage partout, pas d'alternance gauche/droite mécanique. La même grammaire sur chaque page, sans jamais de copier-coller. Des cartes seulement là où elles structurent vraiment — cas cliniques, les 2 piliers, 3 preuves ou médias, articles — et jamais chaque section transformée en carte. (07 §6, §14 ; 01) |
| V9 | **Les boutons** : peu nombreux, clairement hiérarchisés, sobres. Bouton principal fond `#171715`, texte `#FAF8F3`, hauteur 50–54 px, coins arrondis de 2–4 px, sans-serif medium, ni forme de pilule ni effet 3D ; bouton secondaire = texte et flèche fine, souligné au survol ; survols discrets, 150–250 ms. (07 §11 ; 01 ; 08 A) |
| V10 | **Les animations** : seulement un fondu et un léger glissement vertical (8–12 px), en 250–450 ms. Jamais de parallaxe lourde, de défilement détourné, de zoom, de rotation, d'éléments flottants ni de carrousel automatique. Le réglage « réduire les animations » du visiteur est respecté. (07 §16 ; 01) |
| V11 | **Les interdits visuels** : dégradés, or, cartes à grosses ombres, coins très arrondis (20 px), effet verre dépoli, lueurs, dents en 3D, sourire de banque d'images, vidéo de fond automatique, carrousel, défilement de témoignages, chiffres animés, micro-animations gadget, barre de navigation flottante façon logiciel en ligne, gros boutons en pilule, émojis. Icônes seulement si nécessaire : linéaires, monochromes, géométriques, très fines — ni dent façon dessin animé, ni smiley, ni pictogrammes médicaux standards, ni icônes colorées. (08 B ; 07 §14–15 ; 01) |
| V12 | **Les images** : photos réelles uniquement ; emplacements neutres quand la photo manque ; proportions cohérentes ; aucune banque d'images. Portrait : lumière naturelle, cadrage éditorial, attitude calme, regard assuré, fond architectural ou neutre, tenue sobre — ni bras croisés, ni sourire forcé, ni cabinet blanc standard, ni blouse cliché, ni fond bleu. Avant/après : même taille, même cadrage, ni flèche ni cercle rouge, légende minimale, consentement documenté. (07 §10 ; 01 ; 08 A) |
| V13 | **Les composants** : les 30 de `05_COMPONENT_MAP.md`. Aucune variante arbitraire ; un nouveau composant seulement pour un besoin réellement nouveau. Gelés après validation. |
| V14 | **SEO/GEO** : un seul titre principal (H1) par page ; intertitres (H2) formulés comme de vraies questions ou intentions ; blocs de réponse directe de 40 à 100 mots ; liens internes nombreux ; auteur identifié ; sources scientifiques quand il le faut ; entités (personnes, lieux, notions) nommées explicitement ; contenu lisible sans programme (HTML) ; données structurées cohérentes ; ni bourrage de mots-clés ni pages artificielles. Titres, descriptions et données structurées de chaque page : ceux des fichiers 02, 03 et 04. Identifiant unique de Franck pour les moteurs : `https://drfranckmoyal.fr/#franck-moyal` (03). (00 §10) |
| V15 | **L'en-tête et le pied de page** : en-tête fin et aéré, nom ou logo à gauche, navigation au centre ou à droite, bouton rendez-vous discret mais visible ; il peut se compacter au défilement. Menu mobile simple, sans panneau animé spectaculaire ni icône fantaisie. Pied de page calme : les piliers, la page Franck, les publications, l'activité hospitalière, le contact, les mentions légales, éventuellement adresse et téléphone — pas de mur de liens. (07 §12–13) |
| V16 | **Le mobile** : pas un ordinateur rétréci ; grands titres, respiration et hiérarchie conservés ; un H1 ne casse jamais en 5 lignes ; bouton toujours à portée ; aucun tableau large ; menus dépliants (accordéons) seulement s'ils sont réellement utiles. Largeurs à tester : 1440, 1280, 1024, 768, 430 et 390 px. (07 §17 ; 08 A) |
| V17 | **Les livrables de fin de phase** : un site qui se construit sans erreur ; 10 à 12 captures (chaque page en entier à 1440 et à 430 px ; plus, sur ordinateur et sur mobile, la section d'ouverture — le « hero » : grand titre, chapeau, boutons, visuel ; plus une section de contenu et le pied de page) ; la liste des composants, des réglages de design, des emplacements réservés et des questions bloquantes ; un contrôle de rapidité (Lighthouse) ; un contrôle du HTML et des informations pour les moteurs ; un court rapport Design / Technique / Emplacements réservés / Questions. (06 ; 08 G–H) |
| V18 | **Le seuil de qualité** : ce n'est pas fini parce que ça marche. C'est fini quand « ce rendu peut devenir la référence définitive de toutes les pages futures sans devoir repenser le système visuel ». Test : sans le texte, la mise en page, les images et la typographie évoquent-elles encore une pratique esthétique haut de gamme et singulière ? Le golden master n'est validé que si les 8 critères de 08 F sont tous satisfaits : singularité, niveau de gamme, calme, lisibilité, cohérence, personnalité, mobile, extensibilité. Phrase de cohérence de la direction artistique : 07 §18. (06 ; 07 §18–19 ; 08 F et I) |
| V19 | **Rapidité et sobriété technique** : pas de bibliothèque lourde pour de simples animations ; images optimisées ; polices chargées correctement ; aucune ressource extérieure inutile. (08 A) |

**V20 — Règles propres à chaque page**, avec les listes de contrôle contre lesquelles le
rendu sera jugé :

- **Accueil** (07 §7 ; 08 C) — une page manifeste. Section d'ouverture : très peu de texte,
  H1 dominant, grand blanc, portrait ou visuel réel fort, pas d'illustration décorative,
  pas de surcharge. Les deux piliers présentés comme deux territoires majeurs, « pas comme
  deux cartes de services banales ». Bloc Esthétique / Fonction / Préservation visuellement
  fort ; méthode lisible sans ressembler aux écrans d'accueil pas-à-pas d'un logiciel en
  ligne ; bloc TCA présent mais secondaire ; bloc autorité discret ; bouton final net ;
  aucune carte répétée inutilement.
- **Page Franck** (07 §8 ; 08 D) — incarnée, éditoriale, crédible, personnelle. Portrait
  réel dominant, H1 simple, peu d'information secondaire ; phrases fortes en grand format ;
  preuves intégrées naturellement. L'activité esthétique visible avant l'hospitalier, les
  usures clairement présentes, les TCA en expertise spécifique, l'enseignement bien
  valorisé, l'hospitalier plus bas. Ni CV chronologique brut, ni frise gadget, ni mur de
  logos, ni grille de badges.
- **Page Usures** (07 §9 ; 08 E) — plus clinique sans devenir froide : « expertise calme ».
  Structure très lisible, schémas simples, images cliniques propres, fond majoritairement
  clair, quelques blocs vert sauge très discrets. H1 très lisible, réponse directe visible
  rapidement, causes et diagnostic avant le traitement, prévention clairement visible,
  réhabilitation esthétique ET fonctionnelle, liens vers érosion / TCA / réhabilitation,
  pas d'ambiance trop sombre, aucun visuel de dent générique, FAQ lisible, sources et
  auteur présents.

**Ajoutés le 21/09/2026, après les réponses de Franck et de ChatGPT :**

| # | Verrou |
|---|---|
| V21 (levé sur la page pilier, D50) | **Jamais « dentiste esthétique »**, nulle part sur le site ni dans ses informations pour les moteurs. On écrit « dentisterie esthétique », ou « exercice exclusif en dentisterie esthétique ». Règle de Franck, du 21/09/2026 (D6). « Quel dentiste esthétique à Paris ? » reste une question que les patients posent (00 §1), mais le site ne reprend jamais l'expression. **Levé pour la seule page pilier « Dentisterie esthétique à Paris » le 24/09/2026 (D50)** : l'expression y reprend la recherche des patients, jamais la qualification de Franck ; le contrôle des textes l'interdit partout ailleurs. |
| V22 | **Sources scientifiques de la page Usures** : une section « Sources scientifiques » visible en bas de page, avec des liens externes discrets ; les 5 à 7 références principales, repliables ou en fin de page ; pas de paragraphe interrompu par une bibliographie lourde ; les renvois `[1]`, `[2]`… conservés s'ils restent discrets ; liens sortants en `rel="noopener noreferrer"` ; ne jamais présenter la conclusion d'une étude comme plus forte qu'elle ne l'est. (04, V1.3.1) |
| V23 | **Menu de l'en-tête, figé** : à gauche, le nom et le logo « Dr Franck Moyal », qui mènent à l'accueil (pas de rubrique « Accueil ») ; puis Dentisterie esthétique · Usures dentaires · Érosion & TCA · Dr Franck Moyal · Publications & enseignement ; à droite, le bouton « Prendre rendez-vous ». « Publications & enseignement » pourra ouvrir plus tard sur Publications, Conférences & formations, Activité hospitalière, Médias. Affiché dès le golden master, même si les pages n'existent pas encore. (ChatGPT, 21/09/2026 — D10) |
| V24 | **Golden master gelé (21/09/2026), règle après gel** : le design system ne se modifie plus au fil des pages. Toute nouvelle page (1) réutilise les composants gelés, (2) respecte les réglages de design gelés (`src/styles/tokens.css`), (3) préserve la hiérarchie typographique et les espacements, (4) n'introduit un nouveau composant que si aucun composant existant ne traite correctement le besoin, (5) n'« améliore » ni ne réinterprète la direction artistique sans instruction explicite. Les visuels, le téléphone, le lien de rendez-vous et les adresses `sameAs` s'insèrent dans les emplacements prévus, sans modifier le système. (D37) |

---

## 5. Décisions prises

| # | Décision | Date |
|---|---|---|
| D1 | **Projet créé** : dossier `~/Desktop/Claude-Projects/GEO`, dépôt privé `drfranckmoyal-cloud/geo` (créé vide par Franck), branche `main`. | 21/09/2026 |
| D2 | **Le pack Golden Master V1.3 est la référence du projet**, archivé tel quel dans `docs/golden-master/v1.3/`. | 21/09/2026 |
| D3 | **Ce fichier maître** suit la progression, les verrous, les décisions et les échanges. Toute conversation commence par sa lecture ; le fichier `CLAUDE.md` du dépôt le rappelle automatiquement à Claude. | 21/09/2026 |
| D4 | **Logo** : le monogramme « Fm » fin avec l'arc vert sauge (image produite par ChatGPT le 21/09/2026). Original rangé dans `src/assets/brand/logo-fm-source.png` ; Claude en tire une version vectorielle (SVG) pour le site. | 21/09/2026 |
| D5 | **Portrait** : la photo en noir et blanc fournie par Franck (fond noir, tenue de soin sombre). Original rangé dans `src/assets/photos/portrait-franck-source.png`. | 21/09/2026 |
| D6 | **« Dentiste esthétique » est proscrit** (verrou V21). Le titre Google de l'accueil devient « Dr Franck Moyal \| Dentisterie esthétique et usures dentaires à Paris » : le seul mot remplacé est « Dentiste », devenu « Dentisterie ». | 21/09/2026 |
| D7 | **Page Usures : le fichier corrigé par Franck remplace l'original** → pack V1.3.1 (§3), avec ses sources scientifiques (verrou V22). | 21/09/2026 |
| D8 | **Prise de rendez-vous : en attente.** Le bouton « Prendre rendez-vous » garde un emplacement réservé, de même que l'adresse et le téléphone du cabinet. | 21/09/2026 |
| D9 | **Domaine** : Franck demande à Claude de préparer la réservation de `drfranckmoyal.fr` sur son compte OVH, déjà ouvert dans Chrome. La commande n'est passée qu'après son « oui » explicite sur le récapitulatif (prix, moyen de paiement). | 21/09/2026 |
| D10 | **Menu de l'en-tête** : celui décrit au verrou V23 (réponse de ChatGPT au point 17). | 21/09/2026 |
| D11 | **Intertitres de la page Usures** : chaque section garde son libellé comme petite étiquette au-dessus du grand titre (H2). Section 5 : étiquette « Faut-il toujours traiter une usure dentaire ? », titre « Non : toutes les usures ne nécessitent pas une reconstruction » (au lieu de « Non. » seul). Réponse de ChatGPT au point 18. | 21/09/2026 |
| D12 | **Section 2 de la page Usures** : les quatre sous-parties reçoivent leur texte (« Attrition et contraintes mécaniques », « Érosion dentaire », « Abrasion », « Usures multifactorielles »), rédigé par ChatGPT (point 19). | 21/09/2026 |
| D13 | **Lien Bruxisme** : « Comprendre le bruxisme et son rôle dans l'usure dentaire » → `/bruxisme-usure-dentaire/`, dans la section 2 de la page Usures (point 20). | 21/09/2026 |
| D14 | **Domaine réservé** : `drfranckmoyal.fr`, par Franck, chez OVH (commande n° 259047873), pour 3 ans ; créé le 21/09/2026 à 19 h 10, expire le 21/09/2029 ; serveurs de noms OVH. Titulaire : Franck. DNSSEC et une boîte e-mail inclus, aucun hébergement pris. | 21/09/2026 |
| D15 | **Choix techniques appliqués** (rôle de Claude, 00 §13) : Astro 7.3.3, pages HTML statiques ; Cormorant Garamond 500 et Inter hébergées sur le site ; textes rangés à part et contrôlés automatiquement ; aucun traceur ; captures et contrôles reproductibles (§11). | 21/09/2026 |
| D16 | **Police des titres : Newsreader** à la place de Cormorant Garamond, dont les accents hauts et fins étaient trop présents. H1 et H2 en graisse 400, H3 en 400 ou 500 selon le contraste, ajustement automatique au corps (`font-optical-sizing: auto`), Inter inchangée pour le texte. Tailles conservées, à tester d'abord. (ChatGPT, contrôle du tour 1) | 21/09/2026 |
| D17 | **Méthode en 7 étapes** : « Simuler » redevient une étape à part, entre « Planifier » et « Décider ensemble » — c'est un élément différenciant de la méthode esthétique. | 21/09/2026 |
| D18 | **Menu : deux rubriques groupées deviennent des sous-menus**, sur ordinateur comme sur mobile. « Érosion & TCA » → Érosion dentaire, TCA et santé bucco-dentaire. « Publications & enseignement » → Publications, Conférences & formations, Activité hospitalière, Médias & interviews. | 21/09/2026 |
| D19 | **Sources de la page Usures** : les 7 références restent dans la page (HTML), mais les notes « Soutient : » disparaissent de l'affichage. C'est un outil de travail éditorial (l'« Evidence Map »), pas un élément pour le patient. Citation propre, DOI et PubMed discrets. Sur mobile, liste repliable « Voir les 7 sources scientifiques ». | 21/09/2026 |
| D20 | **Bloc auteur court** : « Dr Franck Moyal — Chirurgien-dentiste à Paris » / « Dentisterie esthétique et adhésive, usures dentaires et érosion. » + « Mis à jour le 21 septembre 2026 » + lien vers `/franck-moyal/`. Date de mise à jour ajoutée aux données structurées (`dateModified`). | 21/09/2026 |
| D21 | **Pages liées de la page Usures** : titre « Approfondir les usures dentaires ». | 21/09/2026 |
| D22 | **Adresse du cabinet** : 2 rue Hippolyte Lebas, 75009 Paris (adresse de référence validée). Le téléphone reste à fournir ; le lien de rendez-vous reste provisoire (D8). | 21/09/2026 |
| D23 | **En-tête mobile** (390–430 px) : bouton rendez-vous haut de 40–42 px, texte 14–15 px, marges intérieures 16–18 px, largeur automatique ; « Menu » en 14–15 px ; en-tête compact. Une barre de navigation premium, pas un bandeau de conversion. Les boutons dans les pages restent à 50–52 px. | 21/09/2026 |
| D24 | **Réponse directe de la page Usures sur mobile**, moins massive : texte 19–20 px, marges intérieures 24–28 px, sans perdre son importance. | 21/09/2026 |
| D25 | **Interprétations validées** : répartition des couleurs de 07 ; « Découvrir ma démarche » → section Méthode ; étiquette + grand titre sur la page Usures ; parcours clinique, à condition d'être cliquable (il l'est) ; FAQ ouverte ; monogramme seul sur ordinateur ; bloc TCA de l'accueil en `TextImageSection`. | 21/09/2026 |
| D26 | **Portrait** : mise en page validée, mais le fichier de 480 px ne sert qu'à valider la composition. Il faut un original d'au moins 2 000 px (idéal 2 500–3 000), sans agrandissement artificiel. Garder le traitement noir doux / noir et blanc ; avec la version HD, renforcer légèrement le contraste du visage. | 21/09/2026 |
| D27 | **Robots et IA, avant la mise en ligne** : OAI-SearchBot (ChatGPT Search), Googlebot et Bingbot autorisés ; GPTBot (entraînement) à décider à part. Ne pas traiter « tous les robots d'IA » comme un seul réglage. | 21/09/2026 |
| D28 | **Gel du golden master : pas encore.** Après les corrections P0, une série courte de captures : ouvertures des 3 pages (ordinateur et mobile), section Méthode, sources et auteur, en-tête mobile, menu (ordinateur et mobile). Si c'est conforme, le golden master est gelé et sert à décliner toutes les autres pages. | 21/09/2026 |
| D29 | **Portrait HD intégré** : l'original fourni par Franck (6 048 × 4 024 px, Nikon D780) remplace la version de 480 px. Il est recadré en 4:5, son contraste local est légèrement renforcé, son point noir est calé sur le noir doux (D26). Source : `src/assets/photos/portrait-franck-source.png`. | 21/09/2026 |
| D30 | **Newsreader validée définitivement** : H1/H2 en 400, H3 et noms d'étapes en 500, ajustement au corps automatique. Ce choix typographique n'est plus à rouvrir. | 21/09/2026 |
| D31 | **Méthode : textes définitifs des 7 étapes** — Écouter : « attentes, gêne, objectifs. » · Documenter : « photographies, scans 3D, examens nécessaires. » · Analyser : « esthétique, fonction, tissus, causes. » · Planifier : « construire les formes, les proportions et les options thérapeutiques. » · Simuler : « visualiser le projet en 2D, 3D ou en dynamique selon les cas. » · Décider ensemble : « comparer les options, leurs avantages, leurs limites et le niveau d'intervention. » · Traiter : « uniquement lorsque le bénéfice est réel. » Titre de section : « Écouter, analyser, planifier, simuler, décider ensemble ». | 21/09/2026 |
| D32 | **Plus d'italique** : la phrase clé de la page Usures passe en Newsreader romain 400 (même taille, même filet), la ligne de domaines du bloc auteur en Inter, petit corps, couleur secondaire. Aucun fichier italique n'est plus chargé (−147 Ko sur la page Usures). | 21/09/2026 |
| D33 | **Bouton rendez-vous de l'en-tête mobile** : hauteur 40 px, sans l'élargir. S'il reste dominant à 390 px, il affiche « Rendez-vous » sur mobile seulement, avec le nom complet « Prendre rendez-vous » pour les lecteurs d'écran. | 21/09/2026 |
| D34 | **Portrait HD, accueil, page Franck, menus, sources, bloc auteur, parcours clinique, pages liées : validés.** Ne plus toucher au contraste du portrait pour le moment. | 21/09/2026 |
| D35 | **Condition de gel technique** : temps d'affichage principal (LCP) de la page Usures sur mobile ≤ 2,5 s, médiane de 3 mesures Lighthouse. Au-delà, optimisation technique ciblée sans toucher au design (polices critiques seules préchargées, sous-ensembles de caractères, élément principal inspecté). | 21/09/2026 |
| D36 | **Gel après le P0.5** : palette, Newsreader + Inter, grille, espacements, en-têtes ordinateur et mobile, boutons, les trois ouvertures, `TextImageSection`, `PullStatement`, `DirectAnswer`, FAQ, `SourceList`, `AuthorBlock`, `RelatedPages`, pied de page, sous-menus, animations. Ensuite, ces composants ne bougent plus au fil des nouvelles pages, sauf vrai problème. Les visuels, le téléphone, le lien de rendez-vous et les adresses `sameAs` ne bloquent pas le gel. | 21/09/2026 |
| D37 | **Golden master gelé** (décision transmise par Franck, archivée dans `docs/echanges/2026-09-21-decision-gel-golden-master.md`). Définitivement validés : palette ; Newsreader + Inter ; grille et espacements ; en-têtes ordinateur et mobile ; boutons ; ouvertures Accueil, Profil et Clinique ; `TextImageSection`, `PullStatement`, `DirectAnswer`, FAQ, `SourceList`, `AuthorBlock`, `RelatedPages` ; pied de page ; sous-menus ; animations ; logique d'adaptation mobile ; méthode en 7 étapes et son titre ; décisions du P0.5. Version étiquetée `golden-master-gele` dans GitHub. | 21/09/2026 |
| D38 | **Pack « pages suivantes » V1** (ChatGPT, transmis par Franck), archivé dans `docs/pages-suivantes/v1/` : il reste **exactement 20 pages**, livrées en 4 lots — A : dentisterie esthétique (6 pages), B : usures, érosion, TCA (7), C : autorité, entité, page locale (5), D : contact et mentions légales. Contact est une page (`/contact/`, indexable) ; les mentions légales aussi (`/mentions-legales/`, `noindex,follow`) ; l'article Anorexie sans vomissements est enfant de la page Érosion ; aucun autre contenu (boulimie, reflux…) pour la V1. Textes visibles mot pour mot, sauf `[À FOURNIR]` et notes « NON AFFICHÉES » ; après chaque lot : build, contrôle des textes, contrôle HTML, Lighthouse sur une page, captures des seules compositions nouvelles. | 21/09/2026 |
| D39 | **Police Inter : jeu de caractères latin seul** (optimisation technique autorisée par D35, « sous-ensembles de caractères »). Un seul « ń » (nom d'auteur, page TCA) faisait télécharger un second fichier de 83 Ko et portait le LCP mobile à 2,55 s ; il revient à 1,95 s. Les rares caractères hors de ce jeu (ce « ń », la flèche « → ») s'affichent dans la police du système ; aucune page du golden master n'en contient. Déclaration reprise telle quelle du paquet d'origine (`src/styles/inter-latin.css`). | 22/09/2026 |
| D40 | **Validation consolidée des lots A à D par ChatGPT** (fichier 23, archivé). Compositions validées : ordre des blocs, texte décalé dominant, H3 et grilles sauge, listes, `MethodSteps` en 7 étapes, emplacements d'images, FAQ / Sources / Auteur / « À lire aussi », gras parcimonieux (A) ; sommaire cliquable, grille des sources acides, bloc CMME, appel final réduit, infographie pleine largeur (B) ; ouverture clinique et preuves externes des pages d'autorité, sans bloc auteur ni appel final sur les pages 14 à 17 (C) ; contact et mentions légales (D). Précisions appliquées : page 18, bouton « Prendre rendez-vous » vers `/contact/#prendre-rendez-vous` ; ancre définitive `#prendre-rendez-vous` sur la page Contact ; 7 motifs de consultation cliquables et H1 « … Paris 9e » validés ; ligne auteur retirée de l'ouverture sur Contact et Mentions légales ; date des mentions légales harmonisée au 22 septembre 2026 (visible et `dateModified`) ; publications décrites en `Article` / `Book`, sans métadonnée inventée. La **V1.2** du pack devient la source éditoriale finale. | 22/09/2026 |
| D41 | **V1.2 finale du pack, source unique** des 20 pages (reçue le 22/09/2026, archivée dans `docs/pages-suivantes/v1.2/`) : renvois bibliographiques corrigés et complétés, H1 raccourcis (V16 respecté), consignes retirées du texte patient, appel final de la page Éclaircissement, liens explicités, titre « Du projet au traitement : sept étapes » pour la méthode de la page Bilan, pages Contact et Mentions légales sans auteur. **Règle globale des rendez-vous** : tant que le lien de réservation manque, tous les boutons et liens « Prendre rendez-vous » / « Rendez-vous » du site — en-tête, ouverture de l'accueil, appels finaux, pied de page, page Paris 9 — mènent à `/contact/#prendre-rendez-vous` ; ancre unique `#prendre-rendez-vous` sur la page Contact ; `#rendez-vous` abandonnée. | 22/09/2026 |
| D42 | **Fiche de Franck intégrée** (22/09/2026) : téléphone 01 83 75 52 16 (pied de page, Contact, page Paris 9, mentions légales, cliquable sur mobile) ; pas de réservation en ligne, donc la section Rendez-vous de la page Contact est la destination définitive des boutons ; mentions légales complétées (e-mail `drfranckmoyal@gmail.com`, hébergeur OVH SAS et ses coordonnées légales) ; profils officiels déclarés aux moteurs : LinkedIn, Instagram, AP-HP, Blendi ; aucune mesure d'audience ; aucun autre nom de domaine ; les trois vérifications de déontologie confirmées. DOI des références Alqutaibi et Klein rétablis sur la page Facettes (omissions de la V1.2, confirmées par ChatGPT). | 22/09/2026 |
| D43 | **Hébergement chez Hostinger**, où Franck a déjà un abonnement (offre Premium Web Hosting, échéance du 22/10/2026) ; il remplace OVH, prévu par D42. Le domaine reste enregistré chez OVH. Le 22/09/2026, Claude crée dans l'espace de Franck, ouvert dans Chrome, le site « drfranckmoyal.fr » (site PHP/HTML, domaine existant) et dépose les fichiers du site dans `public_html`. Adresse provisoire de contrôle : https://mediumaquamarine-louse-843680.hostingersite.com. Mentions légales : hébergeur Hostinger International Limited (coordonnées des conditions d'utilisation d'Hostinger). Le fichier `public/.htaccess` redirige définitivement `http://` et `www.` vers `https://drfranckmoyal.fr/`. | 22/09/2026 |
| D44 | **Photos cliniques** : Franck confirme que le consentement de publication est recueilli pour tous les cas du dossier « Icono GEO ». Il lève, pour ce dossier, l'interdit de ranger des photos de patients sur le Bureau (iCloud) : « ce n'est pas un problème ». Les photos restent hors du dépôt GitHub. | 22/09/2026 |
| D45 | **Correctif pré-lancement V1.3 de ChatGPT appliqué** (`docs/pages-suivantes/v1.3/`) : page 06 remplacée (taches de MIH, traitement possible chez l'enfant et l'adolescent, pas d'éclaircissement avant 18 ans) ; plus aucune « prise de rendez-vous en ligne » ; **téléphone et e-mail, deux canaux au même niveau** — page Contact (« Prendre rendez-vous ou nous écrire », boutons « Appeler le cabinet » et « Écrire au cabinet »), bloc final de la page Paris 9, pied de page ; l'e-mail ouvre un message intitulé « Demande de rendez-vous - Dr Franck Moyal » ; profils officiels : LinkedIn, Instagram, AP-HP, Blendi, TikTok, Le Fil Dentaire ; le cabinet, entité distincte (`#practice`, type `Dentist`), sans la fiche Google tant que son adresse publique manque ; DentCA et Smileclub Formation, organisations fondées par Franck, avec un lien visible sur les pages TCA et Conférences ; robots.txt ouvert à tous les robots, entraînement compris ; **un emplacement d'image sans visuel validé disparaît du site public** ; aucun cas patient publié sans consentement couvrant la publication web. | 22/09/2026 |
| D46 | **Domaine branché sur Hostinger**, avec l'accord de Franck (« ok branche le domaine », 22/09/2026) : dans la zone DNS d'OVH, les enregistrements A de `drfranckmoyal.fr` et de `www.drfranckmoyal.fr` passent de `213.186.33.5` (page d'attente d'OVH) à `91.108.101.161` (serveur Hostinger) ; courrier (MX), SPF et autres entrées inchangés. Hostinger reconnaît le domaine et installe son certificat https gratuit, renouvelé automatiquement (« Lifetime SSL »). | 22/09/2026 |
| D47 | **Site déclaré à Google Search Console**, avec l'accord de Franck (« ok fais-le, tu as mon accord », 22/09/2026), sur son compte Google : propriété de type « Domaine » (`drfranckmoyal.fr`, toutes adresses, http et https), validée par l'enregistrement TXT `google-site-verification=…` ajouté dans la zone DNS d'OVH — **à ne jamais supprimer**, sous peine de perdre la validation ; plan du site `https://drfranckmoyal.fr/sitemap-index.xml` envoyé, lu le jour même ; indexation demandée pour `/`, `/franck-moyal/`, `/usures-dentaires/` et `/dentisterie-esthetique-paris/`. Bing Webmaster Tools : en attente d'une première connexion de Franck. | 22/09/2026 |
| D48 | **Site déclaré à Bing Webmaster Tools** (22/09/2026) : Franck ouvre lui-même son compte (connexion avec Google) ; Claude importe le site depuis Google Search Console — Bing reçoit un accès en lecture seule aux données Search Console des sites validés de `drfranckmoyal@gmail.com`, révocable depuis le compte Google —, envoie le plan du site et soumet les 22 pages indexables (quota de 100 adresses par jour). Bing compte pour le GEO : ChatGPT et Copilot s'appuient sur son index. | 22/09/2026 |
| D49 | **Plan du site à l'adresse conventionnelle** (audit du 23/09/2026) : `/sitemap.xml` renvoyait `404`, le plan n'existant que sous `/sitemap-index.xml` et `/sitemap-0.xml`. La fabrication du site en copie désormais une version à `/sitemap.xml` (`npm run build`), et `node scripts/check-html.mjs` vérifie que les deux fichiers restent identiques. Les adresses déclarées à Google et à Bing ne changent pas. | 23/09/2026 |
| D50 | **Page pilier « Dentisterie esthétique à Paris »** (POINT 1 SEO/GEO de ChatGPT, spécification archivée dans `docs/echanges/2026-09-24-chatgpt-point-1-page-pilier-esthetique.md`) : la page répond à l'intention « dentiste esthétique à Paris » sans jamais revendiquer un classement — comment choisir son praticien, six critères d'évaluation, bloc « la bonne question n'est pas toujours quel traitement choisir » et matrice demande → solutions, quatre solutions avec leurs liens, bloc « et si les dents sont usées » vers la page Usures, approche du Dr Moyal, FAQ de dix questions. Texte de la page : `docs/pages-suivantes/v1.4/01_dentisterie-esthetique-paris_V1_4.md`, assemblé sans réécriture à partir de la V1.2 et de la spécification. Aucune page concurrente créée, adresse inchangée. Deux arbitrages de Franck : **verrou V21 levé pour cette seule page** (l'expression « dentiste esthétique » y reprend la recherche des patients) et nouvelle section des traitements conservant l'entrée « Taches blanches et dyschromies ». | 24/09/2026 |

---

## 6. Questions ouvertes et points relevés

Relevés à la lecture intégrale des 10 fichiers, puis complétés après une relecture
indépendante du fichier maître contre le pack, le 21/09/2026. **Aucun n'empêche de
construire le golden master.** « D'ici là » = ce que Claude fait en attendant la réponse.
Quand un point est tranché, il passe dans la liste « Tranchés » en bas, avec son numéro de
décision.

| # | Constat | D'ici là | Qui tranche |
|---|---|---|---|
| 10 | **Photos** : le portrait est fourni, en haute définition depuis D29. Manquent : les visuels des deux piliers, les images cliniques et les « schémas simples » de la page Usures. Depuis D45, un emplacement sans visuel validé est masqué sur le site public. | Emplacements masqués ; `EMPLACEMENTS=1` les montre pour une revue. | Franck (photos), ChatGPT (contenu des schémas). |
| 13 | **Longueur des titres et descriptions pour Google** : le titre de la page Usures (73 caractères) et les descriptions de l'accueil (170) et de la page Franck (189) dépassent ce que Google affiche d'ordinaire (environ 60 caractères pour un titre, 155 pour une description) ; le titre de l'accueil (68 depuis D6) est à la limite. Ils seront coupés dans les résultats. | Repris à l'identique (V2). | ChatGPT, s'il souhaite raccourcir. |
| 15 | **Déontologie** : les trois vérifications de la fiche sont confirmées par Franck (D42), les consentements des photos aussi (D44). Restent, le moment venu, les mentions obligatoires propres à la profession. | — | Franck. |
| 38 | **Photos cliniques** : 22 photos triées par Franck dans « Icono GEO », sur le Bureau ; consentements recueillis et dossier laissé sur le Bureau (D44). Avant intégration, pour chaque cas retenu (correctif V1.3) : consentement couvrant la publication web ; cas d'érosion liée à un TCA seulement si le consentement couvre une information de santé sensible, sans nommer la boulimie ; étape d'éclaircissement du cas MIH décrite seulement si le patient avait 18 ans ou plus. Puis répartition, légendes, recadrage et préparation pour le web, hors du dépôt. | Aucune photo intégrée. | Franck (trois confirmations), ChatGPT (répartition, légendes). |
| 39 | **Page « introuvable » (erreur 404)** : le pack n'en prévoit pas. Une adresse qui n'existe pas affiche la page générique d'Hostinger, en anglais (« This Page Does Not Exist »). | Page d'Hostinger. | ChatGPT (texte d'une page 404). |
| 40 | **Téléphone de l'hébergeur** : la loi pour la confiance dans l'économie numérique demande, dans les mentions légales, le nom, l'adresse et le téléphone de l'hébergeur. Les conditions d'utilisation d'Hostinger ne donnent qu'une adresse électronique ; d'autres sites indiquent un numéro lituanien, +370 645 03378, sans source officielle. | Adresse électronique seule. | Franck (demander le numéro au support Hostinger). |
| 41 | **Fiche Google du cabinet** (correctif V1.3 §3) : ChatGPT recommande de simplifier son nom en « Dr Franck Moyal ». Son adresse publique stable ira dans le `sameAs` du cabinet (`#practice`). | Hors des données structurées. | Franck (nom de la fiche, dans son compte Google ; adresse de la fiche). |
| 42 | **Remarques visuelles du correctif V1.3** : sur les 3 pages gelées, les sections prévues avec image gardent leur composition, et l'autre moitié reste vide sur ordinateur tant que la photo manque ; le titre « Prendre rendez-vous ou nous écrire » passe à la ligne au trait d'union de « rendez-vous ». | Laissé tel quel (V24). | ChatGPT. |
| 26 | **Libellés d'interface ajoutés**, hors contenu éditorial : « Menu », « Fermer », « Accueil » (fil d'Ariane), « Auteur », « © 2026 Dr Franck Moyal », et, invisibles à l'écran, « Aller au contenu », le texte de remplacement du portrait et les intitulés des zones de navigation. Depuis D33 : « Rendez-vous » sur l'en-tête mobile. Les autres interprétations sont listées au §6 du rapport du tour 1. | Appliqué. | ChatGPT. |

### Tranchés

- **Lignes « Prise de rendez-vous en ligne »** (ancien point 3) → supprimées ; téléphone et e-mail au même niveau (D45).
- **Profils complémentaires** (ancien point 11) → TikTok et Le Fil Dentaire ajoutés aux profils ; fiche Google réservée au cabinet ; DentCA et Smileclub Formation décrites comme organisations fondées par Franck (D45).
- **Référencement local** (ancien point 12) → le cabinet est décrit aux moteurs (`#practice`, type `Dentist`) et relié à Franck (D45).
- **Robots d'IA** (ancien point 36) → tous autorisés, recherche et entraînement (D45).
- **Liens vers des pages à venir** (ancien point 7) → plus aucun depuis le lot D : chaque lien interne mène à une page construite ; le lien « Mentions légales » du pied de page aussi.
- **Mesure d'audience** (ancien point 16) → aucune (D42).
- **DOI de la page Facettes** (ancien point 37) → rétablis (D42).
- **Renvois bibliographiques, H1 trop longs, consignes glissées dans le texte, manques et liens, écarts mineurs, V1.2 attendue** (anciens points 28 à 32, 34 et 35) → corrigés dans la V1.2 finale, reconstruite le 22/09/2026 (D41).
- **Choix de mise en page des pages suivantes** (ancien point 33) → validés par ChatGPT (D40).
- **Arborescence** (ancien point 9) → 20 pages, dont une page locale, l'article Anorexie sans vomissements, Contact et Mentions légales (D38).
- **Méthode 6 ou 7 étapes** (ancien point 5) → 7 étapes, « Simuler » rétabli (D17).
- **Répartition des couleurs** (ancien point 6) → celle de 07, validée (D25).
- **« Découvrir ma démarche »** (ancien point 8) → section Méthode de l'accueil, validé (D25).
- **Bloc auteur** (ancien point 14) → bloc court + date de mise à jour (D20).
- **Notes « Soutient : »** (ancien point 22) → retirées de l'affichage (D19).
- **Destinations « Érosion & TCA » et « Publications & enseignement »** (ancien point 23) → sous-menus (D18).
- **Police des titres** (ancien point 24) → Newsreader (D16).
- **En-tête** (ancien point 25) → monogramme seul sur ordinateur validé (D25) ; en-tête mobile corrigé (D23).
- **Textes de « Planifier » et « Simuler »** (ancien point 27) → textes définitifs des 7 étapes fournis par ChatGPT (D31).
- **Nom de domaine** (ancien point 1) → `drfranckmoyal.fr` réservé par Franck chez OVH le 21/09/2026, jusqu'au 21/09/2029 (D14).
- **Sources de la page Usures** (ancien point 2) → fournies par Franck le 21/09/2026, dans le fichier 04 corrigé (D7, V22).
- **Logo** (ancien point 4) → le monogramme « Fm » avec l'arc vert sauge (D4).
- **Portrait** (partie du point 10) → la photo en noir et blanc fournie par Franck (D5).
- **Résolution du portrait** (ancien point 21) → original de 6 048 × 4 024 px fourni et intégré (D29).
- **« Dentiste esthétique »** (partie du point 15) → proscrit (D6, V21).
- **Menu de l'en-tête** (ancien point 17) → figé par ChatGPT (D10, V23).
- **Intertitres de la page Usures** (ancien point 18) → étiquette + grand titre ; nouveau titre pour la section 5 (D11).
- **Sous-blocs de la section 2** (ancien point 19) → textes fournis par ChatGPT (D12).
- **Lien Bruxisme** (ancien point 20) → intitulé fourni par ChatGPT (D13).

---

## 7. Les étapes du projet

| Étape | Contenu | Statut |
|---|---|---|
| **0** | Cadrage : pack V1.3 reçu, lu en entier et archivé ; projet créé ; fichier maître écrit et relu contre le pack | ✅ fait (21/09/2026) |
| **1** | Golden master : les 3 pages et les livrables du verrou V17 | ✅ tour 1 livré (21/09/2026) — `livrables/golden-master-r1/` |
| **2** | Contrôle par ChatGPT, retours de Franck, corrections, jusqu'au « Oui. C'est exactement l'image… » | ✅ fait (21/09/2026) — tour 1, tour 2, micro-tour P0.5 |
| **3** | Gel des composants : le golden master devient la référence figée | ✅ **gelé le 21/09/2026** (D37, V24) — étiquette GitHub `golden-master-gele` |
| **4** | Déclinaison des 20 autres pages (D38) à partir de la base gelée, textes rédigés par ChatGPT | **en cours** — **20 pages reconstruites depuis la V1.2 finale le 22/09/2026** (D41), compositions validées par ChatGPT (D40), correctif pré-lancement V1.3 appliqué (D45) ; restent les photos |
| **5** | Mise en ligne : domaine, hébergement, mentions légales, déclaration du site à Google (Search Console)… | ✅ **en ligne le 22/09/2026** — hébergement Hostinger (D43), domaine branché et https (D46), Google Search Console (D47), Bing Webmaster Tools (D48) |
| **6** | Suivi : positions dans Google et présence dans les réponses des IA ; travail SEO/GEO page par page avec ChatGPT | **en cours** — POINT 1 (page pilier Dentisterie esthétique) en ligne le 24/09/2026 (D50) ; POINT 2 annoncé : page comparative facettes / composite |

### Suivi des 3 pages du golden master

| Page | Adresse | Construite | Contrôlée par ChatGPT | Validée par Franck |
|---|---|---|---|---|
| Accueil | `/` | ✅ P0.5 | ✅ P0.5 | ✅ gel du 21/09/2026 |
| Dr Franck Moyal | `/franck-moyal/` | ✅ P0.5 | ✅ P0.5 | ✅ gel du 21/09/2026 |
| Usures dentaires | `/usures-dentaires/` | ✅ P0.5 | ✅ P0.5 | ✅ gel du 21/09/2026 |

### Suivi des 20 pages suivantes (D38)

| Lot | N° | Page | Adresse | Construite | Contrôlée par ChatGPT | Validée par Franck |
|---|---|---|---|---|---|---|
| A | 01 | Dentisterie esthétique à Paris | `/dentisterie-esthetique-paris/` | ✅ 21/09/2026 | ✅ 22/09/2026 (D40) | |
| A | 02 | Bilan esthétique personnalisé | `/bilan-esthetique-personnalise/` | ✅ 21/09/2026 | ✅ 22/09/2026 (D40) | |
| A | 03 | Composite bonding à Paris | `/composite-bonding-paris/` | ✅ 21/09/2026 | ✅ 22/09/2026 (D40) | |
| A | 04 | Facettes dentaires à Paris | `/facettes-dentaires-paris/` | ✅ 21/09/2026 | ✅ 22/09/2026 (D40) | |
| A | 05 | Éclaircissement dentaire à Paris | `/eclaircissement-dentaire-paris/` | ✅ 21/09/2026 | ✅ 22/09/2026 (D40) | |
| A | 06 | Taches blanches, MIH et dyschromies | `/taches-dentaires-dyschromies-icon/` | ✅ 21/09/2026 ; V1.3 le 22/09/2026 (D45) | ✅ 22/09/2026 (D40) | |
| B | 07 | Diagnostic des usures dentaires | `/diagnostic-usures-dentaires/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| B | 08 | Réhabilitation des dents usées | `/rehabilitation-dents-usees/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| B | 09 | Bruxisme et usure dentaire | `/bruxisme-usure-dentaire/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| B | 10 | Érosion dentaire | `/erosion-dentaire/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| B | 11 | Dents courtes ou usées | `/dents-courtes-usees/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| B | 12 | TCA et santé bucco-dentaire | `/tca-dents/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| B | 13 | Anorexie restrictive et érosion sans vomissements | `/anorexie-erosion-dentaire-sans-vomissements/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| C | 14 | Publications | `/publications/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| C | 15 | Conférences et formations | `/conferences-formations/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| C | 16 | Activité hospitalière | `/activite-hospitaliere/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| C | 17 | Médias et interviews | `/medias-interviews/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| C | 18 | Chirurgien-dentiste Paris 9 | `/chirurgien-dentiste-paris-9/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| D | 19 | Contact et rendez-vous | `/contact/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |
| D | 20 | Mentions légales | `/mentions-legales/` | ✅ 22/09/2026 | ✅ 22/09/2026 (D40) | |

---

## 8. Choix techniques appliqués

Retenus par Claude, dont c'est le rôle (00 §13), et appliqués au tour 1 (D15). Le détail
est dans le rapport (`livrables/golden-master-r1/RAPPORT.md`, §2 et §3).

- **Astro**, l'outil qui fabrique le site : il produit des pages HTML simples, lisibles
  aussitôt par Google et par les IA sans avoir à exécuter de programme, très rapides, et
  construites à partir de composants réutilisables — exactement ce qu'exige le gel des
  composants.
- **Polices hébergées sur le site lui-même**, pas chez Google : plus rapide, et aucune
  adresse de visiteur transmise à un tiers (RGPD). Newsreader pour les titres (D16, à la
  place de Cormorant Garamond) et Inter pour le texte. Une police sous licence pourra les
  remplacer en changeant un seul réglage.
- **Les textes rangés à part de la mise en page**, recopiés du pack, avec un **contrôle
  automatique** : chaque phrase du pack doit se retrouver telle quelle dans les pages
  construites. C'est la garantie mécanique du verrou V2.
- **Pages suivantes lues directement dans le pack** (depuis le lot A) : un programme lit les
  fichiers de `docs/pages-suivantes/v1/` au moment de fabriquer le site (`src/lib/pack.ts`) et
  un seul gabarit les assemble avec les composants gelés (`src/pages/[slug].astro`). Un fichier
  corrigé par ChatGPT remplace l'ancien sans ressaisie. Les choix propres à chaque page
  (emplacements d'images, passages non affichés, liens déduits, lots construits) sont réunis
  dans `src/content/pages-suivantes.ts`. Le contrôle des textes relit le pack par ses propres
  moyens et compare dans les deux sens : rien d'oublié, rien d'ajouté.
- **Fiche de renseignements en ligne** (22/09/2026) : une page privée sur claude.ai, visible de
  Franck seul, où il renseigne ce qui manque (téléphone, rendez-vous, e-mail, hébergeur, profils,
  photos disponibles, décisions). Ses réponses s'enregistrent au fur et à mesure dans une petite
  base de données liée à la page, que Claude lit directement. Aucune photo n'y est déposée.
- **Contrôle avant mise en ligne** (`npm run launch-check`, depuis le 22/09/2026) : la partie
  technique de la checklist 24 (§D) devenue automatique. Il liste ce qui empêche encore la mise
  en ligne — informations « à fournir » visibles, visuels manquants, bouton de rendez-vous
  provisoire, liens « à venir », profils `sameAs`, règles des robots d'IA, écarts du pack — et ne
  passe au vert que lorsque tout est levé.
- **Aucun traceur, aucune ressource extérieure** (V19). Résultat Lighthouse (outil de Google) au
  tour 2 : 100/100 en accessibilité, bonnes pratiques et référencement, 95 à 100 en rapidité
  (Newsreader et le portrait HD pèsent un peu plus) ; pages de 214 à 344 Ko.
- **Emplacements d'images** (D45) : sur le site public, un emplacement sans visuel validé
  disparaît, et la section se compose comme une section sans image (`src/lib/emplacements.ts`).
  `EMPLACEMENTS=1 npm run build` les fait réapparaître, à leur place et à leurs proportions,
  pour une revue de composition.
- **Correctif V1.3** : le fichier 06 du correctif est lu à la place de celui de la V1.2
  (`packReplacements` dans `src/content/pages-suivantes.ts`) ; ses décisions sont appliquées
  comme les autres (remplacements de texte, boutons de section, données structurées).
- **Captures automatiques** avec Google Chrome (déjà installé), aux largeurs du verrou
  V16, et contrôle de rapidité Lighthouse.
- **Lisibilité des couleurs** (mesurée le 21/09/2026) : le vert sauge sombre est lisible
  en texte (contraste 5,5 : 1 sur blanc cassé, 5,1 : 1 sur ivoire, au-dessus du minimum
  recommandé de 4,5 : 1). Le vert sauge clair (1,7 : 1) et le gris chaud (1,4 : 1) ne
  servent jamais pour du texte, seulement pour des fonds et des filets — ce qui correspond
  à la direction artistique.
- **iCloud** : les milliers de petits fichiers des outils (`node_modules`) sont exclus de la
  synchronisation par un marqueur que macOS reconnaît (`com.apple.fileprovider.ignore#P`).
  La parade du lien `.nosync`, qui marche pour Python sur PARCOURS, ne tient pas ici : npm
  remplace le lien par un vrai dossier (constaté le 21/09/2026).

---

## 9. Garde-fous

- Dépôt **privé** ; jamais rendu public sans demande explicite de Franck.
- Aucun mot de passe, aucune clé d'accès, aucun fichier `.env` dans le dépôt.
- **Aucune photo ni donnée de patient dans le dépôt.** Les photos cliniques du site, dont
  Franck a recueilli les consentements, peuvent rester sur le Bureau, synchronisé avec
  iCloud : Franck l'accepte pour ce dossier (D44). Leur préparation pour le web est décidée
  avant l'étape qui les intègre.
- Jamais d'envoi forcé (`push --force`) sur GitHub sans l'accord de Franck.
- Claude n'invente aucun texte et n'ajoute ni page ni fonction hors périmètre (V1, V2).
- Claude n'achète rien et ne crée aucun compte (domaine, hébergement, police) : Franck le
  fait lui-même. Dans les espaces OVH et Hostinger de Franck, Claude ne modifie rien de
  visible du public (enregistrements DNS, mise en ligne) sans son accord explicite.

---

## 10. Journal des échanges

Une ligne par échange qui fait avancer ou décider quelque chose. Source : **F** = Franck,
**G** = ChatGPT (via Franck), **C** = Claude. Les retours longs (contrôles de ChatGPT,
remarques détaillées de Franck) sont archivés tels quels dans
`docs/echanges/AAAA-MM-JJ-sujet.md` et résumés ici.

| Date | Source | Échange | Suite |
|---|---|---|---|
| 21/09/2026 | F | Lance le projet : dépôt `drfranckmoyal-cloud/geo`, pack `GOLDEN_MASTER_FRANCK_MOYAL_V1_3.zip`. Demande un fichier maître dès le départ, pour ne rien perdre des discussions, de la progression et des verrous, et une lecture sérieuse de tout le pack. | D1, D2, D3 |
| 21/09/2026 | C | Lecture intégrale des 10 fichiers. Projet et fichier maître créés ; pack archivé à l'identique (copies vérifiées). Vérifications : le domaine `drfranckmoyal.fr` n'est pas réservé ; deux logos trouvés sur le Bureau ; 16 points relevés (§6). L'enregistrement dans git et l'envoi sur GitHub ont été bloqués par le système de permissions de la session. | Accord de Franck attendu pour GitHub ; feu vert attendu pour l'étape 1 |
| 21/09/2026 | C | Relecture indépendante du fichier maître contre le pack, par un second agent : 1 erreur (les captures du « hero » traduites par « en-tête »), 10 imprécisions, 5 oublis. Tout est corrigé ; deux verrous ajoutés (V19, V20) et quatre questions (§6, points 17 à 20). | — |
| 21/09/2026 | F | Réponses : (1) « Je suis connecté à mon compte OVH sur Chrome, prends la main » pour le domaine ; (2) fichier Usures corrigé, avec les sources ; (3) rendez-vous mis en attente ; (4) logo = monogramme « Fm », portrait fourni ; (5) « ne jamais écrire “dentiste esthétique” mais “dentisterie esthétique” ou “exercice exclusif en dentisterie esthétique” ». Accord pour GitHub ; feu vert pour construire les 3 pages. | D4 à D9, V21, V22, pack V1.3.1 |
| 21/09/2026 | G | Réponse aux points 17 à 20, archivée dans `docs/echanges/2026-09-21-chatgpt-reponses-points-17-20.md` : menu figé ; étiquette + grand titre validés, mais « Non. » seul refusé ; textes des quatre sous-parties ; lien Bruxisme. ChatGPT corrige aussi Claude : aucune règle de Google ne dit que les intertitres en forme de question sont préférés. | D10 à D13, V23 |
| 21/09/2026 | C | Pack V1.3.1 archivé ; logo et portrait rangés dans le projet ; premier enregistrement et envoi sur GitHub. Construction du golden master lancée ; commande du domaine préparée sur OVH jusqu'au récapitulatif (18,70 € TTC pour 3 ans), sans aucun paiement. | Étape 1 |
| 21/09/2026 | F | « Le domaine est créé » : Franck a validé lui-même la commande OVH. Claude vérifie auprès du registre des .fr : domaine actif, jusqu'au 21/09/2029. | D14 |
| 21/09/2026 | C | **Golden master, tour 1 livré.** Les 3 pages sont construites (30 composants du pack + 2 techniques), avec 26 captures aux 6 largeurs, le rapport et une comparaison de polices. Contrôle des textes : aucun écart. Contrôle du HTML : réussi. Lighthouse : 100 partout. Défauts corrigés en cours de route : titre sur 6 lignes, accents vérifiés, bords du portrait, espacement de la phrase clé, noms accessibles. | Étape 2, points 24 à 26 |
| 21/09/2026 | C | À la demande de Franck, dossier de transmission posé sur le Bureau : `~/Desktop/GEO-golden-master-tour1-pour-ChatGPT/` (rapport, comparaison des polices, 14 captures numérotées, message prêt à coller dans ChatGPT). Aucune donnée patient. | Contrôle de ChatGPT |
| 21/09/2026 | G | **Contrôle du tour 1**, archivé dans `docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour1.md` : « structurellement réussi », base du site complet après un tour 2 ciblé, sans refonte. Les 8 critères de 08 F sont validés, deux sous condition (niveau de gamme et personnalité : il faut les vraies photos). 10 corrections P0 (police Newsreader, en-tête mobile, 7 étapes, sous-menus, sources, auteur et date, parcours cliquable, titre des pages liées, adresse, réponse directe sur mobile), puis les photos en P1. | D16 à D28 |
| 21/09/2026 | F | Envoie l'original de sa photo (« Design sans titre.png », 6 048 × 4 024 px) : « cette qualité de photo est meilleure ? » — oui, c'est la résolution native du Nikon D780, avec un vrai détail. | D29 |
| 21/09/2026 | C | **Tour 2 livré** : les 10 corrections P0 de ChatGPT et le portrait HD, avec le rapport `livrables/golden-master-r2/RAPPORT-tour2.md` et 15 captures ciblées. Contrôles : textes sans écart, HTML conforme, Lighthouse 95–100 / 100 / 100 / 100. En cours de route : « Chirurgien-dentiste » débordait avec Newsreader, d'où une colonne de titre élargie et un retour à la coupure naturelle au trait d'union aux petites largeurs. | Contrôle de ChatGPT |
| 21/09/2026 | C | Dossier de transmission du tour 2 posé sur le Bureau : `~/Desktop/GEO-golden-master-tour2-pour-ChatGPT/` (message à coller, rapport, 15 captures numérotées comme dans le rapport). | Contrôle de ChatGPT |
| 21/09/2026 | G | **Contrôle du tour 2**, archivé dans `docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour2.md` : « visuellement validé à 95 % », base définitive du site. Newsreader validée définitivement, portrait HD validé. Dernier micro-tour P0.5 : textes de la méthode, italique supprimé, bouton rendez-vous mobile, rapidité de la page Usures. Si les 4 points passent, le golden master est gelé. | D30 à D36 |
| 21/09/2026 | C | **Micro-tour P0.5 livré** (`livrables/golden-master-r3/RAPPORT-P0-5.md`, 8 captures) : textes définitifs de la méthode et titre complété, phrase clé et ligne auteur en romain, fichier italique supprimé, « Rendez-vous » sur l'en-tête mobile jusqu'à 440 px. Lighthouse mobile de la page Usures : LCP 1,95 s aux 3 passages (cible 2,5 s), 200 Ko au lieu de 344. Conditions de gel remplies. | Gel à prononcer par Franck |
| 21/09/2026 | C | Dossier de transmission du P0.5 posé sur le Bureau : `~/Desktop/GEO-golden-master-P0-5-pour-ChatGPT/` (message à coller, rapport, 8 captures). | Dernier coup d'œil de ChatGPT, gel |
| 21/09/2026 | F | **Décision de gel** transmise (`DECISION_GEL_GOLDEN_MASTER_DR_FRANCK_MOYAL.md`) : « GOLDEN MASTER GELÉ », P0.5 validé, règle après gel, étape suivante : industrialiser les pages restantes. Franck n'a pas souhaité garder l'aparté sur la vitesse et le SEO/GEO (simple curiosité). | D37, V24 |
| 21/09/2026 | C | Décision archivée mot pour mot (fichier déjà retiré du Bureau : recopiée depuis la conversation) ; verrou V24 ; `CLAUDE.md` du dépôt mis à jour ; version étiquetée `golden-master-gele` dans GitHub ; besoins pour les pages suivantes rédigés pour ChatGPT (`docs/besoins-pages-suivantes.md`). | Étape 4 |
| 21/09/2026 | F | Dépose sur le Bureau le pack `PACK_PAGES_SUIVANTES_CLAUDE_CODE_V1` (dossier et zip) : la réponse de ChatGPT à la demande de textes des pages suivantes. | D38 |
| 21/09/2026 | C | Lecture intégrale des 22 fichiers ; pack archivé à l'identique. Les 34 références scientifiques sont vérifiées sur PubMed : toutes existent, titres, revues, années et DOI concordent. En revanche, la numérotation des renvois `[n]` ne correspond pas à la liste des sources sur 9 pages, quelques consignes de rédaction se sont glissées dans le texte « mot pour mot », et 9 titres principaux dépassent 5 lignes sur téléphone (V16). Relevé complet dans le rapport du lot A. | Lot A |
| 21/09/2026 | C | **Lot A livré** (`livrables/pages-suivantes-lot-a/RAPPORT-LOT-A.md`, 14 captures) : les 6 pages esthétiques, fabriquées directement à partir des fichiers du pack, avec les composants gelés. Contrôles : textes sans écart dans les deux sens (essai de sabotage détecté), HTML et 10 contrôles du manifeste réussis, Lighthouse page 01 : mobile 99 / 100 / 100 / 100 (LCP 1,95 s), ordinateur 100 partout. Les 3 pages du golden master sont restées identiques. Écarts du pack consignés (§6, points 28 à 34). | Contrôle de ChatGPT ; lot B |
| 21/09/2026 | C | Dossier de transmission du lot A posé sur le Bureau : `~/Desktop/GEO-pages-suivantes-lot-A-pour-ChatGPT/` (message à coller, rapport, 14 captures). | Contrôle de ChatGPT |
| 22/09/2026 | C | **Lot B livré** (`livrables/pages-suivantes-lot-b/RAPPORT-LOT-B.md`, 9 captures) : les 7 pages usures, érosion, TCA. Textes sans écart, HTML et manifeste réussis. Première mesure de la page TCA : 97, LCP 2,55 s, à cause d'un « ń » qui faisait charger un second fichier de police ; corrigé en ne déclarant que le jeu latin d'Inter (D39) : 99, LCP 1,95 s. | Lot C |
| 22/09/2026 | C | Dossier de transmission du lot B posé sur le Bureau : `~/Desktop/GEO-pages-suivantes-lot-B-pour-ChatGPT/`. | Contrôle de ChatGPT |
| 22/09/2026 | C | **Lot C livré** (`livrables/pages-suivantes-lot-c/RAPPORT-LOT-C.md`, 11 captures) : Publications, Conférences et formations, Activité hospitalière, Médias et interviews, page locale Paris 9. Textes sans écart, HTML et manifeste réussis sur 21 pages, Lighthouse 99 / 100 (LCP 1,95 s). Les 5 publications de la page Publications sont décrites dans les données structurées, auteur relié à Franck. Correction typographique : « Paris 9 » ne se coupe plus en fin de ligne. | Lot D |
| 22/09/2026 | C | Dossier de transmission du lot C posé sur le Bureau : `~/Desktop/GEO-pages-suivantes-lot-C-pour-ChatGPT/`. | Contrôle de ChatGPT |
| 22/09/2026 | C | **Lot D livré** (`livrables/pages-suivantes-lot-d/RAPPORT-LOT-D.md`, 4 captures, bilan des 20 pages) : Contact (100 partout sur Lighthouse, LCP 1,80 s) et Mentions légales (`noindex,follow`). Le contrôle HTML a trouvé les mentions légales dans le plan du site : retirées. Le lien « Mentions légales » du pied de page mène à sa page. Les 20 pages sont construites ; plus aucun lien « à venir ». Dossier de transmission posé sur le Bureau : `~/Desktop/GEO-pages-suivantes-lot-D-pour-ChatGPT/`. | Contrôle de ChatGPT, pack V1.1 |
| 22/09/2026 | G | **Validation consolidée des lots A à D** (fichier 23) et **checklist avant mise en ligne** (fichier 24), transmises par Franck et archivées dans `docs/echanges/`. Toutes les compositions sont validées ; quelques précisions (page 18, page Contact, mentions légales, publications) ; la V1.2 du pack devient la source éditoriale finale. | D40 |
| 22/09/2026 | C | Précisions de D40 appliquées : bouton « Prendre rendez-vous » de la page 18 vers `/contact/#prendre-rendez-vous`, ancre `#prendre-rendez-vous`, ligne auteur retirée sur Contact et Mentions légales, date des mentions légales au 22 septembre 2026, publications en `Article` / `Book`. Contrôle avant mise en ligne ajouté (`npm run launch-check`) : il a trouvé un vrai défaut, corrigé (un lien vers `/contact/#…` pris pour une page à venir). Textes, HTML et golden master : contrôles réussis. La V1.2 n'est pas arrivée : demandée à Franck. | V1.2 |
| 22/09/2026 | F | Demande une page à remplir avec toutes les informations dont Claude a besoin. | Fiche en ligne |
| 22/09/2026 | C | Fiche de renseignements publiée (page privée, §11), pré-remplie des profils AP-HP et Blendi trouvés dans le pack. | Réponses de Franck |
| 22/09/2026 | G | **V1.2 finale du pack** déposée par Franck sur le Bureau (26 fichiers) avec un message de reconstruction : V1.2 source unique, règle globale des rendez-vous vers `/contact/#prendre-rendez-vous`. | D41 |
| 22/09/2026 | C | **Reconstruction depuis la V1.2** (`livrables/pages-suivantes-v1-2/RAPPORT-RECONSTRUCTION-V1-2.md`) : textes sans écart, plus aucun écart de renvois, HTML et plan du site réussis, H1 en 4 lignes au plus sur mobile, 37 références vérifiées sur PubMed, Lighthouse 99–100 ; liens de rendez-vous centralisés, pages gelées comprises. Le contrôle avant mise en ligne ne relève plus que 5 points, tous du ressort de Franck. | Fiche de Franck |
| 22/09/2026 | F | Remplit la fiche en ligne ; transmet la demande de ChatGPT de rétablir deux DOI de la page Facettes. Demande aussi d'insister, sur la page Taches, sur les taches de MIH et le traitement des patients jeunes ; photos triées dans « Icono GEO » sur le Bureau. | D42 |
| 22/09/2026 | C | Fiche intégrée (D42), DOI rétablis ; contrôles réussis ; il ne reste que 3 points avant la mise en ligne. Note des derniers arbitrages pour ChatGPT : `livrables/pre-lancement/POINTS-PRE-LANCEMENT.md`, copiée sur le Bureau. Aucune photo intégrée tant que les consentements et le circuit ne sont pas réglés. | Revue de ChatGPT |
| 22/09/2026 | F | « Consentement : oui, ils ont tous été recueillis » ; « emplacement du dossier : oublie cet interdit, ce n'est pas un problème » ; « j'ai un abonnement chez Hostinger pour la mise en ligne : il est ouvert sur Chrome, prends la main pour créer le site, je ne sais pas faire ». | D43, D44 |
| 22/09/2026 | C | Site « drfranckmoyal.fr » créé dans l'espace Hostinger de Franck, fichiers déposés ; à l'adresse provisoire, les 23 pages sont identiques à la version locale. Hébergeur des mentions légales : Hostinger. Branchement du domaine préparé, sans rien changer chez OVH. | Étape 5 |
| 22/09/2026 | G | **Correctif pré-lancement V1.3**, déposé par Franck sur le Bureau (`PATCH_PRE_LANCEMENT_V1_3_AVEC_CORRECTIF_EMAIL.zip`, 4 fichiers) : page 06 centrée sur la MIH, décisions sur les derniers points, fiche corrective du contact (téléphone et e-mail au même niveau). | D45 |
| 22/09/2026 | C | Correctif appliqué et contrôlé : textes, HTML et données structurées réussis, plus aucun point bloquant avant mise en ligne. Rapport : `livrables/pre-lancement/RAPPORT-CORRECTIF-V1-3.md`, copié sur le Bureau. | Revue de ChatGPT |
| 22/09/2026 | C | Version V1.3 déposée chez Hostinger (la session du gestionnaire de fichiers, expirée, rouverte depuis hPanel) : les 23 pages servies à l'adresse provisoire sont identiques à la version locale. | Étape 5 |
| 22/09/2026 | F | « Ok, branche le domaine. » | D46 |
| 22/09/2026 | C | Enregistrements A de `drfranckmoyal.fr` et `www` modifiés chez OVH vers Hostinger ; nouvelle adresse vue aussitôt par les serveurs d'OVH et les résolveurs de Google et Cloudflare ; `http://` et `www.` redirigés vers `https://drfranckmoyal.fr/` ; certificat https en cours d'installation chez Hostinger. | Étape 5 |
| 22/09/2026 | F | « Ok, fais-le, tu as mon accord » (déclaration du site à Google et Bing). | D47 |
| 22/09/2026 | C | Certificat https actif à 9 h 04 (Let's Encrypt, `drfranckmoyal.fr` et `www`) ; site vérifié en ligne : 23 pages identiques, robots.txt, plan du site, redirections ; archive de déploiement mise à la corbeille d'Hostinger. Google Search Console : propriété validée par TXT chez OVH, plan du site lu, 4 pages en file d'indexation prioritaire. OVH propose la double authentification : non activée par Claude (réglage de sécurité du compte de Franck). Bing : pas de compte Webmaster, à ouvrir par Franck. | Étape 5 |
| 22/09/2026 | F | « Je suis connecté à Bing. » | D48 |
| 22/09/2026 | C | Site importé dans Bing Webmaster Tools depuis Search Console (compte Google `drfranckmoyal@gmail.com`, accès en lecture seule accordé à Bing) ; plan du site envoyé ; 22 pages soumises à 9 h 24. | Étape 5 |
| 23/09/2026 | C | Courriel de Search Console (« page avec redirection », « exclue par la balise noindex ») : comportements voulus, vérifiés en ligne. Redirections : `http://`, `www.` et adresses sans barre oblique finale mènent à l'adresse unique de chaque page. `noindex` : la seule page concernée est celle des mentions légales, hors du plan du site depuis le lot D. Aucune des 22 pages indexables n'est bloquée. Rien à corriger. | Étape 6 |
| 23/09/2026 | G | **Audit de production** demandé : 4 contrôles prioritaires (robots.txt, plan du site, redirections http et www) et 11 contrôles sur les 23 pages, sans toucher à l'architecture, aux contenus ni au design. | D49 |
| 23/09/2026 | C | Audit exécuté sur le site en ligne : une seule anomalie, `/sitemap.xml` en 404, corrigée et remise en ligne. Les 14 autres contrôles passent ; Lighthouse mobile 100 partout ; aucune erreur de données structurées au test de Google (deux recommandations facultatives à trancher). Rapport : `livrables/audit-production-2026-09-23.md`, copié sur le Bureau. | Revue de ChatGPT |
| 24/09/2026 | G | **POINT 1 SEO/GEO** : spécification éditoriale et technique de la page pilier Dentisterie esthétique (27 points), transmise par Franck. | D50 |
| 24/09/2026 | F | Arbitre les deux points signalés avant implémentation : verrou V21 levé pour cette page, nouvelle section des traitements avec l'entrée Taches conservée. | D50 |
| 24/09/2026 | C | Page pilier intégrée, contrôlée et mise en ligne ; rapport après déploiement, avec les dix différences relevées entre la spécification et l'implémentation : `livrables/point-1-page-pilier/RAPPORT-POINT-1.md`. | Revue de ChatGPT |

---

## 11. Informations techniques de référence

- **Dossier** : `~/Desktop/Claude-Projects/GEO` (le Bureau est synchronisé avec iCloud).
- **Dépôt** : `git@github.com:drfranckmoyal-cloud/geo.git`, branche `main`, privé.
  Identité git posée au niveau du dépôt.
- **Outils présents sur le Mac** (21/09/2026) : Node 24.18, npm 11.16, git 2.50,
  Python 3.13, Google Chrome. Ni `gh` ni Homebrew.
- **Fabriquer et contrôler le site** (dans le dossier du projet) : `npm run build` fabrique le
  site dans `dist/` ; `npm run verify` lance le contrôle des textes ; `node scripts/check-html.mjs`
  lance le contrôle du HTML ; `npm run images` prépare le logo et le portrait à partir des
  originaux ; `BASE_URL=http://localhost:4322 npm run captures` refait les captures
  (`SET=lotA OUT=livrables/pages-suivantes-lot-a/captures` pour celles du lot A ; de même `lotB`, `lotC`, `lotD`). Les lots
  construits se règlent dans `src/content/pages-suivantes.ts` (`builtLots`) ; `npm run launch-check`
  dit ce qui empêche encore la mise en ligne.
- **Voir le site en local** : serveurs `geo-dev` (port 4321, mise à jour en direct) et
  `geo-preview` (port 4322, site fabriqué), déclarés dans `~/Desktop/.claude/launch.json`.
- **Où est quoi** : textes dans `src/content/` ; composants dans `src/components/`
  (global, home, editorial, clinical, ui) ; réglages de design dans `src/styles/tokens.css` ;
  pages dans `src/pages/` ; livrables par tour dans `livrables/` (captures non versionnées,
  régénérables).
- **Fiche de renseignements de Franck** : https://claude.ai/artifact/1sKz2QAnH3sbxvqixANouD (page
  privée ; réponses dans sa base de données, document `infos/franck`, lisibles par Claude).
- **Hébergement** : Hostinger, espace de Franck (hPanel, https://hpanel.hostinger.com), offre
  Premium Web Hosting, échéance du 22/10/2026. Site « drfranckmoyal.fr », dossier `public_html` ;
  adresse provisoire https://mediumaquamarine-louse-843680.hostingersite.com (l'aperçu y remplace
  le nom de domaine dans les pages et interdit l'indexation par Google) ; serveur `91.108.101.161`.
  **Mettre en ligne une nouvelle version** : `npm run build`, puis `npm run paquet` (archive
  `livrables/deploiement/drfranckmoyal-site.zip`, fichiers cachés compris) ; dans le
  gestionnaire de fichiers d'Hostinger (hPanel → Fichiers → « Accéder aux fichiers de
  drfranckmoyal.fr » ; la session expire au bout de quelques heures), déposer l'archive dans
  `public_html`, puis « Extract » avec `.` pour nom de dossier et « Overwrite existing files »
  coché ; enfin, mettre l'archive à la corbeille (décocher « Skip trash bin », coché par défaut),
  sinon elle reste téléchargeable par tous.
- **Enregistrements DNS chez OVH** (zone DNS du domaine, dans l'espace OVH de Franck) : depuis le
  22/09/2026 (D46), `drfranckmoyal.fr` et `www` en A vers `91.108.101.161`, le serveur Hostinger
  (avant : `213.186.33.5`, la page d'attente d'OVH) ; `ftp` en CNAME vers `drfranckmoyal.fr` ;
  courrier (MX) et SPF d'OVH, inchangés ; TXT `google-site-verification=…` de Google Search
  Console (D47), à ne jamais supprimer.
- **Plan du site** : `/sitemap-index.xml` (déclaré dans `robots.txt` et aux moteurs), `/sitemap-0.xml`
  (les 22 adresses) et `/sitemap.xml`, copie conventionnelle produite à la fabrication (D49).
- **Google Search Console** : propriété « drfranckmoyal.fr » (type Domaine) sur le compte Google de
  Franck, https://search.google.com/search-console?resource_id=sc-domain%3Adrfranckmoyal.fr ;
  plan du site `https://drfranckmoyal.fr/sitemap-index.xml`.
- **Bing Webmaster Tools** : compte de Franck (connexion avec Google), site `https://drfranckmoyal.fr/`,
  https://www.bing.com/webmasters/home?siteUrl=https://drfranckmoyal.fr/ ; importé depuis Search
  Console, plan du site envoyé, 22 pages soumises le 22/09/2026.
- **Certificat https** : Let's Encrypt, installé et renouvelé automatiquement par Hostinger
  (« Lifetime SSL », hPanel → Sécurité → SSL) ; couvre `drfranckmoyal.fr` et `www`.
- **Domaine** : `drfranckmoyal.fr`, bureau d'enregistrement OVH, compte OVH de Franck ; créé
  le 21/09/2026 (17:10 UTC), expire le 21/09/2029 ; serveurs de noms `dns111.ovh.net` et
  `ns111.ovh.net` (registre AFNIC, vérifié le 21/09/2026). Avant cette date, ni ce domaine ni
  ses variantes n'étaient enregistrés.
- **Empreintes SHA-256 des packs** (V1.3, le seul fichier changé en V1.3.1, le pack « pages suivantes » V1 et le correctif V1.3) :

| Fichier | Empreinte |
|---|---|
| `GOLDEN_MASTER_FRANCK_MOYAL_V1_3.zip` | `113371fbd1db50b48f217efd677341e4ea376530ad170df187b360c96b5a97bd` |
| `00_PROJECT_CONTEXT.md` | `5e483b82cb47e200dbf0b015b9b17b4330199084333bc1a67a4b333b794cf964` |
| `00_README.md` | `e8b29acce305af8b6172fd7d476d3cc0defafc861f3d04e0562494b3c259c484` |
| `01_DESIGN_SYSTEM.md` | `cd436e80760ff344e9e15175d2c169c1b2ac39eda5ffefd5ca91679133a05452` |
| `02_HOME.md` | `58eeb8cf455c4ae597176ffb30dca9835320db34f1d7edfaa6d2b994f38e3e98` |
| `03_FRANCK_MOYAL.md` | `0eff36fcb7a5ff573698af5905daf196994070abea3b4471a3ba185b2bba6d3a` |
| `04_USURES_DENTAIRES.md` | `029c59b06350a2cd539358dd4ccc55d805ab1e170d490e6bdcbf5ca09924db11` |
| `05_COMPONENT_MAP.md` | `79671ddda1e07acf5f03dc4351aa58e1981454ed44eea34734611492737569ec` |
| `06_PROMPT_CLAUDE_CODE.md` | `24e0c73c9d2a3fff93e118433644d3dbc6b2bd4133a2f163cb122325fd8cee4e` |
| `07_ART_DIRECTION.md` | `e7bbde1b3f03e40bc1f1e8a03ec1e54d1e0cee86a6120f479be971683c79246a` |
| `08_VISUAL_QA_CLAUDE.md` | `8c52ec0bad6bb63a71b8724de5716d4cc9aca9dcf0b05dd80d5d716fcbf9a606` |
| `04_USURES_DENTAIRES.md` **corrigé (V1.3.1)** | `7a2dc986046ca233163ac04c63f6b907fdfe3c16064e81db879e0893d7b27acc` |
| `PACK_PAGES_SUIVANTES_CLAUDE_CODE_V1.zip` (22 fichiers, identiques à `docs/pages-suivantes/v1/`) | `07616eecc073d4dfa774642637ff716161a4dce42752b460e3ed82989b980757` |
| `PATCH_PRE_LANCEMENT_V1_3_AVEC_CORRECTIF_EMAIL.zip` (4 fichiers, identiques à `docs/pages-suivantes/v1.3/`) | `f177d5419fdd474abd2280ab9fe88e31a6996b21ef7e78d8ee7fa67d002762ae` |

---

*Dernière mise à jour : 22 septembre 2026.*
