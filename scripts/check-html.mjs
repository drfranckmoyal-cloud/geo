// Contrôle du HTML et des informations pour les moteurs (livrable 9 de 06_PROMPT_CLAUDE_CODE),
// sur toutes les pages construites : un seul H1, intertitres sans saut de niveau, titre,
// description, adresse de référence, langue, images décrites, données structurées conformes au
// pack, plan du site, robots.
// Pages du pack « pages suivantes » : les 10 contrôles de 21_MANIFESTE_INTEGRATION.md (fil
// d'Ariane, dateModified, auteur relié à Person#franck-moyal, sources dans le HTML, liens
// descriptifs, aucune image inventée, réglages de design inchangés depuis le gel…).
// Lancer après « npm run build » : node scripts/check-html.mjs
import { readFile, readdir } from "node:fs/promises";
import { execSync } from "node:child_process";
import { parse } from "node-html-parser";
import { parsePack } from "../src/lib/pack.ts";
import { applyDecisions, arborescence, builtNums, packPath, PACK_DIR } from "../src/content/pages-suivantes.ts";

const SITE = "https://drfranckmoyal.fr";
// Photographies autorisées : le portrait, et les cas cliniques déclarés dans le registre
const registre = await readFile("src/content/cas-cliniques.ts", "utf8");
const PHOTOS_CAS = [...registre.matchAll(/photos\/cas\/([a-z0-9-]+)\.jpg/g)].map((m) => m[1]);
const RDV = "/contact/#prendre-rendez-vous";
const PERSON = `${SITE}/#franck-moyal`;
const PRACTICE = `${SITE}/#practice`;
// Correctif V1.3 : les deux canaux de contact, les profils de Franck, ses organisations
const TEL = "tel:+33183755216";
const MAILTO = "mailto:drfranckmoyal@gmail.com?subject=Demande%20de%20rendez-vous%20-%20Dr%20Franck%20Moyal";
const SAME_AS = [
  "https://www.linkedin.com/in/franck-moyal-7581b6161/",
  "https://www.instagram.com/drfranckmoyal/",
  "https://www.aphp.fr/dr-moyal-franck",
  "https://blendi.fr/formateurs/franck-moyal",
  "https://www.tiktok.com/@drfranckmoyal",
  "https://www.lefildentaire.com/auteur/franck-moyal/",
];
const ORGS = {
  "/tca-dents/": { id: `${SITE}/#dentca`, url: "https://dentca-asso.com/", label: "Découvrir DentCA — prévention et santé bucco-dentaire dans les TCA" },
  "/conferences-formations/": { id: `${SITE}/#smileclub-formation`, url: "https://smileclubformations.com/", label: "Découvrir Smileclub Formation — formations pour chirurgiens-dentistes" },
  "/franck-moyal/": { id: `${SITE}/#smileclub-formation`, url: "https://smileclubformations.com/" },
};
const pages = [
  { file: "dist/index.html", url: `${SITE}/`, types: ["WebSite", "Person", "Dentist"] },
  { file: "dist/franck-moyal/index.html", url: `${SITE}/franck-moyal/`, types: ["ProfilePage", "Person", "Dentist"] },
  { file: "dist/usures-dentaires/index.html", url: `${SITE}/usures-dentaires/`, types: ["MedicalWebPage", "BreadcrumbList", "Person", "Dentist"] },
];

// Pages du pack : ce que le fichier impose
const v12 = await readdir(PACK_DIR);
const packFiles = arborescence.map((a) => packPath(a.num, v12)); // pages 01 à 20 (page 06 : correctif V1.3)
const all = await Promise.all(packFiles.map(async (path) => parsePack(applyDecisions(await readFile(path, "utf8"), path.split("/").pop().slice(0, 2)).md, path.split("/").pop())));
const parents = { "/usures-dentaires/": "/", "/franck-moyal/": "/" };
for (const p of all) parents[p.url] = p.parent;
for (const p of all.filter((p) => builtNums.includes(p.num))) {
  const chain = [p.url];
  while (parents[chain[0]] && parents[chain[0]] !== "/") chain.unshift(parents[chain[0]]);
  chain.unshift("/");
  pages.push({
    file: `dist${p.url}index.html`,
    url: SITE + p.url,
    types: [...p.seo.schema.filter((t) => /Page$/.test(t) || t === "Article"), "BreadcrumbList", "Person", "Dentist"],
    pack: p,
    chain: chain.map((u) => SITE + u),
  });
}

