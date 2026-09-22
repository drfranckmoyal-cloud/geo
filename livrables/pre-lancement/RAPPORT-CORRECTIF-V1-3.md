# Correctif pré-lancement V1.3 : appliqué

*Claude Code, 22 septembre 2026.*

Source : `PATCH_PRE_LANCEMENT_V1_3_AVEC_CORRECTIF_EMAIL`, 4 fichiers archivés tels quels dans
`docs/pages-suivantes/v1.3/`. La fiche corrective du contact prime pour les coordonnées, comme
elle le demande.

---

## 1. Ce qui est appliqué

### Page 06, Taches

Le fichier V1.3 remplace le seul fichier 06. Il est lu directement, comme les autres. Tout y
est :
- H1, title, meta description et réponse directe centrés sur la MIH ;
- la section « Taches de MIH : peut-on les traiter chez un enfant ou un adolescent ? » ;
- les deux nouvelles questions de la FAQ ;
- les références [5] à [7] ;
- la source réglementaire européenne, affichée sous les références avec son lien EUR-Lex.

### Rendez-vous et coordonnées

**Aucune réservation en ligne annoncée.** La mention « Prise de rendez-vous en ligne » a
disparu des pages 18 et 19. Tous les boutons et liens « Prendre rendez-vous » / « Rendez-vous »
mènent toujours à `/contact/#prendre-rendez-vous`.

**Page Contact** (fiche corrective, §3) :
- la section s'intitule « Prendre rendez-vous ou nous écrire » et garde l'ancre
  `#prendre-rendez-vous` ;
- elle commence par le texte d'introduction, puis donne :
  - Téléphone : 01 83 75 52 16, lien `tel:+33183755216` ;
  - E-mail : drfranckmoyal@gmail.com, lien `mailto:` avec l'objet demandé ;
- viennent ensuite deux boutons côte à côte, « Appeler le cabinet » et « Écrire au cabinet ».
  Ils ont le même style, celui du bouton principal gelé, donc la même importance ;
- aucune phrase n'invite à envoyer des documents médicaux.

**Page Paris 9** (§4) :
- le bloc final s'intitule « Prendre rendez-vous ou contacter le cabinet » ;
- il donne « Par téléphone » et « Par e-mail », tous deux cliquables ;
- il garde son bouton « Prendre rendez-vous », qui mène à la page Contact.

La fiche dit « Remplacer le bloc final actuel par… » : l'adresse n'y figure donc plus. Elle
reste dans la section « Cabinet et activité hospitalière » et dans la FAQ de la page.

**Pied de page des 23 pages** : l'e-mail figure sous le téléphone, cliquable.

**Même lien partout.** L'adresse e-mail est cliquable avec le même lien, objet compris, y
compris dans les mentions légales, dont le texte ne change pas.

### Données structurées

**`sameAs` de `Person#franck-moyal`** : les 6 profils de la liste V1.3. TikTok et le profil
auteur du Fil Dentaire s'ajoutent aux quatre précédents. Les six adresses répondent.

**Cabinet** : une entité distincte, `https://drfranckmoyal.fr/#practice`, de type `Dentist`,
présente sur chaque page.
- Elle porte le nom « Dr Franck Moyal », l'adresse, le téléphone et l'e-mail
  (`mailto:drfranckmoyal@gmail.com`).
- `Person` la désigne comme lieu d'exercice (`workLocation`) au lieu de répéter l'adresse.
- La fiche Google reste hors du `sameAs` de Franck. Elle ira dans celui du cabinet quand son
  adresse publique stable sera connue.

**DentCA et Smileclub Formation** : deux organisations distinctes, reliées à Franck par
`founder`, hors de ses `sameAs`.
- DentCA : `#dentca`, de type `Organization`.
- Smileclub Formation : `#smileclub-formation`, de type `EducationalOrganization`. C'est le
  type déjà retenu sur la page Franck. Je l'ai gardé pour que les deux pages décrivent la même
  organisation.

### Liens vers DentCA et Smileclub Formation

Les libellés sont ceux demandés. Ils s'affichent comme les autres liens externes du site et
s'ouvrent dans un nouvel onglet.
- **DentCA** : en fin de la section DentCA de la page TCA.
- **Smileclub Formation** : dans la section Smileclub Formation de la page Conférences, juste
  avant le lien Blendi qui la clôt.

### robots.txt et visuels

**robots.txt** : politique ouverte, avec la ligne de commentaire demandée. Aucun robot n'est
bloqué, et aucun blocage n'a été créé chez l'hébergeur.

**Aucun emplacement d'image vide sur le site public.**
- Les 28 emplacements, dont 6 sur le golden master, disparaissent en production.
- Sur les pages suivantes, une section prévue avec image se compose alors comme une section
  sans image.
- Pour une revue, `EMPLACEMENTS=1` les fait réapparaître à leur place.

