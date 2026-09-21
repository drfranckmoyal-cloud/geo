# Pages suivantes — lot A : dentisterie esthétique

*Claude Code, 21 septembre 2026. Pack « pages suivantes » V1 (`docs/pages-suivantes/v1/`),
fichiers 01 à 06, intégrés avec les seuls composants gelés du golden master (verrou V24).
La partie 5 relève les écarts trouvés dans **tout** le pack (20 pages), pour que tu puisses
les corriger en une fois.*

---

## 1. Ce qui est livré

| N° | Page | Adresse | Données structurées |
|---|---|---|---|
| 01 | Dentisterie esthétique à Paris | `/dentisterie-esthetique-paris/` | WebPage |
| 02 | Bilan esthétique personnalisé | `/bilan-esthetique-personnalise/` | WebPage |
| 03 | Composite bonding à Paris | `/composite-bonding-paris/` | MedicalWebPage |
| 04 | Facettes dentaires à Paris | `/facettes-dentaires-paris/` | MedicalWebPage |
| 05 | Éclaircissement dentaire à Paris | `/eclaircissement-dentaire-paris/` | MedicalWebPage |
| 06 | Taches blanches, dyschromies et ICON | `/taches-dentaires-dyschromies-icon/` | MedicalWebPage |

Toutes : fil d'Ariane, BreadcrumbList, auteur relié à `Person#franck-moyal`, `dateModified`
du 21/09/2026, title et meta du pack, adresse de référence ; sources (`citation`) quand la page
en a.

**Comment les pages sont fabriquées.** Les textes ne sont pas recopiés : le site lit
directement tes fichiers au moment d'être construit (titres, textes, listes, gras, renvois,
liens, FAQ, appel final, sources). Un fichier corrigé remplace l'ancien et la page suit, sans
ressaisie. Pour une nouvelle version, renvoie les fichiers au même format : ils iront dans
`docs/pages-suivantes/v1.1/`.

**Ouverture et ordre des blocs** : celui des contrats de composants — ouverture clinique, réponse
directe, sections, FAQ, sources, bloc auteur, pages liées, appel final.

## 2. Contrôles

- **Textes** (`npm run verify`), dans les deux sens, sur les 6 pages : **aucun passage du pack
  oublié, aucun texte ajouté**. Le contrôle relit tes fichiers par ses propres moyens, sans
  passer par le programme qui fabrique les pages. Essai de sabotage (deux mots changés dans une
  page construite) : les deux écarts sont détectés.
- **HTML et informations pour les moteurs** (`node scripts/check-html.mjs`) : réussi, avec les
  10 contrôles de ton manifeste — un seul H1 ; fil d'Ariane visible et données conformes au
  pack ; title, meta et adresse de référence ; `dateModified` ; auteur relié à
  `…/#franck-moyal` ; sources présentes dans le HTML ; liens internes descriptifs ; « dentiste
  esthétique » absent partout ; aucune image inventée ; réglages de design identiques à la
  version gelée (étiquette `golden-master-gele`). Plus : aucune ancre sans cible, plan du site
  = les 9 pages construites.
- **Golden master intact** : les 3 pages gelées ont été comparées avant et après. Seule
  différence : les liens vers les pages désormais construites ne sont plus marqués « à venir ».
- **Lighthouse**, page 01 (Dentisterie esthétique) :

| | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | Poids |
|---|---|---|---|---|---|---|
| Mobile, passage 1 | 99 | 100 | 100 | 100 | 1,95 s | 199 Ko |
| Mobile, passage 2 | 99 | 100 | 100 | 100 | 1,95 s | 199 Ko |
| Mobile, passage 3 | 99 | 100 | 100 | 100 | 1,95 s | 199 Ko |
| Ordinateur | 100 | 100 | 100 | 100 | 0,44 s | 199 Ko |

  (Lighthouse 13.5 ajoute une note « Agentic Browsing » : 100.)

