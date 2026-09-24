# POINT 3 — preuve clinique — PHASE A : audit et proposition

*Claude Code, 24 septembre 2026. Cahier des charges archivé dans
`docs/echanges/2026-09-24-chatgpt-point-3-preuve-clinique.md`.
**Rien n'a été créé, rien n'a été déplacé, rien n'a été déployé** : cette phase est un état des
lieux et une proposition, conformément au §42.*

---

## 0. Méthode et limite posée d'emblée

Tout ce qui suit sur le contenu clinique des cas vient **de la documentation de Franck** : sa fiche
de renseignements en ligne (base `infos/franck`, remplie le 22/09/2026) et les noms de dossiers de
`~/Desktop/icono GEO`. **Je n'ai rien déduit d'une photographie** : ni diagnostic, ni cause, ni
matériau, ni indication (§44). Quand la documentation s'arrête, je l'écris, et je pose une question
précise plutôt que de combler.

C'est le point important de cette phase : **le site possède de bonnes photographies, mais très peu
de texte clinique**. La documentation dit presque toujours *ce que l'on voit*, rarement *pourquoi
ce traitement a été retenu*. Or c'est exactement ce que le POINT 3 demande de montrer.

---

## 1. Audit de la production (§3) — ce qui est en ligne aujourd'hui

15 emplacements, 13 cas distincts, 22 photographies, sur 10 pages (deux cas sont affichés à deux
endroits). Correspondance complète `CASE_ID → fichiers source → page → légende → étiquettes` :

| CASE_ID | Fichiers source (`~/Desktop/icono GEO`) | Page(s) en production | Composant | Légende affichée | Étiquettes |
|---|---|---|---|---|---|
| `composite-six-dents` | `Composite bonding/1.png` | `/composite-bonding-paris/` et `/` (accueil) | ClinicalImage | Reconstruction esthétique additive de six dents antérieures en composite : avant, puis après. | — (montage avant/après dans une seule image) |
| `composite-quatre-dents` | `Composite bonding/2.png` | `/composite-bonding-paris/` | ClinicalImage | Reconstruction esthétique additive de quatre dents antérieures en composite : avant, puis après. | — (montage) |
| `composite-stratifie` | `Composite bonding/3.jpg` | `/composite-bonding-paris/` | ClinicalImage | Composite stratifié sur une dent antérieure présentant une dyschromie : avant, puis après. | — (montage) |
| `facettes-planification` | `Facettes /1.png`, `2.png`, `3.png` | `/facettes-dentaires-paris/` | ClinicalSequence | Exemple de planification d'un traitement par facettes : situation initiale, projet esthétique et résultat clinique. | Situation initiale / Projet / Résultat |
| `facettes-ceramique` | `Facettes /facettes cas 2 /avant.JPG`, `apres.jpg` | `/facettes-dentaires-paris/` | ClinicalBeforeAfter | Exemple clinique d'un traitement par facettes en céramique. | Avant / Après |
| `eclaircissement-ambulatoire` | `Eclaircissement/1.jpg`, `2.jpg` | `/eclaircissement-dentaire-paris/` et `/dentisterie-esthetique-paris/` | ClinicalBeforeAfter | Évolution de la teinte après 4 semaines d'éclaircissement ambulatoire. | Avant / Après 4 semaines |
| `mih-erosion-infiltration` | `Icon/1.jpg`, `1bis.jpg` | `/taches-dentaires-dyschromies-icon/` | ClinicalBeforeAfter | Tache de MIH sur une incisive — prise en charge associant éclaircissement et érosion-infiltration. | Avant / Après |
| `dyschromie-erosion-infiltration` | `Icon/2.jpg`, `2bis.jpg` | `/taches-dentaires-dyschromies-icon/` | ClinicalBeforeAfter | Dyschromie unitaire associée à une tache blanche — prise en charge par éclaircissement puis érosion-infiltration. | Avant / Après |
| `erosion-exogene` | `Erosion /1.JPG` | `/erosion-dentaire/` | ClinicalImage | Exemple d'usure dentaire érosive associée à une exposition acide exogène. | — |
| `erosion-raccourcissement` | `Erosion /2.jpg` | `/erosion-dentaire/` | ClinicalImage | Usure dentaire érosive avec raccourcissement des dents. | — |
| `bilan-esthetique` | `Bilan esthetique /initial .jpg`, `Projet.png`, `final .jpg` | `/bilan-esthetique-personnalise/` | ClinicalSequence | De la situation initiale au projet esthétique puis au résultat clinique. | Situation initiale / Projet / Résultat |
| `usure-reconstruction` | `Usures /cas 1.jpg` | `/usures-dentaires/` | ClinicalImage | Dents antérieures usées, avant et après reconstruction. | — (montage) |
| `rehabilitation-usure` | `Usures /cas 2 /avant .jpg`, `après.jpg` | `/rehabilitation-dents-usees/` | ClinicalBeforeAfter | Dents usées avant et après reconstruction. | Avant / Après |

