# POINT 2 — page « Facettes ou composite : comment choisir ? » : en ligne

*Claude Code, 24 septembre 2026. Cahier des charges archivé tel quel dans
`docs/echanges/2026-09-24-chatgpt-point-2-facettes-ou-composite.md` ; texte de la page dans
`docs/pages-suivantes/v1.5/21_facettes-ou-composite_V1_5.md`. Contrôles faits sur le site
**en production**.*

---

## Contrôle après déploiement (§42)

| | |
|---|---|
| **URL finale** | https://drfranckmoyal.fr/facettes-ou-composite/ — URL courte, aucune page existante modifiée |
| **Status HTTP** | `200` |
| **Title** | Facettes ou composite : comment choisir ? \| Dr Franck Moyal (59 caractères) |
| **Meta description** | Facettes ou composite ? Comprendre les différences, indications, avantages et limites de chaque approche pour choisir selon votre situation clinique. (149 caractères) |
| **H1** | Facettes ou composite : comment choisir ? — un seul H1 |
| **Hiérarchie** | H1 → 19 H2 → 10 H3, aucun saut de niveau |
| **Canonical** | `https://drfranckmoyal.fr/facettes-ou-composite/`, auto-référente |
| **Indexable** | oui, `follow` : aucune balise `robots`, aucune directive dans `robots.txt` |
| **Sitemap** | présente dans `/sitemap.xml` et `/sitemap-0.xml` (23 adresses) |
| **Liens internes entrants** | **3** |
| **Pages contenant ces liens** | `/dentisterie-esthetique-paris/` (« Facettes ou composite : comment choisir ? », sous la question de FAQ qui pose le problème) ; `/composite-bonding-paris/` (« Composite ou facettes : comprendre les différences », en fin de la section « Composite bonding ou facettes ? ») ; `/facettes-dentaires-paris/` (« Facettes ou composite : comment choisir ? », en fin de la section « Facettes ou composite bonding ? ») |
| **Liens sortants principaux** | `/dentisterie-esthetique-paris/`, `/composite-bonding-paris/`, `/facettes-dentaires-paris/`, `/eclaircissement-dentaire-paris/`, `/usures-dentaires/`, `/rehabilitation-dents-usees/`, `/bilan-esthetique-personnalise/`, `/franck-moyal/`, `/contact/#prendre-rendez-vous`, `/` (fil d'Ariane) |
| **Schema détecté** | `WebSite` (`/#website`), `WebPage` (`…#page`), `BreadcrumbList` (`…#fil`), `Person` (`/#franck-moyal`), `Dentist` (`/#practice`) — **identifiants globaux réutilisés**, aucun second Franck Moyal, aucune nouvelle entité professionnelle |
| **FAQ visible** | oui, 8 questions, réponses ouvertes par défaut |
| **FAQ schema** | **non** — voir le tableau des différences |
| **Mobile 320 px** | aucun débordement ; tableau empilé critère par critère (280 px) ; gradient en 1 colonne ; matrice en 1 colonne ; bouton d'appel 202 px |
| **Mobile 375 px** | aucun débordement ; tableau 335 px |
| **Mobile 390 px** | aucun débordement ; tableau 350 px |
| **Mobile 430 px** | aucun débordement ; tableau 389 px |
| **768 px** | aucun débordement ; tableau 713 px ; gradient en 3 colonnes |
| **Desktop (1440 px)** | tableau sur toute la largeur du site (1240 px), 3 colonnes ; gradient en 6 colonnes ; matrice en colonne de lecture |
| **Débordement horizontal** | **0 px** aux 7 largeurs mesurées (320, 375, 390, 430, 768, 1024, 1440) ; le tableau ne défile jamais horizontalement |
| **Rapidité** | Lighthouse mobile **100 / 100 / 100 / 100** ; LCP 1,8 s ; CLS 0 ; TBT 0 ms ; 197 Ko |
| **Cohérence** | les 24 pages en ligne sont identiques, octet pour octet, à la version fabriquée |

---

## Ce que contient la page, dans l'ordre

1. Ouverture, chapeau, puis **réponse directe** : « La bonne question n'est donc pas “quel matériau est le meilleur ?”… »
2. **En bref** — les deux premiers paragraphes de l'introduction, puis les deux définitions côte à côte (composite bonding / facette en céramique)
3. **Ce que chacune apporte** — la phrase de synthèse du §8, en panneau vert sauge
4. **Le composite bonding : ajouter plutôt que remplacer** + les sept points à retenir + lien vers la page Composite bonding
5. **Les facettes en céramique : stabilité et maîtrise du projet** + les huit points à retenir + lien vers la page Facettes
6. **Composite ou facettes : raisonner en gradient thérapeutique** + la représentation en six étapes (Observer → Éclaircir → Déplacer → Ajouter → Restaurer → Préparer si nécessaire)
7. **Comparer les deux approches, critère par critère** — le tableau de 11 critères
8. **Dans quelles situations le composite peut-il être intéressant ?**
9. **Dans quelles situations les facettes peuvent-elles être envisagées ?**
10. **Et parfois, la réponse est : ni composite ni facettes** + liens Éclaircissement et Usures
11. **Composite ou facettes pour des dents usées ?** + lien Réhabilitation des dents usées
12. **Les facettes nécessitent-elles toujours de tailler les dents ?**
13. **Le composite est-il réellement réversible ?**
14. **Comment vieillissent composite et céramique ?**
15. **Pourquoi planifier avant de choisir ?** + liens Dentisterie esthétique et Bilan esthétique
16. **Faut-il forcément choisir un seul matériau ?**
17. **S'orienter selon la situation** — la matrice de 9 lignes, suivie de la mise en garde
18. **L'approche du Dr Franck Moyal** + lien vers la page Parcours
19. **FAQ** — les 8 questions
20. **À lire aussi** puis l'appel final « Composite, facettes… ou une autre solution ? »

Aucune durée de vie en années nulle part (vérifié en production), aucun classement, aucune
colonne « gagnant », aucun score, aucune promesse de facettes sans préparation, aucun prix.

---

## Rapport de différences (§43)

| Élément | Demandé | Implémenté | Écart | Justification |
|---|---|---|---|---|
| Titre de la section du tableau | §13 donne le tableau sans titre de section | « Comparer les deux approches, critère par critère » | Titre écrit par Claude | Le gabarit du site exige un H2 par section ; le titre est descriptif et neutre. Une ligne à changer si tu préfères un autre libellé. |
| Titre de la section de la matrice | §23 donne la matrice sans titre | « S'orienter selon la situation » | Titre écrit par Claude | Même raison. |
| Titre du bloc de synthèse du §8 | « Puis faire apparaître clairement : … » | Section « Ce que chacune apporte », en panneau vert sauge | Titre écrit par Claude | La phrase ne pouvait pas rester dans le bloc « En bref » : elle se serait collée sous la seule carte « Facette en céramique ». Isolée en panneau, elle se lit comme une synthèse, pas comme un classement. |
| Introduction (§7) | Trois paragraphes | ¶1 et ¶2 ouvrent la section « En bref » ; **¶3 devient la réponse directe**, placée juste sous le chapeau | Ordre d'affichage | Toutes les pages du site placent la phrase extractible dans le bloc `DirectAnswer`, sous l'ouverture. ¶3 est précisément cette phrase. Aucun mot modifié. |
| §9 et §10, « faire ressortir » | Listes de qualités à faire ressortir | Rendues en listes visibles, introduites par « Ce qu'il faut en retenir : » | Phrase d'amorce écrite par Claude | Une liste sans amorce tombe sans transition. Les items sont repris mot pour mot. |
| §14, §15, §21, §22 | Sections décrites par des listes d'idées à « expliquer » | Rédigées au plus près des mots de la consigne (une à deux phrases de liaison par section, les listes reprises telles quelles) | Rédaction par Claude | La consigne ne fournit pas de texte suivi pour ces quatre sections. Tout est relisible et modifiable : `docs/pages-suivantes/v1.5/21_facettes-ou-composite_V1_5.md`. |
| FAQ schema (`FAQPage`) | « uniquement si cela reste cohérent avec l'architecture/schema du site » | **Non posé** | Volontaire | Aucune des 23 pages du site n'utilise `FAQPage` ; l'ajouter ici créerait une exception. La FAQ est entièrement visible dans le HTML. Dis-le si tu veux l'ajouter partout. |
| Photographie clinique (§30) | Éventuellement une illustration discrète à fonction comparative | **Aucune photographie** | Volontaire | Les deux cas qui auraient eu un sens ici (composite, facettes) sont déjà les avant/après des pages techniques, vers lesquelles la page renvoie. La page reste une page de raisonnement. |
| Sous-titre du H1 | « Deux techniques, deux matériaux, mais surtout deux façons différentes de répondre à une même demande esthétique. » | Utilisé comme chapeau, sous le H1 | Aucun | — |
| Title | Deux formulations proposées | La première, 59 caractères | Aucun | La variante « à Paris » aurait dépassé la longueur affichée par Google. |
| Fil d'Ariane | Non précisé | Accueil > Dentisterie esthétique > Facettes ou composite | Ajout | Respecte l'architecture du cluster décrite au §29 : la page est fille de la page pilier. |
| Nouveaux composants | Tableau et gradient à créer, sobres | `ComparisonTable` et `GradientSteps` | Aucun | Deux composants neufs, aucun composant gelé modifié (verrou V24) : aucune couleur d'opinion, aucun score, aucune icône, aucune animation. |

---

## Contrôles automatiques

- **Textes** : 196 passages du fichier de page vérifiés dans les deux sens — aucun oublié, aucun texte inventé ni modifié. Le tableau est comparé cellule par cellule.
- **HTML** : un seul H1, canonical auto-référente, fil d'Ariane conforme, title et meta du fichier, auteur relié à la fiche, 17 liens internes tous avec un libellé descriptif, aucune image inventée, page indexable.
- **Avant mise en ligne** : aucun point bloquant.
- **Verrous** : réglages de design identiques à la version gelée ; « dentiste esthétique » toujours absent de cette page.

---

## Ce que je n'ai pas fait

Conformément au §40 et au §44 : aucune galerie, aucun portfolio, aucune bibliothèque de cas,
aucune page de cas clinique, aucune navigation « Cas cliniques ». **Le POINT 3 n'est pas commencé.**
