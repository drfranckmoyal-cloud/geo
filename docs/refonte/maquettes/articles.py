#!/usr/bin/env python3
"""
Fabrique la rubrique Articles de la maquette : la liste des articles
(articles.html) et une page par article (article-<slug>.html). Sur le futur site,
chaque article a sa propre adresse, https://drfranckmoyal.fr/articles/<slug>/ :
c'est elle que Franck met dans ses posts LinkedIn.

Franck, 21/10/2026 : « plutôt Articles récents et articles où je publie mes
articles directement sur mon site, avec une URL qui pointe dessus pour mes
posts LinkedIn ».

La source d'un article est un fichier texte dans articles/ : quelques lignes
« clé: valeur » (titre, court, date, public, genre, linkedin, voir), une ligne
« --- », puis le texte. Un paragraphe par bloc ; « ## » ouvre un intertitre,
« > » une citation, « - » une liste. Le premier paragraphe sert de chapô.
Le texte est celui de Franck, tel quel : on ne réécrit rien.

    python3 docs/refonte/maquettes/articles.py
"""
import html as H
import json
import math
import os
import re
from urllib.parse import quote

import generer as G

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(ICI, "articles")
MOTS_PAR_MINUTE = 230
PUBLICS = {"patients": "Pour les patients", "confreres": "Pour les confrères"}
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]
POLICES = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
           '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:'
           'wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;'
           '8..60,700&display=swap">')

# Deux articles LinkedIn sont déjà devenus des pages du site : ils figurent dans
# la liste, mais mènent à la page qui les porte. Pas de doublon, pas de seconde
# adresse pour un même texte.
DEJA_SUR_LE_SITE = [
    {"titre": "Réhabiliter un sourire usé sans sacrifier davantage de tissu dentaire",
     "date": "2026-09-24", "public": "patients", "genre": "Cas clinique",
     "page": "cas-usures-dentaires-facettes-minimalement-invasives"},
    {"titre": "Anorexie restrictive : pourquoi observe-t-on des érosions dentaires "
              "en l’absence de vomissements ?",
     "date": "2026-09-11", "public": "patients", "genre": "Article",
     "page": "anorexie-erosion-dentaire-sans-vomissements"},
]


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m - 1]} {a}"


def minutes(mots):
    return max(1, math.ceil(mots / MOTS_PAR_MINUTE))


def t(s):
    """Échappe, et pose les espaces insécables de la typographie française :
    sans elles, un titre peut renvoyer son deux-points seul en début de ligne."""
    s = re.sub(r" ([:»])", "\u00a0\\1", s)
    s = re.sub(r" ([;!?])", "\u202f\\1", s)
    s = s.replace("« ", "«\u00a0")
    return H.escape(s, quote=False)


def lire(chemin):
    brut = open(chemin, encoding="utf-8").read()
    tete, _, texte = brut.partition("\n---\n")
    a = {"slug": os.path.basename(chemin)[:-4]}
    for ligne in tete.splitlines():
        cle, _, val = ligne.partition(":")
        if val:
            a[cle.strip()] = val.strip()
    a["voir"] = [s.strip() for s in a.get("voir", "").split(",") if s.strip()]
    blocs = []
    for bloc in re.split(r"\n\s*\n", texte.strip()):
        lignes = bloc.strip().splitlines()
        if lignes[0].startswith("## "):
            blocs.append(("h2", lignes[0][3:].strip()))
        elif lignes[0].startswith("> "):
            blocs.append(("citation", " ".join(l.lstrip("> ").strip() for l in lignes)))
        elif lignes[0].startswith("- "):
            blocs.append(("liste", [l[2:].strip() for l in lignes]))
        else:
            blocs.append(("p", " ".join(l.strip() for l in lignes)))
    a["chapo"] = blocs[0][1]
    a["blocs"] = blocs[1:]
    mots = sum(len((" ".join(b[1]) if b[0] == "liste" else b[1]).split()) for b in blocs)
    a["minutes"] = minutes(mots)
    a["mots"] = mots
    a["fichier"] = f"article-{a['slug']}"
    a["url"] = f"{G.RACINE_WEB}articles/{a['slug']}/"
    return a


