#!/usr/bin/env python3
"""
Écrit la page Bruxisme de la maquette (site/bruxisme-usure-dentaire.html).

Franck, 11/11/2026 : « je veux beaucoup plus pousser TCA et Usure dentaire et Bruxisme »,
puis « oui go fais tout d'un coup ». La page Bruxisme était la seule des trois à ne pas avoir
été réécrite : elle l'est ici, sur le modèle des pages Usure dentaire et TCA (25/10/2026) —
une question par chapitre, la réponse en tête, « Quel dentiste consulter ».

Le fond reste celui de la page d'origine (pack V1.2, fichier 09) et de la page Usure dentaire :
une usure ne prouve pas un bruxisme, la gouttière protège mais ne guérit pas, l'érosion se
cherche toujours. Ce script ne refait que le haut de la page, le corps et « À lire aussi » :
l'en-tête, le pied, les questions fréquentes (questions.txt) et les données structurées sont
tenus par generer.py, comme pour toute page écrite à la main.

    python3 docs/refonte/maquettes/ecrire-bruxisme.py
"""
import html as H
import json
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(ICI, "site", "bruxisme-usure-dentaire.html")

TITRE = "Bruxisme : signes, gouttière, dents usées | Dentiste à Paris 9e"
DESCRIPTION = ("Bruxisme : comment savoir si l’on serre ou grince des dents, ce que cela fait aux dents, "
               "à quoi sert une gouttière et quand reconstruire. Dr Franck Moyal, Paris 9e.")
CHAPO = ("Serrer ou grincer des dents n’est pas une maladie en soi, et des dents plates ne prouvent pas "
         "qu’on bruxe. Avant de proposer une gouttière, il faut établir si le bruxisme est réel, ce qui "
         "use vraiment les dents — le frottement, l’acide, souvent les deux — et ce qui mérite d’être "
         "protégé, surveillé ou reconstruit.")

PHOTO = ("../../../../src/assets/photos/cas/usure-reflux-grincement-avant-apres.jpg",
         "Avant et après : dents très usées et jaunies par l’érosion et le grincement, puis reconstruites, "
         "sourire de face",
         "Usures avancées dues à des années d’érosion acide, liée à un reflux, et au grincement des dents.")


def lien(page, texte):
    return f'<a class="lt" href="{page}.html">{texte}</a>'


