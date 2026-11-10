# Audit du site drfranckmoyal.fr — 10 novembre 2026

Demande de Franck : « audite-moi ce site sur un plan esthétique, factuel, et principalement référencement
SEO / GEO, avec l'accent sur le GEO, sur les mots-clés importants de l'esthétique dentaire et des autres
sujets traités ».

Le précédent audit date du 25 octobre, le soir de la mise en ligne de la refonte
(`livrables/audit-2026-10-25/`). Celui-ci regarde le site deux semaines plus tard, avec en plus la lecture
des textes et le contrôle des faits.

## Comment l'audit a été fait

- **Les 36 pages en ligne lues une à une** (34 000 mots), avec le relevé automatique de leurs titres,
  descriptions, liens, images et données destinées à Google et aux IA.
- **Le rendu regardé à l'écran**, sur ordinateur et sur téléphone.
- **Les 43 références scientifiques contrôlées une à une** dans les registres officiels (Crossref, PubMed),
  et quatre chiffres clés relus dans les résumés des études.
- **Google** : les relevés quotidiens de Search Console, du 25 octobre (veille de la refonte) au 9 novembre.
- **IA** : 18 questions posées à Google le 10 novembre (17 questions de patients et une sur votre nom),
  pour lire son « aperçu IA », depuis un navigateur neutre (sans compte, sans votre Chrome). Comparées au
  relevé des 21 et 22 octobre.

Ce que l'audit ne dit pas : la vitesse n'a pas été remesurée (99 à 100 sur 100 le 26 octobre, rien n'a
changé depuis) ; ChatGPT et le « Mode IA » de Google n'ont pas été interrogés, car ils demandent votre
Chrome pendant un long moment. Le relevé IA est une photographie sur un seul moteur et une seule passe : les
réponses des IA changent d'un jour à l'autre.

---

## 1. En bref

| Axe | Verdict | L'essentiel |
|---|---|---|
| **Esthétique** | **Très bon, finitions à reprendre** | Identité forte, pages patients élégantes, téléphone impeccable. Mais 22 phrases coupées sur 9 pages, des blocs de sources mal présentés sur 10 pages, et les pages « pro » sont nettement en dessous des pages patients. |
| **Exactitude** | **Bon** | Les 43 références existent toutes et disent bien ce que le site leur fait dire. Les chiffres cités sont fidèles. Restent 10 points à corriger ou à confirmer, dont un titre hospitalier et deux contradictions entre pages. |
| **Google (SEO)** | **Technique très bon, visibilité encore étroite** | 19 recherches en première page : votre nom, le composite, le blanchiment, les facettes à Paris. Mais les pages Usure, Érosion et TCA, les meilleures du site, ne sortent encore sur presque rien. 6 pages vidéo sur 7 toujours absentes de Google. |
| **IA (GEO)** | **Fondations solides, résultat encore mince** | Google vous cite en premier sur « dentiste TCA Paris » et « dentiste spécialiste de l'usure dentaire à Paris ». Sur les 14 autres questions, vous n'apparaissez pas. Et sur votre propre nom, l'IA de Google donne deux adresses qui ne sont pas celle du site. |

### Les cinq priorités

1. **Corriger ce que les IA disent de vous, là où elles le lisent** (hors du site). À la question « qui est
   le Dr Franck Moyal », Google répond que vous consultez au Centre de santé dentaire Flandre (19e) et au
   Centre médico-dentaire Balard (15e), sans citer le 2 rue Hippolyte Lebas. Voir § 5.2.
2. **Donner à la page « Mon parcours » les faits qui lui manquent** : diplôme, université, année, numéro
   RPPS, fonctions datées, titres des publications. Aujourd'hui aucune de ces informations n'est écrite sur
   le site. Voir § 5.4.
3. **Rendre le site de DenTCA lisible par les IA.** Pour la plupart de leurs robots, dentca-asso.com est une
   page vide : votre nom n'y figure pas. Voir § 5.5.
4. **Réparer les phrases coupées et les blocs de sources** (travail technique, sans toucher au sens). Voir § 2.
5. **Écrire sous chaque vidéo le texte intégral de ce qui y est dit.** C'est ce qui manque à Google pour
   retenir ces pages. Voir § 4.3.

---

## 2. Esthétique

### Ce qui est réussi

- **Une identité qui se retient** : l'accueil coupé en deux, noir et blanc, avec le portrait à cheval sur
  les deux espaces. Aucun site de confrère ne ressemble à celui-ci.
