# FICHE CORRECTIVE — CONTACT PATIENT PAR TÉLÉPHONE + E-MAIL
## À joindre au patch pré-lancement V1.3 — 22 septembre 2026

Cette fiche complète et **supersède uniquement les instructions de contact** du fichier
`DECISIONS_PRE_LANCEMENT_V1_3.md`.

## 1. Décision

Le cabinet utilise désormais **deux canaux officiels de contact patient, au même niveau** :

- **Téléphone** : 01 83 75 52 16
- **E-mail** : drfranckmoyal@gmail.com

L’e-mail ne doit donc plus apparaître uniquement dans les mentions légales. Il doit être utilisé
de façon visible pour :
- les demandes de rendez-vous ;
- les questions avant consultation ;
- les demandes d’information concernant un motif de consultation ;
- les échanges préalables lorsqu’un patient souhaite préciser sa situation.

Aucun formulaire de contact n’est demandé à ce stade.

---

## 2. Destination des CTA du site

La règle globale reste inchangée :

**Tous les boutons « Prendre rendez-vous » / « Rendez-vous » du site pointent vers :**

`/contact/#prendre-rendez-vous`

Cela concerne :
- header desktop ;
- header mobile ;
- hero de l’accueil ;
- CTA de fin de page ;
- page Paris 9 ;
- footer ;
- toute autre occurrence équivalente.

La page Contact présente ensuite immédiatement les deux possibilités : **appeler ou écrire**.

---

## 3. Page Contact — contenu définitif

### Titre de section

Remplacer :

**Prendre rendez-vous**

par :

**Prendre rendez-vous ou nous écrire**

Conserver l’ancre :

`id="prendre-rendez-vous"`

### Texte introductif

Afficher :

> Vous pouvez contacter le cabinet par téléphone ou par e-mail pour une demande de rendez-vous,
> une question avant consultation ou pour préciser votre motif de consultation.

### Bloc téléphone

**Téléphone**  
01 83 75 52 16

Lien :

`tel:+33183755216`

Libellé d’action recommandé :

**Appeler le cabinet**

### Bloc e-mail

**E-mail**  
drfranckmoyal@gmail.com

Lien :

`mailto:drfranckmoyal@gmail.com?subject=Demande%20de%20rendez-vous%20-%20Dr%20Franck%20Moyal`

Libellé d’action recommandé :

**Écrire au cabinet**

Les deux actions doivent avoir une importance visuelle comparable, dans le langage graphique gelé.

---

## 4. Page « Chirurgien-dentiste Paris 9 »

Remplacer le bloc final actuel par :

### Prendre rendez-vous ou contacter le cabinet

**Par téléphone**  
01 83 75 52 16

**Par e-mail**  
drfranckmoyal@gmail.com

Le bouton principal peut rester :

**Prendre rendez-vous**

et pointer vers :

`/contact/#prendre-rendez-vous`

L’adresse e-mail doit être cliquable avec le même `mailto:` que sur la page Contact.

---

## 5. Footer — 23 pages

Ajouter l’e-mail professionnel au footer à côté du téléphone :

**01 83 75 52 16**  
**drfranckmoyal@gmail.com**

Liens :
- téléphone → `tel:+33183755216`
- e-mail → `mailto:drfranckmoyal@gmail.com?subject=Demande%20de%20rendez-vous%20-%20Dr%20Franck%20Moyal`

Ne pas remplacer le téléphone par l’e-mail : les deux restent visibles.

---

## 6. Mentions légales

Conserver l’adresse :

`drfranckmoyal@gmail.com`

Aucune autre modification des mentions légales n’est requise par cette fiche.

---

## 7. Données structurées

Dans l’entité `Person#franck-moyal` et/ou l’entité locale `#practice`, utiliser l’adresse e-mail
uniquement si cela correspond à la stratégie actuelle de données structurées du site et sans
dupliquer inutilement les propriétés.

Valeur canonique :

`mailto:drfranckmoyal@gmail.com`

Ne pas créer de nouvelle entité uniquement pour l’e-mail.

---

## 8. Confidentialité / information patient

L’e-mail est un canal de contact général. Le site ne doit pas inviter explicitement les patients
à transmettre par e-mail des informations médicales détaillées, photographies cliniques ou
documents sensibles non sollicités.

Ne pas ajouter de phrase du type « envoyez-nous vos photos/radiographies par e-mail » sans
décision ultérieure sur le canal sécurisé approprié.

---

## 9. Contrôles Claude Code après correction

Relancer :
- `npm run verify`
- contrôle HTML / liens
- `npm run launch-check`

Vérifier en particulier :
1. aucun texte « prise de rendez-vous en ligne » ne subsiste ;
2. téléphone et e-mail sont cliquables ;
3. tous les CTA globaux continuent de pointer vers `/contact/#prendre-rendez-vous` ;
4. la section Contact expose immédiatement les deux canaux ;
5. le footer affiche téléphone + e-mail sur desktop et mobile ;
6. aucun changement de token ou de composant du Golden Master.

## Priorité en cas de conflit

Cette fiche est **postérieure au patch V1.3**.

Pour tout ce qui concerne les coordonnées et la prise de contact patient, elle a donc priorité
sur `DECISIONS_PRE_LANCEMENT_V1_3.md` et `MESSAGE_CLAUDE_PATCH_V1_3.md`.
