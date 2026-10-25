#!/usr/bin/env python3
"""
Fabrique la rubrique Vidéos de la maquette : la page qui présente toutes les vidéos
par thème (videos.html) et une page par vidéo (video-<slug>.html), où la vidéo se
lance sur place, depuis le site, avec un lien vers la page de soins qu'elle concerne.
La page de soins, elle, reçoit une vignette qui mène à la vidéo (composer.py).

Franck, 25/10/2026 : « une section vidéo avec un panel de toutes les vidéos
disponibles, bien identifiées en fonction du thème ; quand on clique dessus, ça va
sur une page qui lance cette vidéo, avec des liens vers la page concernée ».

La source d'une vidéo est un fichier texte dans videos/ : quelques lignes « clé: valeur »
(titre, court, theme, page, lien, chapitre, fichier, duree, date, description), une
ligne « --- », puis une question par ligne, « question | réponse courte ». Le fichier
vidéo et son image de couverture sont dans src/assets/videos/<fichier>.mp4 et .jpg.

    python3 docs/refonte/maquettes/videos.py
"""
import html as H
import json
import os

import generer as G

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(ICI, "videos")
MEDIA = G.VERS_DEPOT + "src/assets/videos/"
POLICES = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
           '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:'
           'wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;'
           '8..60,700&display=swap">')


def t(s):
    return H.escape(s, quote=False)


def lire(chemin):
    """Une source de vidéo : son en-tête, puis ses questions."""
    tete, _, corps = open(chemin, encoding="utf-8").read().partition("\n---\n")
    v = {"slug": os.path.basename(chemin)[:-4]}
    for ligne in tete.splitlines():
        cle, _, val = ligne.partition(":")
        if val:
            v[cle.strip()] = val.strip()
    v["questions"] = [tuple(x.strip() for x in l.split("|", 1))
                      for l in corps.splitlines() if "|" in l]
    v["duree"] = int(v["duree"])
    aussi, v["aussi"] = v.get("aussi", ""), []
    for x in aussi.split(","):
        if x.strip():
            page, _, k = x.strip().partition(":")
            v["aussi"].append((page.strip(), int(k) if k else 1))
    v["fichier_page"] = f"video-{v['slug']}"
    v["url"] = f"{G.RACINE_WEB}videos/{v['slug']}/"
    return v


def toutes():
    if not os.path.isdir(SOURCES):
        return []
    return sorted((lire(os.path.join(SOURCES, n)) for n in os.listdir(SOURCES) if n.endswith(".txt")),
                  key=lambda v: v["date"], reverse=True)


def cibles(v):
    """Les pages qui portent la vignette de la vidéo, chacune avec son chapitre."""
    principale = [(v["page"], int(v.get("chapitre", 1)))] if v.get("page") else []
    return principale + v["aussi"]


def vignette(v):
    return (f'        <a class="vignette-video" href="{v['fichier_page']}.html">\n'
            f'          <span class="vignette-video__image"><img src="{MEDIA}{v['fichier']}.jpg" alt="" '
            f'loading="lazy"><span class="vignette-video__lecture" aria-hidden="true"></span></span>\n'
            f'          <span class="vignette-video__dit"><span class="vignette-video__sur">En vidéo · '
            f'{duree(v['duree'])}</span><span class="vignette-video__titre">{t(v.get('court', v['titre']))}</span>'
            f'<span class="vignette-video__voir">Voir la vidéo →</span></span>\n'
            f'        </a>\n')


def poser_vignettes(vids):
    """Les pages composées reçoivent leurs vignettes de composer.py. Les pages écrites à la
    main (la page Usure dentaire, par exemple) les reçoivent ici, dans la colonne du chapitre
    voulu ; et une vignette dont la vidéo n'existe plus est retirée."""
    import re
    voulues = {v["fichier_page"]: {p for p, _ in cibles(v)} for v in vids}
    for v in vids:
        for page, k in cibles(v):
            chemin = os.path.join(G.SORTIE, page + ".html")
            if not os.path.exists(chemin):
                print(f"  ! page introuvable pour la vignette : {page}")
                continue
            h = open(chemin, encoding="utf-8").read()
            if f'href="{v["fichier_page"]}.html"' in h:
                continue
            m = re.search(rf'<p class="numero">{k} / \d+</p>.*?(<div class="cote">\n)', h, re.S)
            if not m:
                print(f"  ! pas de colonne au chapitre {k} de {page}")
                continue
            h = h[:m.end(1)] + vignette(v) + h[m.end(1):]
            open(chemin, "w", encoding="utf-8").write(h)
            print(f"  vignette posée : {page}, chapitre {k}")
    for nom in os.listdir(G.SORTIE):
        if not nom.endswith(".html"):
            continue
        chemin = os.path.join(G.SORTIE, nom)
        h = open(chemin, encoding="utf-8").read()
        page = nom[:-5]
        neuf = re.sub(r'        <a class="vignette-video" href="(video-[a-z0-9-]+)\.html">.*?</a>\n',
                      lambda m: m.group(0) if page in voulues.get(m.group(1), ()) else "", h, flags=re.S)
        if neuf != h:
            open(chemin, "w", encoding="utf-8").write(neuf)
            print(f"  vignette retirée : {nom}")