CHAPITRES = [
    {"q": "Qu’est-ce que le bruxisme ?",
     "r": "C’est une activité des muscles de la mâchoire : on serre ou on grince des dents, pendant le "
          "sommeil ou en pleine journée, le plus souvent sans s’en rendre compte. Ce n’est pas "
          "automatiquement une maladie : tout dépend de ses conséquences sur les dents, les muscles et "
          "les articulations.",
     "blocs": [
         ("Serrer, grincer, contracter",
          ["Le bruxisme prend trois formes : le <strong>serrement</strong>, silencieux ; le "
           "<strong>grincement</strong>, que l’entourage entend parfois la nuit ; et de simples mises en "
           "tension de la mâchoire. On peut donc bruxer sans jamais grincer des dents."]),
         ("La nuit, ou le jour",
          ["Le bruxisme du sommeil et celui de l’éveil sont deux situations différentes. La nuit, on ne "
           "contrôle rien et l’on ne s’en aperçoit pas. Le jour, le serrement passe tout aussi inaperçu, "
           "mais on peut apprendre à le repérer."]),
         ("Faut-il toujours le traiter ?",
          ["Non. Le bruxisme est multifactoriel, et le stress n’en est pas la seule cause. Beaucoup de "
           "personnes serrent ou grincent des dents sans aucune conséquence. On s’en occupe quand il "
           "abîme les dents ou les restaurations, ou quand il s’accompagne de douleurs."]),
     ],
     "fiche": ("En bref", ["Serrement ou grincement", "La nuit comme le jour",
                           "Souvent sans s’en rendre compte", "Pas toujours une maladie à traiter",
                           "Ce qui compte : ses conséquences"])},
    {"q": "Comment savoir si l’on bruxe ?",
     "r": "Le diagnostic ne repose pas sur une seule observation : selon les cas, il associe "
          "l’interrogatoire, les symptômes, l’examen clinique, l’évaluation des muscles et parfois un "
          "enregistrement du sommeil. L’aspect des dents participe au raisonnement, mais ne suffit pas.",
     "blocs": [
         ("Les signes qui font y penser",
          ["Une mâchoire tendue ou fatiguée au réveil, un grincement entendu par l’entourage, des bords "
           "de dents qui s’ébrèchent, des restaurations qui cassent ou se décollent. Aucun de ces signes "
           "ne suffit à lui seul : c’est leur réunion, et l’examen, qui orientent."]),
         ("Des dents plates ne suffisent pas",
          ["C’est l’idée reçue la plus répandue. Une revue de la littérature publiée en 2024 conclut que "
           "la présence d’une usure ne permet pas, à elle seule, d’affirmer un bruxisme. Il faut "
           "distinguer l’existence d’une usure, sa cause, l’existence éventuelle d’un bruxisme, et le "
           "rôle réel de ce bruxisme dans sa progression."]),
         ("Bruxisme et douleurs : deux questions distinctes",
          ["On peut bruxer sans douleur, avoir des douleurs sans usure marquée, et avoir une usure sans "
           "bruxisme actif. Les douleurs des muscles ou de l’articulation de la mâchoire demandent une "
           "analyse à part : elles ne se déduisent pas de l’état des dents."]),
     ],
     "fiche": ("Le diagnostic associe", ["L’interrogatoire", "Les symptômes rapportés", "L’examen clinique",
                                         "L’évaluation des muscles et de la fonction",
                                         "Un enregistrement du sommeil, quand il est indiqué"])},
    {"q": "Le bruxisme use-t-il les dents ?",
     "r": "Il peut y contribuer, mais il n’explique pas tout : des dents usées ne prouvent pas, à elles "
          "seules, qu’on bruxe. L’érosion par les acides est souvent en cause, seule ou associée au "
          "frottement.",
     "blocs": [
         ("Ce que fait le frottement",
          ["Les contraintes mécaniques aplatissent les reliefs, usent le bord des incisives, provoquent "
           "des éclats et sollicitent les restaurations. C’est l’attrition : l’usure des dents contre "
           "les dents, l’une des formes de l’" + lien("usures-dentaires", "usure dentaire") + "."]),
         ("Quand l’acide s’en mêle",
          ["Une dent régulièrement exposée aux acides — boissons acides, reflux, vomissements — est "
           "ramollie en surface, et s’use alors beaucoup plus vite au moindre frottement. Les consensus "
           "sur l’usure érosive décrivent précisément cette interaction entre la chimie et la mécanique : "
           "l’acide fragilise, le frottement emporte."]),
         ("L’erreur classique",
          ["« Dents usées, donc bruxisme, donc gouttière. » Une protection mécanique seule ne peut pas "
           "contrôler une cause chimique encore active. Devant une usure, je cherche toujours une "
           + lien("erosion-dentaire", "érosion dentaire") + " avant de conclure au bruxisme."]),
     ],
     "photo": True,
     "fiche": ("À rechercher devant une usure", ["Un reflux", "Des vomissements",
                                                 "Des boissons ou des aliments acides",
                                                 "Une salive moins abondante", "Certains médicaments",
                                                 "Un serrement ou un grincement"]),
     "suite": [("erosion-dentaire", "Érosion dentaire : dépistage et prévention"),
               ("usures-dentaires", "Usure dentaire : causes, signes et traitements")]},
    {"q": "À quoi sert une gouttière, et suffit-elle ?",
     "r": "Une gouttière protège les dents et les restaurations des contacts, surtout la nuit, mais elle "
          "ne guérit pas le bruxisme et ne protège pas de l’acide. Elle a sa place quand le frottement "
          "est en cause ; elle ne suffit pas quand une érosion entretient l’usure.",
     "blocs": [
         ("Ce qu’elle fait",
          ["Elle protège les dents ou certaines restaurations, modifie les contacts entre les dents et "
           "aide à gérer certaines situations fonctionnelles. Les dents ne frottent plus l’une contre "
           "l’autre : c’est la gouttière qui s’use."]),
         ("Ce qu’elle ne fait pas",
          ["Elle ne fait pas disparaître le bruxisme, et ce n’est pas une prévention universelle de "
           "l’érosion dentaire. Son intérêt se décide selon le mécanisme dominant de l’usure et la "
           "situation de chacun : la prescrire d’office à toute personne dont les dents sont plates, "
           "c’est risquer de passer à côté de la cause."]),
         ("Après une reconstruction",
          ["Quand des dents usées ont été reconstruites chez une personne qui bruxe, une gouttière est "
           "souvent prévue pour protéger les restaurations la nuit."]),
     ],
     "fiche": ("La gouttière", ["Protège les dents et les restaurations", "Ne guérit pas le bruxisme",
                                "Ne protège pas de l’acide", "Se décide après le diagnostic",
                                "Souvent utile après une reconstruction"]),
     "suite": [("article-bruxisme-gouttiere-suffit-elle",
                "Article : la gouttière suffit-elle à protéger les dents ?")]},
    {"q": "Peut-on reconstruire des dents usées quand on bruxe ?",
     "r": "Oui, lorsque l’indication est posée : les reconstructions collées, peu invasives, disposent "
          "aujourd’hui de données cliniques favorables dans les dentitions usées. Le projet tient "
          "simplement compte des contraintes.",
     "blocs": [
         ("D’abord la cause, ensuite la reconstruction",
          ["Restaurer sur une usure encore active, c’est la voir reprendre sur les restaurations. On "
           "commence donc par maîtriser ce qui use — l’acide, le frottement, ou les deux — avant de "
           "rendre aux dents ce qu’elles ont perdu."]),
         ("Un projet pensé pour durer",
          ["Chez une personne qui bruxe, le choix des matériaux, le réglage des contacts, l’entretien et "
           "la possibilité de réparer comptent autant que la forme des dents. Le composite se répare "
           "facilement ; la céramique prend le relais quand les contraintes le justifient. Un même "
           "patient reçoit souvent les deux."]),
         ("En ajoutant, plutôt qu’en taillant",
          ["Les techniques collées permettent de reconstruire sans tailler les dents, ou presque : "
           "composite stratifié sur les dents de devant, pièces collées sur les molaires, et, quand les "
           "dents ont beaucoup perdu, une réhabilitation complète qui leur rend leur hauteur."]),
     ],
     "fiche": ("Le projet tient compte", ["Des contraintes", "Des matériaux", "De l’entretien",
                                          "De la façon dont les dents se rencontrent",
                                          "De la possibilité de réparer"]),
     "suite": [("usures-dentaires", "Réparer des dents usées"),
               ("dents-courtes-usees", "Dents courtes ou usées")]},
    {"q": "Quel dentiste consulter pour un bruxisme ?",
     "r": "Un chirurgien-dentiste qui ne s’arrête pas à la gouttière. Il faut d’abord établir si l’on "
          "bruxe vraiment, ce qui use les dents, puis décider de ce qui mérite d’être protégé, surveillé "
          "ou reconstruit.",
     "blocs": [
         ("Ce qui fait la différence",
          ["Distinguer une usure par frottement d’une usure par érosion ; ne pas déduire un bruxisme de "
           "la seule forme des dents ; mesurer l’usure pour savoir si elle progresse ; et, quand il faut "
           "reconstruire, maîtriser l’analyse de l’occlusion et les techniques collées."]),
         ("Le Dr Franck Moyal, le bruxisme et les usures",
          ["Le Dr Franck Moyal est un chirurgien-dentiste spécialisé dans la prise en charge des "
           "usures. À la Pitié-Salpêtrière, il est responsable de la consultation des internes en "
           "dentisterie esthétique et usures, et ses confrères l’invitent très régulièrement à "
           "enseigner ce sujet."]),
         ("Au cabinet, à Paris 9e",
          ["Il reçoit à son cabinet de Paris 9<sup>e</sup> les personnes qui serrent ou grincent des "
           "dents, pour un bilan d’usure : entretien, examen des dents et de la façon dont elles se "
           "rencontrent, photographies et empreinte numérique de référence. C’est la comparaison dans le "
           "temps qui dit si l’usure progresse, et ce qu’il faut protéger ou reconstruire."]),
     ],
     "fiche_liens": ("Pour aller plus loin", [("usures-dentaires", "Usure dentaire"),
                                             ("erosion-dentaire", "Érosion dentaire"),
                                             ("dents-courtes-usees", "Dents courtes ou usées"),
                                             ("conferences-formations", "Conférences et formations")])},
]

