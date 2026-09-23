# Audit de production — 23 septembre 2026

*Claude Code. Contrôles exécutés sur le site en ligne, https://drfranckmoyal.fr, par requêtes HTTP
réelles (dernier passage le 24/09/2026 à 00 h 10). Aucune modification d'architecture, de contenu
ni de design.*

**Résultat : 1 anomalie objectivable sur les 15 contrôles — `/sitemap.xml` en 404. Corrigée et
remise en ligne. Tout le reste passe.**

---

## P0 — contrôles prioritaires

| # | Contrôle | Résultat |
|---|---|---|
| 1 | `https://drfranckmoyal.fr/robots.txt` | ✅ `200`, `text/plain` |
| 2 | `https://drfranckmoyal.fr/sitemap.xml` | ⚠️ **était en `404`** → corrigé : `200`, `application/xml`, 22 adresses |
| 3 | `http://drfranckmoyal.fr/*` → `https://` | ✅ `301`, chemin conservé (testé sur l'accueil, Contact, Taches, Mentions légales, Composite) |
| 4 | `https://www.drfranckmoyal.fr/*` → sans `www` | ✅ répond (certificat couvrant `www`) et `301` vers la même adresse sans `www` |

### Anomalie 2 — détail et correction

Le plan du site était publié par Astro sous `/sitemap-index.xml` (index) et `/sitemap-0.xml`
(les 22 adresses). L'adresse conventionnelle `/sitemap.xml`, celle que testent les outils
d'audit et certains robots, renvoyait `404`.

**Correction** : la fabrication du site copie désormais le plan sous `/sitemap.xml`
(`npm run build` → `cp dist/sitemap-0.xml dist/sitemap.xml`). Les deux fichiers sont donc
toujours identiques, et un contrôle automatique le vérifie (`node scripts/check-html.mjs`).
`/sitemap-index.xml` et `/sitemap-0.xml` restent en place : ce sont eux qui ont été déclarés à
Google Search Console et à Bing. `robots.txt` continue de déclarer l'index.

Vérifié en ligne : `/sitemap.xml` → `200 application/xml`, 22 `<loc>`, contenu identique au plan
produit à la fabrication.

## P1 — audit automatisé des 23 pages

| # | Contrôle | Résultat |
|---|---|---|
| 5 | Une canonical absolue auto-référente par page | ✅ 23 / 23 |
| 6 | Aucune page stratégique en `noindex` ou bloquée | ✅ seule la page Mentions légales est en `noindex,follow` (choix du pack) ; `robots.txt` sans aucune interdiction |
| 7 | Un seul H1 par page | ✅ 23 / 23 |
| 8 | `title` et `meta description` remplis et non dupliqués | ✅ 23 titres et 23 descriptions, tous différents |
| 9 | JSON-LD valide, identifiants stables, relations cohérentes | ✅ voir ci-dessous |
| 10 | Liens internes sans 4xx / 5xx | ✅ 23 adresses internes distinctes, toutes en `200` |
| 11 | CTA « Prendre rendez-vous » → `/contact/#prendre-rendez-vous` | ✅ tous ; l'ancre existe une seule fois, sur la page Contact |
| 12 | `tel:+33183755216` et `mailto:` | ✅ dans le pied de page des 23 pages et dans la section de prise de rendez-vous |
| 13 | `à fournir`, `TODO`, `FIXME`, `placeholder`, `lorem ipsum` | ✅ aucune occurrence visible |
| 14 | Plan du site ↔ pages indexables | ✅ 22 = 22, exactement les mêmes |
| 15 | Lighthouse mobile (5 pages) | ✅ 100 partout, voir le tableau |

### 9. Données structurées

**Contrôle automatique, sur les 23 pages** : JSON-LD lisible ; chaque renvoi `@id` pointe vers un
nœud présent sur la page (aucun renvoi orphelin) ; `Person#franck-moyal` et le cabinet
`#practice` (type `Dentist`, avec adresse, téléphone et e-mail) sur chaque page ; `workLocation`
de la personne → `#practice` ; page reliée à la personne (`author`, ou `mainEntity` sur la page de
profil) ; références bibliographiques complètes (titre et adresse).

Types employés, tous existants sur schema.org : `Article`, `BreadcrumbList`, `CollectionPage`,
`ContactPage`, `Dentist`, `EducationalOrganization`, `MedicalWebPage`, `Organization`, `Person`,
`ProfilePage`, `WebPage`, `WebSite`.

**Test des résultats enrichis de Google** (outil officiel) :
- **Accueil** : 2 éléments valides — « Commerces et services à proximité » (le cabinet) et
  « Organisation ». Aucune erreur.
- **Publications** (la page au graphe le plus riche) : 6 éléments valides — 3 `Article`,
  1 fil d'Ariane, 1 commerce local, 1 organisation. Aucune erreur.

**Recommandations facultatives signalées par Google, à trancher par ChatGPT** — aucune n'est une
erreur, aucune n'empêche l'affichage :
- cabinet `#practice` : champs `priceRange` et `image` absents. Une image du cabinet demanderait
  une photo que nous n'avons pas ; `priceRange` relève d'un choix de Franck ;
- publications : champ `image` absent sur les `Article` de la page (les articles d'origine ne sont
  pas hébergés sur le site).

### 8. Longueurs, pour mémoire

7 titres dépassent 60 caractères et 5 descriptions dépassent 155 : ils seront coupés dans les
résultats Google. C'est le point 13 du fichier maître, ouvert depuis le golden master ; les textes
viennent du pack et n'ont pas été touchés.

### 13. Précision

La chaîne `placeholder` apparaît dans le code de chaque page, uniquement comme nom de classe CSS
(`.placeholder-text`), héritée du système de design gelé. Elle n'affiche rien et reste invisible
pour le visiteur. Aucun texte d'attente n'est rendu.

## 15. Lighthouse mobile, sur le site en ligne

| Page | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | CLS | TBT | Poids |
|---|---|---|---|---|---|---|---|---|
| Accueil | 100 | 100 | 100 | 100 | 1,8 s | 0 | 0 ms | 213 Ko |
| Dentisterie esthétique | 100 | 100 | 100 | 100 | 1,8 s | 0 | 0 ms | 195 Ko |
| Composite bonding | 100 | 100 | 100 | 100 | 1,8 s | 0 | 0 ms | 195 Ko |
| Usures dentaires | 100 | 100 | 100 | 100 | 1,8 s | 0 | 0 ms | 196 Ko |
| Contact | 100 | 100 | 100 | 100 | 1,8 s | 0 | 0 ms | 190 Ko |

**INP** : Lighthouse en laboratoire ne le mesure pas — c'est une mesure de terrain, calculée sur
les visites réelles. Son équivalent de laboratoire, le temps de blocage total (TBT), est de
**0 ms** sur les cinq pages : le site ne charge aucun script bloquant. L'INP réel apparaîtra dans
Search Console (Signaux web essentiels) quand le site aura assez de visites.

Les mesures en ligne sont meilleures que celles faites en local le 22/09 (99 en rapidité,
LCP 1,95 à 2,10 s) : le serveur d'Hostinger sert les pages compressées en HTTP/2.

## Ce qui a changé sur le site

Une seule chose, la correction de l'anomalie : le fichier `/sitemap.xml` existe désormais.
Aucune page, aucun texte, aucun réglage de design n'a été modifié. Les 23 pages en ligne sont
identiques, octet pour octet, à la version fabriquée ici.
