#!/usr/bin/env python3
"""
Écrit deux pages d'actes qui n'existaient pas : Gingivectomie et Edge bonding
(site/gingivectomie-paris.html, site/edge-bonding-paris.html).

Franck, 22/11/2026 : « Crée-moi le contenu des pages : Gingivectomie — rentre dans le détail de la
gingivectomie, qui parfois nécessite un petit remodelage osseux, donc élongation coronaire. Laisse de
la place pour les photos cliniques : on va montrer 2 ou 3 avant/après, une photo d'un guide de
gingivectomie et une photo de planification 3D. Edge bonding : pareil, en insistant bien sur la
différence avec des gros composites : on joue seulement sur les bords pour modifier la ligne du
sourire et modifier les formes, mais plus fragile. »

Ce sont les pages D2 et D3 du plan du 20/11/2026 (D110). Le texte est de Claude ; le fond clinique
vient de ce que Franck a dit, de sa vidéo « Le sourire gingival », de la page Composite bonding déjà
validée, et de sources vérifiées sur PubMed le 22/11/2026. **Franck valide chaque affirmation clinique
avant la mise en ligne** : tant qu'il ne l'a pas fait, les deux pages restent dans `EN_ATTENTE` de
publier.py, et aucune page publique ne mène à elles.

Les photographies ne sont pas encore choisies : chaque emplacement est réservé et clairement signalé
(verrou V2), aux proportions de la photographie attendue.

Mise en page : celle des pages Usure, TCA et Bruxisme — une question par chapitre, la réponse en
tête. L'en-tête, le pied, les questions fréquentes (questions.txt) et leurs données structurées sont
tenus par generer.py, comme pour toute page écrite à la main.

    python3 docs/refonte/maquettes/ecrire-actes.py
"""
import html as H
import json
import os
import re

import generer as G

ICI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ICI, "site")
PHOTOS = "../../../../src/assets/photos/cas/"
POLICES = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
           '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:'
           'wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;'
           '8..60,700&display=swap">')
_EXT = 'target="_blank" rel="noopener"'


def lien(page, texte):
    return f'<a class="lt" href="{page}.html">{texte}</a>'


def source(auteurs, titre, revue, ref, doi, pmid):
    return {"auteurs": auteurs, "titre": titre, "revue": revue, "ref": ref, "doi": doi, "pmid": pmid}