- **Les pages patients** : titres en caractères à empattements, colonnes de texte étroites et lisibles,
  grandes photos avant/après étiquetées, une question par chapitre, numérotation « 1 / 5 ». L'ensemble donne
  une impression de sérieux et de calme, cohérente avec le discours « le diagnostic avant le geste ».
- **Le téléphone** : rien ne déborde, le texte est à bonne taille, et la barre fixe du bas (Écrire, Appeler,
  Itinéraire) est exactement ce qu'il faut à un patient.
- **Les photos cliniques** : de qualité, bien cadrées, toutes légendées.

### Ce qui cloche

| | Défaut | Où | Gravité |
|---|---|---|---|
| E1 | **Phrases coupées.** La mise en page automatique a déplacé des listes dans les encadrés « En bref » en laissant derrière elles la phrase qui les annonçait. On lit « Cette pratique impose souvent de composer avec : » puis plus rien. 22 phrases dans ce cas, et un début de phrase amputé sur la page Érosion (« éviter les gestes agressifs… »). | 10 pages, liste en annexe A | **Forte** : c'est ce qu'un lecteur attentif remarque en premier, et les IA recopient ces passages tels quels. |
| E2 | **Encadrés « En bref » fourre-tout** : des listes sans rapport y sont mises bout à bout, mêlées à des liens (« Voir mon profil AP-HP · pathologies multiples · traitements médicaux complexes… »). | Activité hospitalière, Publications, Conférences, Médias | Forte sur ces 4 pages |
| E3 | **Titres des publications absents.** La page Publications n'affiche ni le titre de l'article du Fil Dentaire, ni celui des deux ouvrages : seulement la revue, la date et les coauteurs. Les titres existent dans les données cachées, pas à l'écran. | Publications | **Forte** (et lourde de conséquences pour les IA, § 5.4) |
| E4 | **Blocs « Sources scientifiques » mal présentés** : chaque référence est coupée en deux lignes numérotées (la référence, puis son lien), « DOI » et « PubMed » sont collés sans espace, et le « [1] » fait double emploi avec le « 1. ». Sur les pages Usure et TCA, écrites à la main, les sources sont correctement présentées. | 10 pages, annexe A | Moyenne |
| E5 | **Cartes « Avant / après » déséquilibrées** : une vignette de 275 pixels dans une carte quatre fois plus large, avec un grand vide à gauche. | Facettes, Composite, Éclaircissement, ICON, Usure, TCA | Moyenne |
| E6 | **Bloc en double** en bas de la page Parcours (« Une consultation commence par un diagnostic », deux fois de suite). | Mon parcours | Faible |
| E7 | **Légende sans photo pendant le chargement.** Les images n'ont pas de dimensions déclarées : quand on fait défiler vite, la légende s'affiche seule un instant, puis la page saute. | Toutes les pages à photos | Faible |
| E8 | **Accueil sans geste proposé.** Aucun bouton « Prendre rendez-vous » ; le téléphone est en petits caractères tout en bas. Le sous-titre « Dentisterie esthétique » est très pâle et à cheval sur les deux moitiés. | Accueil (ordinateur) | Faible, à trancher |
| E9 | **Pages « pro » en retrait** : pas de photo, textes hachés, encadrés fourre-tout. Elles ne sont pas au niveau des pages patients, alors que ce sont elles qui portent votre crédit auprès des confrères et des IA. | Les 4 pages pro | Moyenne |

---

## 3. Exactitude

### Ce qui a été vérifié et qui est juste

- **Les 43 références scientifiques existent** et correspondent toutes à l'article annoncé (auteurs, titre,
  revue, année). Les 46 liens PubMed mènent au bon article. Aucune référence inventée, ce qui était le
  risque principal pour des textes préparés avec une IA.
- **Les chiffres cités sont fidèles à leurs sources** :
  - facettes, « 94 à 97 % de survie à environ dix ans » : l'étude donne 93,7 %, 96,1 % et 96,8 % à 10,4 ans ;
  - TCA, « cinq fois plus de risque d'érosion, plus de sept fois en cas de vomissements » : exact ;
  - usure, « près de trois jeunes adultes sur dix » : exact (étude européenne, 3 187 personnes) ;
  - éclaircissement à domicile « comparable au fauteuil, avec moins de sensibilités » : conforme (l'étude
    précise que le niveau de preuve est faible) ;
  - boulimie « 1,5 % des 11–20 ans », hyperphagie « 3 à 5 % » : conformes à la HAS.
