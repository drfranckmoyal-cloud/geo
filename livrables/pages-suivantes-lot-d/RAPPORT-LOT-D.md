# Pages suivantes — lot D : contact et mentions légales, et bilan des 20 pages

*Claude Code, 22 septembre 2026. Pack « pages suivantes » V1, fichiers 19 et 20. Avec ce lot,
les 20 pages du pack sont construites : le site compte 23 pages. Les écarts de l'ensemble du
pack restent détaillés dans le rapport du lot A (partie 5).*

---

## 1. Ce qui est livré

| N° | Page | Adresse | Données structurées | Moteurs |
|---|---|---|---|---|
| 19 | Contact et rendez-vous | `/contact/` | ContactPage + adresse du cabinet (PostalAddress) | indexable |
| 20 | Mentions légales | `/mentions-legales/` | WebPage | `noindex,follow`, hors du plan du site |

Le lien « Mentions légales » du pied de page mène désormais à la page. Sur les trois pages du
golden master, c'est la seule modification de ce lot.

## 2. Contrôles

- **Textes** : sur les 2 pages, aucun passage du pack oublié, aucun texte ajouté. Les
  emplacements « [À FOURNIR] » s'affichent comme emplacements réservés (« à fournir »,
  souligné en pointillé, comme le téléphone du pied de page).
- **HTML et 10 contrôles du manifeste** : réussis sur les 23 pages. Le contrôle a relevé une
  vraie erreur, corrigée aussitôt : les mentions légales figuraient encore dans le plan du site
  envoyé aux moteurs, alors qu'elles sont en `noindex`. Plan du site : les 22 pages
  indexables.
- **Plus aucun lien « à venir »** : chaque lien interne du site mène à une page construite.
- **Lighthouse** :

| Page | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | Poids |
|---|---|---|---|---|---|---|
| Contact, mobile (3 passages) | 100 | 100 | 100 | 100 | 1,80 s | 192 Ko |
| Contact, ordinateur | 100 | 100 | 100 | 100 | 0,40 s | 192 Ko |
| Mentions légales, mobile | 100 | 100 | 100 | 66 * | 1,80 s | 192 Ko |

  \* Voulu : Lighthouse baisse la note de référencement d'une page qui demande à ne pas être
  indexée, ce que ton fichier 20 prévoit.

## 3. Choix à valider

1. **Contact, « Prendre rendez-vous »** : cette section porte l'ancre `#rendez-vous`. Le bouton
   de l'en-tête y mène sur cette page ; le téléphone et le lien de prise de rendez-vous y
   restent « à fournir ».
2. **Contact, « Motifs de consultation »** : les 7 intitulés en gras sont devenus des liens vers
   leurs pages, en liste sobre à flèche (proposition du rapport du lot A, §5.6, appliquée ici ;
   à confirmer).
3. **Contact, H1** : celui du §2, « Contact et rendez-vous — Dr Franck Moyal, Paris 9e » (le
   contenu du §5 dit « … Dr Franck Moyal »).
4. **Contact, pages liées** : « À lire aussi », avec les trois liens à câbler du fichier (Dr
   Franck Moyal, Chirurgien-dentiste Paris 9, Activité hospitalière).
5. **Mentions légales** : « page de lecture simple ». Colonne de lecture et fond uni ; ni appel
   final, ni pages liées, ni bloc auteur.
6. **Ligne auteur de l'ouverture** : l'ouverture clinique gelée l'affiche sur toutes les pages,
   y compris Contact et Mentions légales. À retirer sur ces deux pages si tu le souhaites :
   cela demanderait une variante de l'ouverture.

## 4. Bilan des 20 pages

- **Construites** : les 20 pages, avec un seul gabarit alimenté par tes fichiers, et
  uniquement des composants gelés (adaptations sans effet visuel sur le golden master, rapport
  du lot A §4).
- **Contrôles réussis sur les 23 pages** :
  - textes mot pour mot, dans les deux sens ;
  - HTML et informations pour les moteurs ;
  - 10 contrôles du manifeste ;
  - réglages de design identiques à la version gelée.
- **Rapidité**, une page par lot : 99 à 100 sur mobile (LCP 1,80 à 1,95 s), 100 sur ordinateur,
  192 à 199 Ko.
- **Golden master** : inchangé, hormis ses liens, qui mènent désormais aux pages construites.

## 5. Avant la mise en ligne

**Corrections du pack** (rapport du lot A, partie 5) :
- renvois bibliographiques ;
- H1 trop longs sur mobile ;
- passages non affichés à confirmer ;
- manques et liens.

**Données de Franck** :
- téléphone ;
- lien de prise de rendez-vous ;
- adresse e-mail professionnelle ;
- hébergeur et ses coordonnées (mentions légales) ;
- adresses `sameAs` exactes ;
- visuels propriétaires : 28 emplacements réservés au total, 22 sur les nouvelles pages et 6
  sur le golden master.

**Décisions** :
- vers quoi pointe le bouton « Prendre rendez-vous » tant que le lien manque — proposition :
  `/contact/` ;
- réglage des robots d'IA (D27) ;
- hébergement et mise en ligne (étape 5).

**Tes mentions légales le rappellent** : si un formulaire, un outil de rendez-vous en ligne ou
une mesure d'audience est ajouté, les sections « Données personnelles » et « Cookies » sont à
revoir avant publication. Le site n'a aujourd'hui aucun traceur.

## 6. Captures (`captures/`)

| N° | Contenu |
|---|---|
| 01, 02 | Page Contact entière, ordinateur (1440) et mobile (390) |
| 03, 04 | Page Mentions légales entière, ordinateur (1440) et mobile (390) |
