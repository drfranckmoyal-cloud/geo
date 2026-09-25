<!-- Archivé tel quel par Claude Code le 25/09/2026. Consigne de ChatGPT, transmise par Franck après
avoir repéré une phrase de stratégie GEO publiée sur /medias-interviews/. Rapport rendu dans
AUDIT_ANTI_PROMPT_DRFRANCKMOYAL.md, à la racine du dépôt. Ne pas modifier ce fichier. -->

# AUDIT URGENT — RECHERCHE ET SUPPRESSION DE TEXTES INTERNES / PROMPTS SUR LE SITE PUBLIC
Un problème important a été détecté sur le site public `drfranckmoyal.fr`.
La page :
`/medias-interviews/`
contient actuellement du texte provenant manifestement d'un prompt, d'instructions de rédaction ou d'informations internes qui n'auraient jamais dû être publiées.
OBJECTIF
Effectuer un audit EXHAUSTIF de l'ensemble du site et du code source afin de vérifier qu'aucun autre contenu de ce type n'est exposé publiquement.
Il ne s'agit PAS de vérifier uniquement `/medias-interviews/`.
Il faut contrôler toutes les pages publiques, tous les contenus rendus et toutes les sources de texte utilisées pour construire le site.
1. PRIORITÉ IMMÉDIATE : `/medias-interviews/`
Commencer par examiner intégralement :
`/medias-interviews/`
Identifier précisément :

* le ou les passages anormaux ;
* leur emplacement dans le code ;
* leur origine ;
* la raison pour laquelle ils ont été rendus publiquement.

Supprimer tout texte correspondant à :

* prompt ;
* instruction destinée à Claude ;
* instruction destinée à ChatGPT ;
* note de travail ;
* commentaire éditorial interne ;
* indication SEO/GEO destinée au développeur ;
* instruction de mise en page ;
* texte du type « ajouter ici », « vérifier », « ne pas inventer », etc. ;
* commentaire expliquant ce que le contenu devrait faire au lieu de constituer le contenu lui-même.

IMPORTANT :
Ne pas supprimer aveuglément tout le bloc.
Conserver le véritable contenu éditorial destiné aux patients ou visiteurs et retirer uniquement ce qui relève des instructions internes.
2. CRAWL COMPLET DU SITE
Construire la liste exhaustive de toutes les URL publiques/indexables du site.
Utiliser notamment :

* routes du projet ;
* sitemap ;
* pages statiques ;
* pages générées ;
* pages de cas cliniques ;
* pages éditoriales ;
* pages professionnelles ;
* pages de traitement ;
* pages légales si nécessaire.

Ne pas se limiter aux pages présentes dans le menu.
Inclure également les pages accessibles uniquement par maillage interne ou sitemap.
Comparer la liste obtenue aux URL du sitemap afin de détecter :

* page oubliée ;
* route orpheline ;
* contenu publié accidentellement ;
* ancienne page encore accessible.

3. ANALYSER 100 % DU TEXTE PUBLIC
Pour CHAQUE page, examiner tout le texte susceptible d'être envoyé au navigateur.
Cela comprend notamment :

* H1 ;
* H2/H3/H4 ;
* paragraphes ;
* listes ;
* FAQ ;
* tableaux ;
* boutons ;
* CTA ;
* breadcrumbs ;
* légendes ;
* crédits ;
* textes alternatifs des images ;
* attributs title ;
* aria-label ;
* title SEO ;
* meta description ;
* OpenGraph ;
* Twitter metadata ;
* JSON-LD ;
* données structurées ;
* contenu masqué par CSS ;
* contenu responsive ;
* contenu des composants réutilisés ;
* contenu présent dans le HTML même s'il n'est pas immédiatement visible.

4. RECHERCHE AUTOMATIQUE DE MARQUEURS SUSPECTS
Faire également une recherche globale dans l'ensemble du repository.
Rechercher notamment, sans limiter l'audit à cette liste :
`prompt`
`instruction`
`instructions`
`Claude`
`Claude Code`
`ChatGPT`
`GPT`
`LLM`
`IA`
`AI`
`TODO`
`FIXME`
`placeholder`
`à compléter`
`à vérifier`
`à confirmer`
`ne pas inventer`
`ne pas mentionner`
`ne pas dire`
`ne pas écrire`
`ajouter ici`
`insérer`
`remplacer`
`supprimer`
`garder`
`conserver`
`utiliser`
`SEO`
`GEO`
`keyword`
`mot-clé`
`schema`
`JSON-LD`
`canonical`
`indexable`
`maillage`
`CTA`
`brief`
`draft`
`brouillon`
`version finale`
`source de vérité`
`locked`
`verrouillé`
`Claude doit`
`le site doit`
`la page doit`
`le texte doit`
`objectif`
`consigne`
`note interne`
ATTENTION :
Certains termes comme « IA », « SEO », « objectif », « traitement », etc. peuvent évidemment être légitimes dans un contenu public.
La présence du mot n'est donc PAS suffisante pour supprimer un passage.
Chaque occurrence doit être examinée dans son contexte.
5. RECHERCHER LES FORMULATIONS TYPIQUES D'UN PROMPT
Ne pas faire uniquement une recherche par mots-clés.
Détecter également les phrases qui ressemblent sémantiquement à une instruction adressée à un rédacteur ou à un développeur.
Exemples :