- **Le ton est honnête** : le site dit ce que les traitements ne font pas, signale les limites des études
  (« littérature hétérogène »), présente le « 6 à 7 ans » du composite comme un repère personnel et non comme
  un résultat d'étude. C'est rare, et c'est exactement ce que les IA et Google valorisent en santé.

### Ce qui est à corriger ou à confirmer

| | Point | Où | Ce qu'il faudrait |
|---|---|---|---|
| F1 | **« Praticien hospitalier, Pitié-Salpêtrière »**. C'est un titre statutaire (obtenu par concours national). Votre fiche AP-HP dit seulement « Service de médecine bucco-dentaire », et le site vous dit « praticien attaché » à la CMME. | Signature ou présentation sur 30 pages, texte de la page TCA, données cachées | **À confirmer par vous.** Si votre statut à la Pitié est « praticien attaché », l'écrire partout. Les IA reprennent ce titre mot pour mot. |
| F2 | **Durée du composite : deux réponses.** La page dit « 6 à 7 ans », le résumé de la vidéo dit « entre 6 et 10 ans ». | Composite, Facettes ou composite, Dents courtes / vidéo Composite | Une seule fourchette, par exemple « 6 à 7 ans en moyenne, parfois jusqu'à 10 ». |
| F3 | **Brossage après l'acide : deux pages se contredisent.** La page TCA dit d'attendre 30 minutes à une heure. La page Érosion dit que cette règle est remise en question. | TCA / Érosion | Une phrase de raccord sur chaque page : après un vomissement, l'attente reste conseillée (HAS) ; après un aliment acide, la règle est discutée. |
| F4 | **« Le blanchiment abîme-t-il l'émail ? Non. […] sans toucher à la structure de la dent. »** Trop absolu : des études de laboratoire décrivent des modifications de surface, légères et réversibles. | Éclaircissement | « Non, pas de dommage durable quand le protocole est respecté. » |
| F5 | **Éclaircissement : la règle légale manque.** En Europe, le produit est limité à 6 % de peroxyde d'hydrogène (soit environ 16 % de peroxyde de carbamide) et **interdit avant 18 ans**. La page ICON y fait allusion (« les règles propres à l'âge ») sans le dire. | Éclaircissement, ICON, cas clinique MIH | L'écrire en clair : c'est un fait que les IA cherchent, et cela lève toute ambiguïté sur les cas de MIH présentés. |
| F6 | **Deux noms écrits de deux façons** : « DenTCA » (2 pages) et « DentCA » (2 pages) ; « Smile Club Formations » (3 pages) et « Smileclub Formation » (2 pages). | Publications, Conférences, Parcours | Une seule graphie : « DenTCA » et « Smile Club Formations » (celle du site de l'organisme). |
| F7 | **Le lieu d'exercice n'a pas le même nom partout.** Le site dit « le cabinet », « pratique privée ». Doctolib dit « Centre médical et dentaire Saint-Georges, 2 rue Hippolyte Lebas ». | Cabinet, Contact, Parcours | **À trancher par vous** : si le lieu porte ce nom, le citer une fois sur le site. Sinon les IA ne font pas le lien (§ 5.2). |
| F8 | **« ★ 4,9 / 5 · 113 avis Google »** est écrit en dur : le chiffre ne se mettra pas à jour. | Contact | Voir aussi D1 ci-dessous. |
| F9 | « ADF 2026 — atelier GC **programmé** le 25 novembre 2026 ». | Médias, Conférences | À mettre au passé après le 25 novembre. |
| F10 | « La résine infiltrée est **stable dans le temps**. » Les études suivent les patients quelques années seulement. | ICON | « stable sur plusieurs années dans les études disponibles ». |

### Trois points de déontologie à faire valider

Le code de déontologie (article R. 4127-215-1 du code de la santé publique) autorise la communication
du chirurgien-dentiste si elle est « loyale et honnête », sans « témoignages de tiers » ni comparaison avec
des confrères. Trois formulations du site s'en approchent. Je les signale sans les juger : ce sont vos choix,
et pour deux d'entre elles vous les avez faits en connaissance de cause.

- **D1 — La note Google affichée sur la page Contact.** Reprendre des avis de patients sur son propre site
  est ce que vise l'interdiction des « témoignages de tiers » ; une note globale est un cas limite. Un lien
  vers la fiche Google, sans la note, écarte le risque.
- **D2 — « chirurgien-dentiste spécialisé dans la prise en charge des usures » / « des TCA ».** Le mot
  « spécialiste » est réservé aux trois spécialités reconnues ; « spécialisé » n'est pas interdit en toutes
  lettres, mais peut être lu comme l'annonce d'une spécialité.
- **D3 — « une référence en France ».** C'est aussi, mot pour mot, la phrase que l'IA de Google reprend
  pour vous présenter (§ 5.1) : elle est donc très efficace, et très exposée.

Un échange avec votre conseil départemental réglerait les trois d'un coup.

Enfin, hors déontologie : le site invite les patients à envoyer leurs **documents médicaux à une adresse
Gmail**. Une adresse au nom du site (contact@drfranckmoyal.fr) serait plus crédible et plus prudente pour
des données de santé.

---

## 4. Google (SEO)

### 4.1 La technique : rien à redire

Toutes les pages répondent en 0,3 seconde au plus. Une seule adresse par page, aucun doublon de titre ni de
description, un seul grand titre par page, toutes les images décrites, plan du site à jour, robots autorisés,
aperçus de partage partout, données structurées sur chaque page (praticien, cabinet, fil d'Ariane, questions
fréquentes, pages médicales, vidéos, références). Aucun lien interne cassé.

### 4.2 Les positions : ce qui a bougé depuis la refonte

Relevé Search Console du 9 novembre, comparé au 25 octobre. En dessous de 10, on est en première page.

| Situation | Recherches |
|---|---|
| **Première page (19)** | dont : votre nom (2 à 6) · composite dentaire (2,6) · blanchiment dentaire Paris (2,5) · esthétique du sourire (3) · **facettes dentaires Paris (4,5, contre 7,6)** · **facettes dentaires (4, absent avant)** · meilleur dentiste esthétique Paris (6,7) · composite bonding (7,4) · **bonding dentaire Paris (7,7, absent avant)** · composite bonding Paris (7,8) · spécialiste bruxisme Paris (1) |
| **Deuxième page, à portée (5)** | composite esthétique dentaire (11,5, **était 4,2**) · facette dentaire Paris 9 (11,8) · **dents usées (13, absent avant)** · composite dentaire Paris (15, **était 1**) · **esthétique dentaire Paris (16,7, contre 26,5)**, l'une des deux recherches les plus affichées hors de votre nom |
| **Loin (7)** | anorexie dents (33) · **boulimie dents (37, absent avant)** · dentiste esthétique Paris (39) · bonding dentaire (53) · facettes dentaires Paris 17 (68) · usure dentaire (84) · traitement usure dentaire (85) |
| **Absent (32)** | toute l'érosion · usures dentaires · dentiste TCA · taches blanches, MIH · éclaircissement dentaire Paris · facettes ou composite · dentisterie esthétique Paris · prix des facettes · Smile Club Formations |

Lecture : la refonte a fait **monter l'esthétique** (facettes, bonding, esthétique dentaire Paris) et fait
**entrer deux sujets nouveaux** (dents usées, boulimie). Elle n'a encore **rien changé pour l'usure,
l'érosion et les TCA** sur les recherches générales. Deux reculs à surveiller : « composite dentaire Paris »
et « composite esthétique dentaire ».

Une réserve : une position moyenne de 4,5 dans Search Console ne garantit pas un lien dans les dix premiers.
Sur « facettes dentaires Paris », cherché aujourd'hui depuis un navigateur neutre, le site n'était pas dans les
premiers résultats. Ces positions viennent en partie de la carte et des recherches faites près du cabinet.
Les 165 affichages sans un seul clic, sur les cinq derniers relevés, vont dans ce sens.

### 4.3 Ce qui freine

| | Frein | Détail | Qui |
|---|---|---|---|
| S1 | **Le site est jeune et peu cité.** | En ligne depuis sept semaines. Sur « usure dentaire » ou « érosion dentaire », Google met en tête des sites qui ont dix ans et des centaines de liens : thèses universitaires, Colgate, Dentaly, cabinets installés. Le contenu ne suffit pas : il faut que d'autres sites renvoient vers le vôtre. C'est **le** facteur limitant, pour Google comme pour les IA. | Hors du site, § 6 C |
| S2 | **6 pages vidéo sur 7 hors de Google**, dix jours après la demande (Search Console le 5 novembre, recherche de contrôle aujourd'hui). | Chacune ne contient que 200 mots, un résumé en cinq questions et le même gabarit que ses voisines. Google les juge trop minces. La page d'accueil des vidéos fait 69 mots. | Claude + vos textes |
| S3 | **Grands titres réduits à un mot.** | Le titre affiché en haut de page est « Facettes », « Bruxisme », « Le cabinet », « Mes expertises ». Celui de la page sur les taches blanches et la MIH est « Infiltration ICON », un nom de marque que les patients ne cherchent pas. Google lit ce titre comme le sujet de la page. | À trancher (maquette validée) |
| S4 | **16 titres et 13 descriptions trop longs**, coupés par Google. | Inchangé depuis l'audit du 25 octobre (accueil : 244 caractères de description pour 160 affichés). Liste en annexe B. | Vos validations |
| S5 | **L'accueil ne pèse presque rien** : 146 mots. | C'est la page qui reçoit le plus de liens, et celle qui en dit le moins. Un paragraphe de présentation et les grands sujets, sous les deux portes, suffiraient. | À trancher |
| S6 | **Pas un mot sur les prix** (décision D84). | Trois des recherches suivies portent sur le prix. Sans donner de montant, on peut expliquer ce qui fait le prix, ce que l'Assurance maladie ne rembourse pas, et que le devis est remis après le bilan. Cela reste dans votre règle et donne une réponse citable. | À trancher |
| S7 | **Pages peu reliées** : la vidéo Grossesse, l'article, la rubrique Articles, Médias et l'Espace patients ne reçoivent qu'un lien depuis les textes. | Déjà relevé le 25 octobre. | Claude |
| S8 | **Rien en anglais.** | « composite bonding in Paris » sortait en première page avant la refonte et a disparu. Une seule page en anglais suffirait à tenir ces recherches. | À trancher |

---

## 5. Les IA (GEO)

### 5.1 Ce que Google répond aujourd'hui

18 questions posées le 10 novembre : 17 questions de patients, et une sur votre nom. Google a affiché un
aperçu IA pour toutes.

| Question | Vous êtes cité ? | Qui apparaît |
|---|---|---|
| **dentiste tca paris** | **Oui, en premier, avec le lien vers votre site** : « Référence en France pour la prise en charge dentaire des patients atteints de TCA, praticien attaché à la CMME […] et président de l'association DenTCA » | Sana Oris, Cabinet Paris Monceau, centre expert de la CMME |
| **dentiste spécialiste de l'usure dentaire à Paris** | **Oui, en premier**, mais avec une erreur : « 2 rue Hippolyte Lebas (Centre de santé dentaire Flandre) » | Drs Schachmann et Aubé, Cabinet Paris Carnot |
| **meilleur dentiste pour un composite bonding à Paris** | **Oui, cinquième** : « Réputé pour l'esthétique du sourire et les restaurations en composite », note 4,9/5 | Dr Badaoui, Dr Gucciardi, Dr Trindade… |
| dentiste spécialisé usure dentaire paris | Non | non relevé |
| dentiste spécialiste des troubles alimentaires à Paris | Non | services hospitaliers, sans nom de praticien |
| quel dentiste consulter pour une érosion liée à l'anorexie ou à la boulimie | Non | Le Fil Dentaire, thèses de Lille et de Lyon, Colgate, Sana Oris |
| l'anorexie sans vomissements peut-elle abîmer les dents | Non (vous l'étiez les 21 et 22 octobre) | thèse de Lyon |
| usure dentaire : causes et traitement | Non | Cabinet dentaire D2L |
| anorexie dents · érosion dentaire · usure dentaire traitement | Non (3 questions) | non relevé |
| reconstruire des dents usées sans couronnes | Non | sites de cabinets, presse régionale |
| meilleur dentiste esthétique à Paris | Non | Drs Badaoui, Brahami, Zeitoun, Bellahsen, Varea, Kamioner, Ache |
| dentiste esthétique paris | Non | non relevé |
| facettes dentaires paris | Non | Dr Cohen-Samama, CRPCE, Elone Clinic, Dr Brahami |
| facettes ou composite comment choisir | Non | Dr Kamioner, CRPCE, Opal Dental Studio, sites turcs |
| taches blanches sur les dents : comment les enlever | Non | Qare, Kids Dental Paris, Elone Clinic, Colgate |
| **qui est le Dr Franck Moyal** | Oui, **avec deux adresses qui ne sont pas celle du site** (voir 5.2) | annuairedentaire.com, maquestionmedicale.fr, Instagram |

Quand l'aperçu ne nomme aucun praticien, la dernière colonne donne les premiers sites affichés sous la réponse.

**Trois citations sur dix-sept questions de patients.** Elles ont un point commun : ce sont des questions
« quel dentiste, à Paris, pour… » sur vos trois domaines propres. Sur les questions d'information (« qu'est-ce
que », « comment soigner », « que choisir »), vos pages ne servent encore jamais de source.