A_LIRE = [("usures-dentaires", "Usure dentaire"), ("erosion-dentaire", "Érosion dentaire"),
          ("dents-courtes-usees", "Dents courtes ou usées"),
          ("tca-dents", "Troubles des conduites alimentaires (TCA)"),
          ("article-bruxisme-gouttiere-suffit-elle", "La gouttière suffit-elle ?"),
          ("franck-moyal", "Dr Franck Moyal")]

SOURCE_AJOUTEE = (
    '        <li><strong>Lobbezoo F, Ahlberg J, Raphael KG, et al.</strong> International consensus on the '
    'assessment of bruxism: Report of a work in progress. <em>J Oral Rehabil.</em> 2018;45(11):837–844. — '
    'DOI : <a href="https://doi.org/10.1111/joor.12663" target="_blank" rel="noopener">10.1111/joor.12663</a> — '
    '<a href="https://pubmed.ncbi.nlm.nih.gov/29926505/" target="_blank" rel="noopener">PubMed</a></li>\n')


def fr(s):
    """Les espaces insécables de la typographie française, hors des balises."""
    def texte(m):
        x = m.group(0)
        x = re.sub(r" ([:;?!»])", " \\1", x)
        return x.replace("« ", "« ")
    return re.sub(r"(?<=>)[^<]+|^[^<]+", texte, s)