let problems = 0;
const bad = (m) => {
  problems++;
  console.log("  ✗ " + m);
};
const ok = (m) => console.log("  ✓ " + m);
const info = (m) => console.log("  • " + m);
const VAGUE = /^(en savoir plus|lire la suite|cliquez ici|ici|voir plus|plus d’infos?)$/i;

for (const p of pages) {
  const root = parse(await readFile(p.file, "utf8"));
  console.log(`\n■ ${p.url}`);
  const h1 = root.querySelectorAll("h1");
  h1.length === 1 ? ok(`un seul H1 : « ${h1[0].text.trim()} »`) : bad(`${h1.length} H1`);
  const levels = root.querySelectorAll("h1, h2, h3, h4, h5, h6").map((h) => Number(h.tagName[1]));
  const jumps = levels.filter((l, i) => i > 0 && l > levels[i - 1] + 1);
  jumps.length ? bad(`saut de niveau d'intertitre (${levels.join(" ")})`) : ok(`${levels.length} titres, aucun saut de niveau (H2 : ${levels.filter((l) => l === 2).length}, H3 : ${levels.filter((l) => l === 3).length})`);
  const lang = root.querySelector("html")?.getAttribute("lang");
  lang === "fr" ? ok("langue : fr") : bad(`langue : ${lang}`);
  const title = root.querySelector("title")?.text ?? "";
  title ? ok(`titre (${title.length} caractères)`) : bad("titre absent");
  const desc = root.querySelector('meta[name="description"]')?.getAttribute("content") ?? "";
  desc ? ok(`description (${desc.length} caractères)`) : bad("description absente");
  const canon = root.querySelector('link[rel="canonical"]')?.getAttribute("href");
  canon === p.url ? ok(`adresse de référence : ${canon}`) : bad(`adresse de référence : ${canon}`);
  const imgs = root.querySelectorAll("img");
  const noAlt = imgs.filter((i) => i.getAttribute("alt") === undefined);
  noAlt.length ? bad(`${noAlt.length} image(s) sans attribut alt`) : ok(`${imgs.length} image(s), toutes avec un attribut alt`);
  const main = root.querySelectorAll("main");
  main.length === 1 ? ok("une zone principale <main>") : bad(`${main.length} <main>`);
  let graph = [];
  try {
    graph = root.querySelectorAll('script[type="application/ld+json"]').flatMap((s) => JSON.parse(s.text)["@graph"] ?? []);
    const types = graph.flatMap((n) => [n["@type"]].flat());
    const missing = p.types.filter((t) => !types.includes(t));
    missing.length ? bad(`données structurées : manque ${missing.join(", ")}`) : ok(`données structurées : ${types.join(", ")}`);
    const person = graph.find((n) => n["@type"] === "Person");
    person?.["@id"] === PERSON ? ok("identifiant de Franck : …/#franck-moyal") : bad("identifiant de Franck absent");
    // Profils de Franck : la liste du correctif V1.3, ni plus ni moins
    JSON.stringify(person?.sameAs) === JSON.stringify(SAME_AS) ? ok(`profils de Franck (sameAs) : les ${SAME_AS.length} du correctif V1.3`) : bad(`profils de Franck (sameAs) : ${JSON.stringify(person?.sameAs)}`);
    // Le cabinet, entité distincte : adresse, téléphone, e-mail ; Franck y exerce
    const practice = graph.find((n) => n["@id"] === PRACTICE);
    practice?.["@type"] === "Dentist" && practice.telephone === TEL.slice(4) && practice.email === "mailto:drfranckmoyal@gmail.com" && practice.address?.streetAddress === "2 rue Hippolyte Lebas"
      ? ok("cabinet …/#practice (Dentist) : adresse, téléphone, e-mail")
      : bad(`cabinet …/#practice incomplet : ${JSON.stringify(practice)}`);
    if (person?.workLocation) person.workLocation["@id"] === PRACTICE ? ok("lieu d'exercice de Franck : …/#practice") : bad("lieu d'exercice de Franck : ailleurs que …/#practice");
    // Organisations fondées par Franck, distinctes de lui
    const org = ORGS[new URL(p.url).pathname];
    if (org) {
      const node = graph.find((n) => n["@id"] === org.id);
      node && node.url === org.url && node.founder?.["@id"] === PERSON ? ok(`organisation ${node.name} (${node["@type"]}), fondée par Franck`) : bad(`organisation ${org.id} absente ou incomplète`);
    }
    // Foire aux questions : les questions et réponses balisées sont celles qui s'affichent
    // (arbitrage de Franck du 24/09/2026 : `FAQPage` partout où une FAQ est visible)
    const questions = root.querySelectorAll(".faq__item h3").map((h) => h.structuredText.trim());
    const reponses = root.querySelectorAll(".faq__item p").map((x) => x.structuredText.trim());
    const faq = graph.find((n) => n["@type"] === "FAQPage");
    if (questions.length) {
      if (!faq) bad(`FAQ de ${questions.length} questions visible, mais aucune FAQPage dans les données structurées`);
      else {
        const balQ = faq.mainEntity.map((q) => q.name);
        const balR = faq.mainEntity.map((q) => q.acceptedAnswer?.text ?? "");
        const memes = JSON.stringify(balQ) === JSON.stringify(questions) && balR.every((t, i) => (reponses[i] ?? "").startsWith(t.slice(0, 60)));
        memes ? ok(`FAQPage : ${questions.length} questions, identiques à celles affichées`) : bad("FAQPage : questions ou réponses différentes de celles affichées");
      }
    } else if (faq) bad("FAQPage dans les données structurées, mais aucune FAQ visible");
  } catch (e) {
    bad("données structurées illisibles : " + e.message);
  }
  const future = root.querySelectorAll("[data-a-venir]").map((a) => a.getAttribute("href"));
  // Toutes les pages de l'arborescence construites : un lien « à venir » est désormais une erreur
  if (builtNums.length === arborescence.length) future.length ? bad(`liens vers des pages non construites : ${[...new Set(future)].join(" ")}`) : ok("aucun lien vers une page à venir");
  else info(`${new Set(future).size} adresses de pages à venir en lien : ${[...new Set(future)].sort().join(" ")}`);
  const ext = root.querySelectorAll('a[target="_blank"]');
  const unsafe = ext.filter((a) => !/noopener/.test(a.getAttribute("rel") ?? "") || !/noreferrer/.test(a.getAttribute("rel") ?? ""));
  if (ext.length) unsafe.length ? bad(`${unsafe.length} lien(s) externe(s) sans rel="noopener noreferrer"`) : ok(`${ext.length} liens externes, tous en rel="noopener noreferrer"`);

  // Ancres internes à la page : chaque « #… » mène à un élément existant
  const ids = new Set(root.querySelectorAll("[id]").map((e) => e.getAttribute("id")));
  const anchors = [...new Set(root.querySelectorAll('a[href^="#"]').map((a) => a.getAttribute("href")))].filter((h) => h !== "#");
  const broken = anchors.filter((h) => !ids.has(h.slice(1)));
  broken.length ? bad(`ancres sans cible : ${broken.join(" ")}`) : ok(`${anchors.length} ancres internes, toutes avec une cible`);
  // Prise de rendez-vous (règle globale V1.2, D41) : chaque bouton ou lien « Prendre rendez-vous »
  // mène à /contact/#prendre-rendez-vous ; l'ancre #rendez-vous n'existe plus
  const rdvLinks = root.querySelectorAll("a").filter((a) => /rendez-vous/i.test(a.text) && !/^Contact et rendez-vous/.test(a.text.trim()));
  const offTarget = rdvLinks.filter((a) => a.getAttribute("href") !== RDV);
  offTarget.length ? bad(`liens de rendez-vous ailleurs que ${RDV} : ${offTarget.map((a) => a.getAttribute("href")).join(" ")}`) : ok(`${rdvLinks.length} liens « rendez-vous », tous vers ${RDV}`);
  if (root.querySelector('[id="rendez-vous"], a[href="#rendez-vous"]')) bad("ancre #rendez-vous encore présente");
  // Boutons des appels finaux, quel que soit leur libellé (« Réaliser un bilan… ») : même destination
  const finals = root.querySelectorAll("#appel-final a.btn"); // le bouton, pas le téléphone cliquable du texte
  if (finals.length) finals.every((a) => a.getAttribute("href") === RDV) ? ok(`bouton de l'appel final vers ${RDV}`) : bad("bouton de l'appel final ailleurs que la prise de rendez-vous");

  // Correctif V1.3 : aucune réservation en ligne annoncée ; téléphone et e-mail cliquables dans le
  // pied de page ; aucun emplacement d'image vide sur le site public
  /rendez-vous en ligne/i.test(root.querySelector("body").text) ? bad("« prise de rendez-vous en ligne » encore affiché") : ok("aucune mention de rendez-vous en ligne");
  const foot = root.querySelector(".site-footer");
  foot.querySelector(`a[href="${TEL}"]`) && foot.querySelector(`a[href="${MAILTO}"]`) ? ok("pied de page : téléphone et e-mail cliquables") : bad("pied de page : téléphone ou e-mail absent, ou non cliquable");
  // Audit éditorial du 24/09/2026 : l'anglais « erosive tooth wear » ne revient pas dans le texte
  // patient ; les titres des publications, dans la liste des sources, le gardent
  const zone = parse(root.querySelector("main").toString());
  zone.querySelectorAll(".sources").forEach((e) => e.remove());
  const anglais = (zone.text.match(/erosive tooth wear/gi) ?? []).length;
  anglais ? bad(`« erosive tooth wear » dans le texte patient : ${anglais} fois`) : ok("aucun « erosive tooth wear » dans le texte patient");
  const slots = root.querySelectorAll("[data-emplacement='visuel']").length;
  slots ? bad(`${slots} emplacement(s) d'image vide(s) visible(s)`) : ok("aucun emplacement d'image vide visible");
  const orgLink = ORGS[new URL(p.url).pathname]?.label;
  if (orgLink) {
    const a = root.querySelectorAll("main a").find((a) => a.text.replace(/\s+/g, " ").trim() === orgLink); // espaces insécables de la typographie
    a?.getAttribute("href") === ORGS[new URL(p.url).pathname].url ? ok(`lien visible « ${orgLink} »`) : bad(`lien « ${orgLink} » absent`);
  }

  if (!p.pack) continue;
  // --- Contrôles du manifeste (pages suivantes) ---
  const pk = p.pack;
  // 2. Fil d'Ariane visible et BreadcrumbList
  const crumbs = root.querySelectorAll("nav.breadcrumbs li").map((li) => li.text.trim());
  const bl = graph.find((n) => n["@type"] === "BreadcrumbList");
  const blNames = bl?.itemListElement.map((i) => i.name) ?? [];
  const blUrls = bl?.itemListElement.map((i) => i.item) ?? [];
  JSON.stringify(crumbs) === JSON.stringify(pk.crumbs) && JSON.stringify(blNames) === JSON.stringify(pk.crumbs) && JSON.stringify(blUrls) === JSON.stringify(p.chain)
    ? ok(`fil d'Ariane conforme : ${crumbs.join(" > ")}`)
    : bad(`fil d'Ariane : page « ${crumbs.join(" > ")} », données « ${blNames.join(" > ")} » (${blUrls.join(" ")}), pack « ${pk.crumbs.join(" > ")} »`);
  // 3. Title et meta du pack
  title === pk.seo.title && desc === pk.seo.description ? ok("title et meta description : ceux du pack") : bad("title ou meta description différents du pack");
  // 4 et 5. Page : dateModified, auteur relié à Person#franck-moyal
  const node = graph.find((n) => [n["@type"]].flat().some((t) => /Page$/.test(t)));
  node?.dateModified === pk.author.iso ? ok(`dateModified : ${node.dateModified}`) : bad(`dateModified : ${node?.dateModified}`);
  node?.author?.["@id"] === PERSON ? ok("auteur relié à …/#franck-moyal") : bad("auteur non relié à Person#franck-moyal");
  // 6. Sources dans le HTML
  if (pk.sources.length) {
    const items = root.querySelectorAll("li.source").length;
    items === pk.sources.length ? ok(`${items} sources scientifiques dans le HTML`) : bad(`${items} sources dans la page, ${pk.sources.length} dans le pack`);
  }
  // 7. Liens internes descriptifs
  const internal = root.querySelectorAll("main a[href^='/']").map((a) => a.text.trim());
  const vague = internal.filter((t) => VAGUE.test(t));
  vague.length ? bad(`liens peu descriptifs : ${vague.join(", ")}`) : ok(`${internal.length} liens internes, tous avec un libellé descriptif`);
  // 9. Aucune image inventée : le portrait du Dr Moyal et les photographies des cas cliniques
  // déclarées dans src/content/cas-cliniques.ts, et elles seules
  const images = root.querySelectorAll("main img").map((i) => i.getAttribute("src"));
  const foreign = images.filter((src) => !/portrait-franck/.test(src) && !PHOTOS_CAS.some((p) => src.includes(p)));
  const casPage = [...new Set(root.querySelectorAll("main [data-cas]").map((e) => e.getAttribute("data-cas")))];
  foreign.length
    ? bad(`images inattendues : ${foreign.join(" ")}`)
    : ok(`aucune image inventée${casPage.length ? ` (cas cliniques : ${casPage.join(", ")})` : ""}`);
  // Chaque photographie porte un texte de remplacement utile et une légende visible
  const sansAlt = root.querySelectorAll("main figure[data-cas] img").filter((i) => (i.getAttribute("alt") ?? "").length < 15);
  const sansLegende = root.querySelectorAll("main figure[data-cas]").filter((f) => !f.querySelector("figcaption"));
  if (casPage.length) {
    sansAlt.length ? bad(`${sansAlt.length} photographie(s) sans texte de remplacement utile`) : ok("photographies : textes de remplacement présents");
    sansLegende.length ? bad(`${sansLegende.length} cas sans légende`) : ok("photographies : légendes présentes");
  }
  // Consigne aux moteurs
  const robots = root.querySelector('meta[name="robots"]')?.getAttribute("content");
  (robots ?? "") === (pk.seo.robots ?? "") ? ok(`consigne aux moteurs : ${robots ?? "aucune (page indexable)"}`) : bad(`consigne aux moteurs : ${robots} au lieu de ${pk.seo.robots}`);
}

