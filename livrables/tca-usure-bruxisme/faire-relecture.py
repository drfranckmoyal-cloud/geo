#!/usr/bin/env python3
"""Réunit en une seule page les textes écrits le 12/11/2026 pour pousser TCA, usure et bruxisme,
pour que Franck les relise d'un trait avant la mise en ligne : TEXTES-A-RELIRE.html, à côté de ce script.

    python3 livrables/tca-usure-bruxisme/faire-relecture.py
"""
import html as H
import importlib.util
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
MAQ = os.path.join(ICI, "..", "..", "docs", "refonte", "maquettes")

spec = importlib.util.spec_from_file_location("bruxisme", os.path.join(MAQ, "ecrire-bruxisme.py"))
brux = importlib.util.module_from_spec(spec)
spec.loader.exec_module(brux)


def nu(s):
    return re.sub(r"<(?!/?strong)[^>]+>", "", s)


def article(nom):
    brut = open(os.path.join(MAQ, "articles", nom + ".txt"), encoding="utf-8").read()
    tete, _, texte = brut.partition("\n---\n")
    titre = re.search(r"^titre:\s*(.*)$", tete, re.M).group(1)
    out = [f"<h2>Article — {H.escape(titre)}</h2>",
           f'<p class="ou">Adresse : drfranckmoyal.fr/articles/{nom}/</p>']
    for bloc in re.split(r"\n\s*\n", texte.strip()):
        lignes = bloc.strip().splitlines()
        if lignes[0].startswith("## "):
            out.append(f"<h3>{H.escape(lignes[0][3:])}</h3>")
        elif lignes[0].startswith("> "):
            out.append("<blockquote>" + H.escape(" ".join(l.lstrip("> ") for l in lignes)) + "</blockquote>")
        elif lignes[0].startswith("- "):
            out.append("<ul>" + "".join(f"<li>{H.escape(l[2:])}</li>" for l in lignes) + "</ul>")
        else:
            out.append("<p>" + H.escape(" ".join(lignes)) + "</p>")
    return "\n".join(out)


def page_bruxisme():
    out = ["<h2>Page Bruxisme, réécrite</h2>",
           '<p class="ou">Adresse inchangée : drfranckmoyal.fr/bruxisme-usure-dentaire/</p>',
           f"<p><b>Titre affiché par Google :</b> {H.escape(brux.TITRE)}</p>",
           f"<p><b>Description :</b> {H.escape(brux.DESCRIPTION)}</p>",
           f"<p><b>Ouverture :</b> {H.escape(brux.CHAPO)}</p>"]
    for k, ch in enumerate(brux.CHAPITRES, 1):
        out.append(f"<h3>{k} / {len(brux.CHAPITRES)} — {H.escape(ch['q'])}</h3>")
        out.append(f"<p><b>{nu(ch['r'])}</b></p>")
        for titre, paras in ch["blocs"]:
            out.append(f"<h4>{H.escape(titre)}</h4>")
            out += [f"<p>{nu(p)}</p>" for p in paras]
        if ch.get("fiche"):
            titre, items = ch["fiche"]
            out.append(f'<p class="encadre"><b>Encadré « {H.escape(titre)} » :</b> ' + " · ".join(map(H.escape, items)) + "</p>")
    return "\n".join(out)


COURTS = """
<h2>Les textes courts</h2>
<h3>Accueil</h3>
<p><b>Titre affiché par Google :</b> Dr Franck Moyal | Dentisterie esthétique, usure dentaire, TCA | Paris 9e</p>
<p><b>Description :</b> Dr Franck Moyal, chirurgien-dentiste à Paris 9e : dentisterie esthétique et adhésive (facettes,
composite bonding, éclaircissement), usure dentaire, bruxisme, érosion et dents abîmées par les troubles des conduites
alimentaires (TCA). Espace patients et espace professionnel.</p>
<p><b>Nouveau bloc, sous « Dentisterie esthétique à Paris » — titre :</b> Usure dentaire, bruxisme et TCA</p>
<p><b>Texte :</b> Il prend aussi en charge l’usure dentaire, l’érosion, le bruxisme et les dents abîmées par les troubles
des conduites alimentaires (TCA).</p>
<p><b>Porte « Espace Patients », trois entrées ajoutées à la liste :</b> Usure dentaire · Bruxisme · TCA et dents</p>
<h3>Titres affichés par Google</h3>
<ul>
<li>Usure dentaire : causes, signes, traitements | Dentiste à Paris 9e</li>
<li>TCA et dents : anorexie, boulimie, vomissements | Dentiste à Paris 9e</li>
<li>Dents trop courtes ou usées à Paris | Dr Franck Moyal</li>
</ul>
<h3>Page Dents courtes ou usées</h3>
<p><b>Premier chapitre, nouveau titre :</b> Mes dents sont trop courtes ou devenues plus petites : est-ce de l’usure ?</p>
<p><b>Nouvelle question fréquente :</b> Mes dents sont trop courtes : que peut-on faire ?<br>
D’abord comprendre pourquoi. Des dents trop courtes ont le plus souvent raccourci par usure : on traite alors la cause,
puis on leur rend leur longueur en ajoutant du composite ou de la céramique collée, sans les tailler ou presque. Une
usure légère et stable peut simplement être surveillée.</p>
<h3>Page Bruxisme, deux questions fréquentes ajoutées</h3>
<p><b>Comment savoir si je grince des dents la nuit ?</b><br>Souvent, c’est l’entourage qui l’entend. Sinon, une mâchoire
tendue ou fatiguée au réveil, des bords de dents qui s’ébrèchent ou des restaurations qui cassent peuvent y faire penser.
Le diagnostic repose sur l’entretien et l’examen, parfois sur un enregistrement du sommeil.</p>
<p><b>Le bruxisme se soigne-t-il ?</b><br>Une gouttière ne le fait pas disparaître. On en limite les conséquences : elle
protège les dents quand le frottement est en cause, on recherche une érosion associée, et l’on reconstruit les dents
usées si c’est nécessaire.</p>
"""

