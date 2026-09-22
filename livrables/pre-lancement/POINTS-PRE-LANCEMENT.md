# Pré-lancement — ce qui est intégré, ce qui reste à trancher

> **Note dépassée.** ChatGPT a tranché ces points dans son correctif pré-lancement V1.3 : voir
> `RAPPORT-CORRECTIF-V1-3.md`. L'hébergeur est désormais Hostinger (D43), et non OVH.

*Claude Code, 22 septembre 2026. Franck a rempli sa fiche de renseignements. Cette note liste ce
qui est déjà en place sur le site et les derniers arbitrages, pour ta revue avec lui des `sameAs`,
des robots d'IA et des visuels.*

---

## 1. Intégré sur le site

- **Téléphone du cabinet : 01 83 75 52 16**, cliquable sur mobile.
  - Où : pied de page des 23 pages, page Contact, bloc final de la page Paris 9, mentions légales.
- **Prise de rendez-vous** : pas de réservation en ligne, les patients appellent le cabinet.
  - Tous les boutons « Prendre rendez-vous » mènent à la section `#prendre-rendez-vous` de la page
    Contact, qui donne le téléphone : c'est désormais leur destination définitive.
- **Mentions légales** :
  - adresse électronique : `drfranckmoyal@gmail.com` ;
  - hébergeur : **OVH**, choisi par Franck ;
  - raison sociale : OVH SAS, SAS au capital de 10 069 020 €, RCS Lille Métropole
    424 761 419 00045 ;
  - adresse : 2 rue Kellermann, 59100 Roubaix, France ;
  - contact : 1007 depuis la France, +33 9 72 10 10 07.

  Coordonnées reprises des mentions légales d'OVHcloud ; le numéro vient de l'usage courant, à
  confirmer dans l'espace client OVH.
- **Profils officiels déclarés aux moteurs** (`sameAs` de `Person#franck-moyal`), ceux que tu avais
  retenus :
  - https://www.linkedin.com/in/franck-moyal-7581b6161/
  - https://www.instagram.com/drfranckmoyal/
  - https://www.aphp.fr/dr-moyal-franck
  - https://blendi.fr/formateurs/franck-moyal
- **Page Facettes** : DOI rétablis pour Alqutaibi (`10.1016/j.prosdent.2024.03.019`) et Klein
  (`10.1111/jerd.13351`).
- **Décisions de Franck** :
  - aucune mesure d'audience, donc aucun bandeau de cookies ;
  - aucun autre nom de domaine ;
  - déontologie vérifiée : la formule « exclusivement orientée », la mention de l'AP-HP, du GHU
    Paris et de la CMME, les règles des photos avant / après.

## 2. À trancher

### a. Pages 18 et 19 : « Prise de rendez-vous en ligne »

La page Paris 9 affiche « Prise de rendez-vous en ligne — lien à compléter », et la page Contact
« Prise de rendez-vous en ligne — URL à fournir ». Or il n'y aura pas de réservation en ligne.

Faut-il retirer ces deux lignes, ou les remplacer ? Donne le texte dans ce cas. Ce sont les deux
derniers emplacements « à fournir » visibles sur le site.

### b. Profils complémentaires fournis par Franck

- **TikTok** : https://www.tiktok.com/@drfranckmoyal — à ajouter aux `sameAs` ?
- **Fiche Google du cabinet** : identifiant Google `/g/11g901j57p`. Nom affiché : « Docteur Franck
  Moyal - Esthétique du sourire / Usures dentaires et TCA ». Deux questions :
  - l'ajouter aux `sameAs`, ou la réserver à une future description du cabinet (type `Dentist`) ;
  - ce nom chargé de mots-clés est-il cohérent avec les règles de Google pour les fiches
    d'établissement ?
- **DentCA** (https://dentca-asso.com/) et **Smileclub Formation**
  (https://smileclubformations.com/) : ce sont des organisations, pas des profils de Franck. Ma
  proposition : les décrire comme organisations fondées par lui (`founder` →
  `Person#franck-moyal`), plutôt qu'en `sameAs`. Faut-il aussi un lien vers leurs sites depuis les
  pages TCA (section DentCA) et Conférences (Smileclub Formation) ? Donne alors le libellé.

### c. Robots d'IA : Franck laisse ChatGPT et Claude recommander

Ma recommandation : **tout autoriser, y compris l'entraînement des modèles.**
- **Robots qui citent leurs sources** : Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User,
  PerplexityBot, Claude-SearchBot.
- **Robots d'entraînement** : GPTBot, Google-Extended, ClaudeBot, Applebot-Extended, CCBot.

C'est cohérent avec l'objectif GEO : que les IA connaissent et citent le Dr Moyal. Le contenu est
une information professionnelle publique, sans rien de réservé. Le robots.txt actuel autorise déjà
tout : la décision le rendrait seulement explicite, robot par robot.

Si tu préfères exclure l'entraînement, je bloque les cinq robots d'entraînement et garde ouverts
ceux qui citent leurs sources.

### d. Page 06, taches : demande de Franck

> Mettre bien l'emphase sur le traitement des taches de MIH — c'est une recherche assez fréquente
> — et dire qu'on peut traiter des patients assez jeunes si la tache les gêne.

La page n'en parle pas aujourd'hui : texte à rédiger dans une V1.3 du fichier 06. Le H1, le §9
(images) et la FAQ sont à revoir en conséquence.

### e. Visuels

Franck a trié **22 photos** (16 JPEG, 6 PNG), en 8 dossiers :

| Thème | Cas décrits par Franck |
|---|---|
| Composite | 1) composite sur 6 dents antérieures ; 2) sur 4 dents antérieures ; 3) composite stratifié sur une dent dyschromiée |
| Facettes | un cas en 3 temps : initial, projet, final |
| Éclaircissement | avant, puis après 4 semaines d'éclaircissement ambulatoire |
| Taches, ICON | 1) tache de MIH sur une incisive, éclaircissement puis érosion-infiltration (ICON) ; 2) dyschromie unitaire et tache blanche, éclaircissement puis érosion-infiltration |
| Érosion | 1) érosion d'origine exogène ; 2) érosion avec raccourcissement, due à un TCA (boulimie) |
| Bilan esthétique, usures et réhabilitation | légendes dans le dossier |
| Cabinet, scans de suivi | aucun |

Ce qui reste :

- **Consentement.** La fiche n'indique pas encore le consentement écrit de publication web pour
  chaque cas : c'est la condition de leur mise en ligne.
- **Le cas érosion lié à un TCA** demande une attention particulière. Ton fichier 12 exclut toute
  photo stigmatisante, et une légende qui nomme la boulimie désigne la pathologie du patient.
  Faut-il l'afficher, sous quelle légende, et sur quelle page ?
- **Emplacements.** Il y a 28 emplacements, dont 6 sur le golden master. Il faut décider de ce qui
  va où. Les emplacements sans photo disparaîtront-ils, ou attendront-ils ?

## 3. Contrôle avant mise en ligne (`npm run launch-check`)

Il reste 3 points :
1. les deux lignes « Prise de rendez-vous en ligne » (§2 a) ;
2. les visuels (§2 e) ;
3. la règle des robots d'IA (§2 c).

Ensuite, la mise en ligne elle-même :
- **hébergement OVH à souscrire par Franck** : sa commande du nom de domaine n'en comprenait pas ;
- **déclaration à Google Search Console et Bing Webmaster Tools**, avec le plan du site.
