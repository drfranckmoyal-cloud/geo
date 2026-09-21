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
| **Phase en cours** | Étape 1 — golden master (3 pages) : construction lancée le 21/09/2026, sur le feu vert de Franck. |
| **Dernière étape faite** | Étape 0 — cadrage ; réponses de Franck du 21/09/2026 intégrées (logo, portrait, sources de la page Usures, règle « dentisterie esthétique »). |
| **Prochaine action** | Claude termine les 3 pages, puis remet captures et rapport pour le contrôle de ChatGPT. |
| **La construction est-elle bloquée ?** | Non. Tout élément manquant est remplacé par un emplacement réservé, clairement signalé (verrou V2). |
| **En attente de Franck** | Rien de bloquant. À fournir quand possible : le portrait en haute définition (§6, point 21). |

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
l'en-tête, intertitres et textes de la section 2 de la page Usures, lien Bruxisme — D10 à D13).

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
| V1 | **Trois pages, pas une de plus, pour la phase 1** : `/`, `/franck-moyal/`, `/usures-dentaires/`. Ni les autres pages, ni le CMS complet (système de gestion de contenu), ni fonction marketing non demandée, ni nouveau gabarit, ni variante esthétique. Rien d'autre avant la validation humaine. (00_README ; 00 §12, §14 ; 06) |
| V2 | **Les textes ne se touchent pas.** Ni modifiés, ni raccourcis sans validation, ni complétés. Pas de slogan, pas de chiffre marketing, pas de badge « expert », « premium », « leader ». Si une information manque : un emplacement réservé clairement signalé, jamais une invention. (06 ; 08 B) |
| V3 | **La stratégie, l'arborescence, le positionnement, les titres et l'ordre des sections** restent tels quels. (06) |
| V4 | **Les adresses des pages** (00 §11). Accueil `/` · entité `/franck-moyal/` · pilier esthétique `/dentisterie-esthetique-paris/`, avec `/bilan-esthetique-personnalise/`, `/composite-bonding-paris/`, `/facettes-dentaires-paris/`, `/eclaircissement-dentaire-paris/`, `/taches-dentaires-dyschromies-icon/` · pilier usures `/usures-dentaires/`, avec `/diagnostic-usures-dentaires/`, `/rehabilitation-dents-usees/`, `/bruxisme-usure-dentaire/`, `/erosion-dentaire/`, `/dents-courtes-usees/`, `/tca-dents/` · autorité `/publications/`, `/conferences-formations/`, `/activite-hospitaliere/`, `/medias-interviews/`. |
| V5 | **Les couleurs** : noir doux `#171715` · blanc cassé `#FAF8F3` · ivoire `#F4F0E8` · gris chaud `#D8D3CA` · vert sauge sombre `#5E685D` (accent) · vert sauge clair `#B9C1B5` (accent secondaire). Répartition : 70–80 % blanc cassé et ivoire, 10–15 % noir doux, 5–10 % gris chaud, 5 % de vert au maximum. Le vert ponctue (petite étiquette, filet, survol, petite zone de fond, détail typographique), il n'est jamais le thème. Interdits : bleu médical, bleu nuit corporate, turquoise, violet cosmétique, or, beige trop jaune, dégradés, vert saturé. (07 §3 ; 01 ; 08 B) |
| V6 | **Les polices** : titres en serif éditoriale (dans l'esprit de Canela, Editorial New, Tiempos ; Cormorant Garamond si le choix doit être gratuit) ; texte en sans-serif neutre (Inter, Manrope ; Suisse ou Neue Haas si licence). Tailles sur ordinateur : H1 64–76 px, H2 42–52, H3 26–32, chapeau 22–26, texte 17–19, petit texte 14–15. Sur mobile : H1 42–48, H2 32–38, H3 24–28, chapeau 20–22, texte 17–18. Contraste fort entre les niveaux, interlignage confortable. Le contraste serif / sans-serif fait partie de l'identité : la serif pour le désir et la personnalité, la sans-serif pour la précision clinique. (07 §4 ; 01 ; 08 A) |
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
| V21 | **Jamais « dentiste esthétique »**, nulle part sur le site ni dans ses informations pour les moteurs. On écrit « dentisterie esthétique », ou « exercice exclusif en dentisterie esthétique ». Règle de Franck, du 21/09/2026 (D6). « Quel dentiste esthétique à Paris ? » reste une question que les patients posent (00 §1), mais le site ne reprend jamais l'expression. |
| V22 | **Sources scientifiques de la page Usures** : une section « Sources scientifiques » visible en bas de page, avec des liens externes discrets ; les 5 à 7 références principales, repliables ou en fin de page ; pas de paragraphe interrompu par une bibliographie lourde ; les renvois `[1]`, `[2]`… conservés s'ils restent discrets ; liens sortants en `rel="noopener noreferrer"` ; ne jamais présenter la conclusion d'une étude comme plus forte qu'elle ne l'est. (04, V1.3.1) |
| V23 | **Menu de l'en-tête, figé** : à gauche, le nom et le logo « Dr Franck Moyal », qui mènent à l'accueil (pas de rubrique « Accueil ») ; puis Dentisterie esthétique · Usures dentaires · Érosion & TCA · Dr Franck Moyal · Publications & enseignement ; à droite, le bouton « Prendre rendez-vous ». « Publications & enseignement » pourra ouvrir plus tard sur Publications, Conférences & formations, Activité hospitalière, Médias. Affiché dès le golden master, même si les pages n'existent pas encore. (ChatGPT, 21/09/2026 — D10) |

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

---

## 6. Questions ouvertes et points relevés

Relevés à la lecture intégrale des 10 fichiers, puis complétés après une relecture
indépendante du fichier maître contre le pack, le 21/09/2026. **Aucun n'empêche de
construire le golden master.** « D'ici là » = ce que Claude fait en attendant la réponse.
Quand un point est tranché, il passe dans la liste « Tranchés » en bas, avec son numéro de
décision.

| # | Constat | D'ici là | Qui tranche |
|---|---|---|---|
| 3 | **Destination du bouton « Prendre rendez-vous »** inconnue (Doctolib ? téléphone ? formulaire ?). **Adresse et téléphone du cabinet** absents (pied de page, référencement local, données structurées). | Emplacements signalés. **Mis en attente par Franck le 21/09/2026 (D8).** | Franck, plus tard. Bloque la mise en ligne, pas le prototype. |
| 5 | **La méthode compte 7 étapes dans 00 §5** (avec « Simuler ») **et 6 sur la page d'accueil** (02, où la simulation est comprise dans « Planifier »). | Page d'accueil : les 6 étapes de 02, à l'identique. | ChatGPT, pour la cohérence des pages futures. |
| 6 | **La répartition des couleurs diffère** entre 01 (80 / 15 / 5 %) et 07 (70–80 / 10–15 / 5–10 / 5 % max). Le pack ne dit pas lequel l'emporte. | Application de 07, plus détaillé et qui se déclare « verrouillé » — c'est une lecture de Claude. | ChatGPT, pour confirmer. |
| 7 | **Liens vers des pages qui n'existent pas encore** : les 3 pages renvoient vers 11 pages futures (dentisterie esthétique, bilan esthétique personnalisé, TCA, érosion, diagnostic, réhabilitation, bruxisme, dents courtes, publications, conférences et formations, activité hospitalière), plus le contact et les mentions légales. | Liens vers les adresses définitives (V4), listés « non finalisés » dans le rapport. | Personne pour la phase 1. |
| 8 | **Destination de « Découvrir ma démarche »** (bouton secondaire de l'accueil) non précisée. | Lien vers la section « Méthode » de la page d'accueil. | ChatGPT ou Franck, pour confirmer. |
| 9 | **Arborescence** : 00 §14 parle des « 20 autres pages », l'arborescence de 00 §11 en liste 16 ; le contact et les mentions légales, demandés au pied de page, n'y ont pas d'adresse. | Rien pour la phase 1. | ChatGPT, avant la déclinaison (étape 4). |
| 10 | **Photos** : le portrait est fourni (D5). Manquent : les visuels des deux piliers, les images cliniques et les « schémas simples » de la page Usures. | Emplacements neutres aux bonnes proportions, légendés « à fournir ». | Franck (photos), ChatGPT (contenu des schémas). |
| 11 | **Preuves d'autorité** (00 §7 : AP-HP / Pitié-Salpêtrière, CMME / Sainte-Anne / GHU Paris, AO News, Blendi, Le Fil Dentaire, Entretiens de Garancière, Alpha Oméga, ARTEMIS, GC / ADF, LinkedIn, Smileclub Formation, DentCA) : aucune adresse web fournie. Le site doit « rassembler et redistribuer cette autorité vers les pages cliniques correspondantes » (00 §7). Pour les profils de Franck lui-même (LinkedIn, par exemple), une propriété technique (`sameAs`) signalera en plus aux moteurs qu'il s'agit de la même personne — suggestion de Claude, absente du pack. | Liens signalés « à fournir ». | ChatGPT (liste), Franck (vérification). |
| 12 | **Référencement local** : le pack vise un atout « SEO local », mais les données structurées prévues ne décrivent pas le cabinet (adresse, horaires). Suggestion technique : décrire aussi le cabinet (type `Dentist`) et le relier à Franck. | Rien d'ajouté sans accord (V1). | ChatGPT. |
| 13 | **Longueur des titres et descriptions pour Google** : le titre de la page Usures (73 caractères) et les descriptions de l'accueil (170) et de la page Franck (189) dépassent ce que Google affiche d'ordinaire (environ 60 caractères pour un titre, 155 pour une description) ; le titre de l'accueil (65) est à la limite. Ils seront coupés dans les résultats. | Repris à l'identique (V2). | ChatGPT, s'il souhaite raccourcir. |
| 14 | **Auteur de la page Usures** : exigé (08 E « sources et auteur présents » ; 04 : auteur `Person#franck-moyal` dans les données structurées), mais sa présentation visible n'est pas précisée. Le composant `AuthorBlock` existe (05, famille Éditorial / Profil). Une date de mise à jour, absente du pack, serait utile aux moteurs. | `AuthorBlock` avec le nom, le titre et le lien repris de la page Franck, sans texte nouveau ; pas de date. | ChatGPT. |
| 15 | **Déontologie — à vérifier par Franck**, qui connaît le code mieux que Claude. « Dentiste esthétique » : tranché, proscrit (D6, V21). Restent : « pratique privée exclusivement orientée » (page Franck ; Franck cite « exercice exclusif en dentisterie esthétique » parmi les formules correctes, mais n'a pas demandé de changer ce texte) ; les règles de communication des chirurgiens-dentistes (information loyale, pas de témoignages, pas de comparaison) ; les photos avant/après ; les mentions obligatoires du site ; la mention des établissements (AP-HP, GHU Paris) et de leurs logos. | Rien de modifié (V2). | Franck. |
| 16 | **Mesure d'audience** : le pack n'en prévoit pas. | Aucun traceur, donc aucun bandeau cookies nécessaire. | Franck et ChatGPT, avant la mise en ligne. |
| 21 | **Résolution du portrait** : 480 × 480 pixels. Affiché en grand (page Franck : « portrait dominant »), il paraîtra flou, surtout sur les écrans haute définition (Mac, téléphones récents), qui demandent 2 à 3 fois plus de pixels. | Photo utilisée à une taille raisonnable et harmonisée avec la palette (noir doux et blanc cassé à la place du noir et du blanc purs). | Franck : fournir l'original en haute définition (idéalement 2 000 pixels ou plus de large). |
| 22 | **Notes « Soutient : » des sources** : chaque référence du fichier Usures est suivie d'une note expliquant ce qu'elle soutient. Le fichier ne dit pas si ces notes s'affichent. | Affichées en petit sous chaque référence : elles relient chaque source au texte. | ChatGPT. |
| 23 | **Destination de « Érosion & TCA » dans le menu** : non précisée. L'arborescence a `/erosion-dentaire/` et `/tca-dents/`. De même, « Publications & enseignement » n'a pas encore de page à lui. | « Érosion & TCA » → `/tca-dents/`, la page de l'expertise spécifique ; « Publications & enseignement » → `/publications/`. | ChatGPT, pour confirmer. |

### Tranchés

- **Nom de domaine** (ancien point 1) → `drfranckmoyal.fr` réservé par Franck chez OVH le 21/09/2026, jusqu'au 21/09/2029 (D14).
- **Sources de la page Usures** (ancien point 2) → fournies par Franck le 21/09/2026, dans le fichier 04 corrigé (D7, V22).
- **Logo** (ancien point 4) → le monogramme « Fm » avec l'arc vert sauge (D4).
- **Portrait** (partie du point 10) → la photo en noir et blanc fournie par Franck (D5) ; voir le point 21 pour sa résolution.
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
| **1** | Golden master : les 3 pages et les livrables du verrou V17 | **en cours** (lancée le 21/09/2026) |
| **2** | Contrôle par ChatGPT, retours de Franck, corrections, jusqu'au « Oui. C'est exactement l'image… » | à faire |
| **3** | Gel des composants : le golden master devient la référence figée | à faire |
| **4** | Déclinaison des autres pages (V4) à partir de la base gelée, textes rédigés par ChatGPT | à faire |
| **5** | Mise en ligne : domaine, hébergement, mentions légales, déclaration du site à Google (Search Console)… | hors pack, à cadrer |
| **6** | Suivi : positions dans Google et présence dans les réponses des IA | hors pack, à cadrer |

### Suivi des 3 pages du golden master

| Page | Adresse | Construite | Contrôlée par ChatGPT | Validée par Franck |
|---|---|---|---|---|
| Accueil | `/` | — | — | — |
| Dr Franck Moyal | `/franck-moyal/` | — | — | — |
| Usures dentaires | `/usures-dentaires/` | — | — | — |

---

## 8. Choix techniques prévus pour l'étape 1

Proposés par Claude, dont c'est le rôle (00 §13). Ils deviendront des décisions au fil de
la construction.

- **Astro**, l'outil qui fabrique le site : il produit des pages HTML simples, lisibles
  aussitôt par Google et par les IA sans avoir à exécuter de programme, très rapides, et
  construites à partir de composants réutilisables — exactement ce qu'exige le gel des
  composants.
- **Polices hébergées sur le site lui-même**, pas chez Google : plus rapide, et aucune
  adresse de visiteur transmise à un tiers (RGPD). Par défaut, Cormorant Garamond pour les
  titres (la solution gratuite prévue par le pack) et Inter pour le texte. Une police sous
  licence pourra les remplacer en changeant un seul réglage.
- **Les textes rangés à part de la mise en page**, recopiés du pack, avec un **contrôle
  automatique** : chaque phrase du pack doit se retrouver telle quelle dans les pages
  construites. C'est la garantie mécanique du verrou V2.
- **Aucun traceur, aucune ressource extérieure** (V19).
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
- **Aucune photo ni donnée de patient** dans le dossier du projet (synchronisé avec
  iCloud) ni dans le dépôt. La phase 1 n'utilise que des emplacements neutres. Le circuit
  des photos cliniques (stockage hors iCloud, consentement, anonymisation, préparation pour
  le web) sera décidé avant l'étape qui les intègre.
- Jamais d'envoi forcé (`push --force`) sur GitHub sans l'accord de Franck.
- Claude n'invente aucun texte et n'ajoute ni page ni fonction hors périmètre (V1, V2).
- Claude n'achète rien et ne crée aucun compte (domaine, hébergement, police) : Franck le
  fait lui-même.

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

---

## 11. Informations techniques de référence

- **Dossier** : `~/Desktop/Claude-Projects/GEO` (le Bureau est synchronisé avec iCloud).
- **Dépôt** : `git@github.com:drfranckmoyal-cloud/geo.git`, branche `main`, privé.
  Identité git posée au niveau du dépôt.
- **Outils présents sur le Mac** (21/09/2026) : Node 24.18, npm 11.16, git 2.50,
  Python 3.13, Google Chrome. Ni `gh` ni Homebrew.
- **Domaine** : `drfranckmoyal.fr`, bureau d'enregistrement OVH, compte OVH de Franck ; créé
  le 21/09/2026 (17:10 UTC), expire le 21/09/2029 ; serveurs de noms `dns111.ovh.net` et
  `ns111.ovh.net` (registre AFNIC, vérifié le 21/09/2026). Avant cette date, ni ce domaine ni
  ses variantes n'étaient enregistrés.
- **Empreintes SHA-256 du pack** (V1.3, et le seul fichier changé en V1.3.1) :

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

---

*Dernière mise à jour : 21 septembre 2026.*