Onze de ces questions figuraient déjà dans le relevé d'octobre : Google vous y citait une fois le 21 et deux
fois le 22 ; aujourd'hui deux fois, sur d'autres questions. Les conditions ne sont pas identiques (octobre :
votre Chrome, connecté, à Paris). Il n'y a donc pas de progrès mesurable à ce stade. Mais la citation sur
« dentiste TCA Paris » reprend mot pour mot la nouvelle page TCA : **quand Google lit vos pages, il s'en sert.**

### 5.2 Le problème n° 1 : votre fiche d'identité sur le web

À « qui est le Dr Franck Moyal », l'IA de Google répond :

> « Lieux d'exercice : il consulte notamment au Centre de Santé Dentaire Flandre (83 rue de l'Ourcq, 75019
> Paris) et au Centre Médico-Dentaire Balard (61 rue Balard, 75015 Paris). »

Le 2 rue Hippolyte Lebas n'est pas cité. L'IA tire ces adresses de deux annuaires, annuairedentaire.com (qui
vous dit « omnipraticien », Paris 19e) et maquestionmedicale.fr (Paris 15e). Sur cette question, ces
annuaires sortent **avant** votre site, qui n'arrive qu'en sixième position. Sur la question de l'usure,
l'IA mélange les deux : « 2 rue Hippolyte Lebas (Centre de santé dentaire Flandre) ».