def section(k, n, ch):
    zone = " sect--zone" if k % 2 == 0 else ""
    blocs = [f'        <div class="bloc">\n          <p class="reponse">{fr(ch["r"])}</p>\n        </div>']
    for titre, paras in ch["blocs"]:
        ps = "\n".join(f"          <p>{fr(p)}</p>" for p in paras)
        blocs.append(f'        <div class="bloc">\n          <h3>{fr(titre)}</h3>\n{ps}\n        </div>')
    if ch.get("suite"):
        liens = " · ".join(f'<a href="{p}.html">{fr(t)}</a>' for p, t in ch["suite"])
        blocs.append(f'        <div class="bloc">\n          <p class="suite">{liens}</p>\n        </div>')
    cote = []
    if ch.get("photo"):
        src, alt, leg = PHOTO
        cote.append(f'        <figure class="illus illus--libre">\n'
                    f'          <img src="{src}" alt="{H.escape(alt)}" loading="lazy">\n'
                    f'          <figcaption><span>{fr(leg)}</span></figcaption>\n        </figure>')
    if ch.get("fiche"):
        titre, items = ch["fiche"]
        lis = "\n".join(f"          <li>{fr(x)}</li>" for x in items)
        cote.append(f'        <div class="fiche">\n          <h4>{fr(titre)}</h4>\n          <ul>\n{lis}\n'
                    f'          </ul>\n        </div>')
    if ch.get("fiche_liens"):
        titre, items = ch["fiche_liens"]
        lis = "\n".join(f'          <li><a href="{p}.html">{fr(t)}</a></li>' for p, t in items)
        cote.append(f'        <div class="fiche">\n          <h4>{fr(titre)}</h4>\n          <ul>\n{lis}\n'
                    f'          </ul>\n        </div>')
    return (f'  <section class="sect{zone}">\n    <div class="contenu chapitre">\n      <div>\n'
            f'        <p class="numero">{k} / {n}</p>\n        <h2>{fr(ch["q"])}</h2>\n'
            + "\n".join(blocs) + "\n      </div>\n      <div class=\"cote\">\n"
            + "\n".join(cote) + "\n      </div>\n    </div>\n  </section>")