**Sur les 3 pages gelées, les compositions ne changent pas.** Les sections prévues avec image
gardent leur texte d'un côté, et l'autre moitié reste vide sur ordinateur jusqu'aux photos :
- les deux piliers de l'accueil ;
- « Pratique esthétique » sur la page Franck ;
- « Quand les dents commencent à changer » et « Restaurer l'esthétique et la fonction
  ensemble » sur la page Usures.

**Page 06, §9** : trois emplacements, masqués pour l'instant :
- le cas de MIH dans la nouvelle section MIH ;
- la macro dans « Pourquoi une tache blanche paraît-elle blanche ? » ;
- l'autre cas dans « Qu'est-ce que l'érosion-infiltration de résine ? ».

**Aucune photo de patient n'est publiée.**

## 2. Contrôles

### Textes (`npm run verify`)

Sur les 20 pages : aucun passage oublié, rien d'ajouté, aucun écart de renvois. Les deux
boutons de la page Contact sont listés comme décidés hors du pack.

### HTML et données structurées (`node scripts/check-html.mjs`)

Réussi sur les 23 pages. Les nouveaux contrôles vérifient :
- qu'aucune mention de rendez-vous en ligne ne reste ;
- que le téléphone et l'e-mail sont cliquables dans le pied de page ;
- la section Contact : son titre, le téléphone et l'e-mail cliquables, les deux boutons ;
- le bloc final de la page Paris 9 ;
- les 6 profils `sameAs` ;
- le cabinet `#practice`, complet sur les 23 pages ;
- les deux organisations et leurs liens visibles ;
- qu'aucun emplacement vide n'est visible ;
- que le robots.txt est ouvert.

### Avant mise en ligne et mobile

- **`npm run launch-check`** : aucun point bloquant.
- **H1 de la page 06** : 4 lignes à 390 px, la limite V16 est respectée. Aucun des 23 H1 ne
  dépasse 4 lignes.

### Rapidité (Lighthouse)

Page 06 sur mobile, 3 passages :

| Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | CLS | Poids |
|---|---|---|---|---|---|---|
| 99 | 100 | 100 | 100 | 2,0 s | 0 | 200 Ko |

### Références de la page 06 (PubMed)

Les 7 références existent. Auteurs, revues, années et DOI concordent. Deux détails de citation :
- [4] Kosys : le titre PubMed contient en plus « (International Caries Detection and Assessment
  System (ICDAS) ≤ 2) », après « White Spot Lesions » ;
- [7] : PubMed indexe la première autrice sous « Sara Mistry N » ; le pack écrit « Mistry NS ».

### Golden master

J'ai fabriqué le site avec les emplacements visibles. Les 3 pages gelées sont alors identiques,
octet pour octet, à la version d'avant le correctif, sauf deux choses :
- la ligne e-mail du pied de page ;
- les données structurées.

Les réglages de design sont inchangés : `tokens.css` est identique à l'étiquette
`golden-master-gele`.

## 3. Remarques

- **Titre de la section Contact.** Sur ordinateur comme sur mobile, « Prendre rendez-vous ou
  nous écrire » passe à la ligne au trait d'union de « rendez-vous » : « Prendre rendez- /
  vous ou nous écrire ». La cause est la largeur des titres, gelée. La typographie française
  l'admet ; un titre plus court l'éviterait.
- **Nom de la fiche Google.** « Dr Franck Moyal » se règle dans le compte Google Business
  Profile de Franck, pas sur le site.
- **Page 404.** Le pack n'en prévoit pas. Une adresse inexistante affiche la page d'Hostinger,
  en anglais. Faut-il un texte ?
- **Mentions légales.** La loi demande le téléphone de l'hébergeur. Les conditions d'Hostinger
  n'en donnent pas ; Franck peut le demander à leur support.

## 4. Photos : ce qu'il faut avant de les intégrer

Franck confirme que les consentements des 22 photos sont recueillis. Selon ton correctif, trois
points restent à confirmer pour chaque cas retenu :
1. le consentement écrit couvre bien la **publication web** ;
2. **cas d'érosion liée à un TCA** : le consentement couvre-t-il une information de santé
   sensible ? Sinon, le cas n'illustre pas un TCA ;
3. **cas de MIH avec éclaircissement** : le patient avait-il 18 ans ou plus au moment du
   traitement ?

Reste ensuite ta répartition et tes légendes, selon tes priorités (§8) : composite, facettes,
éclaircissement, MIH / ICON, usures et réhabilitation, érosion.

## 5. Mise en ligne

- **Hébergement.** Le site est hébergé chez Hostinger, sur le compte de Franck, et visible à une
  adresse provisoire, que Google n'indexe pas.
- **Domaine.** Il reste à brancher le domaine chez OVH, avec l'accord de Franck, puis à activer
  le https.
- **Déclaration.** Enfin, déclarer le site à Google Search Console et à Bing Webmaster Tools.