Les textes de remplacement (`alt`) sont descriptifs et sans bourrage : « Six dents antérieures
avant, puis après reconstruction additive en composite », « Tache blanche de MIH visible sur une
incisive avant traitement », etc. Chaque cas porte une fois « Cas clinique — Dr Franck Moyal ».
Les mentions Avant / Après / Situation initiale / Projet / Résultat sont **du texte HTML**, jamais
incrustées dans l'image.

### Réponse à la question du §13 : Facettes 1 et Bilan esthétique sont-ils le même cas ?

**Non. Ce sont deux patients différents.** Je les ai comparés image par image : cadrage, visage,
situation initiale et résultat n'ont rien de commun — l'un est une vue intra-orale rapprochée,
l'autre un sourire complet. **Aucun risque de duplication éditoriale** entre ces deux séquences.

Un fait visible, que je signale sans l'interpréter : sur l'image « Projet » du cas Facettes 1, un
**appareil orthodontique multi-attaches est visible en bouche**. Cela change la façon de raconter
le cas, et c'est l'objet d'une question ci-dessous.

---

## 2. Tableau 1 — inventaire et classement (§7)

Rappel des niveaux : **A** = raisonnement complet possible (page dédiée envisageable) ;
**B** = mini-cas (situation, traitement, résultat) à garder dans la page thérapeutique ;
**C** = illustration clinique, données insuffisantes.

| Case ID | Thème | Photos | Données cliniques disponibles | Niveau | Justification |
|---|---|---|---|---|---|
| `facettes-planification` | Facettes, planification | 3 (initial, projet, résultat) | Séquence documentée par Franck : initial → projet → final. Ni le nombre de dents, ni le matériau, ni la préparation, ni le rôle de l'orthodontie visible sur l'image « Projet » | **A conditionnel** | C'est la meilleure démonstration du raisonnement du site : le projet précède le traitement. Mais en l'état, je ne pourrais écrire que des légendes — pas une analyse. 4 réponses suffisent à le faire passer en A. |
| `bilan-esthetique` | Bilan, planification | 3 (initial, projet, résultat) | « Légendes dans le dossier » : initial, projet, final. Aucun traitement documenté | **A conditionnel** | Même valeur démonstrative, sur un cas plus global. Il manque le cœur : ce qui a été réalisé entre le projet et le résultat. |
| `mih-erosion-infiltration` | Taches, MIH | 2 (avant, après) | **Le mieux documenté** : tache de MIH sur une incisive, prise en charge par éclaircissement **puis** érosion-infiltration | **A conditionnel** | Un enchaînement thérapeutique documenté, une séquence en deux temps, un vrai « pourquoi pas seulement masquer la tache ». Il manque l'âge au traitement (le site affirme qu'on n'éclaircit pas avant 18 ans) et le nombre de séances. |
| `rehabilitation-usure` | Usures, réhabilitation | 2 (avant, après) | Avant / après d'une reconstruction. Ni cause de l'usure, ni matériau, ni étendue, ni fonction | **B, A possible** | L'axe le plus différenciant du site (§19). Mais quatre informations manquent, dont le matériau : sans elles, une page serait une coquille. |
| `composite-six-dents` | Composite | 1 (montage avant/après) | Composite additif sur six dents antérieures | **B** | Situation, traitement et résultat sont clairs ; la réflexion ne l'est pas. Très bien là où il est. |
| `composite-quatre-dents` | Composite | 1 (montage) | Composite additif sur quatre dents antérieures | **B** | Idem, et trop proche du précédent pour justifier une seconde page (§14). |
| `composite-stratifie` | Composite, dyschromie | 1 (montage) | Composite stratifié sur une dent dyschromiée | **B** | Correction ciblée, lisible. Deviendrait A si la demande initiale et la raison du choix étaient documentées. |
| `facettes-ceramique` | Facettes | 2 (avant, après) | Second cas de facettes, avant / après | **B** | Aucune donnée sur le projet, le nombre de dents ni la préparation. |
| `eclaircissement-ambulatoire` | Éclaircissement | 2 (avant, après 4 semaines) | Éclaircissement ambulatoire, résultat à 4 semaines | **B** | Exactement ce que le §15 décrit : un mini-cas utile, pas une page. |
| `dyschromie-erosion-infiltration` | Taches, dyschromie | 2 (avant, après) | Dyschromie unitaire et tache blanche, éclaircissement puis érosion-infiltration | **B** | Même protocole que le cas MIH : deux pages presque identiques seraient un doublon (§17). À garder en mini-cas, ou à citer dans la page du cas MIH. |
| `usure-reconstruction` | Usures | 1 (montage) | « Légendes dans le dossier » : dents usées, avant et après reconstruction | **B faible** | Traitement non documenté. |
| `erosion-exogene` | Érosion | 1 | Érosion d'origine exogène | **C** | Photographie diagnostique, aucun traitement. Ne doit pas devenir un faux avant/après (§18). |
| `erosion-raccourcissement` | Érosion | 1 | Usure érosive avec raccourcissement. Contexte de TCA **non publiable** (§34) | **C** | Photographie diagnostique. Le contexte documenté ne sera jamais rattaché publiquement à cette image. |

