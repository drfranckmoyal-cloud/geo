// Emplacements réservés aux images attendues. Correctif V1.3 (§7) : « Un emplacement sans visuel
// validé disparaît en production. » Le site public n'en montre donc aucun, et chaque section se
// compose comme une section sans image. Pour une revue de composition (captures), fabriquer le
// site avec EMPLACEMENTS=1 les fait réapparaître, à leur place et à leurs proportions.
export const showPlaceholders = process.env.EMPLACEMENTS === "1";