def page_existante(entree):
    """Une entrée qui mène à une page déjà sur le site : son chapô et sa durée de
    lecture se relèvent sur cette page, pour dire ce que le lecteur y trouvera."""
    h = open(os.path.join(G.SORTIE, entree["page"] + ".html"), encoding="utf-8").read()
    corps = re.search(r"<main.*?</main>", h, re.S).group(0)
    corps = re.sub(r'<section class="(?:appel|sect sect--serre)">.*?</section>', " ", corps, flags=re.S)
    mots = len(re.sub(r"<[^>]+>", " ", corps).split())
    desc = re.search(r'<meta name="description" content="([^"]*)"', h)
    return dict(entree, fichier=entree["page"], minutes=minutes(mots),
                chapo=H.unescape(desc.group(1)) if desc else "")


# le nom que porte le lien dans le menu, quand il diffère du titre de la page
LIBELLES = {"franck-moyal": "Mon parcours"}


def libelle(slug):
    if slug in LIBELLES:
        return LIBELLES[slug]
    if slug in G.PUBLIC:
        return G.PUBLIC[slug][2]
    if slug in G.NOUVELLES:
        return G.NOUVELLES[slug]["nom"].split(" | ")[0]
    return G.TITRES.get(slug, (slug,))[0]


def carte(a, niveau="h2"):
    return f'''        <li class="carte-article" data-public="{a['public']}">
          <p class="carte-article__meta"><time datetime="{a['date']}">{date_fr(a['date'])}</time> · {t(PUBLICS[a['public']])} · {a['minutes']} min de lecture</p>
          <{niveau} class="carte-article__titre"><a href="{a['fichier']}.html">{t(a['titre'])}</a></{niveau}>
          <p class="carte-article__chapo">{t(a['chapo'])}</p>
          <span class="carte-article__lire" aria-hidden="true">{'Lire le cas' if a['genre'] == 'Cas clinique' else 'Lire l’article'} →</span>
        </li>'''


def tete(titre, desc, canonique, extra=""):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t(titre)}</title>
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{canonique}">
{extra}{POLICES}
<link rel="stylesheet" href="style.css?v={G.VERSION}">
@@JSONLD@@
</head>
<body>

{G.menu("")}

'''


def jsonld(noeuds):
    socle = G._socle()
    graphe = socle[:1] + noeuds + socle[1:]
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": graphe}, ensure_ascii=False)
            + "</script>")


def fil(url, etapes):
    elements = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": G.RACINE_WEB}]
    for i, (nom, lien) in enumerate(etapes, start=2):
        elements.append({"@type": "ListItem", "position": i, "name": nom, "item": lien})
    return {"@type": "BreadcrumbList", "@id": url + "#fil", "itemListElement": elements}


def corps(blocs):
    sortie = []
    for genre, contenu in blocs:
        if genre == "h2":
            sortie.append(f"        <h2>{t(contenu)}</h2>")
        elif genre == "citation":
            sortie.append(f"        <blockquote><p>{t(contenu)}</p></blockquote>")
        elif genre == "liste":
            sortie.append("        <ul>" + "".join(f"<li>{t(x)}</li>" for x in contenu) + "</ul>")
        else:
            sortie.append(f"        <p>{t(contenu)}</p>")
    return "\n".join(sortie)


def page_article(a, recents):
    url = a["url"]
    partage = "https://www.linkedin.com/sharing/share-offsite/?url=" + quote(url, safe="")
    og = (f'<meta property="og:type" content="article">\n'
          f'<meta property="og:title" content="{H.escape(a["titre"])}">\n'
          f'<meta property="og:description" content="{H.escape(a["chapo"])}">\n'
          f'<meta property="og:url" content="{url}">\n'
          f'<meta property="og:locale" content="fr_FR">\n'
          f'<meta property="article:published_time" content="{a["date"]}">\n'
          '<!-- og:image : une image de partage de 1200 × 627 px par article, '
          'à fournir avant la mise en ligne (aperçu du lien sur LinkedIn) -->\n')
    voir = " · ".join(f'<a href="{s}.html">{t(libelle(s))}</a>' for s in a["voir"])
    linkedin = (f'''
          <div class="fiche">
            <h4>Aussi sur LinkedIn</h4>
            <p><a href="{H.escape(a['linkedin'])}" target="_blank" rel="noopener">Le même article, publié le {date_fr(a['date'])} <span class="ext">↗</span></a></p>
          </div>''' if a.get("linkedin") else "")
    if a["public"] == "patients":
        appel = '''  <section class="appel">
    <div class="contenu">
      <h2>Faire le point</h2>
      <p>Un bilan permet de comprendre l’état des dents et les options possibles,
        avant tout engagement.</p>
      <a class="bouton" href="contact.html">Prendre rendez-vous</a>
    </div>
  </section>