# ══ Gingivectomie ══════════════════════════════════════════════════════════════════════════════════
GINGIVECTOMIE = {
    "slug": "gingivectomie-paris",
    "titre": "Gingivectomie à Paris : sourire gingival | Dr Franck Moyal",
    "description": ("Gingivectomie et élongation coronaire à Paris 9e : corriger un sourire gingival ou des dents "
                    "courtes, avec planification 3D et guide. Dr Franck Moyal."),
    "h1": "Gingivectomie",
    "sous_titre": "Sourire gingival, élongation coronaire",
    "fil": "Gingivectomie",
    "acte": {"@type": "MedicalProcedure", "name": "Gingivectomie",
             "alternateName": ["Élongation coronaire esthétique", "Correction du sourire gingival"]},
    "chapo": ("La gingivectomie retire l’excès de gencive qui recouvre les dents et leur rend leur vraie "
              "longueur, sans les toucher. Quand l’os est trop proche du futur bord de la gencive, un léger "
              "remodelage osseux lui est associé : c’est l’élongation coronaire. Dans les deux cas, le tracé se "
              "décide avant l’intervention, sur une planification en trois dimensions, et se reporte en bouche "
              "à l’aide d’un guide."),
    "couverture": ("reserve", "Avant / après n° 1",
                   "Emplacement réservé — premier avant / après d’une gingivectomie, sourire de face. "
                   "La légende sera écrite avec la photographie."),
    "chapitres": [
        {"q": "Qu’est-ce qu’une gingivectomie ?",
         "r": "C’est une petite intervention, réalisée sous anesthésie locale, qui retire l’excès de gencive "
              "recouvrant les dents et en redessine le contour. Les dents elles-mêmes ne sont pas touchées : "
              "on découvre la partie de la dent qui était cachée. Je la réalise au cabinet, à Paris 9<sup>e</sup>.",
         "blocs": [
             ("Trop de rose, pas assez de blanc",
              ["Un sourire gingival est un sourire qui montre beaucoup de gencive et peu de dents. Les dents "
               "paraissent courtes, parfois carrées, alors qu’elles ont souvent une longueur normale : une "
               "partie de leur émail est simplement restée sous la gencive."]),
             ("Ce que l’intervention change",
              ["La gingivectomie remonte le bord de la gencive à sa juste place et en redessine le contour, "
               "dent par dent : la hauteur visible de chaque dent, la symétrie entre le côté droit et le côté "
               "gauche, la courbe que suivent les gencives d’une canine à l’autre."]),
             ("Ce qu’elle ne touche pas",
              ["Les dents. Ni taille, ni facette, ni composite : la gingivectomie ne fait que découvrir ce qui "
               "existe déjà. C’est ce qui en fait, quand elle est bien indiquée, l’une des corrections les "
               "moins invasives du sourire."]),
         ],
         "cote": [("fiche", "En bref", ["Sous anesthésie locale", "En une séance, au cabinet",
                                        "Les dents ne sont pas touchées", "Un tracé décidé à l’avance",
                                        "Parfois associée à un léger remodelage de l’os"])]},
        {"q": "Dans quels cas propose-t-on une gingivectomie ?",
         "r": "Quand la gencive recouvre une partie de la couronne des dents : sourire gingival, dents qui "
              "paraissent courtes, contours inégaux d’une dent à l’autre. Elle n’est pas la réponse quand le "
              "sourire gingival vient de la lèvre ou de la mâchoire : c’est le diagnostic qui le dit.",
         "blocs": [
             ("Des dents qui paraissent courtes sans l’être",
              ["Quand une dent a fini de sortir, la gencive se retire normalement jusqu’à la limite de "
               "l’émail. Chez certaines personnes, elle s’arrête avant : on parle d’éruption passive "
               "altérée. La dent est entière, mais sa partie haute reste couverte. C’est la situation où la "
               "gingivectomie est la plus logique : il suffit de découvrir la dent."]),
             ("Des gencives qui ne sont pas à la même hauteur",
              ["Un contour plus bas sur une incisive que sur sa voisine, deux canines asymétriques : l’œil le "
               "remarque tout de suite dans un sourire. La correction peut alors ne concerner qu’une ou deux "
               "dents."]),
             ("Avant des facettes ou des composites",
              ["La gencive est le cadre des dents. Quand un projet esthétique prévoit des "
               + lien("facettes-dentaires-paris", "facettes") + " ou du "
               + lien("composite-bonding-paris", "composite bonding")
               + ", on commence par mettre ce cadre à sa place : la forme des futures dents en dépend."]),
             ("Quand ce n’est pas la bonne réponse",
              ["Un sourire gingival peut aussi venir d’une lèvre supérieure courte ou très mobile, ou d’une "
               "mâchoire supérieure trop haute. Retirer de la gencive n’y changerait rien, ou pas assez : ces "
               "situations relèvent d’autres traitements, parfois associés. Et une gencive gonflée par "
               "l’inflammation se soigne d’abord : on n’opère pas une gencive qui saigne."]),
         ],
         "cote": [("fiche", "D’où vient un sourire gingival ?",
                   ["Une gencive qui recouvre trop les dents", "Une lèvre supérieure courte ou très mobile",
                    "Une mâchoire supérieure trop haute", "Des dents usées, qui ont continué à sortir",
                    "Souvent plusieurs causes à la fois"])]},
        {"q": "Gingivectomie ou élongation coronaire : quelle différence ?",
         "r": "La gingivectomie ne retire que de la gencive. L’élongation coronaire y ajoute un léger "
              "remodelage de l’os qui entoure la dent, quand il est trop proche du futur bord de la gencive. "
              "Sans ce geste, la gencive reviendrait peu à peu vers sa position de départ.",
         "blocs": [
             ("La gencive a besoin de sa place",
              ["La gencive ne se pose pas n’importe où : elle s’attache à la dent sur une hauteur à peu près "
               "constante au-dessus de l’os, un peu plus de 2 millimètres en moyenne, avec des variations "
               "d’une personne à l’autre. En pratique, on retient qu’il faut environ 3 millimètres entre l’os "
               "et le bord de la gencive pour qu’elle reste stable et saine."]),
             ("Quand la gencive seule suffit",
              ["Si l’os est à bonne distance, on peut retirer l’excès de gencive en conservant cet espace. "
               "C’est l’intervention la plus simple : le plus souvent sans point de suture, avec une "
               "cicatrisation rapide."]),
             ("Quand un petit remodelage osseux est nécessaire",
              ["Si l’os monte jusqu’à la limite de l’émail, ou s’il se retrouvait trop près du nouveau bord de "
               "la gencive, celle-ci n’aurait plus la place de s’attacher : elle resterait enflammée, ou "
               "repousserait. On retire alors, dans la même séance et sous la même anesthésie locale, une "
               "petite quantité d’os — de l’ordre du millimètre — autour des dents concernées, avant de "
               "remettre la gencive en place. C’est ce que l’on appelle une élongation coronaire."]),
             ("Comment le sait-on à l’avance ?",
              ["En mesurant, avant l’intervention, la position de l’os par rapport à l’émail : par un sondage "
               "sous anesthésie et, de plus en plus, sur une radiographie en trois dimensions superposée à "
               "l’empreinte numérique. Le choix entre gingivectomie simple et élongation coronaire se fait "
               "donc dent par dent, avant le jour de l’intervention."]),
         ],
         "tableau": (["Critère", "Gingivectomie", "Élongation coronaire"],
                     [("Ce que l’on retire", "De la gencive", "De la gencive et un peu d’os"),
                      ("Quand", "L’os est à bonne distance",
                       "L’os est trop proche du futur bord de la gencive"),
                      ("Points de suture", "Le plus souvent aucun", "Quelques points, retirés au contrôle"),
                      ("Cicatrisation", "Environ deux semaines",
                       "Quelques semaines ; la gencive se stabilise en quelques mois"),
                      ("Facettes ou composites, s’il y en a", "Après la cicatrisation",
                       "Une fois la gencive stabilisée")]),
         "cote": [("fiche", "À retenir", ["La gencive seule : gingivectomie",
                                          "La gencive et l’os : élongation coronaire",
                                          "Même séance, même anesthésie locale",
                                          "Le choix se fait dent par dent",
                                          "Il est décidé avant l’intervention"])]},
        {"q": "Comment l’intervention est-elle préparée ?",
         "r": "Sur l’écran, avant de toucher à la gencive. Les photographies, l’empreinte numérique et, si "
              "nécessaire, une radiographie en trois dimensions sont réunies pour dessiner le futur contour "
              "des gencives, dent par dent. Ce tracé est ensuite reporté en bouche par un guide imprimé en 3D.",
         "blocs": [
             ("Partir du sourire, pas de la gencive",
              ["Le projet commence par le visage : la position des lèvres au repos et au sourire, la longueur "
               "et les proportions que devraient avoir les dents. On en déduit où doit se trouver le bord de "
               "la gencive, et non l’inverse. C’est le travail du "
               + lien("bilan-esthetique-personnalise", "bilan esthétique") + "."]),
             ("La planification en trois dimensions",
              ["L’empreinte numérique donne la forme des dents et de la gencive ; la radiographie 3D montre "
               "l’émail caché sous la gencive et le niveau de l’os. Superposées, elles permettent de mesurer, "
               "sur chaque dent, la hauteur de gencive à retirer, et de savoir si l’os devra être remodelé."]),
             ("Le guide de gingivectomie",
              ["C’est une fine gouttière, conçue sur l’ordinateur et imprimée en 3D, que l’on pose sur les "
               "dents le jour de l’intervention. Son bord dessine exactement le contour décidé : le geste "
               "suit le projet, au lieu d’être tracé à main levée. Lorsqu’un remodelage osseux est prévu, le "
               "guide indique aussi le niveau où l’os doit se trouver."]),
             ("Ce que le guide apporte, et ce qu’il ne garantit pas",
              ["Les essais cliniques qui comparent l’intervention guidée et l’intervention classique montrent "
               "que les deux donnent de bons résultats. Le guide ne remplace pas le diagnostic : il sécurise "
               "le report des mesures, raccourcit l’intervention, et permet surtout de voir et de valider le "
               "tracé avant d’opérer."]),
         ],
         "cote": [("reserve", "Planification 3D",
                   "Emplacement réservé — capture de la planification en trois dimensions : le futur contour "
                   "des gencives dessiné sur le modèle numérique."),
                  ("reserve", "Guide de gingivectomie",
                   "Emplacement réservé — photographie du guide de gingivectomie imprimé en 3D, en place sur "
                   "les dents."),
                  ("fiche", "La préparation", ["Photographies du visage et du sourire",
                                               "Empreinte numérique des dents",
                                               "Radiographie 3D, si nécessaire",
                                               "Tracé du futur contour des gencives",
                                               "Guide imprimé en 3D"])]},
        {"q": "Comment se passe l’intervention, et après ?",
         "r": "Elle se fait en une séance, sous anesthésie locale, et laisse le plus souvent peu de douleurs. "
              "La semaine qui suit demande surtout de l’attention au brossage et à l’hygiène. Après une "
              "gingivectomie simple, la gencive est cicatrisée en deux semaines environ.",
         "blocs": [
             ("Le jour de l’intervention",
              ["Une fois l’anesthésie locale installée, le guide est mis en place et l’excès de gencive est "
               "retiré en suivant son bord. Si un remodelage osseux est prévu, la gencive est délicatement "
               "écartée, l’os est ajusté, puis la gencive est remise en place et maintenue par quelques "
               "points. Le nouveau contour est visible tout de suite."]),
             ("La semaine qui suit",
              ["Les suites sont le plus souvent modérées, et des antalgiques simples suffisent en général. "
               "L’essentiel est de protéger la gencive pendant qu’elle cicatrise : un brossage adapté, très "
               "doux, et des mesures d’hygiène précises, remises par écrit. Le tabac ralentit la "
               "cicatrisation."]),
             ("La cicatrisation",
              ["Après une gingivectomie simple, la gencive est cicatrisée en deux semaines environ. Après une "
               "élongation coronaire, les points sont retirés au contrôle, et la gencive continue d’évoluer "
               "pendant les premiers mois : c’est pourquoi l’on attend avant de réaliser des facettes ou des "
               "composites sur ces dents."]),
             ("Le résultat est-il stable ?",
              ["Oui, quand le diagnostic est juste et que la gencive a gardé la place dont elle a besoin. Un "
               "léger retour de la gencive vers la dent reste possible dans les premiers mois, surtout quand "
               "elle est épaisse ou que l’os est proche : c’est précisément ce que la mesure de l’os, avant "
               "l’intervention, sert à éviter."]),
         ],
         "cote": [("fiche", "Après l’intervention", ["Peu de douleurs, le plus souvent",
                                                     "Un brossage très doux pendant une semaine",
                                                     "Pas de tabac pendant la cicatrisation",
                                                     "Un contrôle dans les deux semaines",
                                                     "Un résultat visible tout de suite"])]},
        {"bande": "Avant / après",
         "cas": [("reserve", "Avant / après n° 2",
                  "Emplacement réservé — cas n° 2. La légende sera écrite avec la photographie : la demande, "
                  "le geste (gingivectomie seule ou élongation coronaire), le délai de la photo d’après."),
                 ("reserve", "Avant / après n° 3",
                  "Emplacement réservé — cas n° 3. La légende sera écrite avec la photographie.")]},
        {"q": "Faut-il ensuite des facettes ou des composites ?",
         "r": "Pas forcément. Quand les dents sont belles sous la gencive, la gingivectomie suffit à "
              "transformer le sourire. Dans d’autres projets, elle est la première étape, avant un "
              "éclaircissement, des composites ou des facettes.",
         "blocs": [
             ("Seule, quand la dent est intacte",
              ["Si la dent découverte a une forme et une teinte satisfaisantes, il n’y a rien à ajouter. C’est "
               "le cas le plus conservateur : aucune dent n’est touchée."]),
             ("En première étape d’un projet esthétique",
              ["Dans un projet plus large, on corrige d’abord les gencives, on laisse cicatriser, puis on "
               "traite les dents : " + lien("eclaircissement-dentaire-paris", "éclaircissement") + ", "
               + lien("composite-bonding-paris", "composite bonding") + " ou "
               + lien("facettes-dentaires-paris", "facettes")
               + ". Les restaurations sont alors réalisées sur une gencive stable, à sa place définitive."]),
             ("Dents courtes : gencive en trop, ou dents usées ?",
              ["Des dents courtes ne le sont pas toujours pour la même raison. Si la gencive les recouvre, on "
               "la remonte. Si elles ont perdu de la matière par " + lien("usures-dentaires", "usure")
               + ", c’est la dent qu’il faut reconstruire, après avoir compris ce qui l’a usée. Les deux "
               "situations peuvent se combiner : le diagnostic les distingue avant toute intervention."]),
         ],
         "cote": [("fiche_liens", "Pour aller plus loin",
                   [("bilan-esthetique-personnalise", "Bilan esthétique"),
                    ("facettes-dentaires-paris", "Facettes"),
                    ("composite-bonding-paris", "Composite bonding"),
                    ("dents-courtes-usees", "Dents courtes ou usées"),
                    ("video-sourire-gingival", "En vidéo : le sourire gingival")])]},
    ],
    "a_lire": [("dentisterie-esthetique-paris", "Dentisterie esthétique"),
               ("bilan-esthetique-personnalise", "Bilan esthétique personnalisé"),
               ("facettes-dentaires-paris", "Facettes dentaires"),
               ("composite-bonding-paris", "Composite bonding"),
               ("dents-courtes-usees", "Dents courtes ou usées"),
               ("franck-moyal", "Dr Franck Moyal")],
    "appel": ("Savoir si une gingivectomie est indiquée",
              "Une consultation permet de déterminer d’où vient le sourire gingival, ce qu’une gingivectomie "
              "peut corriger, et s’il faut l’associer à un autre traitement."),
    "sources": [
        source("Mele M, Felice P, Sharma P, Mazzotti C, Bellone P, Zucchelli G.",
               "Esthetic treatment of altered passive eruption.", "Periodontol 2000", "2018;77(1):65–83",
               "10.1111/prd.12206", "29504162"),
        source("Tatakis DN, Silva CO.",
               "Contemporary treatment techniques for excessive gingival display caused by altered passive "
               "eruption or lip hypermobility.", "J Dent", "2023;138:104711",
               "10.1016/j.jdent.2023.104711", "37730094"),
        source("Schmidt JC, Sahrmann P, Weiger R, Schmidlin PR, Walter C.",
               "Biologic width dimensions – a systematic review.", "J Clin Periodontol", "2013;40(5):493–504",
               "10.1111/jcpe.12078", "23461747"),
        source("Pilalas I, Tsalikis L, Tatakis DN.",
               "Pre-restorative crown lengthening surgery outcomes: a systematic review.",
               "J Clin Periodontol", "2016;43(12):1094–1108", "10.1111/jcpe.12617", "27535216"),
        source("Borham E, Abuel-Ela HA, Mohamed IS, Fouad YA.",
               "Treatment of excessive gingival display using conventional esthetic crown lengthening versus "
               "computer guided esthetic crown lengthening: a randomized clinical trial.",
               "BMC Oral Health", "2024;24(1):317", "10.1186/s12903-024-04080-5", "38461241"),
        source("Gonçalves V, de Almeida Malzoni CM, Santos JCD, et al.",
               "Predictability of Periodontal Surgical Guides Manufactured by Digital Flow in Clinical Crown "
               "Lengthening. A Randomized Trial.", "J Esthet Restor Dent", "2025;37(9):2125–2133",
               "10.1111/jerd.13487", "40423240"),
    ],
    "note_sources": ("<strong>Repère clinique du Dr Franck Moyal</strong> : les délais de cicatrisation sont "
                     "donnés comme des ordres de grandeur ; ils sont précisés à chaque patient selon le "
                     "geste réalisé."),
}