**Bilan : 0 cas de niveau A aujourd'hui. 3 le deviennent avec des réponses courtes de Franck, 1 de
plus (usures) si les informations existent.**

---

## 3. Tableau 2 — pages proposées, si et seulement si les réponses arrivent (§7)

| Cas | URL proposée | H1 proposé | Intention | Page source (lien entrant) | Liens sortants prévus |
|---|---|---|---|---|---|
| `facettes-planification` | `/cas-cliniques/planification-facettes-ceramique/` | Planification et réalisation d'un traitement par facettes en céramique | Exemple clinique : montrer que le traitement final est précédé d'un projet | `/facettes-dentaires-paris/` (section « Smile design et simulation ») | Facettes, page pilier, Facettes ou composite, prise de rendez-vous |
| `mih-erosion-infiltration` | `/cas-cliniques/tache-mih-eclaircissement-infiltration/` | Correction d'une tache de MIH par éclaircissement et érosion-infiltration | Exemple clinique : un enchaînement thérapeutique, pas un masquage | `/taches-dentaires-dyschromies-icon/` (section MIH) | Taches et ICON, Éclaircissement, page pilier, rendez-vous |
| `bilan-esthetique` | `/cas-cliniques/du-projet-esthetique-au-resultat/` | D'un projet esthétique à sa réalisation | Exemple clinique : analyse, projet, réalisation | `/bilan-esthetique-personnalise/` | Bilan esthétique, page pilier, Facettes ou composite, rendez-vous |
| `rehabilitation-usure` *(si données)* | `/cas-cliniques/reconstruction-de-dents-anterieures-usees/` | Reconstruction de dents antérieures usées par approche additive | Exemple clinique sur l'axe usures | `/rehabilitation-dents-usees/` | Réhabilitation, Usures, page pilier, rendez-vous |

Les titres sont descriptifs, sans superlatif ; ils ne seront retenus que si les données les
justifient précisément (§29). **Aucune de ces URL n'est créée.**

---

## 4. Tableau 3 — données manquantes et questions précises à Franck (§43)

Une ligne = une information réellement nécessaire.

| Cas | Information manquante | Bloquante ? | Question précise |
|---|---|---|---|
| Facettes 1 | Nombre de dents traitées | **Oui** | Combien de dents ont reçu une facette dans ce cas ? |
| Facettes 1 | Rôle de l'orthodontie | **Oui** | Un appareil orthodontique est visible sur la photographie « Projet » : l'orthodontie faisait-elle partie du plan de traitement, et a-t-elle précédé les facettes ? |
| Facettes 1 | Nature du projet | Oui | Le « projet » est-il une simulation numérique, un wax-up, un mock-up en bouche, ou plusieurs de ces étapes ? |
| Facettes 1 | Préparation | Non | Les dents ont-elles été préparées, et si oui de façon limitée à l'émail ? |
| Facettes 1 | Demande initiale | Non | Qu'est-ce que le patient souhaitait changer en venant ? |
| Bilan esthétique | Traitement réalisé | **Oui** | Entre le projet et la photographie finale, qu'est-ce qui a été réalisé : éclaircissement, composites, facettes, ou une association ? |
| Bilan esthétique | Étendue | **Oui** | Combien de dents ont été traitées, et sur une seule arcade ou les deux ? |
| Bilan esthétique | Nature du projet | Oui | Le projet montré est-il une simulation numérique validée avec le patient avant de commencer ? |
| MIH | Âge au traitement | **Oui** | Quel âge avait le patient lors de l'éclaircissement ? (le site écrit qu'on n'éclaircit pas avant 18 ans : il faut pouvoir être cohérent) |
| MIH | Séquence | **Oui** | L'éclaircissement et l'érosion-infiltration faisaient-ils partie du même plan de traitement, et combien de temps les sépare ? |
| MIH | Nombre de dents | Non | L'infiltration a-t-elle concerné une seule incisive ? |
| MIH | Pourquoi ce choix | Non | Pourquoi l'infiltration plutôt qu'un composite ou une facette dans cette situation ? |
| Usures cas 2 | Matériau | **Oui** | Avec quoi les dents ont-elles été reconstruites : composite direct, composite indirect, céramique ? |
| Usures cas 2 | Étendue | **Oui** | Combien de dents ont été reconstruites, et sur quelle(s) arcade(s) ? |
| Usures cas 2 | Origine de l'usure | Oui | L'usure était-elle attribuée à une cause identifiée, et laquelle peut être écrite publiquement ? |
| Usures cas 2 | Dimension verticale | Non | La reconstruction a-t-elle nécessité de modifier la dimension verticale ? |
| Usures cas 1 | Traitement | **Oui** | Ce cas a-t-il été traité, et si oui avec quoi ? Sinon, il reste une illustration. |
| Composite 1 et 2 | Ce qui différencie les deux cas | Non | Ces deux cas correspondent-ils à des demandes différentes (par exemple usure vs forme) ? Sinon, un seul suffira le jour venu. |
| Composite 3 | Origine de la dyschromie | Non | La dyschromie de cette dent avait-elle une origine documentée (traumatisme, dent dépulpée, autre) ? |
| Tous les cas retenus | Consentement du canal | **Oui** | Les consentements recueillis couvrent-ils la publication d'un cas commenté sur le site, et non seulement la photographie ? |
| Tous les cas retenus | Date | Non | Connais-tu l'année de réalisation de chaque cas ? (sinon aucune date ne sera inventée) |