// Cible des liens de rendez-vous : une seule section #prendre-rendez-vous, sur la page Contact
console.log("\n■ Cible des liens de rendez-vous");
const contact = parse(await readFile("dist/contact/index.html", "utf8"));
contact.querySelectorAll('[id="prendre-rendez-vous"]').length === 1 ? ok("section #prendre-rendez-vous unique sur /contact/") : bad("section #prendre-rendez-vous absente ou en double sur /contact/");
// Correctif V1.3 : la section expose aussitôt les deux canaux — téléphone et e-mail cliquables,
// deux boutons d'égale importance
const rdvSection = contact.querySelector("#prendre-rendez-vous");
const buttons = rdvSection?.querySelectorAll("a.btn").map((a) => `${a.text.trim()} → ${a.getAttribute("href")}`) ?? [];
rdvSection?.querySelector("h2")?.text.trim() === "Prendre rendez-vous ou nous écrire" ? ok("titre : « Prendre rendez-vous ou nous écrire »") : bad(`titre de la section : ${rdvSection?.querySelector("h2")?.text}`);
rdvSection?.querySelector(`p a[href="${TEL}"]`) && rdvSection?.querySelector(`p a[href="${MAILTO}"]`) ? ok("téléphone et e-mail cliquables dans la section") : bad("téléphone ou e-mail non cliquable dans la section");
JSON.stringify(buttons) === JSON.stringify([`Appeler le cabinet → ${TEL}`, `Écrire au cabinet → ${MAILTO}`]) ? ok("deux boutons : « Appeler le cabinet », « Écrire au cabinet »") : bad(`boutons de la section : ${buttons.join(" ; ")}`);
// Page Paris 9 : le bloc final donne les deux canaux, cliquables, et garde son bouton
const paris9 = parse(await readFile("dist/chirurgien-dentiste-paris-9/index.html", "utf8")).querySelector("#appel-final");
paris9?.querySelector("h2")?.text.trim() === "Prendre rendez-vous ou contacter le cabinet" && paris9.querySelector(`a[href="${TEL}"]`) && paris9.querySelector(`a[href="${MAILTO}"]`) && paris9.querySelector(`a.btn[href="${RDV}"]`)
  ? ok("page Paris 9 : bloc final « Prendre rendez-vous ou contacter le cabinet », téléphone et e-mail cliquables, bouton vers la page Contact")
  : bad("page Paris 9 : bloc final non conforme à la fiche corrective");