# ══ Edge bonding ═══════════════════════════════════════════════════════════════════════════════════
EDGE = {
    "slug": "edge-bonding-paris",
    "titre": "Edge bonding à Paris : bord des dents | Dr Franck Moyal",
    "description": ("Edge bonding à Paris 9e : un composite limité au bord des dents pour redessiner la ligne "
                    "du sourire et les formes, sans tailler. Indications et limites."),
    "h1": "Edge bonding",
    "sous_titre": "Le composite du bord des dents",
    "fil": "Edge bonding",
    "acte": {"@type": "MedicalProcedure", "name": "Edge bonding",
             "alternateName": ["Composite du bord incisif", "Composite bonding du bord des dents"]},
    "chapo": ("L’edge bonding consiste à ajouter une petite quantité de composite sur le seul bord des dents "
              "de devant. On ne recouvre pas la dent : on en redessine le contour, pour corriger la ligne du "
              "sourire et la forme des dents. C’est le geste le plus léger de la dentisterie esthétique, sans "
              "tailler la dent. Sa contrepartie est connue : posé là où les dents travaillent, ce petit ajout "
              "est plus fragile qu’un composite étendu."),
    "couverture": ("reserve", "Avant / après n° 1",
                   "Emplacement réservé — premier avant / après d’un edge bonding, sourire de face. "
                   "La légende sera écrite avec la photographie."),
    "chapitres": [
        {"q": "Qu’est-ce que l’edge bonding ?",
         "r": "C’est un " + lien("composite-bonding-paris", "composite bonding")
              + " limité au bord libre des dents de devant : une petite quantité de résine, collée sur "
              "l’émail, sculptée puis polie, sans tailler la dent et sans recouvrir sa face visible. Je le "
              "pratique au cabinet, à Paris 9<sup>e</sup>.",
         "blocs": [
             ("Le bord, et seulement le bord",
              ["Le bord libre est l’extrémité de la dent, celle qui coupe. L’edge bonding y ajoute de la "
               "résine — un millimètre ou deux, souvent moins — pour en changer la longueur ou le dessin. Tout "
               "le reste de la dent reste tel qu’il est : son émail, sa teinte, sa brillance."]),
             ("Ce que l’on modifie : la ligne du sourire",
              ["Vus de face, les bords des dents du haut dessinent une courbe qui suit normalement celle de "
               "la lèvre inférieure : c’est la ligne du sourire. Quand les incisives ont raccourci, cette "
               "ligne s’aplatit, parfois s’inverse. Très peu de matière, ajoutée aux bons endroits, suffit à "
               "la redessiner."]),
             ("Et la forme des dents",
              ["Un angle à adoucir ou à marquer, un bord ébréché, deux incisives centrales de longueurs "
               "inégales, une incisive latérale un peu courte : ce sont les bords et les angles qui donnent "
               "aux dents leur caractère. L’edge bonding travaille précisément là."]),
         ],
         "cote": [("fiche", "En bref", ["Uniquement sur le bord des dents", "Sans tailler la dent",
                                        "Le plus souvent en une séance",
                                        "Redessine la ligne du sourire et les formes",
                                        "Plus fragile qu’un composite étendu", "Se répare facilement"])]},
        {"q": "Quelle différence avec un composite bonding étendu ?",
         "r": "La surface traitée. Un composite étendu recouvre toute la face visible de la dent et peut en "
              "changer la teinte, le volume et la forme. L’edge bonding ne concerne que le bord : il modifie "
              "le contour de la dent, pas sa surface.",
         "blocs": [
             ("Le composite étendu : toute la face de la dent",
              ["Dans un composite bonding étendu, la résine couvre la face visible de la dent, souvent sur "
               "plusieurs dents de devant. On peut alors changer la teinte, fermer un espace, redonner du "
               "volume, reconstruire une dent très usée. C’est une transformation plus complète, qui demande "
               "plus de matière, plus de temps, et l’entretien de toute la surface."]),
             ("L’edge bonding : le contour seulement",
              ["Ici, l’essentiel de ce que l’on voit reste la dent naturelle. La résine ne représente qu’une "
               "petite partie du sourire : c’est ce qui rend le résultat discret, et c’est aussi pourquoi "
               "l’edge bonding ne peut ni changer la couleur des dents, ni fermer un espace, ni corriger une "
               "position."]),
             ("Pourquoi il est plus fragile",
              ["Le bord est l’endroit où les dents se rencontrent, coupent et reçoivent les chocs. Un petit "
               "ajout de résine y est collé sur une surface réduite et travaille presque seul, en bout de "
               "dent. Un composite étendu, lui, s’appuie sur toute la face de la dent : les contraintes s’y "
               "répartissent mieux. Les études sur les composites des dents de devant vont dans le même "
               "sens : la fracture est leur première cause d’échec, et les restaurations qui n’intéressent "
               "pas le bord de la dent sont celles qui durent le mieux."]),
             ("Ce que cela change en pratique",
              ["On le choisit en connaissance de cause : un edge bonding se surveille et se retouche. La "
               "contrepartie de sa légèreté, c’est qu’un éclat reste possible ; son avantage, c’est qu’il se "
               "répare vite, sans rien refaire d’autre."]),
         ],
         "tableau": (["Critère", "Edge bonding", "Composite bonding étendu"],
                     [("Surface traitée", "Le bord de la dent", "Toute la face visible"),
                      ("Ce que l’on change", "La longueur, les angles, la ligne du sourire",
                       "La forme entière, le volume, la teinte, les espaces"),
                      ("Ce que l’on voit", "Surtout la dent naturelle", "Surtout le composite"),
                      ("Taille de la dent", "Aucune", "Aucune, ou très limitée"),
                      ("Solidité", "Plus exposé aux éclats", "Contraintes mieux réparties"),
                      ("Entretien", "La retouche d’un bord, au besoin",
                       "Le polissage de toute la surface")]),
         "cote": [("photo", PHOTOS + "composite-rehabilitation-avant-apres.jpg",
                   "Avant et après : dents antérieures usées et colorées, puis reconstruites en composite, "
                   "sourire de face",
                   "Pour comparer, un composite étendu : composite direct sur les six dents antérieures, sans "
                   "préparation. Toute la face visible des dents est recouverte."),
                  ("reserve", "Edge bonding en gros plan",
                   "Emplacement réservé — gros plan sur un bord de dent avant et après edge bonding, pour "
                   "montrer que seul le bord est en composite.")]},
        {"q": "Dans quels cas propose-t-on un edge bonding ?",
         "r": "Quand la dent est saine, d’une teinte satisfaisante, et que seul son contour gêne : bords "
              "ébréchés ou irréguliers, dents un peu courtes, ligne du sourire aplatie, angles à redessiner. "
              "Dès qu’il faut changer la teinte, le volume ou fermer un espace, un autre traitement est plus "
              "adapté.",
         "blocs": [
             ("Les bonnes indications",
              ["Réparer un éclat. Égaliser des bords irréguliers. Rendre un peu de longueur à des incisives "
               "qui ont raccourci. Redonner sa courbe à la ligne du sourire. Harmoniser deux dents voisines. "
               "Finir un traitement d’orthodontie, quand les dents sont alignées mais que leurs bords ne le "
               "sont pas."]),
             ("Quand un composite étendu ou des facettes conviennent mieux",
              ["Si la dent doit changer de teinte, de volume ou de proportions, si un espace doit être fermé, "
               "ou si l’usure a emporté une grande partie de la dent, ne traiter que le bord ne suffit pas. "
               "Un composite étendu ou des " + lien("facettes-dentaires-paris", "facettes")
               + " répondent alors mieux à la demande."]),
             ("Quand il vaut mieux s’abstenir",
              ["L’edge bonding supporte mal les contraintes fortes : des dents qui se rencontrent bord à bord, "
               "un bruxisme non protégé, l’habitude de ronger ses ongles ou de mordiller un stylo. Dans ces "
               "situations, le composite casserait vite : on traite d’abord la cause, ou l’on choisit une "
               "autre solution."]),
             ("Si les bords sont usés : comprendre d’abord pourquoi",
              ["Quand les bords sont usés, je cherche d’abord pourquoi : rallonger des dents sans avoir "
               "compris la cause de leur " + lien("usures-dentaires", "usure")
               + " expose à voir le composite s’ébrécher à son tour."]),
         ],
         "cote": [("fiche", "Bonnes indications", ["Un bord ébréché", "Des bords irréguliers",
                                                   "Des incisives un peu courtes",
                                                   "Une ligne du sourire aplatie",
                                                   "Des angles à redessiner",
                                                   "Des finitions après orthodontie"]),
                  ("fiche", "Moins adapté", ["Changer la teinte des dents", "Fermer un espace",
                                             "Des dents très usées",
                                             "Des dents qui se touchent bord à bord",
                                             "Un bruxisme non protégé"])]},
        {"q": "Comment se déroule la séance ?",
         "r": "En une séance le plus souvent, sans tailler la dent et généralement sans anesthésie : on choisit "
              "la forme ensemble, puis le composite est collé sur l’émail, sculpté et poli.",
         "blocs": [
             ("Décider de la forme avant de coller",
              ["Tout part de l’analyse du sourire : photographies, position des lèvres, longueur souhaitable "
               "des dents. La nouvelle forme peut être essayée directement en bouche, avec un peu de composite "
               "posé sans colle, pour la voir et la corriger avant de décider."]),
             ("Éclaircir d’abord, si on le souhaite",
              ["Le composite ne s’éclaircit pas. Si un "
               + lien("eclaircissement-dentaire-paris", "éclaircissement")
               + " est envisagé, il se fait avant : la teinte de la résine est ensuite choisie sur la dent "
               "éclaircie, une fois sa couleur stabilisée."]),
             ("Coller, sculpter, polir",
              ["La dent est isolée de la salive, l’émail est préparé pour le collage, puis le composite est "
               "monté en fines couches. Le bord naturel d’une dent est translucide : pour que l’ajout ne se "
               "voie pas, il faut reproduire cette translucidité, puis polir jusqu’à faire disparaître la "
               "jonction entre la dent et la résine."]),
             ("En sortant",
              ["On repart avec le résultat, sans temps de cicatrisation. Un contrôle permet de vérifier les "
               "contacts entre les dents et de parfaire le polissage."]),
         ],
         "cote": [("fiche", "La séance", ["Analyse du sourire et choix de la forme",
                                          "Éclaircissement avant, si on le souhaite",
                                          "Collage sur l’émail, sans taille",
                                          "Composite monté en couches, puis poli",
                                          "Contrôle des contacts"])]},
        {"bande": "Avant / après",
         "cas": [("reserve", "Avant / après n° 2",
                  "Emplacement réservé — cas n° 2. La légende sera écrite avec la photographie : la demande, "
                  "les dents traitées, ce qui a été ajouté."),
                 ("reserve", "Avant / après n° 3",
                  "Emplacement réservé — cas n° 3. La légende sera écrite avec la photographie.")]},
        {"q": "Combien de temps tient un edge bonding ?",
         "r": "Plusieurs années quand il est bien indiqué et entretenu, mais c’est le composite le plus exposé "
              "aux éclats : il faut s’attendre à des retouches. Rien n’ayant été taillé, toutes les options "
              "restent ouvertes par la suite.",
         "blocs": [
             ("Pas de durée garantie",
              ["La longévité d’un composite antérieur dépend de l’indication, de sa taille, de la façon dont "
               "les dents se rencontrent, des habitudes de chacun et de la qualité du collage. Pour un edge "
               "bonding, je préfère parler d’entretien que de durée : un petit ajout sur un bord peut rester "
               "intact des années, ou demander une retouche plus tôt."]),
             ("Ce qui le fait durer",
              ["Des contacts entre les dents bien réglés, une gouttière de nuit quand on serre ou grince des "
               "dents, et quelques précautions : ne pas ronger ses ongles, ne pas couper de fil ni ouvrir "
               "d’emballage avec les dents, croquer les aliments très durs sur le côté."]),
             ("S’il s’ébrèche",
              ["Il se répare, le plus souvent sans tout refaire : on ajoute de la matière sur place, puis on "
               "repolit. La réparabilité est l’un des grands intérêts de cette technique."]),
             ("Et ensuite ?",
              ["L’edge bonding n’engage pas l’avenir : la dent n’a pas été taillée. Si le projet évolue, on "
               "peut le retoucher, le compléter, ou passer plus tard à un composite étendu ou à des "
               "facettes."]),
         ],
         "cote": [("fiche", "Pour le faire durer", ["Des contacts bien réglés",
                                                    "Une gouttière de nuit en cas de bruxisme",
                                                    "Ne pas ronger ses ongles",
                                                    "Ne pas croquer très dur avec les dents de devant",
                                                    "Un polissage d’entretien au cabinet"]),
                  ("fiche_liens", "Pour aller plus loin",
                   [("composite-bonding-paris", "Composite bonding"),
                    ("facettes-ou-composite", "Facettes ou composite ?"),
                    ("eclaircissement-dentaire-paris", "Éclaircissement dentaire"),
                    ("usures-dentaires", "Usure dentaire"),
                    ("bilan-esthetique-personnalise", "Bilan esthétique")])]},
    ],
    "a_lire": [("composite-bonding-paris", "Composite bonding"),
               ("facettes-ou-composite", "Facettes ou composite ?"),
               ("dentisterie-esthetique-paris", "Dentisterie esthétique"),
               ("bilan-esthetique-personnalise", "Bilan esthétique personnalisé"),
               ("dents-courtes-usees", "Dents courtes ou usées"),
               ("franck-moyal", "Dr Franck Moyal")],
    "appel": ("Savoir si un edge bonding suffit",
              "Une consultation esthétique permet de déterminer ce qui peut être obtenu en ne traitant que le "
              "bord des dents, et ce qui demanderait un composite plus étendu ou des facettes."),
    "sources": [
        source("Wolff D, Frese C, Frankenberger R, et al.",
               "Direct Composite Restorations on Permanent Teeth in the Anterior and Posterior Region — An "
               "Evidence-Based Clinical Practice Guideline — Part 1: Indications for Composite Restorations.",
               "J Adhes Dent", "2024;26:185–200", "10.3290/j.jad.b5748881", "39286910"),
        source("Demarco FF, Collares K, Coelho-de-Souza FH, et al.",
               "Anterior composite restorations: A systematic review on long-term survival and reasons for "
               "failure.", "Dent Mater", "2015;31(10):1214–1224", "10.1016/j.dental.2015.07.005", "26303655"),
        source("Shah YR, Shiraguppi VL, Deosarkar BA, Shelke UR.",
               "Long-term survival and reasons for failure in direct anterior composite restorations: A "
               "systematic review.", "J Conserv Dent", "2021;24(5):415–420", "10.4103/jcd.jcd_527_21",
               "35399771"),
        source("Burke FJT.", "Longevity of Indirect and Direct Restorations in Anterior Teeth.",
               "Prim Dent J", "2023;12(2):76–84", "10.1177/20501684231175591", "37313877"),
    ],
    "note_sources": ("<strong>Repère clinique du Dr Franck Moyal</strong> : aucune étude ne compare directement "
                     "l’edge bonding et le composite étendu ; la plus grande fragilité de l’edge bonding est "
                     "une observation clinique, cohérente avec les données sur les restaurations du bord "
                     "des dents."),
}