* « Cette section doit... »
* « L'objectif de cette page est... »
* « Ne pas... »
* « Il faut... »
* « Ajouter un lien vers... »
* « Utiliser cette formulation... »
* « Cette page doit permettre... »
* « Pour le SEO... »
* « Pour le GEO... »
* « Le lecteur doit comprendre... »
* « Claude devra... »
* « Conserver ce texte... »
* « Ne pas faire de promesse... »
* « Éviter les formulations... »
* « Insérer les photographies... »

Une phrase peut être une fuite de prompt même si elle ne contient aucun des mots-clés précédents.
6. DISTINGUER TROIS CATÉGORIES
Pour chaque élément suspect, classer :
A — FUITE CERTAINE
Instruction interne, prompt, note de travail ou texte développeur clairement publié par erreur.
→ Corriger immédiatement.
B — SUSPECT
Texte qui pourrait être éditorial mais dont la formulation semble provenir d'une instruction interne.
→ Ne pas supprimer automatiquement.
→ Le signaler dans le rapport pour validation.
C — NORMAL
Contenu éditorial légitime.
→ Ne rien modifier.
L'objectif est d'éviter à la fois les faux négatifs ET les suppressions abusives.
7. VÉRIFIER LES COMPOSANTS PARTAGÉS
Une erreur dans un composant commun peut contaminer plusieurs pages.
Examiner donc particulièrement :

* Header
* Footer
* Navigation
* Breadcrumbs
* CTA
* FAQ
* blocs de cas cliniques
* blocs auteur
* composants SEO
* composants Schema
* composants images
* composants éditoriaux réutilisés.

Si un texte anormal provient d'un composant partagé, corriger sa source et vérifier toutes les pages qui l'utilisent.
8. VÉRIFIER AUSSI LE CODE NON RENDU
Chercher les prompts/instructions présents dans le repository même lorsqu'ils ne sont pas actuellement visibles.
Je veux identifier les contenus qui pourraient être accidentellement publiés lors d'une future modification.
Examiner notamment :

* fichiers de données ;
* JSON ;
* Markdown ;
* MDX ;
* constantes ;
* fichiers de configuration éditoriale ;
* contenus stockés dans des objets TypeScript/JavaScript ;
* anciens composants ;
* commentaires contenant des contenus destinés à être injectés ;
* fichiers de génération de pages.

Ne pas supprimer les véritables documents de développement simplement parce qu'ils contiennent des instructions.
Le but ici est de repérer les données éditoriales internes susceptibles d'être rendues par erreur.
9. CONTRÔLE DU BUILD FINAL
Après correction :

1. lancer le build de production ;
2. crawler le build réellement généré ;
3. extraire le texte/HTML final de toutes les pages ;
4. refaire la recherche anti-prompt sur le résultat du build.

La vérification du code source seule n'est PAS suffisante.
Je veux une validation du contenu réellement produit pour le navigateur.
10. CONTRÔLE DE `/medias-interviews/`
Après correction, vérifier particulièrement que cette page :

* ne contient plus aucune instruction interne ;
* conserve son véritable contenu ;
* conserve son title ;
* conserve sa meta description ;
* conserve son canonical ;
* reste indexable ;
* conserve ses données structurées pertinentes ;
* conserve son maillage interne ;
* ne présente pas de régression visuelle.

11. NE PAS PROFITER DE CET AUDIT POUR RÉÉCRIRE LE SITE
C'est important.
Cet audit n'est PAS une nouvelle phase de rédaction ou de redesign.
Ne pas :

* réécrire arbitrairement les pages ;
* modifier le positionnement ;
* changer les H1 sans nécessité ;
* modifier les URL ;
* modifier le design général ;
* changer les textes validés simplement pour les améliorer ;
* créer de nouvelles pages ;
* modifier l'architecture SEO sans rapport avec le problème.

Corriger uniquement :

1. les fuites certaines ;
2. les erreurs directement liées ;
3. les éventuelles conséquences techniques de ces erreurs.

Les éléments seulement suspects doivent être signalés pour validation.
12. RAPPORT FINAL OBLIGATOIRE
À la fin, produire un rapport intitulé :
`AUDIT_ANTI_PROMPT_DRFRANCKMOYAL.md`
Le rapport doit indiquer :
Périmètre

* nombre total d'URL contrôlées ;
* nombre de pages indexables ;
* nombre de fichiers source analysés ;
* build contrôlé ou non.

Fuites certaines détectées
Pour chacune :

* URL ;
* texte problématique ;
* source/fichier ;
* origine probable ;
* correction effectuée.

Éléments suspects
Pour chacun :

* URL ;
* extrait ;
* raison du doute ;
* aucune modification sans validation si le caractère interne n'est pas certain.

Contrôle automatique
Indiquer les familles de marqueurs recherchées et le résultat.
Contrôle du build
Confirmer que l'ensemble du HTML final a été rescanné après correction.
Résultat final
Donner explicitement :
`Fuites certaines restantes : 0 / X`
`Éléments suspects restant à valider : X`
`Pages contrôlées : X / X`
Ne jamais écrire « tout est propre » si toutes les pages et tous les contenus rendus n'ont pas réellement été vérifiés.
13. IMPORTANT — ARRÊT APRÈS CETTE MISSION
Après :

* audit ;
* corrections certaines ;
* build ;
* second crawl ;
* rapport ;

STOP.
Ne pas poursuivre spontanément le développement du site.
Ne pas commencer une nouvelle phase SEO/GEO.
Me remettre uniquement le rapport complet afin que je puisse le transmettre à ChatGPT pour contre-vérification.
