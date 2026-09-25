# POINT 3 — phase B : trois preuves cliniques en ligne

*Claude Code, 25 septembre 2026 (travail du 24 au 25). Cahier des charges archivé dans
`docs/echanges/2026-09-24-chatgpt-point-3-phase-b.md` ; textes des pages dans
`docs/pages-suivantes/v1.6/`. Tous les contrôles ci-dessous sont faits **sur le site en ligne**.*

---

## A — URLs créées

| Cas | URL | HTTP | Indexable | Canonical | Sitemap | H1 |
|---|---|---|---|---|---|---|
| A | https://drfranckmoyal.fr/cas-cliniques/planification-facettes-ceramique/ | `200` | oui | auto-référente | oui | Planification et réalisation d’un traitement par facettes en céramique |
| B | https://drfranckmoyal.fr/cas-cliniques/planification-rehabilitation-facettes/ | `200` | oui | auto-référente | oui | Planification d’une réhabilitation esthétique par facettes |
| C | https://drfranckmoyal.fr/cas-cliniques/mih-eclaircissement-erosion-infiltration/ | `200` | oui | auto-référente | oui | Prise en charge conservatrice de taches de MIH |

Un seul H1 par page, title et meta description uniques, fils d’Ariane rattachés à la page
thérapeutique : *Accueil > Dentisterie esthétique > Facettes dentaires > Planification et
facettes* ; *… > Bilan esthétique personnalisé > Réhabilitation par facettes* ; *… > Taches et
dyschromies > Taches de MIH*. Le site compte désormais **26 pages indexables**.

---

## B — Contenus créés

**Cas A — planification, orthodontie pré-prothétique, 4 facettes.** Six sections : la situation
initiale (patient complexé par son sourire et la forme de ses dents) ; le projet numérique
SmileCloud ; **l’orthodontie guidée par le projet prothétique** — la section différenciante, qui
explique que la planification a déterminé où les dents devaient être placées avant les
restaurations, et renvoie au gradient thérapeutique ; les quatre facettes Empress Multi avec la
réalisation prothétique Labeldent — Sophie Dallem ; le résultat ; ce que le cas permet de
comprendre. La photographie du projet montre l’appareil orthodontique : il est expliqué, pas masqué.

**Cas B — réhabilitation par 20 facettes.** Six sections : usures importantes et déficit esthétique
majeur, sans un mot sur l’étiologie ; la simulation SmileCloud montrée à la patiente avant le
traitement ; **de la simulation au projet clinique**, où la simulation devient la référence commune
du praticien et du prothésiste ; les 20 facettes Empress, 10 maxillaires et 10 mandibulaires ; le
résultat ; ce que le cas permet de comprendre.

**Cas C — deux situations de MIH, une seule page.** Sept sections : le contraste comme vrai
problème ; **pourquoi éclaircir avant l’érosion-infiltration** (réduction du delta de teinte) ;
cas 1 — patiente de 30 ans, tache de MIH sur la 21 ; cas 2 — MIH sur une dent dyschromiée après un
traumatisme de l’enfance ; pourquoi privilégier une approche conservatrice, avec le composite de
surface présenté comme une possibilité et non comme réalisé ; ce que les deux cas permettent de
comprendre.

Sur chaque page : la réponse directe extractible sous l’ouverture, « Cas clinique — Dr Franck
Moyal » **une seule fois**, la mention commune de fin de page (§32) et l’appel à prendre
rendez-vous. Aucun des mots interdits du §31 n’apparaît — vérifié automatiquement sur les trois
pages fabriquées.

---

## C — Photographies réutilisées

**Aucune nouvelle image, aucune copie de fichier, aucun retraitement.** Les pages appellent les
mêmes fichiers que les pages thérapeutiques, dans `src/assets/photos/cas/` :

| Cas | Photographies | Composant | Affichage |
|---|---|---|---|
| A | `facettes-planification` (3) | ClinicalImage ×3 | une photographie par étape, chacune dans sa section, avec sa propre légende |
| B | `bilan-esthetique` (3) | ClinicalImage ×3 | idem |
| C | `mih-erosion-infiltration` (2) et `dyschromie-erosion-infiltration` (2) | ClinicalBeforeAfter ×2 | Avant / Après en texte HTML |