## 3. Choix de mise en page, à valider

1. **Ordre** : celui des contrats (pages liées **puis** appel final). Sur la page Usures du
   golden master, l'appel final précède les sources : les deux ordres coexistent donc.
2. **Composition dominante** : le texte décalé, comme sur la page Usures. La variété vient des
   listes, des grilles d'intertitres, des emplacements d'images côte à côte et d'un fond ivoire
   une section sur trois. Si tu veux plus d'alternance (colonne de lecture à gauche), dis-le.
3. **Intertitres `###`** : sous-titre H3 sous le titre de section (« Très souvent, non ou très
   peu », « Écouter avant de proposer »…). Quand une section aligne 2 à 4 intertitres courts, ils
   passent en grille à filets vert sauge — la composition « mécanismes » de la page Usures
   (capture 04).
4. **Listes** : liste clinique sans légende, la phrase qui précède l'annonçant ; deux colonnes
   pour les listes longues d'éléments courts ; colonne latérale quand une seule liste clôt la
   section (capture 09) ; liste numérotée avec les numéros du parcours clinique (capture 10).
5. **Page 02** : le contrat demande `MethodSteps` pour la séquence en 7 étapes, que le texte de
   la page ne contient pas. J'ai repris les 7 étapes et le titre validés au gel (D31), avant
   « Première étape : écouter » (capture 08) — le même bloc que sur l'accueil. À confirmer, ou
   donne un titre propre à la page.
6. **Images** : 12 emplacements réservés, légendés d'après le §9 de chaque fichier (partie 6).
   L'ouverture clinique gelée n'a pas d'image : la « photographie de planification » prévue pour
   l'ouverture de la page 01 est placée dans la section smile design.
7. **Titres de blocs non fournis**, repris du golden master : « FAQ » (comme la page Usures) ;
   sources : titre, phrase d'introduction et « Voir les N sources scientifiques » de la page
   Usures ; bloc auteur court (D20) ; pages liées : « À lire aussi », le titre que tu utilises
   dans les pages 14 à 17. Pas de date de vérification bibliographique, le pack n'en donnant
   pas ; les références ayant été vérifiées sur PubMed le 21/09/2026 (partie 5.2), je peux
   l'afficher si tu le confirmes.
8. **Gras** : la graisse standard d'Inter. Le golden master n'avait pas de gras dans le texte
   courant ; à regarder sur les captures.

## 4. Adaptations des composants gelés — aucune n'a d'effet visuel sur le golden master

- `SymptomList` : légende facultative, gras possible dans les éléments.
- `FAQAccordion` : gras et renvois possibles dans les réponses.
- `SourceList` : notes sous la liste, date de vérification facultative, un renvoi sans
  référence mène au bloc des sources.
- `FinalCTA` : phrase et bouton facultatifs (pages 07 à 13 : titre seul ; page 18 : pas de
  libellé de bouton).
- `MethodSteps` : introduction et lien facultatifs.
- `TextLink` : une adresse externe s'ouvre dans un nouvel onglet (`rel="noopener noreferrer"`).
- Mise en forme du texte : gras, retours à la ligne, emplacements « à fournir », adresses web.
- Un composant d'assemblage (`PackBlocks`) pose paragraphes, listes, intertitres et liens avec
  les composants existants. Il n'apporte aucun style nouveau : tailles, filets et espacements
  sont ceux du golden master.

## 5. Écarts relevés dans le pack (les 20 pages) — à corriger

### 5.1 Renvois bibliographiques — à corriger avant la mise en ligne

Le numéro `[n]` du texte doit désigner la bonne référence de la liste. Pages 01, 02, 07 et
08 : cohérentes. Ailleurs :

- **03 Composite bonding** : « …font partie de leur cycle de vie. [2,3,5] » — pas de
  référence [5] (liste [1] à [4]).