C'est le point le plus important de l'audit. Tout le travail du site vise à faire de vous une référence sur
trois sujets ; il perd de sa force si, sur votre nom, la machine décrit un autre praticien que celui du site.

Ces annuaires recopient en général le répertoire national des professionnels de santé (RPPS), que tient
l'Ordre. **Deux cas, selon ce qui est vrai :**

- **Vous n'exercez plus à Flandre ni à Balard** : la correction se fait à la source, par une déclaration de
  vos lieux d'exercice actuels auprès de l'Ordre ; puis une demande de mise à jour aux annuaires
  (annuairedentaire.com, maquestionmedicale.fr, lemedecin.fr). Le « lien Flandre » de votre fiche
  Google (D89) relève sans doute du même problème.
- **Vous y exercez encore** : alors le site doit le dire, sur la page Parcours, pour que les sources
  concordent.

Dans les deux cas, trois choses à aligner partout, au mot près : le nom du lieu (F7), l'adresse, le téléphone.
Sur « Dr Franck Moyal » tout court, la situation est saine : Doctolib d'abord, votre site ensuite, puis
l'AP-HP, Blendi et AO News.

### 5.3 Ce que le site fait déjà bien pour les IA

- **Le format questions/réponses** : une question de patient en titre, une réponse de deux phrases dessous,
  puis le détail. C'est le format que les IA découpent et citent.
