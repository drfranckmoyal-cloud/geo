# DÉCISIONS PRÉ-LANCEMENT — V1.3
## drfranckmoyal.fr — 22 septembre 2026

## 1. Rendez-vous
Supprimer partout les libellés « Prise de rendez-vous en ligne » : il n’y aura pas de réservation en ligne.

### Page Paris 9
Afficher :
**Prendre rendez-vous par téléphone**  
**01 83 75 52 16**

### Page Contact
Afficher :
**Par téléphone**  
**01 83 75 52 16**

Tous les CTA « Prendre rendez-vous » / « Rendez-vous » gardent comme destination définitive :
`/contact/#prendre-rendez-vous`

## 2. `sameAs` de `Person#franck-moyal`
Conserver :
- LinkedIn : https://www.linkedin.com/in/franck-moyal-7581b6161/
- Instagram : https://www.instagram.com/drfranckmoyal/
- AP-HP : https://www.aphp.fr/dr-moyal-franck
- Blendi : https://blendi.fr/formateurs/franck-moyal

Ajouter :
- TikTok : https://www.tiktok.com/@drfranckmoyal
- Le Fil Dentaire — profil auteur : https://www.lefildentaire.com/auteur/franck-moyal/

Ne pas mettre DentCA ni Smileclub Formation dans `sameAs` de Franck : ce sont des organisations distinctes.

## 3. Fiche Google
Ne pas rattacher la fiche Google au `sameAs` de `Person#franck-moyal` pour l’instant.

Créer / conserver une entité locale distincte :
`https://drfranckmoyal.fr/#practice`
Type Schema.org : `Dentist`

Quand l’URL publique stable de la fiche Google sera disponible, l’ajouter au `sameAs` de `#practice`.

### Nom de la fiche Google
Le nom actuel « Docteur Franck Moyal - Esthétique du sourire / Usures dentaires et TCA » est à simplifier, sauf si cette formulation complète est réellement utilisée de façon cohérente sur la signalétique et les documents professionnels.

Nom recommandé :
**Dr Franck Moyal**

Les notions « dentisterie esthétique », « usures dentaires » et « TCA » doivent être travaillées dans les catégories, services, description, site et contenus — pas ajoutées artificiellement au nom de la fiche.

## 4. DentCA et Smileclub Formation
Créer deux entités `Organization` distinctes reliées à Franck par `founder`.

### DentCA
URL : https://dentca-asso.com/  
Lien visible depuis la page TCA :
**Découvrir DentCA — prévention et santé bucco-dentaire dans les TCA**

### Smileclub Formation
URL : https://smileclubformations.com/  
Lien visible depuis la page Conférences et formations :
**Découvrir Smileclub Formation — formations pour chirurgiens-dentistes**

## 5. Robots IA
Décision : **autoriser la recherche, la récupération et l’entraînement**.

Le but du site est la diffusion maximale de l’identité professionnelle et des contenus publics. L’autorisation des robots d’entraînement n’est pas nécessaire pour être cité dans les recherches IA, mais il n’existe ici pas d’objectif de protection d’un corpus propriétaire qui justifierait leur blocage.

Conserver une politique ouverte et future-proof :
```txt
# Search engines and AI crawlers are intentionally allowed.
User-agent: *
Allow: /
```

Si le fichier robots.txt énumère déjà les agents individuellement, autoriser explicitement au minimum :
- Googlebot
- Bingbot
- OAI-SearchBot
- ChatGPT-User
- PerplexityBot
- Perplexity-User
- Claude-SearchBot
- Claude-User
- Applebot
- GPTBot
- ClaudeBot
- Google-Extended
- Applebot-Extended
- CCBot

Ne pas créer de blocage WAF/CDN qui contredirait robots.txt. En cas de trafic excessif, limiter la charge sans bloquer les robots de recherche/citation prioritaires.

## 6. Page 06 — MIH
Remplacer le fichier 06 V1.2 par :
`06_taches-dentaires-dyschromies-icon_V1_3.md`

Objectifs :
- MIH visible dans H1, title, meta et réponse directe ;
- vraie section patient « peut-on traiter chez l’enfant / adolescent ? » ;
- ne pas imposer d’attendre l’âge adulte ;
- ne pas suggérer un éclaircissement au peroxyde chez les moins de 18 ans ;
- prioriser le vrai cas clinique MIH dans les visuels.

## 7. Visuels
### Règle de production
Un emplacement sans visuel validé **disparaît en production**. Aucun placeholder gris ou « image à venir » ne doit rester sur le site public.

### Consentement
Aucun cas clinique patient n’est publié sans consentement écrit couvrant explicitement la publication web.

### Cas érosion / TCA
Par défaut, **ne pas publier le diagnostic « boulimie » dans la légende**.

Si le consentement ne couvre pas explicitement la publication d’une information de santé sensible, ne pas utiliser le cas pour illustrer un TCA.

Si l’image est utilisée hors contexte TCA, légende neutre possible :
**« Usure érosive avec raccourcissement antérieur — exemple clinique »**

Le cas d’érosion exogène est prioritaire sur la page Érosion pour éviter toute ambiguïté.

## 8. Emplacements visuels — stratégie
Prioriser les visuels qui constituent une preuve clinique :
1. Composite
2. Facettes
3. Éclaircissement
4. MIH / ICON
5. Usures / réhabilitation
6. Érosion

Ne pas chercher à remplir artificiellement les 28 emplacements. La qualité et la cohérence des cas priment sur le nombre d’images.