- **04 Facettes** : liste décalée. Dans le texte, [1,2] = Digital Smile Design, mais la liste
  donne [1] Alqutaibi (facettes, substrats) et [2] Klein (survie des facettes). Le [3] du
  texte (collage sur émail) correspond à Alqutaibi, alors que la liste donne [3] = Alwabel
  (DSD). Le [4] (survie de 94 à 97 % à environ dix ans) correspond à Klein, absent sous ce
  numéro. Saini (DSD) manque. Liste qui colle au texte : [1] Alwabel, [2] Saini, [3] Alqutaibi,
  [4] Klein.
- **05 Éclaircissement** : trois références listées (de Geus, Hardan, Terra), aucun renvoi
  dans le texte.
- **06 Taches** : [4] Kosys 2026 listée, jamais citée.
- **09 Bruxisme** : deux références portent le [1] (Bronkhorst et Loomans). « …données
  cliniques favorables dans les dentitions usées. [4,5] » : ni [4] ni [5] — sans doute Fan 2025
  et Chantler 2025, références [2] et [3] de la page 08.
- **10 Érosion** : « …même en l'absence de vomissements. [4–6] » et « umbrella review publiée
  en 2026… [7] » (deux fois). Or la liste s'arrête à [4], et ce [4] est justement l'umbrella
  review (Gómez 2026). Il manque les trois références sur l'anorexie — candidates déjà listées
  page 13 : Kisely 2015, Chan 2024, Niederau 2025 — et Gómez devrait porter le [7].
- **11 Dents courtes** : le texte cite [3–5] (approches non ou minimalement invasives) et
  [6,7] (dimension verticale) ; la liste s'arrête à [4], et ce [4] (Goldstein, consensus sur
  la DVO) correspond plutôt au renvoi [6,7].
- **12 TCA** : [6,7] (publications historiques sur le report des reconstructions) et [8,9]
  (techniques adhésives) absents. Probable inversion de [4] et [5] : « flux salivaire et pH
  chez les patients anorexiques [1,4] » correspond à Niederau 2025 (listé [5]), « rôle du
  chirurgien-dentiste [1,3,5] » à Anderson 2023 (listé [4]). Enfin, « Une méta-analyse a
  montré… [2] » renvoie à Nijakowski 2023, qui se présente comme une revue systématique : à
  vérifier.
- **13 Anorexie sans vomissements** : décalage à partir de [4].
  - « Processus chimico-mécanique [5,6] » renvoie à Gómez (dentifrices), alors qu'il s'agit
    du consensus EFCD (listé [4]) et de Schlueter 2020 (absent).
  - « Umbrella review 2026 [7] » = Gómez, listé [5].
  - [8] (reconstruction adhésive) absent.
  - Le titre de [4] est abrégé (« EFCD Consensus Report… ») au lieu du titre exact.

*D'ici là : renvois affichés tels quels ; un renvoi sans référence mène au bloc des sources.
Le contrôle des textes les signale à chaque construction. Rien n'est en ligne.*

### 5.2 Vérification des 34 références sur PubMed : correcte

Les 34 PMID existent. Titres, revues, années, premiers auteurs et DOI concordent. Deux détails :

- 11 [2] Bartlett et O'Toole : publié en ligne en décembre 2020 (le pack indique 2021, année
  du numéro).
- 13 [4] : titre abrégé (ci-dessus).

### 5.3 H1 trop longs pour le mobile (V16 : « un H1 ne casse jamais en 5 lignes »)

Taille du H1 gelée (44 px sur mobile). Mesuré dans l'ouverture clinique réelle :

| Page | Caractères | Lignes à 390 px | à 430 px |
|---|---|---|---|
| 01 Dentisterie esthétique | 80 | 6 | 5 |
| 02 Bilan esthétique | 83 | 6 | 5 |
| 03 Composite bonding | 84 | 6 | 5 |
| 06 Taches blanches | 90 | 6 | 6 |
| 08 Réhabilitation | 95 | 7 | 6 |
| 09 Bruxisme | 79 | 5 | 5 |
| 10 Érosion | 93 | 7 | 6 |
| 12 TCA | 110 | 8 | 7 |
| 13 Anorexie | 89 | 7 | 6 |