PAGES = [GINGIVECTOMIE, EDGE]


# ══ mise en page ═══════════════════════════════════════════════════════════════════════════════════
def fr(s):
    """Les espaces insécables de la typographie française, hors des balises."""
    def texte(m):
        x = m.group(0)
        x = re.sub(r" ([:;?!»])", " \\1", x)
        return x.replace("« ", "« ").replace("n° ", "n° ")
    return re.sub(r"(?<=>)[^<]+|^[^<]+", texte, s)


def reserve(libelle, legende, classe):
    """Un emplacement réservé pour une photographie à venir, clairement signalé (verrou V2)."""
    return (f'<figure class="{classe} reserve">\n'
            f'          <div class="reserve__zone"><b>{fr(libelle)}</b><span>Photographie à venir</span></div>\n'
            f'          <figcaption><span>{fr(legende)}</span></figcaption>\n        </figure>')


def element(e, classe="illus illus--libre"):
    genre = e[0]
    if genre == "reserve":
        return "        " + reserve(e[1], e[2], classe)
    if genre == "photo":
        return (f'        <figure class="{classe}">\n'
                f'          <img src="{e[1]}" alt="{H.escape(e[2])}" loading="lazy">\n'
                f'          <figcaption><span>{fr(e[3])}</span></figcaption>\n        </figure>')
    if genre == "fiche":
        lis = "\n".join(f"          <li>{fr(x)}</li>" for x in e[2])
        return (f'        <div class="fiche">\n          <h4>{fr(e[1])}</h4>\n          <ul>\n{lis}\n'
                f'          </ul>\n        </div>')
    if genre == "fiche_liens":
        lis = "\n".join(f'          <li><a href="{p}.html">{fr(t)}</a></li>' for p, t in e[2])
        return (f'        <div class="fiche">\n          <h4>{fr(e[1])}</h4>\n          <ul>\n{lis}\n'
                f'          </ul>\n        </div>')
    raise ValueError(genre)