- **Les pages Usure et TCA sont au niveau des meilleures sources françaises** : définition en une phrase,
  chiffres sourcés, listes, tableau, questions fréquentes, références, et un chapitre « Quel dentiste
  consulter » qui est précisément ce que Google a repris.
- **Les données cachées sont riches et justes** : praticien, lieu, horaires, domaines d'expertise, hôpitaux,
  DenTCA, profils (LinkedIn, Instagram, AP-HP, Doctolib, YouTube, Blendi, Le Fil Dentaire), références de
  chaque page.
- **Les robots des IA sont autorisés**, les pages sont du texte simple, lisible sans rien exécuter.
- **Les sources sont citées et vérifiables**, ce qui est le premier critère de confiance en santé.

### 5.4 Ce qui manque sur le site

| | Manque | Pourquoi cela compte pour les IA |
|---|---|---|
| G1 | **La page « Mon parcours » ne contient aucun fait vérifiable.** Pas de diplôme, pas d'université, pas d'année de thèse, pas de numéro RPPS, pas d'années d'exercice, pas de date d'arrivée à la Pitié (« 2012 » n'apparaît que sur l'Espace pro). L'université figure dans les données cachées (« Paris Diderot »), nulle part dans le texte. 576 mots, surtout des principes. | Une IA qui répond à « qui est… » cherche des faits datés qu'elle peut recouper avec l'annuaire santé, l'AP-HP ou LinkedIn. Faute de les trouver chez vous, elle prend ceux des annuaires (§ 5.2). C'est la page qui devrait faire autorité sur votre nom. |
| G2 | **Les titres de vos publications ne sont écrits nulle part.** « Front Wing Technique », le nom de votre technique, n'apparaît dans aucun texte du site. Idem pour « Cancers de la cavité buccale » et « La chirurgie orale ». Les thèses dirigées sont décrites par thème, sans titre, auteur, année ni lien. | En octobre, ChatGPT vous citait sur « Front Wing Technique » grâce au Fil Dentaire, pas grâce à votre site. Une liste propre (titre, coauteurs, revue, année, lien) est ce que les IA recopient le plus volontiers. |
| G3 | **Les conférences ne sont pas nommées.** « Intervention consacrée aux usures dentaires. AO News référence la soirée du 5 février 2026 à Marseille. » Ni titre, ni organisateur lisible, ni liste datée. Les Entretiens de Garancière et Alpha Omega ne sont cités que sur la page Usure. | Une liste « date · lieu · organisateur · titre » fait la preuve de l'expertise mieux que n'importe quelle phrase. |
| G4 | **Les pages vidéo n'ont pas le texte de la vidéo.** | Les IA ne regardent pas les vidéos : elles lisent le texte qui les accompagne. Le texte intégral transforme 45 secondes d'image en une page citable. |
| G5 | **Pas de page sur la grossesse**, alors que la vidéo existe et que le sujet est peu traité en français (reflux, nausées, hyperémèse et érosion). | Sujet de niche, concurrence faible, lien direct avec votre expertise : c'est le type de question où un site jeune peut être cité vite. Déjà prévu (audit du 25 octobre, point 10). |
| G6 | **Pas de page « sourire gingival »**, alors que la vidéo existe. | Même raisonnement. |
| G7 | **Pas de fichier `llms.txt`** (un sommaire du site écrit pour les IA). | Coût : une heure. Effet : non démontré à ce jour, aucun grand moteur ne s'est engagé à le lire. À faire parce que c'est gratuit, pas parce que c'est décisif. |
| G8 | **Phrases coupées et contradictions** (E1, F2, F3). | Les IA citent des passages isolés. Un passage amputé ou contredit par une autre page est un passage qu'elles écartent, ou qu'elles citent de travers. |

