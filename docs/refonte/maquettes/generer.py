#!/usr/bin/env python3
"""
Génère les maquettes de la refonte à partir du site actuel.

Le principe : on ne réécrit aucun texte. On relit les pages construites dans dist/,
on en extrait les titres, les paragraphes, les listes, les questions, les sources et
les photographies, et on les réimprime dans la mise en page de la direction « Revue ».

Ce que le générateur fait de lui-même :
  · les listes passent en encadré, à côté du texte, au lieu de s'empiler dessous ;
  · les sections alternent fond clair et fond teinté, pour donner un rythme ;
  · les questions se mettent sur deux colonnes ;
  · les sources se resserrent en bas de page.

Ce qu'il NE fait PAS : regrouper les douze chapitres en cinq. Ce regroupement demande
de décider ce qu'on garde et ce qu'on fond, c'est-à-dire du texte — cela revient à
ChatGPT. La page Usures, faite à la main, montre ce que ça donne quand c'est fait.

    python3 docs/refonte/maquettes/generer.py
"""
import html as H
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DIST = os.path.join(RACINE, "dist")
SORTIE = os.path.join(RACINE, "docs", "refonte", "maquettes", "site")
# la feuille de style est signée par sa date, pour contourner le cache du navigateur
VERSION = str(int(os.path.getmtime(os.path.join(SORTIE, "style.css"))))

# ── l'arborescence décidée le 16 octobre ──────────────────────────────────────
CONSTATS = [
    ("Mes dents s’usent", "usures-dentaires"),
    ("Mes dents deviennent fines", "erosion-dentaire"),
    ("Je serre des dents la nuit", "bruxisme-usure-dentaire"),
    ("Mes dents paraissent courtes", "dents-courtes-usees"),
    ("J’ai des taches blanches", "taches-dentaires-dyschromies-icon"),
    ("Mes dents sont jaunes", "eclaircissement-dentaire-paris"),
    ("Troubles alimentaires et dents", "tca-dents"),
]
TRAITEMENTS = [
    ("Dentisterie esthétique", "dentisterie-esthetique-paris"),
    ("Composite bonding", "composite-bonding-paris"),
    ("Facettes céramique", "facettes-dentaires-paris"),
    ("Facettes ou composite ?", "facettes-ou-composite"),
    ("Éclaircissement", "eclaircissement-dentaire-paris"),
    ("Réhabilitation des dents usées", "rehabilitation-dents-usees"),
    ("Bilan esthétique", "bilan-esthetique-personnalise"),
]
CONFRERES = [
    ("Conférences et formations", "conferences-formations"),
    ("Publications", "publications"),
    ("Activité hospitalière", "activite-hospitaliere"),
    ("Médias et interviews", "medias-interviews"),
]
# surtitre affiché en haut de chaque page, et fil d'Ariane
PUBLIC = {}
for lib, slug in CONSTATS:
    PUBLIC[slug] = ("Ce que vous constatez", "Patient", lib)
for lib, slug in TRAITEMENTS:
    PUBLIC.setdefault(slug, ("Ce qu’on peut faire", "Patient", lib))
for lib, slug in CONFRERES:
    PUBLIC[slug] = ("Pour les chirurgiens-dentistes", "Chirurgien-dentiste", lib)
PUBLIC["franck-moyal"] = ("Le praticien", None, "Dr Franck Moyal")
PUBLIC["chirurgien-dentiste-paris-9"] = ("Le cabinet", None, "Paris 9ᵉ")
PUBLIC["contact"] = ("Le cabinet", None, "Contact")
PUBLIC["mentions-legales"] = ("Informations", None, "Mentions légales")

# pages déjà faites à la main, qu'on n'écrase pas
A_LA_MAIN = {"usures-dentaires", "facettes-ou-composite"}
# le diagnostic est fondu dans les usures (D77) : plus de page à lui
FONDUES = {"diagnostic-usures-dentaires"}


# ── extraction ────────────────────────────────────────────────────────────────
def texte(frag):
    """Garde le gras et les liens internes, jette le reste du balisage."""
    f = re.sub(r"<(script|style)\b.*?</\1>", "", frag, flags=re.S)
    f = re.sub(r"<sup[^>]*class=\"cite\"[^>]*>.*?</sup>", "", f, flags=re.S)
    f = re.sub(r"<span[^>]*visually-hidden[^>]*>.*?</span>", "", f, flags=re.S)
    f = re.sub(r"<(?!/?(strong|em|b|i)\b)[^>]+>", " ", f)
    f = re.sub(r"\s+", " ", f)
    return f.strip()