def tableau(entetes, lignes):
    tete = "".join(f"<th>{fr(x)}</th>" for x in entetes)
    corps = "\n".join(
        '            <tr><th scope="row">' + fr(l[0]) + "</th>" + "".join(f"<td>{fr(x)}</td>" for x in l[1:])
        + "</tr>" for l in lignes)
    return (f'        <div class="tableau">\n          <table>\n            <thead><tr>{tete}</tr></thead>\n'
            f'            <tbody>\n{corps}\n            </tbody>\n          </table>\n        </div>')


def section(rang, k, n, ch):
    zone = " sect--zone" if rang % 2 == 0 else ""
    if "bande" in ch:
        cas = "\n".join(element(c, "parcours__etape") for c in ch["cas"])
        return (f'  <section class="sect{zone}">\n    <div class="contenu">\n'
                f'      <h2 class="tete-bande">{fr(ch["bande"])}</h2>\n'
                f'      <div class="parcours parcours--large">\n{cas}\n      </div>\n    </div>\n  </section>')
    blocs = [f'        <div class="bloc">\n          <p class="reponse">{fr(ch["r"])}</p>\n        </div>']
    for titre, paras in ch["blocs"]:
        ps = "\n".join(f"          <p>{fr(p)}</p>" for p in paras)
        blocs.append(f'        <div class="bloc">\n          <h3>{fr(titre)}</h3>\n{ps}\n        </div>')
    if ch.get("tableau"):
        blocs.append(tableau(*ch["tableau"]))
    cote = "\n".join(element(e) for e in ch.get("cote", []))
    return (f'  <section class="sect{zone}">\n    <div class="contenu chapitre">\n      <div>\n'
            f'        <p class="numero">{k} / {n}</p>\n        <h2>{fr(ch["q"])}</h2>\n'
            + "\n".join(blocs) + '\n      </div>\n      <div class="cote">\n' + cote
            + "\n      </div>\n    </div>\n  </section>")


