# Suivi quotidien de la visibilité dans les IA

*Mis en place le 21 octobre 2026, à la demande de Franck : « quotidien, avec une liste très
exhaustive des recherches » (décision D88).*

## Ce que c'est

Chaque matin vers 9 h, un agent pose **83 questions** — celles qu'un patient ou un confrère
écrirait — à trois IA, et note pour chacune :

- si la réponse **nomme Franck** ;
- si elle s'appuie sur **drfranckmoyal.fr** comme source ;
- **qui elle cite à sa place** : les sites et les confrères nommés.

C'est le pendant, pour les IA, du relevé des positions Google (`suivi/releves/`), qui tourne
à 8 h et ne mesure que le référencement classique.

## Les trois moteurs suivis

| Moteur | Ce que c'est |
|---|---|
| **Aperçu IA de Google** | Le paragraphe écrit par l'IA en tête d'une recherche ordinaire. Ce que voient la plupart des patients. Il n'apparaît pas sur toutes les recherches. |
| **Mode IA de Google** | La conversation de Google qui remplace la page de résultats. |
| **ChatGPT** | Avec la recherche web, en **conversation temporaire** : rien ne s'inscrit dans l'historique de Franck, et ChatGPT ne se sert pas de ce qu'il sait déjà de lui (sans cela, il répond « ton site »). |

**Pas encore suivis, faute d'une action de Franck** (vérifié le 21/10/2026) :

| Moteur | Ce qui bloque | Ce que Franck doit faire, une fois |
|---|---|---|
| Gemini | Google demande d'accepter les conditions de Gemini au premier usage. | Ouvrir gemini.google.com dans Chrome et cliquer « Utiliser Gemini ». |
| Copilot | Microsoft demande d'accepter la mise à jour de ses conditions de service. | Ouvrir copilot.microsoft.com dans Chrome et accepter. |
| Perplexity | Sans compte, Perplexity répond « Inscrivez-vous et répétez votre demande ». | Se connecter à perplexity.ai dans Chrome (avec Google, par exemple). |

Claude ne peut ni accepter des conditions ni se connecter à la place de Franck. Une fois
débloqué, un moteur s'ajoute en écrivant son lecteur dans `LECTEURS.md`, en le testant, et en
l'ajoutant à `questions.json` et à la tâche.

## Les fichiers

| | |
|---|---|
| `questions.json` | Les 83 questions, en 11 familles. **C'est ici qu'on ajoute ou retire une question.** |
| `LECTEURS.md` | Les trois petits programmes qui lisent chaque page de réponse. |
| `noter.mjs` | Enregistre les lectures dans le relevé du jour, au fil de l'eau. `--reste` dit ce qui manque. |
| `comparer.mjs` | Compare le dernier relevé au précédent. |
| `releves/AAAA-MM-JJ.json` | Un relevé par jour. |

## Lire un relevé

**« Cité »** veut dire : la réponse nomme Franck, ou cite son site comme source. Pour la
famille « Marque », dont les questions contiennent déjà son nom, seul compte le site : la
question est de savoir si l'IA parle de lui **à partir de son site** ou à partir d'ailleurs.

Les IA ne répondent jamais deux fois pareil, même quand rien n'a changé. **Un gain ou une
perte isolés ne veulent rien dire** : ce qui compte, c'est la tendance sur une ou deux
semaines.

Deux biais à garder en tête : les recherches partent du Chrome de Franck, connecté à son
compte Google et situé à Paris, et Google personnalise un peu ses réponses. Et le Mode IA
comme ChatGPT localisent : « à Paris » dans la question favorise les cabinets parisiens,
ce qui est le but.

## Si Google bloque

Plus de 160 recherches Google par jour depuis le même navigateur peuvent déclencher le test
« je ne suis pas un robot ». L'agent s'arrête alors aussitôt côté Google, sans jamais toucher
au test, et note les lectures manquantes `anti-robot`. Si cela se répète, il faudra alléger :
ne garder qu'un des deux moteurs Google, ou faire tourner la liste sur deux jours.

## Ajouter une question

Ouvrir `questions.json`, ajouter la ligne dans la bonne famille, entre guillemets, avec une
virgule. Elle est suivie le lendemain matin.
