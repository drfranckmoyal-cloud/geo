// Menu : les volets s'ouvrent au survol sur grand écran, au clic partout.
(function () {
  var nav = document.getElementById('nav');
  var burger = document.getElementById('burger');
  var boutons = Array.prototype.slice.call(document.querySelectorAll('[data-volet]'));

  function fermerTout(sauf) {
    boutons.forEach(function (b) {
      if (b === sauf) return;
      b.setAttribute('aria-expanded', 'false');
      document.getElementById(b.dataset.volet).removeAttribute('data-ouvert');
    });
  }

  boutons.forEach(function (b) {
    var volet = document.getElementById(b.dataset.volet);
    var parent = b.parentElement;

    b.addEventListener('click', function (e) {
      e.stopPropagation();
      var ouvert = b.getAttribute('aria-expanded') === 'true';
      fermerTout(b);
      b.setAttribute('aria-expanded', ouvert ? 'false' : 'true');
      if (ouvert) volet.removeAttribute('data-ouvert');
      else volet.setAttribute('data-ouvert', '');
    });

    if (window.matchMedia('(hover:hover)').matches) {
      parent.addEventListener('mouseenter', function () {
        fermerTout(b);
        b.setAttribute('aria-expanded', 'true');
        volet.setAttribute('data-ouvert', '');
      });
      parent.addEventListener('mouseleave', function () {
        b.setAttribute('aria-expanded', 'false');
        volet.removeAttribute('data-ouvert');
      });
    }
  });

  document.addEventListener('click', function () { fermerTout(null); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fermerTout(null); });

  if (burger) {
    burger.addEventListener('click', function (e) {
      e.stopPropagation();
      var deplie = nav.hasAttribute('data-deplie');
      if (deplie) nav.removeAttribute('data-deplie'); else nav.setAttribute('data-deplie', '');
      burger.setAttribute('aria-expanded', deplie ? 'false' : 'true');
    });
  }
})();