Les 11 autres tiennent en 4 lignes au plus (07, 72 caractères : 4 lignes). Deux voies sans
toucher au système :

- des H1 plus courts (jusqu'à 70 caractères environ) ;
- une décision explicite d'accepter ces longueurs.

Capture 03 : la page 06 à 390 px.

### 5.4 Passages qui ressemblent à des consignes de rédaction — non affichés, à confirmer

- **05** : le bloc final « Direction éditoriale validée pour le versant esthétique » /
  « Expertise assumée, bénéfice esthétique clairement vendu… ».
- **10** : « Sur le site patient, le message doit donc rester simple : » (la phrase en gras
  qui suit reste affichée).
- **12**, section DentCA : « Cette présence devra être reliée à une page officielle DentCA
  indexable afin de renforcer la continuité… ».
- **14** : le bloc « Note de normalisation bibliographique », sous « La chirurgie orale ».

Dans les rubriques « Sources », les phrases de consigne ne sont pas affichées :

- 01, 02 : « À présenter comme documentation du logiciel… » ;
- 05 : « À ne pas écrire : … » ;
- 14 à 17 : consignes sur les preuves externes.

Sont en revanche affichés sous la liste des sources :

- 01, 02, 04 : « Source fonctionnelle — SmileCloud : https://smilecloud.com/fr/ ». La ligne
  est hors numérotation, donc présentée comme documentation du logiciel.
- 03 : « Repère clinique du Dr Franck Moyal : … » (capture 12).

### 5.5 Éléments manquants

- **05** : pas de bloc CTA → pas d'appel final (capture 14).
- **18** : le bloc CTA n'a pas de libellé de bouton (adresse ; téléphone « à compléter » ;
  lien « à compléter »). Prévu sans bouton, à moins que tu donnes un libellé.
- **14 à 17** : pas de CTA, donc pas d'appel final (conforme à « si pertinent »).

### 5.6 Liens

- **Libellés absents de la liste « Liens internes » de leur page** — adresse déduite :
  - 07 « Comprendre le bruxisme et son rôle dans l'usure dentaire » → `/bruxisme-usure-dentaire/`
    (libellé déjà validé sur la page Usures, D13) ;
  - 09 « Érosion dentaire : dépistage et prévention » → `/erosion-dentaire/` ;
  - 10 « Anorexie restrictive : pourquoi peut-on observer des érosions sans vomissements ? » →
    `/anorexie-erosion-dentaire-sans-vomissements/` ;
  - 14 « Découvrir le composite bonding » → `/composite-bonding-paris/` ;
  - 15 « Usures dentaires : comprendre avant de reconstruire » → `/usures-dentaires/` ;
  - 19 « Découvrir l'activité hospitalière » → `/activite-hospitaliere/`.
- **Liens à câbler placés nulle part dans le texte.** Pages cliniques : ils vont dans « À lire
  aussi ». Pages 15 et 17, dont la liste « À lire aussi » est écrite : « Composite bonding à
  Paris » (15) et « Usures dentaires » (17) ne figurent nulle part. Faut-il les ajouter à la
  liste ?
- **19, « Motifs de consultation »** : 7 intitulés en gras, sans lien. Je propose d'en faire des
  liens vers les pages correspondantes.
- **Bouton « Prendre rendez-vous »** : tant que le lien de rendez-vous manque, il mène au bloc
  final de la page ; sur les pages sans bloc final (05, 14 à 17, 20), il ne mène nulle part.
  Proposition : dès que la page Contact existe (lot D), le faire pointer vers `/contact/`
  (section « Prendre rendez-vous »).

### 5.7 Écarts mineurs

- **19** : le H1 du §2 (« Contact et rendez-vous — Dr Franck Moyal, Paris 9e ») diffère de
  celui du contenu (« … Dr Franck Moyal », sans « Paris 9e »). J'affiche celui du §2.