def locale(src):
    """/_astro/nom.hash_hash.webp → le fichier d'origine dans le dépôt."""
    nom = re.sub(r"\.[A-Za-z0-9_-]+_[A-Za-z0-9_-]+\.(?:webp|jpg|png)$", ".jpg",
                 os.path.basename(src))
    if os.path.exists(os.path.join(RACINE, "src", "assets", "photos", "cas", nom)):
        return "/src/assets/photos/cas/" + nom
    return "/dist" + src


def lire(slug):
    chemin = os.path.join(DIST, slug, "index.html") if slug else os.path.join(DIST, "index.html")
    if not os.path.exists(chemin):
        return None
    brut = open(chemin, encoding="utf-8").read()
    main = re.search(r"<main.*?</main>", brut, re.S)
    if not main:
        return None
    main = main.group(0)

    page = {"slug": slug}
    t = re.search(r"<title>(.*?)</title>", brut, re.S)
    page["title"] = H.unescape(t.group(1).strip()) if t else slug
    d = re.search(r'<meta name="description" content="([^"]*)"', brut)
    page["description"] = H.unescape(d.group(1)) if d else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    page["h1"] = texte(h1.group(1)) if h1 else page["title"]

    # le chapô : premier paragraphe long avant la première section
    avant = main.split("<section", 1)[0]
    ps = [texte(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", avant, re.S)]
    ps = [p for p in ps if len(p) > 60]
    page["chapo"] = ps[0] if ps else ""

    # photographies de la page
    page["photos"] = []
    for fig in re.findall(r"<figure.*?</figure>", main, re.S):
        imgs = re.findall(r'\bsrc="(/_astro/[^"]+\.(?:webp|jpg|png))"', fig)
        alts = re.findall(r'\balt="([^"]*)"', fig)
        cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", fig, re.S)
        if imgs:
            page["photos"].append({
                "src": [locale(i) for i in imgs[:2]],
                "alt": [H.unescape(a) for a in alts[:2]] or [""],
                "legende": texte(cap.group(1)) if cap else "",
            })

    # sections
    page["sections"] = []
    page["faq"] = []
    page["sources"] = []
    for sec in re.findall(r"<section[^>]*>.*?</section>", main, re.S):
        h2 = re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S)
        titre = texte(h2.group(1)) if h2 else ""

        if "faq__item" in sec:
            # chaque item est <div class="faq__item"><h3>…</h3><p>…</p></div> ;
            # on découpe sur l'ouverture plutôt que de deviner les fermetures.
            for item in sec.split('class="faq__item"')[1:]:
                q = re.search(r"<h3[^>]*>(.*?)</h3>", item, re.S)
                r = re.search(r"<p[^>]*>(.*?)</p>", item, re.S)
                if q and r:
                    page["faq"].append({"q": texte(q.group(1)), "r": texte(r.group(1))})
            continue
        if "source__ref" in sec:
            for s in re.findall(r'<div[^>]*class="source__ref"[^>]*>(.*?)</div>', sec, re.S):
                page["sources"].append(texte(s))
            continue

        paras = [texte(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", sec, re.S)]
        # la ligne d'auteur et le chapô réapparaissent dans la première section
        paras = [p for p in paras
                 if len(p) > 45
                 and "Dr Franck Moyal — Chirurgien" not in p
                 and p != page["chapo"]]
        lis = [texte(x) for x in re.findall(r"<li[^>]*>(.*?)</li>", sec, re.S)]
        lis = [l for l in lis if 10 < len(l) < 240]
        liens = []
        for href, lib in re.findall(r'<a[^>]*href="(/[^"#?]+/)"[^>]*>(.*?)</a>', sec, re.S):
            lib = texte(lib)
            if (lib and len(lib) < 60 and "Franck Moyal" not in lib
                    and href.strip("/") != slug and (href, lib) not in liens):
                liens.append((href, lib))
        if titre or paras:
            page["sections"].append({"titre": titre, "p": paras, "li": lis, "liens": liens[:4]})
    return page


# ── rendu ─────────────────────────────────────────────────────────────────────
AUTORISES = ("strong", "em", "b", "i")


def e(s):
    """Échappe, puis rend leur rôle aux seules balises qu'on a gardées."""
    out = H.escape(s, quote=False)
    for t in AUTORISES:
        out = out.replace(f"&lt;{t}&gt;", f"<{t}>").replace(f"&lt;/{t}&gt;", f"</{t}>")
    return out


def menu(slug):
    def liste(items):
        return "\n".join(
            f'              <li><a href="{s}.html">{e(l)}</a></li>' for l, s in items
        )
    return f'''<header class="entete">
  <div class="entete__barre">
    <a class="marque" href="index.html">Dr Franck Moyal</a>
    <button class="burger" id="burger" aria-expanded="false">Menu</button>
    <nav class="nav" id="nav">
      <div>
        <button data-volet="v1" aria-expanded="false">Vous êtes patient</button>
        <div class="volet volet--deux" id="v1">
          <div>
            <h4>Ce que vous constatez</h4>
            <ul>
{liste(CONSTATS)}
            </ul>
          </div>
          <div>
            <h4>Ce qu’on peut faire</h4>
            <ul>
{liste(TRAITEMENTS)}
            </ul>
          </div>
        </div>
      </div>
      <div>
        <button data-volet="v2" aria-expanded="false">Vous êtes chirurgien-dentiste</button>
        <div class="volet" id="v2">
          <ul>
{liste(CONFRERES)}
            <li><a href="https://smileclubformations.com/" target="_blank" rel="noopener">Smile Club Formations <span class="ext">↗</span></a></li>
          </ul>
        </div>
      </div>
      <a class="lien" href="franck-moyal.html">Le praticien</a>
    </nav>
    <a class="rdv" href="contact.html">Prendre rendez-vous</a>
  </div>
</header>'''


PIED = '''<footer class="pied">
  <div class="contenu">
    <div class="pied__grille">
      <div><h4>Le cabinet</h4><ul><li>2 rue Hippolyte Lebas</li><li>75009 Paris</li><li>01 83 75 52 16</li></ul></div>
      <div><h4>Vous constatez</h4><ul><li><a href="usures-dentaires.html">Usures dentaires</a></li><li><a href="erosion-dentaire.html">Érosion dentaire</a></li><li><a href="tca-dents.html">Troubles alimentaires</a></li></ul></div>
      <div><h4>Traitements</h4><ul><li><a href="composite-bonding-paris.html">Composite bonding</a></li><li><a href="facettes-dentaires-paris.html">Facettes céramique</a></li><li><a href="eclaircissement-dentaire-paris.html">Éclaircissement</a></li></ul></div>
      <div><h4>Le praticien</h4><ul><li><a href="franck-moyal.html">Parcours</a></li><li><a href="publications.html">Publications</a></li><li><a href="activite-hospitaliere.html">Activité hospitalière</a></li></ul></div>
    </div>
    <p class="pied__bas">Maquette de refonte — rien n’est en ligne. Mentions légales.</p>
  </div>
</footer>'''


def photo(p, classe="solo"):
    alts = p.get("alt") or [""]
    if len(p["src"]) >= 2:
        imgs = "".join(
            f'<img src="{s}" alt="{H.escape(alts[i] if i < len(alts) else "")}" loading="lazy">'
            for i, s in enumerate(p["src"][:2]))
        bloc = f'<div class="paire">{imgs}</div>'
    else:
        bloc = f'<img src="{p["src"][0]}" alt="{H.escape(alts[0])}" loading="lazy">'
        classe = "solo"
    leg = f'<figcaption>{e(p["legende"])}</figcaption>' if p["legende"] else ""
    return f'<figure class="{classe}">{bloc}{leg}</figure>'


def rendre(page):
    slug = page["slug"]
    surtitre, public, libelle = PUBLIC.get(slug, ("", None, page["h1"][:40]))
    ariane = '<a href="index.html">Accueil</a>'
    if public:
        ariane += f' › {e(public)}'
    ariane += f' › {e(libelle)}'

    corps = []
    photos = list(page["photos"])
    ouverture = photos.pop(0) if photos else None

    # ── la une ──
    fig = ""
    if ouverture:
        src = ouverture["src"][0]
        alt = H.escape((ouverture.get("alt") or [""])[0])
        leg = f'<figcaption>{e(ouverture["legende"])}</figcaption>' if ouverture["legende"] else ""
        fig = f'      <figure><img src="{src}" alt="{alt}">{leg}</figure>\n'
    corps.append(f'''  <div class="contenu">
    <p class="ariane">{ariane}</p>
    <div class="une">
      <div>
        <p class="eyebrow">{e(surtitre)}</p>
        <h1>{e(page["h1"])}</h1>
        <p class="une__chapo">{e(page["chapo"])}</p>
        <div class="signature">
          <img src="img/portrait-fm.png" alt="Dr Franck Moyal">
          <div><b>Dr Franck Moyal</b> — chirurgien-dentiste, Paris 9<sup>e</sup><br>
            Praticien hospitalier, Pitié-Salpêtrière · CMME, Sainte-Anne</div>
        </div>
      </div>
{fig}    </div>
  </div>''')

    # ── les sections ──
    # La première section d'une page n'a pas de titre : c'est le bloc d'ouverture,
    # déjà repris dans la une. L'imprimer une seconde fois répétait le chapô.
    sections = page["sections"]
    if sections and not sections[0]["titre"]:
        sections = sections[1:]
    zone = False
    for i, s in enumerate(sections):
        if not s["titre"] and not s["p"]:
            continue
        zone = not zone
        cls = "sect sect--zone" if zone else "sect"
        titre = f'<h2>{e(s["titre"])}</h2>' if s["titre"] else ""
        paras = "\n        ".join(f"<p>{e(p)}</p>" for p in s["p"][:4])
        liens = ""
        if s["liens"]:
            liens = '\n        <p class="suite">' + " · ".join(
                f'<a href="{h.strip("/")}.html">{e(l)}</a>' for h, l in s["liens"]
            ) + "</p>"

        if s["li"]:
            items = "\n            ".join(f"<li>{e(l)}</li>" for l in s["li"][:7])
            corps.append(f'''  <section class="{cls}">
    <div class="contenu chapitre">
      <div>
        {titre}
        {paras}{liens}
      </div>
      <div class="fiche">
        <h4>En bref</h4>
        <ul>
            {items}
        </ul>
      </div>
    </div>
  </section>''')
        else:
            inner = f'<div class="deux-col">{paras}</div>' if len(s["p"]) >= 3 else paras
            img = ""
            if photos and i % 2 == 1:
                img = f'\n      <div class="cas">{photo(photos.pop(0), "paire-ou-solo")}</div>'
            corps.append(f'''  <section class="{cls}">
    <div class="contenu">
      <div class="chapitre chapitre--plein">
        <div>
          {titre}
          {inner}{liens}
        </div>
      </div>{img}
    </div>
  </section>''')

    # ── photographies restantes ──
    if photos:
        figs = "\n        ".join(photo(p) for p in photos)
        corps.append(f'''  <section class="sect">
    <div class="contenu">
      <p class="eyebrow">Cas cliniques</p>
      <h2>Cas du cabinet, photographiés avant et après</h2>
      <div class="cas">
        {figs}
      </div>
    </div>
  </section>''')

    # ── questions ──
    if page["faq"]:
        qs = "\n        ".join(
            f'<div><b>{e(q["q"])}</b><p>{e(q["r"])}</p></div>' for q in page["faq"][:8]
        )
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu">
      <p class="eyebrow">Questions fréquentes</p>
      <div class="qa">
        {qs}
      </div>
    </div>
  </section>''')

    # ── appel ──
    corps.append('''  <section class="appel">
    <div class="contenu">
      <h2>Faire le point</h2>
      <p>Un bilan permet de comprendre l’état des dents et les options possibles,
        avant tout engagement.</p>
      <a class="bouton" href="contact.html">Prendre rendez-vous</a>
    </div>
  </section>''')

    # ── sources ──
    if page["sources"]:
        src = "\n        ".join(f"<li>{e(s)}</li>" for s in page["sources"])
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu sources">
      <p class="eyebrow">Sources scientifiques</p>
      <ol>
        {src}
      </ol>
    </div>
  </section>''')

    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(page["title"])}</title>
<meta name="description" content="{H.escape(page["description"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap">
<link rel="stylesheet" href="style.css?v={VERSION}">
</head>
<body>

{menu(slug)}

<main>

{chr(10).join(corps)}

</main>

{PIED}

<script src="menu.js"></script>
</body>
</html>
'''


# ── exécution ─────────────────────────────────────────────────────────────────
def main():
    slugs = sorted(
        d for d in os.listdir(DIST)
        if os.path.isdir(os.path.join(DIST, d))
        and os.path.exists(os.path.join(DIST, d, "index.html"))
        and d not in ("_astro", "cas-cliniques")
    )
    for cas in sorted(os.listdir(os.path.join(DIST, "cas-cliniques"))
                      if os.path.isdir(os.path.join(DIST, "cas-cliniques")) else []):
        if os.path.exists(os.path.join(DIST, "cas-cliniques", cas, "index.html")):
            slugs.append(f"cas-cliniques/{cas}")

    faits, passes = [], []
    for slug in slugs:
        court = slug.replace("cas-cliniques/", "cas-")
        if court in A_LA_MAIN:
            passes.append((court, "faite à la main"))
            continue
        if court in FONDUES:
            passes.append((court, "fondue dans les usures (D77)"))
            continue
        page = lire(slug)
        if not page:
            passes.append((court, "illisible"))
            continue
        page["slug"] = court
        open(os.path.join(SORTIE, f"{court}.html"), "w", encoding="utf-8").write(rendre(page))
        faits.append((court, len(page["sections"]), len(page["faq"]), len(page["photos"])))

    print(f"{len(faits)} page(s) générée(s) dans docs/refonte/maquettes/site/\n")
    print(f"  {'page':44s} {'chapitres':>9s} {'questions':>9s} {'photos':>6s}")
    for c, ns, nf, np_ in faits:
        alerte = "  ← encore trop de chapitres" if ns > 7 else ""
        print(f"  {c:44s} {ns:9d} {nf:9d} {np_:6d}{alerte}")
    if passes:
        print("\n  non générées :")
        for c, pourquoi in passes:
            print(f"    {c:42s} {pourquoi}")


if __name__ == "__main__":
    main()