### 5.5 Ce qui manque hors du site

C'est ici que se joue l'essentiel. Les IA ne vous citent pas parce que votre site le dit, mais parce que
**d'autres sources le confirment**. Le relevé d'octobre montrait qui elles lisent : YouTube, Doctolib,
Instagram, puis les sites des cabinets concurrents, l'AP-HP, Le Fil Dentaire, Blendi, les thèses (DUMAS), AO
News, L'Information Dentaire.

| | Action | État |
|---|---|---|
| H1 | **Fiche d'identité** : Ordre / RPPS, annuaires, fiche Google, Doctolib (§ 5.2). | **À faire, priorité 1** |
| H2 | **Site de DenTCA.** Il est construit de telle façon que son contenu ne s'affiche qu'après l'exécution d'un programme, ce que la plupart des robots des IA ne font pas : ils n'y lisent que le titre, « Sensibilisation aux effets dentaires des TCA ». Pour eux, votre nom n'y figure pas. Aucun lien ne mène à votre site, et il n'a ni description ni fichier d'accueil des robots. Une recherche « DenTCA association » ne remonte rien. Or c'est votre meilleur atout sur les TCA : l'IA de Google le cite déjà d'après votre seule page. Il faut une page lisible : objet de l'association, président, bureau, actions, lien vers votre page TCA. | **À faire, priorité 1** |
| H3 | **La CMME / le GHU Paris.** L'IA cite le centre expert TCA de Sainte-Anne à côté de vous. Une ligne sur la page du centre (« consultation de dépistage bucco-dentaire, Dr Franck Moyal ») vaudrait plus que dix pages sur votre site. | À demander |
| H4 | **Les thèses que vous avez dirigées** (2025 et 2026 sur les TCA) : déposées sur DUMAS, avec votre nom comme directeur ? Les thèses sont la source la plus citée sur ces questions. | À vérifier |
| H5 | **La FFAB** (Fédération française anorexie boulimie) : annuaire des professionnels et pages d'information. Les IA y renvoient les patients. | À demander |
| H6 | **Un article signé dans une revue lue par les IA** sur TCA et dents ou sur les usures : L'Information Dentaire, Le Fil Dentaire, Clinic, AO News. Votre seul article indexé date de 2023 et porte sur le composite. | À écrire |
| H7 | **YouTube** : six Shorts publiés le 26 octobre. C'est la première source des IA. Prochaine marche : des vidéos de 3 à 5 minutes, format classique, avec le texte en description, sur « érosion dentaire », « dents usées », « TCA et dents ». | En cours |
| H8 | **Liens depuis vos propres présences** : Smile Club Formations renvoie bien vers le site. Vérifier Doctolib (champ « site web »), Blendi, Eugenol, ARTEMIS, LinkedIn, Instagram. | À vérifier |