// 8 et 10. « Dentiste esthétique » (contrôle des textes) ; réglages de design inchangés depuis le gel
console.log("\n■ Réglages de design (src/styles/tokens.css)");
try {
  execSync("git diff --quiet golden-master-gele -- src/styles/tokens.css");
  ok("identiques à la version gelée (étiquette golden-master-gele)");
} catch {
  bad("modifiés depuis le gel");
}

const sitemap = await readFile("dist/sitemap-0.xml", "utf8");
const locs = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const expected = pages.filter((p) => !p.pack?.seo.robots?.includes("noindex")).map((p) => p.url);
console.log(`\n■ Plan du site : ${locs.length} adresses`);
JSON.stringify([...locs].sort()) === JSON.stringify([...expected].sort())
  ? ok(`les ${expected.length} pages indexables construites, et elles seules`)
  : bad(`plan du site : ${locs.join(", ")} ; attendu : ${expected.join(", ")}`);
// Adresse conventionnelle du plan du site : /sitemap.xml, copie du plan produit par Astro
const conventional = await readFile("dist/sitemap.xml", "utf8").catch(() => "");
conventional === sitemap ? ok("/sitemap.xml : présent, identique au plan du site") : bad("/sitemap.xml absent ou différent du plan du site");
const robots = await readFile("dist/robots.txt", "utf8");
// Correctif V1.3 §5 : politique ouverte — moteurs, robots d'IA de recherche et d'entraînement
/Sitemap: https:\/\/drfranckmoyal\.fr\/sitemap-index\.xml/.test(robots) && /^User-agent: \*$/m.test(robots) && /^Allow: \/$/m.test(robots) && !/^Disallow:/im.test(robots)
  ? ok("robots.txt : tout est ouvert aux moteurs et aux robots d'IA, plan du site déclaré")
  : bad("robots.txt : politique ouverte ou plan du site absents");

