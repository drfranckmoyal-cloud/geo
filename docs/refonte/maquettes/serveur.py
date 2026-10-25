#!/usr/bin/env python3
"""
Sert la maquette en local, sans jamais laisser le navigateur garder une page en mémoire.

Le serveur de Python (« python3 -m http.server ») n'envoie aucune consigne de cache :
le navigateur se croit alors autorisé à resservir pendant des heures une page déjà vue,
sans redemander au serveur. Franck voyait ainsi l'ancienne page Usure dentaire alors
que la nouvelle était en place (25/10/2026). Ici, chaque page est redemandée à chaque fois.

    python3 docs/refonte/maquettes/serveur.py 4330 /chemin/vers/GEO
"""
import functools
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class SansCache(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4330
    racine = sys.argv[2] if len(sys.argv) > 2 else "."
    serveur = ThreadingHTTPServer(("", port), functools.partial(SansCache, directory=racine))
    print(f"Maquette servie sans cache sur http://localhost:{port}/ (dossier {racine})")
    serveur.serve_forever()
