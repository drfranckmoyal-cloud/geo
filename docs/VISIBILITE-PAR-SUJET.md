# Où le site est visible, et où il ne l'est pas

Relevé du 8 octobre 2026. Deux sources, qui ne disent pas la même chose :

- **la liste de mots de Franck**, testée un par un par l'agent quotidien —
  `suivi/releves/2026-10-08.json` ;
- **les requêtes que Google a réellement servies**, 105 sur 28 jours —
  `suivi/requetes/2026-10-08.json`.

**Il faut lire les deux, et dans cet ordre.** Les requêtes servies ne contiennent, par
construction, que celles où le site est apparu au moins une fois : les lire seules
donne une image fausse et flatteuse. La liste de Franck, elle, teste aussi les mots
sur lesquels il n'apparaît pas.

Total du site sur 28 jours : **58 clics, 800 impressions, 105 requêtes, position
moyenne 9,4.**

---

## 1. Le chiffre qui compte

**Sur les 47 mots suivis par Franck, 33 ne donnent rien du tout. 14 sortent.**
Et sur ces 14, cinq sont son nom.

Il reste donc **neuf mots de métier** sur lesquels le site existe :

| Mot suivi | Position | Impressions |
|---|---|---|
| facettes dentaires paris | 2,0 | 1 — *trop peu pour être fiable* |
| blanchiment dentaire paris | **2,6** | 7 |
| composite dentaire | **3,5** | 32 |
| tca | **3,8** | 8 |
| esthetique du sourire paris | **4,7** | 10 |
| esthetique dentaire paris | **5,5** | 11 |
| composite bonding paris | **6,7** | 19 (1 clic) |
| composite bonding | 10,5 | 12 |
| dentiste esthetique paris | 15,0 | 1 |
| bonding dentaire | 51,0 | 3 |
| usure dentaire | **86,0** | 3 |

Un seul sujet est vraiment gagné : **le composite et le bonding**, avec le
blanchiment et l'esthétique du sourire autour. Tout le reste est à faire.

---

## 2. Les 33 mots qui ne donnent rien

Rangés par sujet, pour voir ce qui manque :

- **Érosion** — érosion dentaire, erosion dentaire, erosion dentaire paris,
  dentiste erosion dentaire, erosion dentaire tca : *aucun*.
- **TCA** — dentiste tca, tca dentaire, anorexie dents, boulimie dents,
  troubles alimentaires dents : *aucun*. Seul « tca » tout court sort, en 3,8.
- **Usures** — usures dentaires, dentiste usure dentaire, usure dentaire paris,
  dents usées, dents courtes, reconstruction dents usées, dimension verticale
  dentaire : *aucun*. Seul « usure dentaire » sort, en **position 86**.
- **Bruxisme** — bruxisme, bruxisme usure dentaire : *aucun*. En revanche une
  requête voisine que Franck ne suivait pas, **« specialiste bruxisme paris », sort
  en 3,8** : le mot nu ne donne rien, le mot qualifié oui.
- **Facettes** — facettes dentaires, facettes ou composite, facettes ceramique
  paris, prix facettes dentaires paris : *aucun*. Google a servi
  « facette dentaire paris 9 » en 36,6 et « facettes dentaires paris 17 » en 37,8.
- **Composite, le reste** — dentiste composite bonding, composite dentaire paris,
  composite dentaire avant apres, bonding dentaire paris, stratification
  composite : *aucun*.
- **Autres pages de soins** — dentisterie esthetique paris, eclaircissement
  dentaire paris, taches blanches dents, mih dents : *aucun*.
- **Marque** — smile club formations : *aucun* depuis drfranckmoyal.fr.

---

## 3. Pourquoi, et ce que ça ne sert à rien de faire

Les pages de ces sujets ont été vérifiées une par une : **titres, descriptions et H1
sont justes et bien ciblés.** Exemples : « Érosion dentaire à Paris | Prévention et
traitement | Dr Franck Moyal », « Bruxisme et usure dentaire à Paris | Dr Franck
Moyal ». Ce n'est donc **ni un problème de contenu, ni un problème de ciblage**.

Le détail qui le prouve : `/usures-dentaires/` est la page la **mieux reliée** du site
après l'accueil — dix-neuf liens internes — et le site est en **position 86** sur
« usure dentaire ». Une page bien faite, bien reliée, bien titrée, et invisible.

La cause est l'autorité du domaine : dix-sept jours d'index, presque aucun lien
entrant. « Usure dentaire », « érosion dentaire », « facettes dentaires » sont des
requêtes nationales tenues par des sites installés depuis des années.

**Donc : réécrire ces pages ne changerait rien.** C'est la conclusion la plus utile de
ce relevé, parce qu'elle évite un travail inutile.

---

## 4. Les pages que Google n'a jamais explorées

Cinq pages sur vingt-huit, au 7 octobre : `/activite-hospitaliere/`,
`/anorexie-erosion-dentaire-sans-vomissements/`, `/bruxisme-usure-dentaire/`,
`/dents-courtes-usees/`, `/medias-interviews/`. Relancées le 7 octobre.

**Une faute de navigation en expliquait une partie, elle est corrigée (D71).**
`/bruxisme-usure-dentaire/` et `/dents-courtes-usees/` n'étaient dans aucun menu et
n'avaient que deux ou trois liens internes, atteignables seulement en passant par la
page pilier des usures — alors qu'elles portent deux des mots suivis par Franck.
Elles ont maintenant vingt-sept liens entrants.

**Mais le maillage n'explique pas tout, et il faut le dire.**
`/activite-hospitaliere/` est dans le pied de page des vingt-huit pages, donc
parfaitement reliée, et Google ne l'a jamais explorée non plus. La cause dominante
reste le **budget d'exploration** d'un domaine jeune et peu cité — même conclusion
qu'au 4 octobre (D64).

---

## 5. Ce qu'il faut faire

1. **Ne rien réécrire** sur les usures, l'érosion et les facettes. Les pages sont
   justes ; leur position ne dépend pas d'elles.
2. **Les liens entrants sont le seul levier** sur ces sujets. La liste des annuaires
   et des publications à viser est dans `docs/LIENS-ENTRANTS.md` ; six messages
   attendent d'être envoyés par Franck, et trois annuaires affichent une adresse
   fausse à corriger.
3. **Préférer les mots qualifiés aux mots nus.** C'est le fait le plus net du relevé :
   « bruxisme » ne donne rien, « specialiste bruxisme paris » sort en 3,8 ;
   « bonding dentaire » est en 51, « composite bonding paris » en 6,7. Un cabinet
   parisien gagne sur le mot + le lieu, ou le mot + la précision clinique, pas sur le
   mot seul. **À soumettre à Franck** : ajouter ces variantes qualifiées à la liste
   suivie, puisque ce sont elles qui sortent.
4. **Refaire ce relevé dans un mois**, avec `node suivi/comparer.mjs`, qui dira ce
   qui a bougé.

---

*Dernière mise à jour : 8 octobre 2026.*