def main():
    page = open(PAGE, encoding="utf-8").read()

    # le titre et la description, dans la page et dans ses données structurées
    page = re.sub(r"<title>.*?</title>", lambda _m: f"<title>{H.escape(TITRE, quote=False)}</title>",
                  page, count=1, flags=re.S)
    page = re.sub(r'<meta name="description" content="[^"]*">',
                  lambda _m: f'<meta name="description" content="{H.escape(DESCRIPTION)}">', page, count=1)

    def donnees(m):
        d = json.loads(m.group(1))
        for n in d.get("@graph", []):
            if str(n.get("@type", "")).endswith("WebPage"):
                n["name"], n["description"] = TITRE, DESCRIPTION
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"
    page = re.sub(r'<script type="application/ld\+json">(.*?)</script>', donnees, page, flags=re.S)

    # du fil d'Ariane jusqu'aux questions fréquentes : l'ouverture et les chapitres
    debut = page.index('  <div class="contenu">\n    <p class="ariane">')
    fin = page.index('  <section class="sect sect--serre">\n    <div class="contenu">\n'
                     '      <h2 class="tete-bande">Questions fréquentes</h2>')
    n = len(CHAPITRES)
    une = f'''  <div class="contenu">
    <p class="ariane"><a href="index.html">Accueil</a> › Patient › Bruxisme</p>
    <div class="une">
      <div>
        <p class="eyebrow">Le sujet</p>
        <h1>Bruxisme</h1>
        <p class="sous-titre">Serrement, grincement, gouttière</p>
        <p class="une__chapo">{fr(CHAPO)}</p>
        <div class="signature">
          <img src="img/portrait-fm.png?v=1792223424" alt="Dr Franck Moyal">
          <div><b>Dr Franck Moyal</b> — chirurgien-dentiste spécialisé dans la prise en charge des usures, Paris 9<sup>e</sup><br>
            Responsable de la consultation des internes en dentisterie esthétique et usures, Pitié-Salpêtrière</div>
        </div>
      </div>
    </div>
  </div>

'''
    corps = "\n".join(section(k, n, ch) for k, ch in enumerate(CHAPITRES, 1))
    page = page[:debut] + une + corps + "\n" + page[fin:]

    # « À lire aussi » : des renvois sans doublon, et l'article sur la gouttière
    liens = " · ".join(f'<a href="{p}.html">{fr(t)}</a>' for p, t in A_LIRE)
    page, fait = re.subn(r'(<p class="eyebrow">À lire aussi</p>\s*<p class="suite">).*?(</p>)',
                         lambda m: m.group(1) + liens + m.group(2), page, count=1, flags=re.S)
    assert fait == 1, "bloc « À lire aussi » introuvable"

    # la source du consensus international sur le bruxisme (vérifiée sur PubMed le 12/11/2026)
    if "10.1111/joor.12663" not in page:
        repere = "      <ol>\n"
        i = page.index(repere, page.index('<div class="contenu sources">'))
        j = page.index("</li>\n", i) + len("</li>\n")
        page = page[:j] + SOURCE_AJOUTEE + page[j:]

    open(PAGE, "w", encoding="utf-8").write(page)
    print("page Bruxisme écrite :", n, "chapitres")


if __name__ == "__main__":
    main()
