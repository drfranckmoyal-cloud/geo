# POINT 3.5 — cas clinique « usures antérieures et facettes minimalement invasives » : en ligne

*Claude Code, 25 septembre 2026. Cahier des charges archivé dans
`docs/echanges/2026-09-25-chatgpt-point-3-5-cas-usure.md` ; texte de la page dans
`docs/pages-suivantes/v1.7/25_cas-usures-facettes-minimalement-invasives_V1_7.md`.
Contrôles faits **en production**.*

---

## A — URL définitive

**https://drfranckmoyal.fr/cas-cliniques/usures-dentaires-facettes-minimalement-invasives/**

| | |
|---|---|
| HTTP | `200` |
| Indexable | oui, aucune balise `robots` |
| Canonical | auto-référente |
| Sitemap | oui — le site compte **27 pages indexables** |
| H1 | Usures dentaires : du diagnostic aux facettes minimalement invasives (unique) |
| Title | Usures dentaires et facettes minimalement invasives \| Cas clinique — Dr Franck Moyal |
| Meta | celle du cahier des charges, mot pour mot |
| Fil d’Ariane | Accueil > Usures dentaires > Facettes minimalement invasives |
| Structure | 16 H2, 3 H3, 12 photographies, 6 questions de FAQ, 5 références |
| Aucune page concurrente | aucune autre URL sur ce patient ; rien sous `/blog/` ni `/actualites/` |

---

## B — Texte final publié

Seize sections, dans cet ordre : une demande initialement esthétique ; des usures importantes à
l’examen ; comprendre avant de restaurer ; **une habitude ancienne retrouvée à l’interrogatoire** ;
pourquoi rechercher la cause d’une usure (encadré) ; pourquoi ne pas simplement poser des
couronnes ; étape 1, la planification esthétique numérique ; étape 2, l’augmentation de la
dimension verticale ; étape 3, les facettes minimalement invasives au maxillaire ; à la mandibule,
le composite injecté ; le résultat ; les vues finales ; ce que ce cas permet de comprendre (trois
enseignements) ; la FAQ ; les sources ; l’appel final.

La réponse directe placée sous l’ouverture est **celle du §8, mot pour mot**. Le texte des sections
reprend l’article de Franck **sans réécriture** ; les formulations imposées par le cahier des
charges (§11, §13, §16, §17) sont reprises telles quelles.

Le fil éditorial demandé est respecté : demande → observation → anamnèse → compréhension des
lésions → projet → traitement conservateur → résultat. Le cas n’est jamais présenté comme un
avant/après.

---

## C — Sources photographiques utilisées

**Les douze photographies viennent du document de Franck lui-même**
(`Cas_clinique_usure_3Step_Page_GEO_site_V2_facettes_minimalement_invasives.docx`), où chacune est
accompagnée de sa légende. C’est cette correspondance écrite qui les rattache au cas — **aucune
identification visuelle, aucune photographie « qui ressemble »** (§18).

Deux d’entre elles — la vue intra-orale initiale et la vue intra-orale finale — sont **les mêmes
fichiers que ceux déjà publiés** sur la page Réhabilitation (`rehabilitation-usure-avant` et
`-apres`) : vérifié par comparaison des images elles-mêmes, pas à l’œil. C’est donc bien le même
patient, et le registre réutilise ces deux fichiers sans les recopier. Dix photographies nouvelles
ont été préparées (`npm run photos-usure`) : largeur maximale 2000 px, JPEG qualité 84 sans
sous-échantillonnage, **aucune retouche**, métadonnées supprimées, 1,7 Mo au total.

Le mini-cas de la page Réhabilitation est conservé (§28).

---

## D — Informations récupérées de l’article de Franck

L’article n’existait pas dans le dépôt : il a été lu depuis le document. Aucune URL antérieure sur
ce cas (vérifié dans le plan du site). En sont repris :

