// Mise en forme du texte, sans jamais en changer les mots.

// Typographie française : espace insécable devant « : » et à l'intérieur des guillemets,
// espace fine insécable devant « ; ? ! », insécable devant le tiret long. Évite qu'un signe
// se retrouve seul en début de ligne ; « à » ne reste jamais seul en fin de ligne ; le numéro
// d'arrondissement reste avec « Paris ».
// Caractères invisibles, construits par leur code pour rester lisibles dans le source.
const NBSP = String.fromCharCode(0x00a0); // espace insécable
const NNBSP = String.fromCharCode(0x202f); // espace fine insécable

export function fr(text: string): string {
  return text
    .replace(/ :/g, NBSP + ":")
    .replace(/ ([;?!])/g, NNBSP + "$1")
    .replace(/« /g, "«" + NBSP)
    .replace(/ »/g, NBSP + "»")
    .replace(/ — /g, NBSP + "— ")
    .replace(/ à /g, " à" + NBSP)
    .replace(/Paris (\d)/g, "Paris" + NBSP + "$1"); // « Paris 9 », « Paris 9e » : l'arrondissement ne part pas seul à la ligne
}

export function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

// Texte courant avec renvois bibliographiques : « … fonctionnel. [1–3] » devient un exposant
// discret relié à la source correspondante (verrou V22). Retourne du HTML sûr.
// Pour les fichiers du pack « pages suivantes », le texte garde aussi ses marques : **gras**,
// retours à la ligne, adresses web (liens externes), emplacements « [À FOURNIR] ».
export function rich(text: string): string {
  return escapeHtml(fr(text))
    .replace(/\*\*(\[\d+(?:[–,]\d+)*\])\*\*/g, "$1") // renvoi en gras dans le pack : exposant normal
    .replace(/\*\*([\s\S]+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\s\[(\d+(?:[–,]\d+)*)\]/g, (_, refs: string) => {
      const first = refs.split(/[–,]/)[0];
      const many = /[–,]/.test(refs);
      const spoken = refs.replace("–", " à ").replace(/,/g, ", ");
      return `${NBSP}<sup class="cite"><a href="#source-${first}"><span class="visually-hidden">Source${many ? "s" : ""} ${spoken} </span>[${refs}]</a></sup>`;
    })
    .replace(/\[([^\]]*À FOURNIR[^\]]*)\]/g, (_, s: string) => `<span class="placeholder-text">${s.toLowerCase().replace("url", "URL")}</span>`)
    .replace(/^((?:lien\s)?à\scompléter)$/gm, '<span class="placeholder-text">$1</span>')
    .replace(/https?:\/\/[^\s<]+/g, (url) => `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`)
    .replace(/\n/g, "<br>");
}

// Titres et textes sans renvois : typographie française seule, en HTML sûr.
export function plain(text: string): string {
  return escapeHtml(fr(text));
}