'''
    else:
        appel = ""
    autres = "\n".join(carte(x, "h3") for x in recents[:3])
    page = tete(f"{a['titre']} | Dr Franck Moyal", a["chapo"], url, og)
    page += f'''<main>

  <div class="contenu">
    <p class="ariane"><a href="index.html">Accueil</a> › <a href="articles.html">Articles</a> › {t(a.get('court', a['titre']))}</p>
  </div>

  <div class="contenu billet">
    <article class="billet__texte">
      <header class="billet__tete">
        <p class="eyebrow">{t(a['genre'])} · {t(PUBLICS[a['public']])}</p>
        <h1>{t(a['titre'])}</h1>
        <p class="billet__meta"><time datetime="{a['date']}">{date_fr(a['date'])}</time> · {a['minutes']} min de lecture</p>
        <p class="billet__chapo">{t(a['chapo'])}</p>
        <div class="signature">
          <img src="{G.PORTRAIT}" alt="Dr Franck Moyal">
          <div><b>Dr Franck Moyal</b> — chirurgien-dentiste, Paris 9<sup>e</sup><br>
            Praticien hospitalier, Pitié-Salpêtrière · CMME, Sainte-Anne</div>
        </div>
      </header>
      <div class="billet__corps">
{corps(a['blocs'])}
      </div>
    </article>
    <aside class="billet__cote">
      <div class="fiche">
        <h4>Partager</h4>
        <p class="billet__partage"><a href="{partage}" target="_blank" rel="noopener">Sur LinkedIn <span class="ext">↗</span></a> · <button type="button" class="billet__copier" data-lien="{url}">Copier le lien</button></p>
      </div>{linkedin}
      <div class="fiche">
        <h4>Sur le même sujet</h4>
        <p class="billet__voir">{voir}</p>
      </div>
    </aside>
  </div>

  <section class="sect">
    <div class="contenu">
      <h2 class="tete-bande">Articles récents</h2>
      <ol class="liste-articles liste-articles--courte">
{autres}
      </ol>
      <p class="billet__tous"><a href="articles.html">Tous les articles</a></p>
    </div>
  </section>
{appel}
</main>

{G.PIED}