A_VERIFIER = """
<h2>Ce qui est nouveau, à vérifier en priorité</h2>
<p>Presque tout reprend des phrases déjà validées sur les pages Usure dentaire, TCA et Bruxisme. Les phrases ci-dessous,
elles, n’existaient pas sur le site.</p>
<ul>
<li><b>Page Bruxisme :</b> « Le jour, le serrement passe tout aussi inaperçu, mais on peut apprendre à le repérer. »</li>
<li><b>Page Bruxisme :</b> « Beaucoup de personnes serrent ou grincent des dents sans aucune conséquence. »</li>
<li><b>Page Bruxisme :</b> « Les dents ne frottent plus l’une contre l’autre : c’est la gouttière qui s’use. »</li>
<li><b>Page Bruxisme :</b> les signes « une mâchoire tendue ou fatiguée au réveil, un grincement entendu par l’entourage,
des bords de dents qui s’ébrèchent, des restaurations qui cassent ou se décollent ».</li>
<li><b>Article sur le brossage :</b> « Se rincer la bouche, si possible avec un bain de bouche fluoré », et le paragraphe
« Trouble alimentaire, reflux, grossesse : le même acide ».</li>
<li><b>Article sur la gouttière :</b> « je ne prescris pas une gouttière avant d’avoir compris ce qui use » — une phrase
dite en votre nom.</li>
<li><b>Source ajoutée à la page Bruxisme :</b> le consensus international sur le bruxisme (Lobbezoo et coll., 2018),
vérifié sur PubMed.</li>
</ul>
"""

STYLE = """
body{font:17px/1.6 Georgia,serif;max-width:46rem;margin:2rem auto;padding:0 1.1rem;color:#1a1c19;background:#fffefb}
h1{font-size:1.7rem;line-height:1.2}h2{font-size:1.3rem;margin-top:2.6rem;padding-top:1.2rem;border-top:2px solid #1a1c19}
h3{font-size:1.08rem;margin-top:1.6rem}h4{font-size:.98rem;margin:1.1rem 0 .2rem}
p{margin:.5rem 0}.ou{font:13px/1.4 -apple-system,Helvetica,sans-serif;color:#666}
blockquote{margin:.8rem 0;padding-left:1rem;border-left:3px solid #1a1c19;font-style:italic}
.encadre{font-size:.92rem;background:#f1efe8;padding:.6rem .8rem;border-radius:4px}
"""


def main():
    corps = ["<h1>Textes à relire avant la mise en ligne</h1>",
             "<p>Écrits le 12 novembre 2026 pour pousser TCA, usure dentaire et bruxisme. Rien n’est en ligne.</p>",
             A_VERIFIER, COURTS, page_bruxisme()]
    corps += [article(n) for n in ("boulimie-dents", "se-brosser-les-dents-apres-avoir-vomi",
                                   "bruxisme-gouttiere-suffit-elle", "dents-usees-quand-consulter")]
    page = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f"<title>Textes à relire</title><style>{STYLE}</style></head><body>\n"
            + "\n".join(corps) + "\n</body></html>\n")
    open(os.path.join(ICI, "TEXTES-A-RELIRE.html"), "w", encoding="utf-8").write(page)
    print("écrit : TEXTES-A-RELIRE.html,", len(re.sub(r"<[^>]+>", " ", page).split()), "mots")


if __name__ == "__main__":
    main()