- **16** : la note non affichée donne comme « formulation publique à conserver » : « J'exerce
  au sein du service de Médecine Bucco-dentaire de l'Hôpital Pitié-Salpêtrière, notamment dans
  le cadre de la PASS bucco-dentaire. » Le texte du §5 s'arrête à « …Pitié-Salpêtrière. », la
  PASS venant à la phrase suivante. J'affiche le §5.
- **13** : « MedicalWebPage + Article si le template le permet » → les deux types sont posés ;
  pas de date de publication (non fournie).
- **14** : « Person auteur lorsqu'une publication lui est attribuée » → les publications seront
  décrites dans les données structurées, auteur relié à `Person#franck-moyal` (lot C).

## 6. Emplacements réservés du lot A

| Page | Section | Légende (§9 du fichier) |
|---|---|---|
| 01 | Quelle place pour le smile design ? | Photographie réelle de planification esthétique |
| 01 | Quels traitements peuvent transformer un sourire ? (pleine largeur) | 3 à 5 cas cliniques réels |
| 02 | Deuxième étape : documenter | Séquence photo / scan / simulation d'un vrai cas, avec consentement |
| 02 | Qu'apporte le smile design ? | Vidéo ou capture réelle de simulation SmileCloud |
| 03 | Qu'est-ce que la stratification composite ? | Macro-photo de texture et de stratification |
| 03 | Ce que je recherche avec un composite antérieur | 2 cas de composite antérieur stratifié, cadrage constant |
| 04 | Sublimer un sourire plutôt que remplacer des dents | 2 cas de facettes complets : état initial → projet → résultat |
| 04 | Smile design et simulation | Vidéo / simulation SmileCloud réelle |
| 05 | La technique que je privilégie… | Photo sobre de gouttières personnalisées |
| 05 | Est-ce que le résultat est visible ? | Cas avant / après éclaircissement, mêmes conditions photographiques |
| 06 | Pourquoi une tache blanche paraît-elle blanche ? | Macro clinique réelle de lésion et résultat |
| 06 | Qu'est-ce que l'érosion-infiltration de résine ? | 2 cas de dyschromie / white spot : avant / après, avec consentement |

Non posés :

- le cas de fermeture de diastème / Front Wing (03), la section concernée étant une liste
  latérale ;
- la photo de laboratoire (04), « uniquement si réelle et premium ».

## 7. Toujours attendus

Téléphone, lien de prise de rendez-vous, adresse e-mail professionnelle et hébergeur (mentions
légales), adresses `sameAs` exactes, visuels propriétaires.

## 8. Captures (`captures/`)

| N° | Contenu |
|---|---|
| 01, 02 | Page Dentisterie esthétique entière, ordinateur (1440) et mobile (390) |
| 03 | Ouverture clinique avec un H1 long, mobile 390 (page 06) |
| 04, 05 | Intertitres en grille, avec liens et emplacement pleine largeur (page 01), ordinateur et mobile |
| 06 | Sous-titre H3 et liste sur deux colonnes (page 01) |
| 07 | Texte, liste et emplacement d'image côte à côte (page 01) |
| 08 | Méthode en 7 étapes sur la page Bilan esthétique |
| 09 | Liste en colonne latérale (page 03) |
| 10, 11 | Liste numérotée — le parcours des facettes (page 04), ordinateur et mobile |
| 12 | Sources avec la note « Repère clinique », bloc auteur (page 03) |
| 13 | Pages liées puis appel final (page 01) |
| 14 | Fin de page sans appel final (page 05) |

## 9. Suite

Lots B, C et D dans l'ordre du pack, chacun avec son rapport. Les corrections de la partie 5
pourront arriver en une seule nouvelle version du pack : les pages se mettront à jour
d'elles-mêmes, et le contrôle des textes confirmera que plus rien ne manque.