def donnees(p):
    """Les données structurées, sur le modèle des autres pages d'actes : le site, la page et ses
    sources, le fil d'Ariane, le praticien, le cabinet. Les questions fréquentes y sont ajoutées par
    generer.py depuis le bloc affiché."""
    socle = G._socle()
    url = f"{G.RACINE_WEB}{p['slug']}/"
    page = {"@type": "MedicalWebPage", "@id": url + "#page", "url": url, "name": p["titre"],
            "description": p["description"], "inLanguage": "fr-FR",
            "isPartOf": {"@id": G.RACINE_WEB + "#website"}, "author": {"@id": G.RACINE_WEB + "#franck-moyal"},
            "about": p["acte"], "breadcrumb": {"@id": url + "#fil"},
            "citation": [{"@type": "ScholarlyArticle", "name": s["titre"], "author": s["auteurs"],
                          "datePublished": s["ref"][:4],
                          "isPartOf": {"@type": "Periodical", "name": s["revue"]},
                          "sameAs": f"https://doi.org/{s['doi']}",
                          "url": f"https://pubmed.ncbi.nlm.nih.gov/{s['pmid']}/"} for s in p["sources"]]}
    fil = {"@type": "BreadcrumbList", "@id": url + "#fil", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": G.RACINE_WEB},
        {"@type": "ListItem", "position": 2, "name": "Dentisterie esthétique",
         "item": G.RACINE_WEB + "dentisterie-esthetique-paris/"},
        {"@type": "ListItem", "position": 3, "name": p["fil"], "item": url}]}
    graphe = [socle[0], page, fil] + socle[1:]
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": graphe}, ensure_ascii=False) + "</script>")