- la demande et le profil : patient de **72 ans** (l'article écrivait 64 ; Franck a corrigé le 25/09/2026), sourire jugé usé, abîmé, vieilli ;
- la perte de substance des dents antérieures, maxillaires et mandibulaires ;
- l’habitude ancienne d’interposition d’un morceau de sucre entre les incisives ;
- le caractère multifactoriel de l’usure et la composante érosive associée ;
- l’approche 3-Step et ses cinq références ;
- la planification numérique SmileCloud pour ce patient ;
- l’augmentation additive de la dimension verticale par les secteurs postérieurs ;
- les facettes céramiques minimalement invasives de type TACO au maxillaire ;
- le composite injecté à la mandibule et la gouttière de transfert ;
- les six questions fréquentes et les douze légendes de photographies.

---

## E — Informations volontairement exclues faute de validation

- **le nombre de facettes** : nulle part dans l’article ni dans le cahier des charges ;
- **le laboratoire** de ce cas : non nommé (celui du cas A ne s’applique pas) ;
- l’épaisseur des restaurations, le protocole de préparation, le protocole de collage ;
- la durée du traitement, le nombre de rendez-vous ;
- la chronologie précise de l’habitude et sa durée exacte ;
- toute pathologie médicale, tout diagnostic psychologique ou comportemental ;
- **le bruxisme, le reflux, l’alimentation acide** : jamais écrits ;
- l’année du traitement : inconnue, donc absente.

---

## F — Maillage entrant

Trois liens, vérifiés en production :

| Page source | Forme | Ancre |
|---|---|---|
| `/usures-dentaires/`, section Diagnostic | `ClinicalCaseSummary` — « Comprendre l’origine avant de restaurer » | Découvrir le cas clinique |
| `/facettes-dentaires-paris/`, section « Faut-il beaucoup tailler les dents pour poser des facettes ? » | `ClinicalCaseSummary` — « Facettes et préservation tissulaire » | Voir ce cas d’usures traité par facettes minimalement invasives |
| `/dentisterie-esthetique-paris/`, section « Et si les dents sont usées ? » | lien contextuel | Un cas d’usures : du diagnostic aux facettes minimalement invasives |

Les deux annonces ont des textes différents, comme demandé (§22). **Aucun lien depuis
`/facettes-ou-composite/`** : le §24 le laisse optionnel et la page est déjà dense.

---

## G — Maillage sortant

Usures dentaires (dans la section sur l’examen), Facettes dentaires et Facettes ou composite (dans
la section sur l’approche minimalement invasive), Réhabilitation des dents usées (pages liées),
Dr Franck Moyal (bloc auteur), prise de rendez-vous. Les liens sont posés **dans le raisonnement**,
pas en bloc de fin de page.

---

## H — Schema

`WebSite` → `MedicalWebPage` (`…#page`) → `BreadcrumbList` (`…#fil`), plus `Person`
(`/#franck-moyal`), `Dentist` (`/#practice`) et `FAQPage` (la page a une FAQ visible, conformément
à la règle posée hier pour tout le site).

`datePublished` = `2026-09-25`, `dateModified` = `2026-09-25` — dates réelles de publication de la
page, jamais l’âge du patient ni une date de traitement. **Aucun nouvel identifiant** : ni second
Franck Moyal, ni type inventé.

---

## I — Responsive et performance

| Largeur | Photographies | Débordement |
|---|---|---|
| 320 px | 280 px, empilées | 0 |
| 375 px | 335 px | 0 |
| 390 px | 350 px | 0 |
| 430 px | 389 px | 0 |
| 768 px | 345 px en paire, 704 px seule | 0 |
| 1440 px | 602 px en paire, 704 px seule | 0 |

Les douze photographies se chargent à toutes les largeurs. Lighthouse mobile en production :
**100 / 100 / 100 / 100**, LCP 1,8 s, CLS 0, TBT 0 ms, 403 Ko au chargement. Les douze
photographies pèsent **867 Ko** une fois la page entièrement lue : chargement différé, trois
largeurs par image, WebP, dimensions posées, aucun fichier dupliqué.

---

## J — Contrôle factuel (§37 et §38)

Vérifié automatiquement sur la page fabriquée :

| Contrôle | Résultat |
|---|---|
| Âge | « 72 ans », et aucun autre — vérifié automatiquement, sur cette page comme sur tout le site |
| Nombre de facettes | **jamais chiffré** |
| Matériau | « céramique » et « composite injecté » ; type TACO ; rien d’autre |
| Laboratoire | aucun nommé |
| SmileCloud | présent, **documenté pour ce patient** par l’article |
| « no-prep », « sans préparation », « aucune perte de substance », « totalement réversible » | absents |
| « garanti », « spectaculaire », « parfait », « incroyable » | absents |
| Bruxisme, reflux, alimentation acide | absents |
| Sucre | 2 occurrences, toutes deux liées à **ce** patient : « pendant plusieurs années, il intercalait régulièrement un morceau de sucre entre ses incisives. Cette répétition a **probablement participé** à l’abrasion très localisée observée » |
| Généralisation interdite | la page n’affirme nulle part que le sucre provoque l’usure : elle rappelle au contraire que l’usure est multifactorielle |

Les cinq références ont été **vérifiées sur PubMed** ; les deux PMID manquants dans l’article ont
été retrouvés (33751006 et 33871489) à partir des DOI.

---

## K — Divergences entre l’article et le cahier des charges

| Élément | Cahier des charges | Article de Franck | Décision |
|---|---|---|---|
| Âge du patient | 64 ans | 64 ans | **72 ans** — correction de Franck du 25/09/2026, appliquée sur la page, dans le texte de remplacement de la première photographie, dans la copie éditoriale de l'article et dans les contrôles automatiques |
| Dimension verticale | « ne pas inventer une modification de dimension verticale » | documentée, et centrale | **Publiée** — Franck l’a validée le 25/09 ; sans elle, la page ne peut pas expliquer pourquoi les facettes ont pu rester minimalement invasives |
| Approche 3-Step + 5 références | absente | documentée | Publiée |
| Composite injecté à la mandibule | absent | documenté | Publié |
| Facettes de type TACO | « ne pas inventer le matériau » | documenté | Publié |
| SmileCloud | « ne pas écrire SmileCloud sans donnée validée pour ce patient » | documenté pour ce patient | Publié |
| Composante érosive | « ne pas inventer une étiologie supplémentaire » | documentée | Publiée, avec la formulation prudente de l’article |
| Étendue de l’usure | « secteur antérieur » | antérieur **maxillaire et mandibulaire** | Formulation de l’article |
| « carreau de sucre » / « morceau de sucre » | carreau | morceau | « carreau » dans la réponse directe (texte imposé), « morceau » dans le corps (texte de Franck) |
| H1, title, meta, URL | fournis | l’article en proposait d’autres | **Ceux du cahier des charges**, comme demandé |
| Chapeau | non fourni | non fourni | écrit par Claude |
| Titres « À la mandibule : composite injecté » et « Les vues finales » | non prévus | non titrés | écrits par Claude pour porter deux séries de photographies |
| Citation « dont les résultats à six ans ont été documentés [4,5] » | — | références listées sans phrase d’appel | demi-phrase ajoutée par Claude pour citer les deux études dans le texte |

**Tout ce qui précède a été soumis à Franck avant publication ; il a répondu « tout ton article »
et a validé les douze photographies, sourires compris.**

---

## Faut-il désormais créer `/cas-cliniques/` ?

**Oui, et c’est maintenant qu’il faut le faire — mais je ne l’ai pas créée** (§27, §42).

Quatre raisons, à partir de l’état réel du site :

1. **Les quatre cas démontrent quatre raisonnements différents** — planification puis orthodontie,
   planification d’une réhabilitation étendue, réduction du contraste avant infiltration, diagnostic
   d’usure avant restauration. Ce n’est pas une galerie : c’est un corpus.
2. **Découvrabilité** : aujourd’hui, chaque cas n’est atteignable que depuis une page thérapeutique.
   Un patient arrivé par Google sur un cas ne peut pas en voir un autre. Il n’existe aucune page qui
   réponde à « quels cas ce praticien a-t-il documentés ? ».
3. **`/cas-cliniques/` répond `403`** : le dossier existe sans page d’accueil. Une page d’index
   supprimerait cette anomalie au passage.
4. **GEO** : une page qui regroupe les quatre raisonnements donne aux moteurs génératifs une entrée
   unique reliant Franck Moyal à sa pratique documentée — ce qu’aucune page thérapeutique ne fait.

Réserve honnête : quatre cas, c’est le minimum pour qu’un index ne paraisse pas vide. Une page sobre
— une introduction, quatre entrées avec problématique, approche et lien — suffirait. **Pas d’entrée
de menu pour autant** : le menu compte déjà neuf entrées, et les cas restent d’abord des preuves
rencontrées au fil des pages de traitement.

---

**POINT 3.5 VALIDABLE : OUI.**

*Conformément au §42 : **STOP**. Pas de page `/cas-cliniques/`, pas de modification du menu, aucun
cinquième cas, aucun second article sur ce patient, les trois premiers cas intacts, POINT 4 non
commencé.*