---

## 6. Plan d'action

### A. Ce que Claude peut faire seul, sans toucher au sens des textes

| | Action | Réf. |
|---|---|---|
| A1 | Recoller les 22 phrases coupées à leurs listes, rétablir le début de phrase amputé | E1, E2 |
| A2 | Refaire les blocs « Sources scientifiques » des 10 pages sur le modèle des pages Usure et TCA | E4 |
| A3 | Afficher les titres des publications, déjà présents dans les données cachées | E3, G2 |
| A4 | Unifier « DenTCA » et « Smile Club Formations » | F6 |
| A5 | Supprimer le bloc en double de la page Parcours ; déclarer les dimensions des images | E6, E7 |
| A6 | Rééquilibrer les cartes « Avant / après » | E5 |
| A7 | Relier davantage la vidéo Grossesse, l'article, Médias | S7 |
| A8 | Ajouter le fichier `llms.txt` | G7 |

Chaque correction vous sera montrée avant publication, comme d'habitude.

### B. Ce qui demande votre décision ou vos textes

| | Décision | Réf. |
|---|---|---|
| B1 | Votre titre exact à la Pitié-Salpêtrière | F1 |
| B2 | Le nom du lieu d'exercice, et vos lieux actuels | F7, § 5.2 |
| B3 | Les faits de la page Parcours : diplôme, université, année, RPPS, dates, formations suivies | G1 |
| B4 | La liste datée de vos conférences et des thèses dirigées | G2, G3 |
| B5 | Le texte intégral des six vidéos (je peux le transcrire, vous le relisez) | S2, G4 |
| B6 | Les corrections de fond : durée du composite, brossage, émail, règle des 18 ans, résine | F2 à F5, F10 |
| B7 | Les trois points de déontologie, et l'adresse de courriel | D1 à D3 |
| B8 | Les grands titres de page, l'accueil, les titres et descriptions trop longs | S3 à S5 |
| B9 | Une page Grossesse, une page Sourire gingival, une page en anglais, un mot sur ce qui fait le prix | G5, G6, S6, S8 |

### C. Hors du site

Dans l'ordre : fiche d'identité (H1), site de DenTCA (H2), CMME (H3), thèses (H4), FFAB (H5), article (H6),
vidéos longues (H7), liens (H8).

### Mesurer

Refaire ce même relevé de 18 questions dans un mois : il prend dix minutes et n'utilise pas votre Chrome. Le
relevé quotidien des positions continue.

---

## Annexe A — Défauts de mise en page, par page

| Page | Phrases coupées | Bloc de sources à refaire |
|---|---|---|
| Activité hospitalière | 4 | |
| Médias et interviews | 4 | |
| Publications | 4 | |
| Anorexie restrictive | 2 | oui |
| Bruxisme | 2 | oui |
| Conférences et formations | 2 | |
| Facettes ou composite | 2 | |
| Bilan esthétique | 1 | oui |
| Dents courtes ou usées | 1 | oui |
| Érosion dentaire | un début de phrase amputé | oui |
| Éclaircissement | | oui |
| Facettes | | oui |
| Composite bonding | | oui |
| Infiltration ICON | | oui |
| Cas clinique Usures | | oui |
| Mon parcours | un bloc en double | |

## Annexe B — Titres et descriptions trop longs

Titres de plus de 60 caractères (16) : accueil (63) · Anorexie restrictive (64) · article « Jeunes
chirurgiens-dentistes » (110) · les 4 cas cliniques (73 à 84) · Composite bonding (70) · Dentisterie
esthétique (71) · Éclaircissement (73) · Érosion (69) · Espace patients (66) · Espace pro (80) · vidéos
Composite (61), Grossesse (68), Première consultation (73).

Descriptions de plus de 160 caractères (13) : accueil (244) · cas clinique Usures (195) · Conférences (170) ·
Contact (191) · Espace patients (165) · Espace pro (174) · Mon parcours (189) · les 6 vidéos (176 à 206).

## Annexe C — Liens reçus depuis les textes des autres pages

Un seul lien : article « Jeunes chirurgiens-dentistes », rubrique Articles, Espace patients, Médias, vidéo
Grossesse. Deux liens : Le cabinet, Espace pro, Publications. Les mieux reliées : accueil (35), Contact (25),
Composite et Parcours (19), Usure (18), Dentisterie esthétique (17), Érosion (16), Facettes (15), TCA (12).
