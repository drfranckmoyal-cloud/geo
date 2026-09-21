// Mise en forme du texte, sans jamais en changer les mots.

// Typographie française : espace insécable devant « : » et à l'intérieur des guillemets,
// espace fine insécable devant « ; ? ! », insécable devant le tiret long. Évite qu'un signe
// se retrouve seul en début de ligne ; « à » ne reste jamais seul en fin de ligne.
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
    .replace(/ à /g, " à" + NBSP);
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
export function rich(text: string): string {
  return escapeHtml(fr(text)).replace(/\s\[(\d+(?:[–,]\d+)*)\]/g, (_, refs: string) => {
    const first = refs.split(/[–,]/)[0];
    const many = /[–,]/.test(refs);
    const spoken = refs.replace("–", " à ").replace(/,/g, ", ");
    return `${NBSP}<sup class="cite"><a href="#source-${first}"><span class="visually-hidden">Source${many ? "s" : ""} ${spoken} </span>[${refs}]</a></sup>`;
  });
}

// Titres et textes sans renvois : typographie française seule, en HTML sûr.
export function plain(text: string): string {
  return escapeHtml(fr(text));
}
