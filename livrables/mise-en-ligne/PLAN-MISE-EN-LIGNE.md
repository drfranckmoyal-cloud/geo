# Mise en ligne de la refonte — plan du 25/10/2026

Franck, 25/10/2026 : « il reste des corrections et des ajouts à faire, mais il est temps de pousser le nouveau site
en ligne (ce n'est pas un nouveau site, je sais) ; je te laisse commencer à planifier la mise en place ».

Ce document planifie ; **rien n'est encore mis en ligne**. Chaque étape est validée par Franck avant la suivante, et
le dépôt sur le serveur ne se fera qu'avec son accord explicite, donné au moment même.

## 1. Où on en est

| | Aujourd'hui en ligne | La refonte |
|---|---|---|
| Ce que c'est | le site Astro du golden master | la maquette `docs/refonte/maquettes/site/` (pages HTML fabriquées par `construire.sh`) |
| Pages publiques | 27 adresses (plan du site) | 36 pages (38 moins deux pages internes) |
| Poids | 11 Mo, déposé le 08/10/2026 | environ 60 Mo, dont 45 Mo de vidéos |
| Hébergement | Hostinger, `domains/drfranckmoyal.fr/public_html`, accès SSH vérifié le 25/10/2026 (lecture seule) | même endroit |

## 2. Les adresses — la règle : aucune adresse connue de Google ne doit tomber en erreur

**Gardées telles quelles (26)** : `/`, `/activite-hospitaliere/`, `/anorexie-erosion-dentaire-sans-vomissements/`,
`/bilan-esthetique-personnalise/`, `/bruxisme-usure-dentaire/`, les quatre `/cas-cliniques/…/`,
`/chirurgien-dentiste-paris-9/`, `/composite-bonding-paris/`, `/conferences-formations/`, `/contact/`,
`/dentisterie-esthetique-paris/`, `/dents-courtes-usees/`, `/eclaircissement-dentaire-paris/`, `/erosion-dentaire/`,
`/facettes-dentaires-paris/`, `/facettes-ou-composite/`, `/franck-moyal/`, `/medias-interviews/`, `/mentions-legales/`,
`/publications/`, `/taches-dentaires-dyschromies-icon/`, `/tca-dents/`, `/usures-dentaires/`.

**Nouvelles (10)** : `/espace-patients/`, `/espace-pro/`, `/articles/`, `/articles/jeunes-chirurgiens-dentistes-formes-en-europe/`,
`/videos/` et les cinq `/videos/…/`.

**Fondues, redirigées définitivement (301) vers `/usures-dentaires/` (2)** : `/diagnostic-usures-dentaires/` (D77),
`/rehabilitation-dents-usees/` (D95).

**Internes, jamais publiées (2)** : `sommaire.html`, `polices.html`.

## 3. Les étapes

### Étape 1 — Fabriquer la version « en ligne » (Claude)

**Faite le 25/10/2026 (D96)** : `npm run refonte`, aperçu sur le port 4340, essai de dépôt (135 fichiers à envoyer, 180 à retirer). Les 20 liens extérieurs perdus par la maquette sont rétablis.

Un programme de publication transforme la maquette en site déposable, sans toucher à la maquette :

- chaque page à son adresse propre (`usures-dentaires.html` → `/usures-dentaires/`), les cas cliniques sous
  `/cas-cliniques/`, les vidéos sous `/videos/`, l'article sous `/articles/` ;
- photos, vidéos, guide PDF et images copiés sous `/assets/`, seulement ceux qui servent ;
- **polices hébergées sur le site** : la maquette les charge chez Google Fonts, ce qui transmet l'adresse IP des
  visiteurs à Google (point RGPD) ;
- le pied de page définitif (la maquette affiche « Maquette de refonte — rien n'est en ligne ») ;
- une balise d'adresse de référence (canonical) sur chaque page : 30 pages sur 38 n'en ont pas dans la maquette ;
- le plan du site sous les mêmes noms qu'aujourd'hui (`/sitemap-index.xml`, `/sitemap-0.xml`, `/sitemap.xml`), pour que
  Search Console et Bing continuent de le lire sans rien redéclarer ; `robots.txt` ;
- `.htaccess` : les règles actuelles (https, sans www, formats d'images) plus les deux redirections et une page 404 ;
- contrôles automatiques : aucun lien mort, aucune image manquante, aucune trace de chemin de maquette, données
  structurées valides, chaque adresse du site actuel servie ou redirigée.

Puis aperçu sur le Mac, aux vraies adresses, pour que Franck clique partout. En option : un aperçu protégé par mot de
passe sur le serveur du portail, pour l'essayer sur téléphone.

### Étape 2 — Les corrections avant lancement (Franck, puis Claude)

Bloquantes :

1. ~~**Hébergement**~~ — **réglé le 25/10/2026** : offre active, en renouvellement automatique, prochaine échéance le 22/11/2026.
2. **Le guide TCA** porte le logo du GHU Paris : accord de l'hôpital, ou guide retiré jusqu'à son accord.
3. **La vidéo de la première consultation** montre le visage d'une patiente : accord confirmé pour le site.
4. ~~**Les liens extérieurs** perdus dans la maquette~~ — **rétablis le 25/10/2026** (D96).
5. **La liste de corrections de Franck.**

Le reste peut suivre la mise en ligne : le site se met à jour en une commande, à tout moment.

### Étape 3 — Le dépôt (avec l'accord explicite de Franck, le jour venu)

**Faite le 25/10/2026 (D97)**, sur l'accord de Franck (« toutes les autorisations sont OK, tu peux mettre en ligne »). Sauvegarde : `domains/drfranckmoyal.fr/sauvegardes/public_html-202610252154`.

1. Sauvegarde du site actuel, sur le serveur (hors du dossier public) et sur le Mac : retour arrière possible en une
   commande. Le code de l'ancien site reste de toute façon dans GitHub.
2. Dépôt par SSH, comme pour Smile Club : seuls les fichiers changés partent, le site n'est jamais vide.
3. Vérification immédiate sur le vrai domaine : les 36 pages répondent, les 2 redirections et les 27 anciennes adresses
   aussi, https et www corrects.

### Étape 4 — Après la mise en ligne

**Faite le 25/10/2026 (D98)** : Search Console (plans du site, 8 pages), Bing par IndexNow (35 adresses).

- Search Console : renvoyer le plan du site, demander l'indexation des pages nouvelles et des pages réécrites
  (Espace patients, Usure dentaire, TCA, Vidéos) ; surveiller les erreurs les jours suivants.
- Bing Webmaster Tools : même chose.
- Le relevé quotidien des positions continue : il dira, page par page, si la refonte fait monter le site.
- Les corrections et ajouts suivants, publiés au fil de l'eau.

## 4. Ce que Franck décide

1. ~~Vérifier le renouvellement de l'hébergement~~ — fait.
2. Sa liste de corrections, et ce qui doit absolument être fait avant le lancement.
3. Le guide TCA (logo du GHU) et la vidéo de consultation (accord de la patiente).
4. La date de mise en ligne.
