// Page d'accueil — textes repris à l'identique de docs/golden-master/v1.3.1/02_HOME.md.
// Exceptions décidées : le titre Google (D6, verrou V21 — « dentiste esthétique » proscrit) ;
// l'étape « Simuler » rétablie (D17), avec un texte provisoire repris de 00 §5 (§6, point 27).

export const home = {
  seo: {
    title: "Dr Franck Moyal | Dentisterie esthétique et usures dentaires à Paris",
    description:
      "Dr Franck Moyal, chirurgien-dentiste à Paris : dentisterie esthétique et adhésive, composite bonding, facettes, usures dentaires, érosion et réhabilitation conservatrice.",
  },
  hero: {
    eyebrow: "Dr Franck Moyal — Paris",
    h1: "Dentisterie esthétique, adhésive et usures dentaires à Paris",
    lead: "Préserver les tissus dentaires, comprendre avant de traiter et reconstruire lorsque c’est nécessaire.",
    ctaPrimary: "Prendre rendez-vous",
    ctaSecondary: { label: "Découvrir ma démarche", href: "#methode" }, // validé par ChatGPT (D25)
  },
  pillars: {
    title: "Deux axes de pratique, une même exigence",
    items: [
      {
        title: "Dentisterie esthétique et adhésive",
        text: "Améliorer un sourire ne commence pas par le choix d’une technique. Le projet part de la demande du patient, de l’analyse du sourire et d’une planification précise. Éclaircissement, composite bonding, facettes ou traitements des dyschromies sont ensuite choisis selon le résultat recherché et le niveau d’intervention réellement nécessaire.",
        cta: { label: "Découvrir la dentisterie esthétique", href: "/dentisterie-esthetique-paris/" },
        media: "Visuel — dentisterie esthétique et adhésive — à fournir",
      },
      {
        title: "Usures dentaires",
        text: "Une dent usée ne doit pas seulement être reconstruite : il faut comprendre pourquoi elle s’use, déterminer si le phénomène progresse et protéger ce qui peut encore l’être. Lorsque la réhabilitation est indiquée, l’objectif est de restaurer conjointement la fonction, les volumes et l’esthétique du sourire.",
        cta: { label: "Comprendre les usures dentaires", href: "/usures-dentaires/" },
        media: "Visuel — usures dentaires — à fournir",
      },
    ],
  },
  philosophy: {
    title: "Esthétique. Fonction. Préservation.",
    text: "Ces trois principes guident chaque décision clinique. Le résultat esthétique compte, mais il ne doit pas être obtenu au prix d’un sacrifice inutile de tissus dentaires. La fonction compte, mais elle doit s’intégrer à l’esthétique du sourire. Et la préservation ne signifie pas faire moins : elle signifie choisir le traitement le plus juste pour chaque situation.",
  },
  method: {
    title: "Écouter, analyser, planifier, décider ensemble",
    intro:
      "Une consultation esthétique ou une consultation d’usure n’aboutit pas automatiquement à un traitement. Elle sert d’abord à comprendre la demande, documenter la situation et poser un diagnostic.",
    steps: [
      { name: "Écouter", text: "attentes, gêne, objectifs." },
      { name: "Documenter", text: "photographies, scans 3D, examens nécessaires." },
      { name: "Analyser", text: "esthétique, fonction, tissus, causes." },
      { name: "Planifier", text: "simulation et projet lorsque pertinent." },
      { name: "Simuler", text: "simulation 2D / 3D / dynamique selon les cas." },
      { name: "Décider ensemble", text: "options, avantages, limites, niveau d’intervention." },
      { name: "Traiter", text: "uniquement si le bénéfice est réel." },
    ],
    link: { label: "Découvrir le bilan esthétique personnalisé", href: "/bilan-esthetique-personnalise/" },
  },
  tca: {
    title: "Érosion dentaire et troubles des conduites alimentaires",
    text: "Les érosions dentaires liées aux TCA constituent un domaine d’implication spécifique. Le dépistage précoce, la prévention et la compréhension des mécanismes d’érosion permettent parfois d’agir bien avant qu’une réhabilitation importante ne soit nécessaire.",
    cta: { label: "TCA et santé bucco-dentaire", href: "/tca-dents/" },
  },
  authority: {
    title: "Clinique, enseignement, hôpital",
    text: "La pratique clinique du Dr Franck Moyal est complétée par une activité d’enseignement, de formation, de publication et une activité hospitalière à Paris. Ces différents environnements nourrissent une même approche : documenter, comprendre et traiter de manière précise et conservatrice.",
    links: [
      { label: "Publications", href: "/publications/" },
      { label: "Conférences et formations", href: "/conferences-formations/" },
      { label: "Activité hospitalière", href: "/activite-hospitaliere/" },
      { label: "À propos du Dr Franck Moyal", href: "/franck-moyal/" },
    ],
  },
  final: {
    title: "Commencer par comprendre",
    text: "Une première consultation permet de faire le point sur votre demande, d’établir un diagnostic et de déterminer les options réellement adaptées à votre situation.",
    cta: "Prendre rendez-vous",
  },
};