def duree(s):
    return f"{s} s" if s < 60 else f"{s // 60} min {s % 60:02d}"


def carte(v):
    return f'''        <li data-theme="{H.escape(v['theme'])}">
          <a class="carte-video" href="{v['fichier_page']}.html">
            <img src="{MEDIA}{v['fichier']}.jpg" alt="" loading="lazy">
            <span class="carte-video__theme">{t(v['theme'])}</span>
            <span class="carte-video__lecture" aria-hidden="true"></span>
            <span class="carte-video__pied">
              <span class="carte-video__titre">{t(v.get('court', v['titre']))}</span>
              <span class="carte-video__duree">{duree(v['duree'])}</span>
            </span>
          </a>
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
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": socle[:1] + noeuds + socle[1:]},
                         ensure_ascii=False)
            + "</script>")


def fil(url, etapes):
    elements = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": G.RACINE_WEB}]
    for i, (nom, lien) in enumerate(etapes, start=2):
        elements.append({"@type": "ListItem", "position": i, "name": nom, "item": lien})
    return {"@type": "BreadcrumbList", "@id": url + "#fil", "itemListElement": elements}


def noeud_video(v):
    return {"@type": "VideoObject", "@id": v["url"] + "#video", "name": v["titre"],
            "description": v["description"], "inLanguage": "fr-FR",
            # adresses du futur site, à confirmer à la fabrication du site Astro
            "thumbnailUrl": f"{G.RACINE_WEB}videos/{v['fichier']}.jpg",
            "contentUrl": f"{G.RACINE_WEB}videos/{v['fichier']}.mp4",
            "uploadDate": v["date"], "duration": f"PT{v['duree']}S",
            "author": {"@id": G.RACINE_WEB + "#franck-moyal"},
            "publisher": {"@id": G.RACINE_WEB + "#franck-moyal"}}


def page_video(v, autres):
    questions = "\n".join(f"          <li><b>{t(q)}</b><span>{t(r)}</span></li>" for q, r in v["questions"])
    libelle = G.PUBLIC.get(v["page"], ("", None, v["page"]))[2] if v.get("page") else ""
    suite = (f'''
  <section class="sect">
    <div class="contenu">
      <h2 class="tete-bande">Autres vidéos</h2>
      <ul class="videos-grille">
{chr(10).join(carte(x) for x in autres[:4])}
      </ul>
    </div>
  </section>''' if autres else "")
    bouton = (f'      <a class="film__lien" href="{v["page"]}.html">{t(v["lien"])} '
              f'<span aria-hidden="true">→</span></a>\n') if v.get("page") else ""
    suite_page = f' · <a href="{v["page"]}.html">{t(libelle)}</a>' if v.get("page") else ""
    og = (f'<meta property="og:type" content="video.other">\n'
          f'<meta property="og:title" content="{H.escape(v["titre"])}">\n'
          f'<meta property="og:description" content="{H.escape(v["description"])}">\n'
          f'<meta property="og:url" content="{v["url"]}">\n')
    page = tete(f"{v['titre']} | Dr Franck Moyal", v["description"], v["url"], og)
    page += f'''<main>

  <div class="contenu">
    <p class="ariane"><a href="index.html">Accueil</a> › <a href="videos.html">Vidéos</a> › {t(v.get('court', v['titre']))}</p>
  </div>

  <div class="contenu film">
    <div class="film__ecran">
      <video controls playsinline preload="none" poster="{MEDIA}{v['fichier']}.jpg">
        <source src="{MEDIA}{v['fichier']}.mp4" type="video/mp4">
        <a href="{MEDIA}{v['fichier']}.mp4">Voir la vidéo</a>
      </video>
    </div>
    <div class="film__texte">
      <p class="eyebrow">Vidéo · {t(v['theme'])} · {duree(v['duree'])}</p>
      <h1>{t(v['titre'])}</h1>
      <p class="film__resume">{t(v['description'])}</p>
      <div class="film__dans">
        <p class="film__titre-liste">Dans cette vidéo</p>
        <ul class="film__questions">
{questions}
        </ul>
      </div>
{bouton}      <div class="signature">
        <img src="{G.PORTRAIT}" alt="Dr Franck Moyal">
        <div><b>Dr Franck Moyal</b> — chirurgien-dentiste, Paris 9<sup>e</sup><br>
          Praticien hospitalier, Pitié-Salpêtrière · CMME, Sainte-Anne</div>
      </div>
      <p class="film__tout"><a href="videos.html">Toutes les vidéos</a>{suite_page}</p>
    </div>
  </div>
{suite}
</main>

