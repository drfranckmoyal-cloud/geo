# Arborescence de la refonte

*12 octobre 2026. Décidée par Franck : premier niveau par public, puis, côté patient,
deux axes — ce qu'on constate, ce qu'on peut faire.*

---

## Le menu

```
Vous êtes patient ▾
   CE QUE VOUS CONSTATEZ          CE QU'ON PEUT FAIRE
   Mes dents s'usent              Composite bonding
   Mes dents deviennent fines     Facettes céramique
   Je serre des dents la nuit     Facettes ou composite ?
   Mes dents paraissent courtes   Éclaircissement
   J'ai des taches blanches       Infiltration des taches
   Troubles alimentaires          Réhabilitation des dents usées
                                  Bilan esthétique

Vous êtes chirurgien-dentiste ▾
   Conférences et formations · Smile Club Formations ↗ · Publications
   Activité hospitalière · TCA et santé bucco-dentaire · Médias et interviews

Dr Franck Moyal        Cas cliniques        [ Prendre rendez-vous ]
```

---

## Où va chacune des 28 pages

### Côté patient — ce que vous constatez

| Entrée du menu | Page |
|---|---|
| Mes dents s'usent | `/usures-dentaires/` *(page pilier ; absorbe le diagnostic)* |
| Mes dents deviennent fines et transparentes | `/erosion-dentaire/` |
| Je serre ou grince des dents la nuit | `/bruxisme-usure-dentaire/` |
| Mes dents paraissent courtes | `/dents-courtes-usees/` |
| J'ai des taches blanches | `/taches-dentaires-dyschromies-icon/` |
| Mes dents sont jaunes ou ternes | `/eclaircissement-dentaire-paris/` *(même page que la colonne des traitements)* |
| Troubles alimentaires et dents | `/tca-dents/` · `/anorexie-erosion-dentaire-sans-vomissements/` |

### Côté patient — ce qu'on peut faire

| Entrée du menu | Page |
|---|---|
| Dentisterie esthétique et adhésive | `/dentisterie-esthetique-paris/` *(page pilier de l'axe)* |
| Composite bonding | `/composite-bonding-paris/` |
| Facettes céramique | `/facettes-dentaires-paris/` |
| Facettes ou composite ? | `/facettes-ou-composite/` |
| Éclaircissement | `/eclaircissement-dentaire-paris/` |
| ~~Réhabilitation des dents usées~~ | `/rehabilitation-dents-usees/` — **fondue dans `/usures-dentaires/` le 25/10/2026 (D95)** : redirection permanente à prévoir à la mise en ligne |
| Bilan esthétique | `/bilan-esthetique-personnalise/` |

### Côté chirurgien-dentiste

`/conferences-formations/` · Smile Club Formations ↗ · `/publications/` ·
`/activite-hospitaliere/` · `/medias-interviews/` — *les TCA passent côté patient*

### Hors menu déroulant

`/franck-moyal/` · `/chirurgien-dentiste-paris-9/` · les 3 pages de cas cliniques ·
`/contact/` · `/mentions-legales/`

---

## Les trois points, tranchés le 16 octobre 2026

### 1. Le diagnostic des usures est fondu dans la page Usures ✓

**Ce n'est pas une addition.** Les deux pages se recouvrent : quatre des douze
chapitres du diagnostic redisent ce que la page Usures dit déjà.

| Chapitre du diagnostic | Déjà dit par la page Usures |
|---|---|
| L'usure vient-elle forcément du bruxisme ? | Le bruxisme n'explique pas tout |
| Que recherche-t-on dans l'interrogatoire ? | Une enquête clinique avant toute restauration |
| Faut-il toujours restaurer une usure diagnostiquée ? | Non : toutes les usures ne nécessitent pas une reconstruction |
| FAQ, sources, appel final | les mêmes |

**Ce qui est propre au diagnostic et doit être gardé** : « une dent usée n'est pas un
diagnostic », les signes qui font penser à une usure, la distinction attrition /
érosion / abrasion, la photographie et le scanner, le BEWE, et le suivi de la
progression.

**La page fusionnée, en cinq chapitres** — et non vingt-trois :

1. **Ce qui se passe** — quand les dents changent, les signes qui alertent
2. **Pourquoi** — attrition, érosion, abrasion ; le bruxisme n'explique pas tout
3. **Comment on l'évalue** — interrogatoire, photographies, scanner, BEWE, suivi
4. **Ce qu'on fait, ou pas** — toutes les usures ne se restaurent pas ; esthétique et fonction ensemble
5. **Faire le point** — le bilan, le rendez-vous

Puis les questions fréquentes et les sources, comme aujourd'hui.

**Conséquence technique** : l'adresse `/diagnostic-usures-dentaires/` disparaît. Elle
est dans l'index de Google (sans aucune impression au relevé du 8 octobre), donc il
faut une **redirection permanente** vers `/usures-dentaires/`. Sans elle, les liens
existants tomberaient sur une page d'erreur.

**Ce point relève de ChatGPT** : décider quoi garder et quoi couper, c'est du texte.
Je peux préparer le relevé des recouvrements à lui soumettre.

### 2. Les TCA passent côté patient ✓

`/tca-dents/` appartient à la colonne « ce que vous constatez », avec
`/anorexie-erosion-dentaire-sans-vomissements/`. Son fil d'Ariane devient
**Accueil › Patient › Troubles alimentaires et dents**.

La page reste citée côté confrère, mais comme un lien dans le corps de la page
« Activité hospitalière », pas comme une entrée de menu — une page n'a qu'un seul
chemin.

### 3. « Mes dents sont jaunes » — pas de nouvelle page

**Décidé par Claude, à confirmer par Franck.** La colonne des constats reçoit l'entrée
« Mes dents sont jaunes ou ternes », qui **pointe vers la page éclaircissement**
existante. Même page, deux portes, deux libellés.

Créer une page de constat séparée coûterait une page de plus à faire explorer par
Google, alors que le relevé du 8 octobre montre que le site peine déjà à faire
explorer celles qu'il a. On n'ajoute pas de page tant que l'autorité du domaine n'a
pas progressé.

---

## Ce que l'arborescence change pour les adresses

**Une seule adresse disparaît** : `/diagnostic-usures-dentaires/`, redirigée en permanence
vers `/usures-dentaires/`. Les vingt-sept autres gardent leur URL : ce qui change,
c'est la façon dont on y accède et les mots du menu. C'est important — changer les
adresses ferait perdre les positions déjà acquises dans Google, qui sont peu nombreuses
mais réelles.

---

*Dernière mise à jour : 16 octobre 2026.*