<script src="menu.js"></script>
<script>
document.querySelectorAll('.billet__copier').forEach(function (b) {{
  b.addEventListener('click', function () {{
    if (!navigator.clipboard) return;
    navigator.clipboard.writeText(b.dataset.lien).then(function () {{
      b.textContent = 'Lien copié';
      setTimeout(function () {{ b.textContent = 'Copier le lien'; }}, 2000);
    }});
  }});
}});
</script>
</body>
</html>
'''
    noeuds = [
        {"@type": "WebPage", "@id": url + "#page", "url": url, "name": a["titre"],
         "inLanguage": "fr-FR", "isPartOf": {"@id": G.RACINE_WEB + "#website"},
         "breadcrumb": {"@id": url + "#fil"}},
        {"@type": "BlogPosting", "@id": url + "#article", "headline": a["titre"],
         "description": a["chapo"], "datePublished": a["date"], "dateModified": a["date"],
         "inLanguage": "fr-FR", "wordCount": a["mots"], "url": url,
         "mainEntityOfPage": {"@id": url + "#page"},
         "isPartOf": {"@id": G.RACINE_WEB + "articles/#blog"},
         "author": {"@id": G.RACINE_WEB + "#franck-moyal"},
         "publisher": {"@id": G.RACINE_WEB + "#franck-moyal"},
         "audience": {"@type": "Audience", "audienceType":
                      "Patients" if a["public"] == "patients" else "Chirurgiens-dentistes"}},
        fil(url, [("Articles", G.RACINE_WEB + "articles/"), (a.get("court", a["titre"]), url)]),
    ]
    return page.replace("@@JSONLD@@", jsonld(noeuds))


def page_liste(entrees, articles):
    url = G.RACINE_WEB + "articles/"
    desc = ("Les articles du Dr Franck Moyal, chirurgien-dentiste à Paris 9e : "
            "pour les patients et pour les confrères.")
    cartes = "\n".join(carte(x) for x in entrees)
    page = tete("Articles | Dr Franck Moyal", desc, url)
    page += f'''<main>

  <p class="ariane ariane--seule"><a href="index.html">Accueil</a> › Articles</p>

  <section class="sect">
    <div class="contenu">
      <h1 class="tete-bande tete-bande--haut">Articles</h1>
      <div class="filtres" role="group" aria-label="Afficher les articles">
        <button type="button" aria-pressed="true" data-public="">Tous</button>
        <button type="button" aria-pressed="false" data-public="patients">Pour les patients</button>
        <button type="button" aria-pressed="false" data-public="confreres">Pour les confrères</button>
      </div>
      <ol class="liste-articles">
{cartes}
      </ol>
    </div>
  </section>

</main>

{G.PIED}

<script src="menu.js"></script>
<script>
(function () {{
  var boutons = document.querySelectorAll('.filtres button');
  boutons.forEach(function (b) {{
    b.addEventListener('click', function () {{
      boutons.forEach(function (x) {{ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }});
      document.querySelectorAll('.liste-articles > li').forEach(function (li) {{
        li.hidden = !!b.dataset.public && li.dataset.public !== b.dataset.public;
      }});
    }});
  }});
}})();
</script>
</body>
</html>
'''
    noeuds = [
        {"@type": "CollectionPage", "@id": url + "#page", "url": url,
         "name": "Articles | Dr Franck Moyal", "description": desc, "inLanguage": "fr-FR",
         "isPartOf": {"@id": G.RACINE_WEB + "#website"}, "breadcrumb": {"@id": url + "#fil"},
         "mainEntity": {"@id": url + "#blog"}},
        {"@type": "Blog", "@id": url + "#blog", "url": url,
         "name": "Articles du Dr Franck Moyal", "inLanguage": "fr-FR",
         "author": {"@id": G.RACINE_WEB + "#franck-moyal"},
         "blogPost": [{"@id": a["url"] + "#article"} for a in articles]},
        fil(url, [("Articles", url)]),
    ]
    return page.replace("@@JSONLD@@", jsonld(noeuds))


def main():
    articles = [lire(os.path.join(SOURCES, n)) for n in sorted(os.listdir(SOURCES))
                if n.endswith(".txt")]
    entrees = sorted(articles + [page_existante(x) for x in DEJA_SUR_LE_SITE],
                     key=lambda x: x["date"], reverse=True)
    # les anciennes pages d'article disparaissent avec leur source
    for n in os.listdir(G.SORTIE):
        if n.startswith("article-") and n.endswith(".html") and \
                n[len("article-"):-5] not in {a["slug"] for a in articles}:
            os.remove(os.path.join(G.SORTIE, n))
    for a in articles:
        recents = [x for x in entrees if x["fichier"] != a["fichier"]]
        open(os.path.join(G.SORTIE, a["fichier"] + ".html"), "w", encoding="utf-8").write(
            page_article(a, recents))
    open(os.path.join(G.SORTIE, "articles.html"), "w", encoding="utf-8").write(
        page_liste(entrees, articles))
    print(f"articles : {len(articles)} page(s) d'article, {len(entrees)} entrée(s) dans la liste")
    for x in entrees:
        print(f"  {x['date']}  {x['minutes']:2d} min  {x['fichier']}")


if __name__ == "__main__":
    main()