{G.PIED}

<script src="menu.js"></script>
</body>
</html>
'''
    noeuds = [
        {"@type": "WebPage", "@id": v["url"] + "#page", "url": v["url"], "name": v["titre"],
         "inLanguage": "fr-FR", "isPartOf": {"@id": G.RACINE_WEB + "#website"},
         "breadcrumb": {"@id": v["url"] + "#fil"}, "mainEntity": {"@id": v["url"] + "#video"}},
        noeud_video(v),
        fil(v["url"], [("Vidéos", G.RACINE_WEB + "videos/"), (v.get("court", v["titre"]), v["url"])]),
    ]
    return page.replace("@@JSONLD@@", jsonld(noeuds))


def page_liste(vids):
    url = G.RACINE_WEB + "videos/"
    desc = ("Le Dr Franck Moyal, chirurgien-dentiste à Paris 9e, répond en vidéo aux questions des patients : "
            "composite, facettes, éclaircissement, usures.")
    themes = []
    for v in vids:
        if v["theme"] not in themes:
            themes.append(v["theme"])
    boutons = "\n".join(f'        <button type="button" aria-pressed="false" data-theme="{H.escape(x)}">{t(x)}</button>'
                        for x in themes)
    page = tete("Vidéos | Dr Franck Moyal", desc, url)
    page += f'''<main>

  <p class="ariane ariane--seule"><a href="index.html">Accueil</a> › Vidéos</p>

  <section class="sect">
    <div class="contenu">
      <h1 class="tete-bande tete-bande--haut">Vidéos</h1>
      <p class="videos__intro">Le Dr Franck Moyal répond en vidéo aux questions des patients.</p>
      <div class="filtres" role="group" aria-label="Afficher les vidéos">
        <button type="button" aria-pressed="true" data-theme="">Toutes</button>
{boutons}
      </div>
      <ul class="videos-grille">
{chr(10).join(carte(v) for v in vids)}
      </ul>
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
      document.querySelectorAll('.videos-grille > li').forEach(function (li) {{
        li.hidden = !!b.dataset.theme && li.dataset.theme !== b.dataset.theme;
      }});
    }});
  }});
}})();
</script>
</body>
</html>
'''
    noeuds = [
        {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": "Vidéos | Dr Franck Moyal",
         "description": desc, "inLanguage": "fr-FR", "isPartOf": {"@id": G.RACINE_WEB + "#website"},
         "breadcrumb": {"@id": url + "#fil"},
         "hasPart": [{"@id": v["url"] + "#video"} for v in vids]},
        fil(url, [("Vidéos", url)]),
    ]
    return page.replace("@@JSONLD@@", jsonld(noeuds))


def main():
    vids = toutes()
    # une page de vidéo disparaît avec sa source
    for n in os.listdir(G.SORTIE):
        if n.startswith("video-") and n.endswith(".html") and n[6:-5] not in {v["slug"] for v in vids}:
            os.remove(os.path.join(G.SORTIE, n))
    for v in vids:
        autres = [x for x in vids if x["slug"] != v["slug"]]
        autres.sort(key=lambda x: x["theme"] != v["theme"])  # le même thème d'abord
        open(os.path.join(G.SORTIE, v["fichier_page"] + ".html"), "w", encoding="utf-8").write(
            page_video(v, autres))
    open(os.path.join(G.SORTIE, "videos.html"), "w", encoding="utf-8").write(page_liste(vids))
    poser_vignettes(vids)
    print(f"vidéos : {len(vids)} page(s) de vidéo")
    for v in vids:
        print(f"  {v['date']}  {duree(v['duree']):>8}  {v['theme']:16s} {v['fichier_page']} → "
              f"{', '.join(f'{p} (ch. {k})' for p, k in cibles(v)) or 'aucune page'}")


if __name__ == "__main__":
    main()
