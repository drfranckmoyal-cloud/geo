# Réponse de ChatGPT aux points 17 à 20 du fichier maître

*Transmise par Franck dans la conversation Claude du 21/09/2026. Archivée telle quelle.
Fait foi pour les textes qu'elle apporte, en attendant leur intégration dans une prochaine
version du pack (décisions D10 à D13 du fichier maître).*

---

Oui. Les quatre remarques sont bonnes, avec une petite correction sur le point 2. Voilà ce que je répondrais et ce que je ferais modifier dans le pack.

1. Menu du haut : il faut le figer explicitement. Je retiens pour le menu desktop final : Dentisterie esthétique · Usures dentaires · Érosion & TCA · Dr Franck Moyal · Publications & enseignement, puis à droite le CTA Prendre rendez-vous. Le nom/logo Dr Franck Moyal à gauche renvoie vers la Home, donc inutile d’ajouter « Accueil ». « Publications & enseignement » pourra ouvrir plus tard vers Publications, Conférences & formations, Activité hospitalière et Médias. Pendant le Golden Master, on affiche déjà cette architecture pour valider le header, même si toutes les routes ne sont pas encore construites.
2. Je valide complètement l’idée question + grand titre, mais pas “Non.” seul. Il n’existe pas de règle Google disant que les H2 en forme de question sont systématiquement préférés. En revanche, reprendre les formulations réelles des patients rend les sections beaucoup plus lisibles et extractibles. Je ferais donc :
petite étiquette : Faut-il toujours traiter une usure dentaire ?
grand H2 : Non : toutes les usures ne nécessitent pas une reconstruction
C’est meilleur sémantiquement que « Non. » tout seul et on conserve exactement l’intention conversationnelle que l’on veut pour le GEO. Google recommande par ailleurs des intitulés et liens descriptifs plutôt que des libellés qui n’ont de sens qu’avec leur contexte.
3. Oui, les quatre sous-parties sont actuellement incomplètes. Je mets ce texte :
Attrition et contraintes mécaniques
L’attrition correspond à une usure liée aux contacts entre les dents. Elle peut être favorisée par certaines contraintes fonctionnelles ou parafonctionnelles, notamment le bruxisme, mais la présence d’une usure ne permet pas à elle seule de conclure à un bruxisme.
Érosion dentaire
L’érosion correspond à une perte de substance favorisée par des acides d’origine alimentaire ou intrinsèque, par exemple en cas de reflux ou de vomissements. Une surface fragilisée chimiquement devient également plus sensible aux contraintes mécaniques.
Abrasion
L’abrasion correspond à une usure provoquée par l’action répétée d’un élément extérieur à la dent : certaines habitudes, un brossage traumatique ou d’autres contraintes mécaniques peuvent y participer.
Usures multifactorielles
En pratique, les mécanismes sont souvent associés. Une même dent peut subir à la fois une agression acide et des contraintes mécaniques. Le diagnostic consiste donc surtout à identifier les facteurs dominants et modifiables, plutôt qu’à chercher une cause unique.
4. Oui, il manque le lien Bruxisme. Je mets, juste après le bloc Attrition ou à la fin de « Pourquoi les dents s’usent-elles ? » :
→ Comprendre le bruxisme et son rôle dans l’usure dentaire
qui pointe vers `/bruxisme-usure-dentaire/`. C’est beaucoup mieux que « En savoir plus » : Google recommande des textes d’ancrage descriptifs qui permettent de comprendre la destination du lien même hors contexte.

Donc sur les quatre points : 1 corrigé, 2 accepté avec H2 plus descriptif, 3 à compléter, 4 à ajouter. C’est exactement le genre de retour que je veux que Claude nous fasse avant de coder : ça permet de fermer les trous du pack au lieu de les découvrir dans le rendu.
