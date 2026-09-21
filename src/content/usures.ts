// Page Usures dentaires — textes repris à l'identique de docs/golden-master/v1.3.1/04_USURES_DENTAIRES.md,
// complétés par la réponse de ChatGPT du 21/09/2026
// (docs/echanges/2026-09-21-chatgpt-reponses-points-17-20.md) : étiquette et titre de la
// section 5 (D11), textes des quatre mécanismes (D12), lien Bruxisme (D13).
// Les renvois [1], [1–3]… deviennent des exposants reliés aux sources (verrou V22).
// Contrôle du tour 1 (D19 à D21) : notes « Soutient » gardées ici pour la traçabilité mais non
// affichées, bloc auteur court et daté, titre des pages liées.

export const usures = {
  seo: {
    title: "Usures dentaires à Paris | Diagnostic et réhabilitation | Dr Franck Moyal",
    description:
      "Usures dentaires, bruxisme, érosion, dents courtes : diagnostic, prévention et réhabilitation adhésive à Paris avec le Dr Franck Moyal.",
  },
  hero: {
    h1: "Usures dentaires : comprendre avant de reconstruire",
    lead: "Des dents qui raccourcissent, s’aplatissent ou se fragilisent ne doivent pas simplement être “réparées”. Avant de reconstruire, il faut comprendre pourquoi elles s’usent.",
  },
  answer:
    "Une usure dentaire correspond à une perte progressive de tissu dentaire qui n’est pas liée à la carie. Elle peut être mécanique, érosive ou multifactorielle. Toutes les usures ne nécessitent pas une reconstruction. La prise en charge commence par identifier les causes, déterminer si l’usure progresse, prévenir son aggravation et évaluer son impact esthétique et fonctionnel. [1–3]",

  recognize: {
    id: "reconnaitre",
    label: "Comment reconnaître une usure ?",
    title: "Quand les dents commencent à changer",
    listLabel: "Signes possibles",
    list: [
      "dents qui paraissent plus courtes ;",
      "bords incisifs plus plats ;",
      "perte de relief ;",
      "fissures ou éclats ;",
      "sensibilité ;",
      "dentine plus visible ;",
      "sourire qui change progressivement.",
    ],
    text: "L’évolution est souvent lente. Beaucoup de patients s’habituent à ces changements et ne les remarquent qu’en comparant d’anciennes photographies ou lorsque les conséquences esthétiques deviennent plus visibles.",
    media: "Photographie clinique — à fournir",
  },
  causes: {
    id: "causes",
    label: "Pourquoi les dents s’usent-elles ?",
    title: "Le bruxisme n’explique pas tout",
    text: "Certaines usures sont principalement mécaniques, d’autres sont dominées par l’érosion acide. Plusieurs phénomènes peuvent se combiner, ce qui justifie une analyse étiologique plutôt qu’une attribution automatique au bruxisme. [2–4]",
    mechanisms: [
      {
        title: "Attrition et contraintes mécaniques",
        text: "L’attrition correspond à une usure liée aux contacts entre les dents. Elle peut être favorisée par certaines contraintes fonctionnelles ou parafonctionnelles, notamment le bruxisme, mais la présence d’une usure ne permet pas à elle seule de conclure à un bruxisme.",
      },
      {
        title: "Érosion dentaire",
        text: "L’érosion correspond à une perte de substance favorisée par des acides d’origine alimentaire ou intrinsèque, par exemple en cas de reflux ou de vomissements. Une surface fragilisée chimiquement devient également plus sensible aux contraintes mécaniques.",
      },
      {
        title: "Abrasion",
        text: "L’abrasion correspond à une usure provoquée par l’action répétée d’un élément extérieur à la dent : certaines habitudes, un brossage traumatique ou d’autres contraintes mécaniques peuvent y participer.",
      },
      {
        title: "Usures multifactorielles",
        text: "En pratique, les mécanismes sont souvent associés. Une même dent peut subir à la fois une agression acide et des contraintes mécaniques. Le diagnostic consiste donc surtout à identifier les facteurs dominants et modifiables, plutôt qu’à chercher une cause unique.",
      },
    ],
    keyMessage:
      "Le diagnostic ne consiste pas à trouver une étiquette unique, mais à identifier les facteurs réellement actifs et modifiables.",
    link: { label: "Comprendre le bruxisme et son rôle dans l’usure dentaire", href: "/bruxisme-usure-dentaire/" },
    media: "Schéma — mécanismes d’usure — à fournir",
  },
  prevention: {
    id: "prevention",
    label: "Dépistage et prévention",
    title: "Agir avant que la perte de substance ne devienne importante",
    text: "La prévention des usures commence par leur détection précoce. L’examen clinique, la photographie et l’analyse des facteurs de risque permettent de documenter la situation ; les scans intra-oraux peuvent également contribuer au suivi longitudinal, tout en gardant à l’esprit leurs limites pour les pertes très faibles. [2,5,6]",
    listLabel: "Axes",
    list: [
      "alimentation et expositions acides ;",
      "reflux / vomissements ;",
      "environnement salivaire ;",
      "médicaments ;",
      "hygiène ;",
      "facteurs mécaniques ;",
      "surveillance.",
    ],
    link: { label: "Comprendre l’érosion dentaire", href: "/erosion-dentaire/" },
  },
  diagnosis: {
    id: "diagnostic",
    label: "Diagnostic",
    title: "Une enquête clinique avant toute restauration",
    text: "L’objectif est de répondre à cinq questions : s’agit-il réellement d’une usure pathologique ? Quelle en est la cause ? Est-elle encore active ? Peut-on agir sur les facteurs de progression ? Et enfin, y a-t-il un bénéfice réel à reconstruire ?",
    listLabel: "Outils",
    list: [
      "entretien clinique ;",
      "photographie ;",
      "scan 3D ;",
      "analyse des surfaces ;",
      "analyse fonctionnelle / occlusale ;",
      "BEWE lorsque pertinent ;",
      "suivi dans le temps.",
    ],
    link: { label: "Diagnostic des usures dentaires", href: "/diagnostic-usures-dentaires/" },
  },
  treat: {
    id: "faut-il-traiter",
    label: "Faut-il toujours traiter une usure dentaire ?",
    title: "Non : toutes les usures ne nécessitent pas une reconstruction",
    text: "Une usure dentaire ne doit pas être restaurée systématiquement. Dans certaines situations, prévention, conseil et surveillance suffisent. La décision restauratrice est multifactorielle et dépend notamment de la sévérité, de l’évolution, des conséquences fonctionnelles ou esthétiques, des symptômes et des attentes du patient. [1]",
  },
  rehab: {
    id: "rehabilitation",
    label: "Réhabilitation",
    title: "Restaurer l’esthétique et la fonction ensemble",
    paragraphs: [
      "Lorsqu’une réhabilitation est indiquée, l’objectif n’est pas simplement de remplacer ce qui a été perdu. Il faut reconstruire les volumes, retrouver des rapports fonctionnels cohérents et redonner au sourire ses proportions, tout en préservant au maximum les tissus dentaires restants.",
      "Les techniques adhésives contemporaines permettent souvent de travailler de manière additive, avec du composite ou des restaurations partielles indirectes selon les situations, plutôt que de recourir systématiquement à des préparations périphériques. Les données récentes soutiennent de bonnes performances cliniques des réhabilitations minimalement invasives chez des patients présentant des usures modérées à sévères. [1,7]",
    ],
    link: { label: "Réhabilitation des dents usées", href: "/rehabilitation-dents-usees/" },
    media: "Cas clinique avant / après — à fournir (consentement documenté)",
  },
  smile: {
    id: "esthetique-du-sourire",
    label: "Esthétique du sourire",
    title: "Quand l’usure change le sourire",
    text: "Des incisives qui raccourcissent, des bords qui s’aplatissent ou une perte progressive de volume peuvent modifier profondément la perception du sourire. Dans ces situations, la réhabilitation fonctionnelle et la reconstruction esthétique ne sont pas deux traitements séparés : elles font partie du même projet.",
    link: { label: "Dents courtes ou usées", href: "/dents-courtes-usees/" },
  },
  erosion: {
    id: "erosion-tca",
    label: "Érosion & TCA",
    title: "Une attention particulière aux érosions",
    text: "L’érosion dentaire peut être liée à l’alimentation, au reflux, aux vomissements, à la salive ou à plusieurs facteurs combinés. Les TCA constituent un domaine d’implication spécifique, avec une importance particulière donnée au dépistage précoce et à la prévention.",
    links: [
      { label: "Érosion dentaire", href: "/erosion-dentaire/" },
      { label: "TCA et santé bucco-dentaire", href: "/tca-dents/" },
    ],
  },
  faq: {
    title: "FAQ",
    items: [
      {
        q: "Toutes les usures viennent-elles du bruxisme ?",
        a: "Non. Le bruxisme peut contribuer à certaines usures, mais l’érosion et d’autres facteurs peuvent intervenir seuls ou en association.",
      },
      {
        q: "Comment savoir si mes dents continuent de s’user ?",
        a: "L’examen clinique, les photographies et, dans certains cas, la comparaison de scans numériques permettent de suivre l’évolution.",
      },
      {
        q: "Peut-on reconstruire des dents usées sans couronnes ?",
        a: "Dans de nombreux cas, oui. Les techniques adhésives permettent souvent des reconstructions plus conservatrices.",
      },
      {
        q: "Faut-il toujours augmenter la dimension verticale ?",
        a: "Non. Une modification de la DVO n’est envisagée que si elle répond à un besoin clinique et au plan de traitement.",
      },
      {
        q: "Peut-on simplement surveiller ?",
        a: "Oui, lorsque l’usure est stable, peu sévère et sans retentissement significatif.",
      },
    ],
  },
  // Bloc auteur court + date de mise à jour (D20)
  author: {
    label: "Auteur",
    name: "Dr Franck Moyal — Chirurgien-dentiste à Paris",
    tagline: "Dentisterie esthétique et adhésive, usures dentaires et érosion.",
    updated: "Mis à jour le 21 septembre 2026",
    updatedIso: "2026-09-21",
  },
  related: {
    title: "Approfondir les usures dentaires", // D21
  },
  final: {
    title: "Faire le point sur une usure dentaire",
    text: "Une consultation permet d’identifier le type d’usure, ses causes possibles, son évolution et les différentes options de prévention ou de réhabilitation.",
    cta: "Prendre rendez-vous",
  },
  sources: {
    title: "Sources scientifiques",
    intro: "Les références ci-dessous soutiennent les principaux messages cliniques de cette page.",
    toggle: "Voir les 7 sources scientifiques", // repli sur mobile (D19)
    verifiedLabel: "Date de vérification bibliographique",
    verifiedDate: "21 septembre 2026",
    verifiedIso: "2026-09-21",
    items: [
      {
        n: 1,
        authors: "Loomans B, Opdam N, Attin T, et al.",
        title: "Severe Tooth Wear: European Consensus Statement on Management Guidelines.",
        journal: "J Adhes Dent.",
        details: "2017;19(2):111–119.",
        year: "2017",
        doi: "10.3290/j.jad.a38102",
        pubmed: "https://pubmed.ncbi.nlm.nih.gov/28439579/",
        supports:
          "distinction usure physiologique/pathologique ; diagnostic étiologique ; prévention, conseil et monitoring ; décision restauratrice multifactorielle ; principe de traitement conservateur.",
      },
      {
        n: 2,
        authors: "Carvalho TS, Colon P, Ganss C, et al.",
        title: "Consensus report of the European Federation of Conservative Dentistry: erosive tooth wear—diagnosis and management.",
        journal: "Clin Oral Investig.",
        details: "2015;19(7):1557–1561.",
        year: "2015",
        doi: "10.1007/s00784-015-1511-7",
        pubmed: "https://pubmed.ncbi.nlm.nih.gov/26121968/",
        supports:
          "caractère chimico-mécanique de l’usure érosive ; facteurs étiologiques multiples ; BEWE ; prévention ; restauration associée à une stratégie préventive.",
      },
      {
        n: 3,
        authors: "Schlueter N, Amaechi BT, Bartlett D, et al.",
        title: "Terminology of Erosive Tooth Wear: Consensus Report of a Workshop Organized by the ORCA and the Cariology Research Group of the IADR.",
        journal: "Caries Res.",
        details: "2020;54(1):2–6.",
        year: "2020",
        doi: "10.1159/000503308",
        pubmed: "https://pubmed.ncbi.nlm.nih.gov/31610535/",
        supports:
          "terminologie actuelle de l’usure érosive ; distinction entre processus, condition clinique, facteurs de risque, prévention et prise en charge.",
      },
      {
        n: 4,
        authors: "Bronkhorst H, Kalaykova S, Huysmans MC, Loomans B, Pereira-Cenci T.",
        title: "Tooth wear and bruxism: A scoping review.",
        journal: "J Dent.",
        details: "2024;145:104983.",
        year: "2024",
        doi: "10.1016/j.jdent.2024.104983",
        pubmed: "https://pubmed.ncbi.nlm.nih.gov/38574847/",
        supports:
          "ne pas inférer une activité de bruxisme sur la seule présence d’usure ; association bruxisme/usure souvent faible ou incertaine selon les méthodes d’évaluation.",
      },
      {
        n: 5,
        authors: "Carvalho JC, Scaramucci T, Aimée NR, Mestrinho HDM, Hara AT.",
        title: "Early diagnosis and daily practice management of erosive tooth wear lesions.",
        journal: "Br Dent J.",
        details: "2018;224(5):311–318.",
        year: "2018",
        doi: "10.1038/sj.bdj.2018.172",
        pubmed: "https://pubmed.ncbi.nlm.nih.gov/29495025/",
        supports:
          "dépistage précoce ; évaluation individuelle du risque ; prise en charge non opératoire visant à ralentir ou arrêter la progression.",
      },
      {
        n: 6,
        authors: "Schlenz MA, Schlenz MB, Wöstmann B, Glatt AS, Ganss C.",
        title: "Intraoral scanner-based monitoring of tooth wear in young adults: 36-month results.",
        journal: "Clin Oral Investig.",
        details: "2024;28(6):350.",
        year: "2024",
        doi: "10.1007/s00784-024-05740-0",
        pubmed: "https://pubmed.ncbi.nlm.nih.gov/38822893/",
        supports:
          "potentiel des scans intra-oraux pour le suivi longitudinal et individualisé de la progression de l’usure.",
      },
      {
        n: 7,
        authors: "Fan J, Wang B, Wang L, et al.",
        title: "Clinical performance of minimally invasive full-mouth rehabilitation using different materials and techniques for patients with moderate to severe tooth wear: a systematic review and meta-analysis.",
        journal: "Clin Oral Investig.",
        details: "2025;29(2):96.",
        year: "2025",
        doi: "10.1007/s00784-025-06181-z",
        pubmed: "https://pubmed.ncbi.nlm.nih.gov/39875663/",
        supports:
          "performances cliniques favorables des stratégies de réhabilitation minimalement invasives pour les usures modérées à sévères, avec résultats dépendant des matériaux et techniques.",
      },
    ],
  },
};