Pour permettre d’afficher **une seule photographie d’une séquence** dans sa propre section, le
registre accepte désormais l’écriture `cas#n`, et chaque photographie peut porter une légende
propre. Les séquences complètes restent affichées telles quelles sur les pages thérapeutiques.

---

## D — Liens entrants

Vérifiés page source par page source, en production :

| Cas | Page source | Ancre |
|---|---|---|
| A | `/facettes-dentaires-paris/`, section « Smile design et simulation » | Voir un cas clinique associant planification, orthodontie pré-prothétique et facettes |
| B | `/bilan-esthetique-personnalise/`, section « Qu’apporte le smile design ? » | Voir un exemple de projet esthétique planifié avant une réhabilitation par facettes |
| C | `/taches-dentaires-dyschromies-icon/`, section sur la MIH | Voir deux cas cliniques de MIH traités par éclaircissement et érosion-infiltration |

Chaque lien est porté par le composant **`ClinicalCaseSummary`** créé pour cela (§24) : une petite
photographie, la problématique en une ligne, l’approche en une phrase, le lien. Un filet, du texte,
aucune carte.

---

## E — Liens sortants

| Cas | Liens |
|---|---|
| A | Facettes dentaires, Facettes ou composite, Dentisterie esthétique, Dr Franck Moyal, prendre rendez-vous |
| B | Bilan esthétique, Facettes dentaires, Dentisterie esthétique, Dr Franck Moyal, prendre rendez-vous |
| C | Taches et dyschromies, Éclaircissement dentaire, Facettes ou composite, Dentisterie esthétique, Dr Franck Moyal, prendre rendez-vous |

Le lien vers `/facettes-ou-composite/` est posé dans le raisonnement, pas en pied de page : sur le
cas A au moment du gradient thérapeutique (« déplacer avant de préparer »), sur le cas C au moment
où l’on explique qu’on ne restaure pas si une solution plus conservatrice répond à la situation.
Le cas B n’en porte pas : le §20 le laisse optionnel et rien ne l’appelait naturellement.

---

## F — Schema

Identique sur les trois pages : `WebSite` → `MedicalWebPage` (`…#page`) → `BreadcrumbList`
(`…#fil`), plus `Person` (`/#franck-moyal`) et `Dentist` (`/#practice`).

- **Les identifiants globaux sont réutilisés** : aucun second Franck Moyal, aucune nouvelle entité
  professionnelle, aucun type inventé.
- `datePublished` = **2026-09-25** (date réelle de publication des pages), `dateModified` idem.
  La date des traitements n’est pas connue et n’est écrite nulle part.
- Pas de `FAQPage` : ces pages n’ont pas de FAQ.

---

## G — Responsive

18 mesures (3 pages × 6 largeurs), page déroulée jusqu’en bas :

| Largeur | Photographies | Débordement horizontal |
|---|---|---|
| 320 px | 280 px de large, une par ligne | 0 |
| 375 px | 335 px | 0 |
| 390 px | 350 px | 0 |
| 430 px | 389 px | 0 |
| 768 px | 704 à 713 px | 0 |
| 1440 px | 704 px pour une photographie seule ; 2 × 602 px pour un avant/après | 0 |

Les avant/après s’empilent verticalement sous 768 px, sans jamais réduire la taille utile des
photographies. Toutes les photographies se chargent à toutes les largeurs (12/12 puis 4/4).

---

## H — Performance

Lighthouse mobile en production, cas A : **100 / 100 / 100 / 100**, LCP 1,9 s, CLS 0, 296 Ko.
Les pages pèsent 73 à 76 Ko de HTML. Les photographies sont servies en WebP, en trois largeurs,
en chargement différé, dimensions posées : aucun décalage de mise en page, aucun fichier dupliqué,
aucun original lourd téléchargé.

---

## I — Écarts par rapport au cahier des charges

