/* Booking conversion kit for Skin, Slim & Laser Solutions.
   - Reveals the floating "Book" button and mobile action bar after the hero.
   - Tracks book_click / call_click into dataLayer (and GA4 if an ID is set).
   - Handles the contact form as a demo (no backend): validates, then shows a
     confirmation and a mailto fallback so nothing is silently lost. */
(function () {
  // --- floating button + mobile bar reveal ---
  var fab = document.getElementById('rrFab');
  var mbar = document.getElementById('rrMbar');
  function toggle() {
    var past = window.scrollY > window.innerHeight * 0.7;
    if (fab) fab.classList.toggle('show', past);
    if (mbar) mbar.classList.toggle('show', past);
  }
  toggle();
  window.addEventListener('scroll', toggle, { passive: true });

  // --- conversion tracking ---
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="fresha.com"], a[href^="tel:"], a[href*="contact.html"]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var type = href.indexOf('tel:') === 0 ? 'call_click' : 'book_click';
    var where = a.getAttribute('data-book') ||
      (a.closest('.ftco-navbar-light') ? 'nav' : (a.closest('.hero-wrap') ? 'hero' : 'link'));
    if (window.GA_MEASUREMENT_ID) gtag('event', type, { location: where });
    window.dataLayer.push({ event: type, location: where });
    console.log('[Skin, Slim & Laser] ' + type + ' → ' + where);
  }, true);

  // --- contact form (demo handler) ---
  var form = document.getElementById('enquiry');
  if (!form) return;
  var status = document.getElementById('cf-status');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity && form.reportValidity();
      return;
    }
    var data = {
      name: (form.name && form.name.value || '').trim(),
      email: (form.email && form.email.value || '').trim(),
      phone: (form.phone && form.phone.value || '').trim(),
      clinic: (form.clinic && form.clinic.value || '').trim(),
      service: (form.service && form.service.value || '').trim(),
      message: (form.message && form.message.value || '').trim()
    };
    window.dataLayer.push({ event: 'enquiry_submit', clinic: data.clinic, service: data.service });
    if (window.GA_MEASUREMENT_ID) gtag('event', 'generate_lead', { clinic: data.clinic, service: data.service });

    // Demo build: no backend wired up, so fall back to the client's mail app.
    var subject = 'Website enquiry: ' + (data.service || 'general') +
      (data.clinic ? ' (' + data.clinic + ')' : '');
    var body = 'Name: ' + data.name + '\n' +
      'Email: ' + data.email + '\n' +
      'Phone: ' + data.phone + '\n' +
      'Clinic: ' + data.clinic + '\n' +
      'Interested in: ' + data.service + '\n\n' + data.message;
    if (status) {
      status.style.display = 'block';
      status.style.color = '#8a7355';
      status.innerHTML = 'Thanks ' + (data.name || '') +
        ' &mdash; your email app will open so you can send this to us. ' +
        'If it does not, email <a href="mailto:info@thecahayaskinclinic.co.uk">info@thecahayaskinclinic.co.uk</a>.';
    }
    window.location.href = 'mailto:info@thecahayaskinclinic.co.uk?subject=' +
      encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    form.reset();
  });
})();