// Faits cliniques verrouillés : l'âge du patient du cas d'usure, corrigé par Franck le 25/09/2026
// (son article écrivait 64 ans). Aucune page du site ne doit plus porter l'ancien âge.
console.log("\n■ Âge du patient du cas d'usure (POINT 3.5)");
{
  const casUsure = "dist/cas-cliniques/usures-dentaires-facettes-minimalement-invasives/index.html";
  const texte = parse(await readFile(casUsure, "utf8")).querySelector("main").structuredText;
  const ages = [...new Set((texte.match(/\b\d{2} ans\b/g) ?? []))];
  JSON.stringify(ages) === JSON.stringify(["72 ans"]) ? ok("la page du cas ne cite que « 72 ans »") : bad(`âges cités sur la page du cas : ${ages.join(", ") || "aucun"}`);
  const partout = [];
  for (const { file } of pages) {
    const html = await readFile(file, "utf8");
    if (/64\s?ans/.test(html)) partout.push(file.replace(/^dist|index\.html$/g, ""));
  }
  partout.length ? bad(`« 64 ans » subsiste : ${partout.join(" ")}`) : ok("« 64 ans » n'apparaît nulle part sur le site");
}

console.log(problems ? `\n${problems} problème(s).` : "\nContrôle HTML réussi.");
process.exit(problems ? 1 : 0);