| Élément | Demandé | Implémenté | Écart | Justification |
|---|---|---|---|---|
| Rédaction des pages | Structure, angles et faits validés ; quelques formulations mot pour mot | Pages rédigées par Claude à partir de ces éléments, formulations fournies reprises telles quelles | Rédaction | Le cahier des charges donne la structure et les faits, pas un texte suivi. Tout est relisible dans `docs/pages-suivantes/v1.6/`. |
| Titres de sections | Donnés pour l’essentiel | Repris ; trois titres courts écrits par Claude : « Une tache, deux situations » (cas C), « Situation initiale » / « Résultat clinique » (cas B, formulations du §12) | Titres | Le gabarit exige un H2 par section. |
| Légendes des photographies | Non fournies | Trois légendes écrites pour les photographies affichées seules (situation initiale, projet, résultat), strictement factuelles | Légendes | Une photographie isolée dans sa section a besoin d’une légende. Celle du projet du cas A signale l’appareil orthodontique, comme demandé au §7. |
| Textes de l’annonce de cas | Exemple conceptuel donné (§24) | « Planifier avant de restaurer », « Voir le projet avant de le réaliser », « Réduire le contraste avant de traiter la tache » + une ligne d’approche | Rédaction | Les libellés de lien sont ceux du §21, mot pour mot. |
| Lien Facettes ou composite sur le cas B | « lien possible mais moins essentiel, ne pas forcer » | Non posé | Choix assumé | Rien ne l’appelait dans le raisonnement de cette page. |
| Laboratoire du cas B | Ne pas attribuer sans information validée | Non nommé | Conforme | — |
| Page `/cas-cliniques/` | Ne pas créer | Non créée | Conforme | L’adresse `/cas-cliniques/` répond `403` (le serveur refuse de lister un dossier). Voir les anomalies. |
| Menu | Ne pas modifier | Inchangé | Conforme | Les trois cas se découvrent depuis leur page thérapeutique. |
| Article usures | Ne pas anticiper | Rien créé, rien fusionné, aucune URL réservée | Conforme | — |
| Mini-cas existants | Conserver | Tous conservés | Conforme | Les mêmes photographies figurent donc à deux endroits : dans la page thérapeutique et dans le cas dédié, comme le §23 l’autorise. |

---

## J — Anomalies restantes

1. **`/cas-cliniques/` répond `403`** au lieu de `404`. C’est le comportement par défaut du serveur
   Hostinger face à un dossier sans page d’accueil. Aucun lien ne mène à cette adresse et elle n’est
   pas dans le plan du site ; l’effet SEO est nul. Elle disparaîtra le jour où une page index sera
   créée — décision que le §25 réserve à plus tard.
2. **Incident de fabrication, rattrapé** : iCloud a de nouveau dupliqué des éléments dans le dossier
   de travail, cette fois des **dossiers entiers** (`planification-facettes-ceramique 3`…), partis
   sur le serveur avec le paquet. Les trois dossiers en double ont été mis à la corbeille du
   serveur, et la fabrication du paquet écarte désormais les dossiers comme les fichiers dupliqués.
   Vérifié dossier par dossier après coup : le serveur ne porte plus aucune copie.
3. **Rien d’autre.** Les 27 pages en ligne sont identiques, octet pour octet, à la version
   fabriquée ; les trois contrôles automatiques du site passent (textes vérifiés dans les deux sens,
   HTML, contrôle avant mise en ligne).

---

## Contrôle de cohérence clinique (§39)

Vérifié automatiquement sur les pages fabriquées :

| Contrôle | Résultat |
|---|---|
| Cas A — nombre de facettes | « quatre facettes » uniquement ; aucun autre nombre |
| Cas A — matériau et laboratoire | Empress Multi, Labeldent — Sophie Dallem ; rien d’autre |
| Cas A — préparation chiffrée | aucune |
| Cas B — nombre et répartition | 20 facettes, 10 maxillaires et 10 mandibulaires ; rien d’autre |
| Cas B — étiologie de l’usure | aucune ; aucun laboratoire nommé |
| Cas C1 — âge et dent | 30 ans, dent 21 ; aucun autre chiffre |
| Cas C2 — origine de la dyschromie | traumatisme de l’enfance uniquement ; **aucune mention de dent dépulpée ni de traitement endodontique** |
| Vocabulaire interdit (§31) | aucune occurrence sur les trois pages |

---

**POINT 3 — PHASE B VALIDABLE : OUI.**

Les trois contenus sont créés, déployés, contrôlés en production, conformes aux faits validés et
aux interdits du cahier des charges. Les écarts sont listés au point I ; aucun ne porte sur un fait
clinique.

*Conformément au §42 : **STOP**. Pas de page `/cas-cliniques/`, pas de modification du menu, aucun
autre cas, aucune page composite supplémentaire, l’article usures n’est pas anticipé et le POINT 4
n’est pas commencé.*
