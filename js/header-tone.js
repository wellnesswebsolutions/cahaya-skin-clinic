// Header tone: the hero photo's own colour while the hero is on screen,
// black once you scroll past it. Kept in its own file so nothing earlier
// in main.js can stop it running.
(function () {
  function init() {
    var nav = document.getElementById('ftco-navbar');
    if (!nav) return;
    function update() {
      var hero = document.querySelector('.hero-wrap');
      var limit = hero ? (hero.offsetTop + hero.offsetHeight - nav.offsetHeight) : 0;
      var y = window.pageYOffset || document.documentElement.scrollTop || 0;
      nav.classList.toggle('past-hero', y >= limit);
    }
    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    window.addEventListener('load', update);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
