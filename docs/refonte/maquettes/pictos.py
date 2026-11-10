"""Les pictogrammes du site, dessinés ici (10/11/2026).

Franck, en regardant les pages Parcours, Publications et Conférences : « aère plus la page
et mets du relief et de l'iconographie générée ou choisie sur internet ». Plutôt qu'un jeu
d'icônes pris ailleurs, un jeu dessiné pour le site : même trait, même encre, même grille
de 24 × 24, si bien qu'ils se tiennent entre eux et avec la typographie.

Chaque pictogramme est une liste de tracés SVG, dessinés au trait (currentColor), sans
remplissage. Ils sont décoratifs : aria-hidden, le texte voisin dit déjà tout.
"""

TRACES = {
    # diplôme, thèse, certificat : la toque
    "diplome": ["M2.5 9.2 12 4.5l9.5 4.7L12 14z", "M6.2 11.2v4.6c0 1.5 2.6 3 5.8 3s5.8-1.5 5.8-3v-4.6",
                "M21.5 9.2v5.6"],
    # l'hôpital
    "hopital": ["M4.5 20.5V7.5h4V3.8h7v3.7h4v13", "M2.5 20.5h19", "M12 6.3v5M9.5 8.8h5",
                "M10.2 20.5v-4h3.6v4", "M6.8 11.5h.01M6.8 14.5h.01M17.2 11.5h.01M17.2 14.5h.01"],
    # le Service de santé des armées : un écu frappé de la croix
    "reserve": ["M12 3.2 19 6v5.3c0 4.4-2.9 8.1-7 9.5-4.1-1.4-7-5.1-7-9.5V6z", "M12 8.4v6.2M8.9 11.5h6.2"],
    # un article : la page et ses lignes
    "article": ["M6 3.5h8.5l3.5 3.5v13.5H6z", "M14.5 3.5V7H18", "M8.8 11h6.4M8.8 14h6.4M8.8 17h3.8"],
    # une revue : la une, une image, des colonnes
    "revue": ["M4 4.5h16v15H4z", "M7 8h6v5H7z", "M15.3 8h1.7M15.3 10.5h1.7M15.3 13h1.7M7 16h10"],
    # un ouvrage : le livre ouvert
    "livre": ["M12 6.6C10.3 5.2 7.7 4.6 3.5 4.6v13.6c4.2 0 6.8.6 8.5 2 1.7-1.4 4.3-2 8.5-2V4.6c-4.2 0-6.8.6-8.5 2z",
              "M12 6.6v13.6"],
    # une consultation de dépistage : la feuille cochée
    "depistage": ["M6 4.5h12v16H6z", "M9.2 4.5V3h5.6v1.5", "M8.8 12.6l2.3 2.3 4.2-4.6"],
    # enseigner : le tableau
    "enseigner": ["M3.5 4.5h17v11h-17z", "M12 15.5v3.2", "M8.5 20.5 12 18.7l3.5 1.8", "M7 9.5h6M7 12h4"],
    # une conférence : le micro
    "micro": ["M9.2 6a2.8 2.8 0 0 1 5.6 0v5.2a2.8 2.8 0 0 1-5.6 0z", "M6.2 10.8a5.8 5.8 0 0 0 11.6 0",
              "M12 16.6v3.9M9 20.5h6"],
    # un atelier pratique : le miroir de bouche
    "atelier": ["M15.3 3.8a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8z", "M11.8 12.1 4 19.9",
                "M15.3 6.4a2.3 2.3 0 0 1 2.3 2.3"],
    # deux métiers ensemble : le praticien et le prothésiste
    "duo": ["M8.8 4.8a3 3 0 1 1 0 6 3 3 0 0 1 0-6z", "M3.5 19.5c0-3.1 2.4-5.6 5.3-5.6s5.3 2.5 5.3 5.6",
            "M16.6 6.2a2.6 2.6 0 1 1 0 5.2 2.6 2.6 0 0 1 0-5.2z", "M15.6 14.1c.3-.1.7-.1 1-.1 2.6 0 4.6 2.2 4.6 4.9"],
    # une association
    "association": ["M12 4.2a2.7 2.7 0 1 1 0 5.4 2.7 2.7 0 0 1 0-5.4z", "M7 19.5c0-2.9 2.2-5.3 5-5.3s5 2.4 5 5.3",
                    "M5.4 8.4a2 2 0 1 1 0 4 2 2 0 0 1 0-4z", "M18.6 8.4a2 2 0 1 1 0 4 2 2 0 0 1 0-4z",
                    "M2.5 18c0-2 1.3-3.6 3-3.9M21.5 18c0-2-1.3-3.6-3-3.9"],
    # la dent
    "dent": ["M12 5.2C10.6 4.2 9.2 3.7 7.6 3.7 5 3.7 3.6 5.7 3.6 8.2c0 2.4 1 3.9 1.6 6.3.6 2.7 1.1 6 2.6 6 "
             "1.6 0 1.8-4.4 4.2-4.4s2.6 4.4 4.2 4.4c1.5 0 2-3.3 2.6-6 .6-2.4 1.6-3.9 1.6-6.3 0-2.5-1.4-4.5-4-4.5"
             "-1.6 0-3 .5-4.4 1.5z"],
    # les composites : la stratification, couche après couche
    "strates": ["M12 3.8 20.5 8.3 12 12.8 3.5 8.3z", "M3.5 12.1 12 16.6l8.5-4.5", "M3.5 15.9 12 20.4l8.5-4.5"],
    # l'esthétique et les préparations : l'éclat
    "eclat": ["M12 3.5c.6 3.9 1.9 5.6 5.5 6.3-3.6.7-4.9 2.4-5.5 6.3-.6-3.9-1.9-5.6-5.5-6.3 3.6-.7 4.9-2.4 5.5-6.3z",
              "M18.5 15.5c.3 1.6.8 2.2 2.2 2.5-1.4.3-1.9.9-2.2 2.5-.3-1.6-.8-2.2-2.2-2.5 1.4-.3 1.9-.9 2.2-2.5z"],
    # la gencive et les tissus mous : le feston au-dessus des dents
    "gencive": ["M3 8.8c1.6 0 2.4-2.1 4.5-2.1S10.4 8.8 12 8.8s2.4-2.1 4.5-2.1 2.9 2.1 4.5 2.1",
                "M5.8 11.6v4.6a2.2 2.2 0 0 0 4.4 0v-4.6M13.8 11.6v4.6a2.2 2.2 0 0 0 4.4 0v-4.6"],
    # l'occlusion : les deux arcades qui se rencontrent
    "occlusion": ["M3.5 9.8C6 6.6 8.8 5.2 12 5.2s6 1.4 8.5 4.6", "M3.5 14.2c2.5 3.2 5.3 4.6 8.5 4.6s6-1.4 8.5-4.6",
                  "M3.5 12h17", "M8 10.4v3.2M12 10.4v3.2M16 10.4v3.2"],
    # la photographie
    "photo": ["M3.5 8.2h3.6l1.6-2.4h6.6l1.6 2.4h3.6v11h-17z", "M12 10.2a3.6 3.6 0 1 1 0 7.2 3.6 3.6 0 0 1 0-7.2z"],
    # les contentions fibrées : le lien
    "contention": ["M10.2 13.8a3.8 3.8 0 0 0 5.4 0l3.1-3.1a3.8 3.8 0 0 0-5.4-5.4l-1.1 1.1",
                   "M13.8 10.2a3.8 3.8 0 0 0-5.4 0l-3.1 3.1a3.8 3.8 0 0 0 5.4 5.4l1.1-1.1"],
    # l'endodontie : la dent et ses canaux
    "endo": ["M12 5.2C10.6 4.2 9.2 3.7 7.6 3.7 5 3.7 3.6 5.7 3.6 8.2c0 2.4 1 3.9 1.6 6.3.6 2.7 1.1 6 2.6 6 "
             "1.6 0 1.8-4.4 4.2-4.4s2.6 4.4 4.2 4.4c1.5 0 2-3.3 2.6-6 .6-2.4 1.6-3.9 1.6-6.3 0-2.5-1.4-4.5-4-4.5"
             "-1.6 0-3 .5-4.4 1.5z", "M9.6 8.6 8.9 16M14.4 8.6l.7 7.4"],
    # l'implantologie : la couronne sur sa vis
    "implant": ["M7.5 3.5h9c0 2.4-1.2 4-4.5 4s-4.5-1.6-4.5-4z", "M9.4 9.5h5.2l-.6 8.2L12 20.5l-2-2.8z",
                "M9.1 12.2h5.8M9.4 15h5.2"],
    # l'anatomie de la tête et du cou : le profil
    "anatomie": ["M14 20.5v-3.2h2.6a1.4 1.4 0 0 0 1.4-1.4v-2.4l2-1-2-3.6C17.8 5.6 15 3.5 11.2 3.5 7.3 3.5 4.5 6.4 4.5 10.2"
                 "c0 2.4 1.1 4.4 2.9 5.8v4.5"],
    # la sédation consciente : le souffle
    "sedation": ["M3.5 8.5h10.3a2.8 2.8 0 1 0-2.8-2.8", "M3.5 12h14.5a2.8 2.8 0 1 1-2.8 2.8", "M3.5 15.5h6.5"],
    # le numéro RPPS : la carte professionnelle
    "carte": ["M3.5 5.5h17v13h-17z", "M8.6 9a2 2 0 1 1 0 4 2 2 0 0 1 0-4z",
              "M5.6 16c.5-1.4 1.6-2.1 3-2.1s2.5.7 3 2.1", "M14.2 10h3.6M14.2 13h3.6"],
}


def picto(nom, classe="picto"):
    """Le pictogramme en SVG en ligne, à la couleur du texte qui l'entoure."""
    traces = "".join(f'<path d="{d}"/>' for d in TRACES[nom])
    return (f'<svg class="{classe}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'{traces}</svg>')