def rendre(p):
    chapitres = [c for c in p["chapitres"] if "q" in c]
    n, k, sections = len(chapitres), 0, []
    for rang, ch in enumerate(p["chapitres"], 1):
        if "q" in ch:
            k += 1
        sections.append(section(rang, k, n, ch))
    a_lire = " · ".join(f'<a href="{s}.html">{fr(t)}</a>' for s, t in p["a_lire"])
    sources = "\n".join(
        f'        <li><strong>{H.escape(s["auteurs"], quote=False)}</strong> {H.escape(s["titre"], quote=False)} '
        f'<em>{s["revue"]}.</em> {s["ref"]}. — DOI : <a href="https://doi.org/{s["doi"]}" {_EXT}>{s["doi"]}</a> — '
        f'<a href="https://pubmed.ncbi.nlm.nih.gov/{s["pmid"]}/" {_EXT}>PubMed</a></li>' for s in p["sources"])
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(p["titre"], quote=False)}</title>
<meta name="description" content="{H.escape(p["description"])}">
{POLICES}
<link rel="stylesheet" href="style.css?v={G.VERSION}">
{donnees(p)}
</head>
<body>

{G.menu(p["slug"])}

<main>

  <div class="contenu">
    <p class="ariane"><a href="index.html">Accueil</a> › Patient › {fr(p["fil"])}</p>
    <div class="une">
      <div>
        <p class="eyebrow">L’acte</p>
        <h1>{fr(p["h1"])}</h1>
        <p class="sous-titre">{fr(p["sous_titre"])}</p>
        <p class="une__chapo">{fr(p["chapo"])}</p>
        <div class="signature">
          <img src="{G.PORTRAIT}" alt="Dr Franck Moyal">
          <div><b>Dr Franck Moyal</b> — chirurgien-dentiste, Paris 9<sup>e</sup><br>
            Praticien hospitalier, Pitié-Salpêtrière · CMME, Sainte-Anne</div>
        </div>
      </div>
      {reserve(p["couverture"][1], p["couverture"][2], "une__reserve").replace(chr(10) + "        ", chr(10) + "      ")}
    </div>
  </div>