---

## 5. Recommandation d'architecture

1. **Pages de cas à créer aujourd'hui : aucune.** Aucun cas n'atteint le niveau A en l'état. Créer
   une page maintenant reviendrait à écrire une histoire clinique à partir d'une photographie :
   c'est précisément ce que le §9 et le §44 interdisent.
2. **Dès que Franck répond aux questions bloquantes : deux pages, puis une troisième.** Dans cet
   ordre de valeur — le cas **MIH** (le mieux documenté, pédagogiquement le plus fort), puis
   **Facettes 1** (la démonstration de la planification), puis **Bilan esthétique**. Le cas
   **Usures 2** rejoindrait la liste s'il est documenté : c'est l'axe le plus différenciant du site.
3. **Mini-cas : ne rien bouger.** Les huit cas de niveau B restent exactement où ils sont, dans les
   pages thérapeutiques. Ils y jouent déjà leur rôle, et les sortir appauvrirait ces pages.
4. **Illustrations : ne rien bouger non plus.** Les deux photographies d'érosion restent des
   illustrations diagnostiques dans la page Érosion. Le contexte de TCA du second cas ne sera pas
   publié.
5. **Page `/cas-cliniques/` : pas maintenant.** Le §39 est clair : avec 0 à 2 cas de niveau A, pas
   d'index. À reproposer quand trois cas complets existeront.
6. **Entrée « Cas cliniques » dans le menu : pas maintenant** (§41). Le menu compte déjà neuf
   entrées ; une rubrique qui mènerait à deux pages ferait une promesse que le site ne tient pas
   encore. Les cas seront d'abord atteignables depuis leur page thérapeutique.
7. **Quand les pages existeront**, elles réutiliseront les photographies déjà préparées
   (`src/assets/photos/cas/`) et les composants existants — aucune duplication de fichier, aucune
   nouvelle version d'image (§23, §37). Le registre `src/content/cas-cliniques.ts` a été écrit pour
   cela : un cas peut recevoir demande, diagnostic, options, traitement et suivi sans toucher aux
   pages qui l'affichent déjà.
8. **Un composant à prévoir** le moment venu : `ClinicalCaseSummary` (problématique, approche,
   traitement, lien vers le cas), sobre, pour annoncer un cas depuis sa page thérapeutique.

---

## 6. Ce que cette phase dit du fond

La question n'est pas « quelles photographies publier ». Elle est : **de quels cas Franck peut-il
raconter le raisonnement ?** Aujourd'hui, la documentation permet de dire ce qu'on voit, pas
pourquoi il a été décidé ainsi. Les **21 questions** du tableau 3 sont l'exact travail à faire
faire à Franck : une demi-heure de réponses transforme trois séries de photographies en trois
vraies preuves cliniques.

Deux d'entre elles ne sont pas des questions de confort : l'âge du patient MIH lors de
l'éclaircissement (le site affirme qu'on n'éclaircit pas avant 18 ans) et l'étendue du consentement
(publier un cas commenté n'est pas publier une photographie).

---

*Conformément au §42 et au §46 : **STOP**. Aucune page créée, aucune photographie déplacée, rien
déployé. La phase B attend la validation de ChatGPT et les réponses de Franck.*