{chr(10).join(sections)}
  <section class="sect sect--serre">
    <div class="contenu chapitre chapitre--plein">
      <div>
        <p class="eyebrow">À lire aussi</p>
        <p class="suite">{a_lire}</p>
      </div>
    </div>
  </section>
  <section class="appel">
    <div class="contenu">
      <h2>{fr(p["appel"][0])}</h2>
      <p>{fr(p["appel"][1])}</p>
      <a class="bouton" href="contact.html">Prendre rendez-vous</a>
    </div>
  </section>
  <section class="sect sect--serre">
    <div class="contenu sources">
      <p class="eyebrow">Sources scientifiques</p>
      <p style="margin-bottom:.6rem">Les références ci-dessous soutiennent les principaux messages cliniques de cette page.</p>
      <ol>
{sources}
      </ol>
      <p style="margin-top:.6rem">{fr(p["note_sources"])}</p>
    </div>
  </section>

</main>

{G.PIED}

<script src="menu.js"></script>
</body>
</html>
'''


def main():
    for p in PAGES:
        assert len(p["titre"]) <= 60, f"titre Google trop long ({len(p['titre'])}) : {p['titre']}"
        assert len(p["description"]) <= 155, f"description trop longue ({len(p['description'])}) : {p['slug']}"
        open(os.path.join(SITE, p["slug"] + ".html"), "w", encoding="utf-8").write(rendre(p))
        reserves = sum(1 for c in p["chapitres"] for e in c.get("cote", []) + c.get("cas", [])
                       if e[0] == "reserve") + 1
        print(f"page {p['slug']} écrite : {sum(1 for c in p['chapitres'] if 'q' in c)} chapitres, "
              f"{reserves} emplacements de photographie réservés, {len(p['sources'])} sources")


if __name__ == "__main__":
    main()
