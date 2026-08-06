#!/usr/bin/env python3
"""Static site generator for Skin, Slim & Laser Solutions (formerly The Cahaya Skin Clinic).

Every page shares one head/nav/footer so SEO markup and navigation stay in sync.
Run `python3 _build.py` from this directory to regenerate all HTML.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Business facts. All taken from the clinic's own site — nothing invented.
# --------------------------------------------------------------------------
BRAND = "Skin, Slim &amp; Laser Solutions"
BRAND_PLAIN = "Skin, Slim & Laser Solutions"
FORMERLY = "formerly The Cahaya Skin Clinic"
PHONE = "07479 686312"
TEL = "+447479686312"
EMAIL = "info@thecahayaskinclinic.co.uk"
BOOKING = ("https://www.fresha.com/book-now/skin-slim-laser-solutions-prs0gwgv/"
           "all-offer?share=true&amp;pId=3011819")
INSTAGRAM = "https://www.instagram.com/skin_slim_and_laser_solutions/"
IG_HANDLE = "@skin_slim_and_laser_solutions"
ORIGIN = "https://thecahayaskinclinic.co.uk"

LOCATIONS = [
    {
        "name": "Beverley",
        "venue": "Walkergate Wellness",
        "lines": ["Walkergate House", "Walkergate", "Beverley", "HU17 9ER"],
        "street": "Walkergate House, Walkergate",
        "town": "Beverley",
        "postcode": "HU17 9ER",
        "tag": "Online booking available",
        "note": ("Parking at Tesco. The back of our Grade II listed building is directly "
                 "opposite Tesco &mdash; follow the footpath around and you will find our "
                 "black front door, opposite Dog &amp; Duck Lane. Use the intercom, select "
                 "Skin &amp; Slim, then the bell. Reception is on the first floor."),
    },
    {
        "name": "Hessle",
        "venue": "Loft Beauty Co",
        "lines": ["4A The Weir", "Hessle", "HU13 0RU"],
        "street": "4A The Weir",
        "town": "Hessle",
        "postcode": "HU13 0RU",
        "tag": "Email to book",
        "note": "Appointments at Hessle are arranged by email or phone.",
    },
]

IMG = {
    "hero": "images/clinic-4.jpeg",
    "treatment": "images/clinic-4.jpeg",
    "flatlay": "images/g-1781.jpg",
    "gift": "images/g-1783.jpg",
    "products": "images/g-1785.jpg",
    "menu": "images/clinic-6.jpeg",
    "ba_skin": "images/clinic-1.jpeg",
    "ba_body": "images/clinic-3.jpeg",
    "ba_extra": "images/clinic-2.jpeg",
    "logo": "images/logo.jpeg",
}

# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------
TREATMENT_NAV = [
    ("facials.html", "Facials"),
    ("advanced-skin-treatments.html", "Advanced Skin Treatments"),
    ("chemical-peels.html", "Chemical Peels"),
    ("non-surgical-lifting.html", "Non-Surgical Lifting"),
    ("aesthetic-treatments.html", "Aesthetic Treatments"),
    ("laser-hair-removal.html", "Laser Hair Removal"),
    ("fat-loss.html", "Fat Loss &amp; Non-Surgical Lipo"),
    ("body-wellness.html", "Body &amp; Wellness"),
    ("skin-health-packages.html", "Skin Health Packages"),
    ("medical-grade-skincare.html", "Medical Grade Skincare"),
]

TREATMENT_SLUGS = {slug for slug, _ in TREATMENT_NAV} | {"treatments.html"}


def nav(current):
    """Primary navigation. `current` is the filename of the page being built."""
    def item(href, label):
        active = ' active' if href == current else ''
        return ('<li class="nav-item%s"><a href="%s" class="nav-link">%s</a></li>'
                % (active, href, label))

    drop_active = ' active' if current in TREATMENT_SLUGS else ''
    drop_items = '\n'.join(
        '              <a class="dropdown-item" href="%s">%s</a>' % (slug, label)
        for slug, label in TREATMENT_NAV)

    return """<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
      <div class="container">
        <a class="navbar-brand" href="index.html">Skin, Slim &amp; Laser <span class="d-none d-sm-inline">Solutions</span></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="hh-bars"><i></i><i></i><i></i></span>
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
          <ul class="navbar-nav ml-auto">
            {home}
            {about}
            <li class="nav-item dropdown{drop_active}">
              <a href="treatments.html" class="nav-link dropdown-toggle" id="treatmentsMenu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Treatments</a>
              <div class="dropdown-menu" aria-labelledby="treatmentsMenu">
                <a class="dropdown-item" href="treatments.html"><strong>All Treatments</strong></a>
{drop_items}
              </div>
            </li>
            {gallery}
            {contact}
          </ul>
        </div>
      </div>
    </nav>
    <!-- END nav -->""".format(
        home=item("index.html", "Home"),
        about=item("about.html", "About"),
        gallery=item("gallery.html", "Gallery"),
        contact=item("contact.html", "Contact"),
        drop_active=drop_active,
        drop_items=drop_items,
    )


# --------------------------------------------------------------------------
# Structured data
# --------------------------------------------------------------------------
def _location_ld(loc):
    return {
        "@type": "MedicalClinic",
        "@id": "%s/#%s" % (ORIGIN, loc["name"].lower()),
        "name": "%s — %s" % (BRAND_PLAIN, loc["name"]),
        "alternateName": "The Cahaya Skin Clinic",
        "description": "Advanced skin, laser and non-surgical body clinic at %s in %s, East Yorkshire."
                       % (loc["venue"], loc["name"]),
        "telephone": TEL,
        "email": EMAIL,
        "url": ORIGIN + "/contact.html",
        "image": ORIGIN + "/" + IMG["hero"],
        "priceRange": "££",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": loc["street"],
            "addressLocality": loc["town"],
            "addressRegion": "East Yorkshire",
            "postalCode": loc["postcode"],
            "addressCountry": "GB",
        },
        "areaServed": [
            {"@type": "City", "name": c}
            for c in ["Beverley", "Hessle", "Hull", "East Yorkshire"]
        ],
        "sameAs": [INSTAGRAM],
    }


ORGANISATION_LD = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": ["MedicalBusiness", "HealthAndBeautyBusiness"],
            "@id": ORIGIN + "/#organisation",
            "name": BRAND_PLAIN,
            "alternateName": ["The Cahaya Skin Clinic", "Skin & Slim Solutions"],
            "url": ORIGIN + "/",
            "logo": ORIGIN + "/" + IMG["logo"],
            "image": ORIGIN + "/" + IMG["hero"],
            "telephone": TEL,
            "email": EMAIL,
            "founder": {"@type": "Person", "name": "Lucy-Anne",
                        "jobTitle": "Advanced Skin & Laser Practitioner"},
            "description": ("Advanced skin, laser and non-surgical body clinic with clinics in "
                            "Beverley and Hessle, East Yorkshire. Medical grade "
                            "facials, chemical peels, microneedling, laser hair removal, "
                            "fat loss and lymphatic drainage."),
            "memberOf": {"@type": "Organization", "name": "British Medical Laser Association"},
            "sameAs": [INSTAGRAM],
            "department": [_location_ld(l) for l in LOCATIONS],
        }
    ],
}


def breadcrumb_ld(trail):
    """trail = [(name, href), ...] starting at Home."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": "%s/%s" % (ORIGIN, href) if href else None}
            for i, (name, href) in enumerate(trail)
        ],
    }


def service_ld(name, description, offers=None, url=""):
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": name,
        "name": name,
        "description": description,
        "url": "%s/%s" % (ORIGIN, url),
        "provider": {"@id": ORIGIN + "/#organisation"},
        "areaServed": {"@type": "AdministrativeArea", "name": "East Yorkshire"},
    }
    if offers:
        data["hasOfferCatalog"] = {
            "@type": "OfferCatalog",
            "name": name,
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {"@type": "Service", "name": o["name"]},
                    "price": o["price"],
                    "priceCurrency": "GBP",
                }
                for o in offers if o.get("price")
            ],
        }
    return data


def ld_script(*blocks):
    out = []
    for b in blocks:
        if not b:
            continue
        out.append('    <script type="application/ld+json">%s</script>'
                   % json.dumps(b, separators=(",", ":"), ensure_ascii=False))
    return "\n".join(out)


# --------------------------------------------------------------------------
# Page chrome
# --------------------------------------------------------------------------
def head(title, description, slug, ld="", image=None, robots=None):
    canonical = "%s/%s" % (ORIGIN, "" if slug == "index.html" else slug)
    og_image = ORIGIN + "/" + (image or IMG["hero"])
    robots_tag = ('    <meta name="robots" content="%s">\n' % robots) if robots else ""
    return """<!DOCTYPE html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{title}</title>
    <meta name="description" content="{description}">
{robots_tag}    <link rel="canonical" href="{canonical}">

    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{brand_plain}">
    <meta property="og:locale" content="en_GB">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{og_image}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{og_image}">
    <meta name="theme-color" content="#a3878b">
    <meta name="geo.region" content="GB-ERY">
    <meta name="geo.placename" content="Beverley, East Yorkshire">

    <link rel="icon" href="{logo}">
    <link rel="apple-touch-icon" href="{logo}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,600,700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="css/open-iconic-bootstrap.min.css">
    <link rel="stylesheet" href="css/animate.css">
    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" href="css/magnific-popup.css">
    <link rel="stylesheet" href="css/aos.css">
    <link rel="stylesheet" href="css/ionicons.min.css">
    <link rel="stylesheet" href="css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="css/jquery.timepicker.css">
    <link rel="stylesheet" href="css/flaticon.css">
    <link rel="stylesheet" href="css/icomoon.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/site.css">

{ld}
    <!-- Analytics: paste the clinic's GA4 Measurement ID to go live.
         Booking and call events fire into dataLayer regardless. -->
    <script>
      window.GA_MEASUREMENT_ID = ""; /* e.g. "G-XXXXXXXXXX" */
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      if (window.GA_MEASUREMENT_ID){{
        var s=document.createElement('script');s.async=true;
        s.src='https://www.googletagmanager.com/gtag/js?id='+window.GA_MEASUREMENT_ID;
        document.head.appendChild(s);
        gtag('js', new Date()); gtag('config', window.GA_MEASUREMENT_ID);
      }}
    </script>
  </head>
  <body>
""".format(title=title, description=description, canonical=canonical, og_image=og_image,
           brand_plain=BRAND_PLAIN, logo=IMG["logo"], ld=ld, robots_tag=robots_tag)


def hero(heading, sub=None, breadcrumb=None, image=None, home=False, compact=False):
    img = image or IMG["hero"]
    if home:
        inner = """            <span class="eyebrow">Beverley &middot; Hessle</span>
            <div class="icon">
              <a href="index.html" class="logo">
                <span class="flaticon-flower"></span>
                <h1>{brand}</h1>
              </a>
            </div>
            <h1 class="mb-4" data-scrollax="properties: {{ translateY: '30%', opacity: 1.6 }}">{heading}</h1>
            <p class="mb-5" data-scrollax="properties: {{ translateY: '30%', opacity: 1.6 }}">{sub}</p>
            <p data-scrollax="properties: {{ translateY: '30%', opacity: 1.6 }}">
              <a href="{booking}" target="_blank" rel="noopener" class="btn btn-white btn-outline-white px-4 py-3 mr-md-2 mb-2" data-book="hero">Book Beverley Online</a>
              <a href="treatments.html" class="btn btn-white btn-outline-white px-4 py-3 mb-2">View Treatments</a>
            </p>""".format(brand=BRAND, heading=heading, sub=sub, booking=BOOKING)
    else:
        crumbs = ' '.join(
            '<span class="mr-2"><a href="%s">%s</a></span>' % (href, name) if href
            else '<span>%s</span>' % name
            for name, href in breadcrumb)
        inner = """            <div class="icon">
              <a href="index.html" class="logo">
                <span class="flaticon-flower"></span>
                <h1>{brand}</h1>
              </a>
            </div>
            <h1 class="mb-3 mt-5 bread" data-scrollax="properties: {{ translateY: '30%', opacity: 1.6 }}">{heading}</h1>
            <p class="breadcrumbs" data-scrollax="properties: {{ translateY: '30%', opacity: 1.6 }}">{crumbs}</p>""".format(
            brand=BRAND, heading=heading, crumbs=crumbs)

    if compact:
        # No photo hero: a slim, solid-colour title band. Kept as .hero-wrap so
        # the nav, header-tone.js and sticky logic all key off it exactly as
        # they do on the full-hero pages.
        return """    <div class="hero-wrap hero-compact">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text align-items-center justify-content-center">
          <div class="col-md-9 ftco-animate text-center">
{inner}
          </div>
        </div>
      </div>
    </div>
""".format(inner=inner)

    return """    <div class="hero-wrap js-fullheight" style="background-image: url('{img}');" data-stellar-background-ratio="0.5">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text js-fullheight align-items-center justify-content-center" data-scrollax-parent="true">
          <div class="col-md-9 ftco-animate text-center" data-scrollax=" properties: {{ translateY: '70%' }}">
{inner}
          </div>
        </div>
      </div>
    </div>
""".format(img=img, inner=inner)


CTA_BAND = """    <section class="ftco-section ftco-appointment">
      <div class="overlay"></div>
      <div class="container">
        <div class="row d-md-flex align-items-center">
          <div class="col-md-2"></div>
          <div class="col-md-4 d-flex align-self-stretch ftco-animate">
            <div class="appointment-info text-center p-5">
              <div class="mb-4">
                <h3 class="mb-3">Call the clinic</h3>
                <p class="day"><strong><a href="tel:{tel}" style="color:inherit;" data-book="cta-call">{phone}</a></strong></p>
              </div>
              <div class="mb-4">
                <h3 class="mb-3">Email</h3>
                <p><a href="mailto:{email}" style="color:inherit;word-break:break-all;">{email}</a></p>
              </div>
              <div>
                <h3 class="mb-3">Clinics</h3>
                <p class="day">Beverley &middot; Hessle</p>
                <span>Strictly appointment only</span>
              </div>
            </div>
          </div>
          <div class="col-md-6 appointment pl-md-5 ftco-animate">
            <h3 class="mb-3">Book your consultation</h3>
            <p>Every treatment here starts with an in-depth consultation, so you leave understanding your skin, your treatment plan and the products that will actually work for you. Beverley takes online bookings; Hessle is arranged by email.</p>
            <p class="mt-4">
              <a href="{booking}" target="_blank" rel="noopener" class="btn btn-white btn-outline-white py-3 px-4" data-book="cta-band">Book Beverley Online</a>
            </p>
            <p class="mt-2"><a href="contact.html#enquiry" style="color:#fff; text-decoration:underline;">Or send an enquiry for Hessle</a></p>
          </div>
        </div>
      </div>
    </section>
""".format(tel=TEL, phone=PHONE, email=EMAIL, booking=BOOKING)


FOOTER = """    <footer class="ftco-footer ftco-section img">
      <div class="overlay"></div>
      <div class="container">
        <div class="row mb-5">
          <div class="col-md-4">
            <div class="ftco-footer-widget mb-4">
              <h2 class="ftco-heading-2">{brand}</h2>
              <p>Advanced skin, laser and non-surgical body clinic in East Yorkshire. Results-driven, clinically validated treatments in an honest, judgement-free, confidential setting. {formerly}.</p>
              <ul class="ftco-footer-social list-unstyled float-md-left float-lft mt-4">
                <li class="ftco-animate"><a href="{instagram}" target="_blank" rel="noopener" aria-label="Instagram"><span class="icon-instagram"></span></a></li>
              </ul>
            </div>
          </div>
          <div class="col-md-4">
            <div class="ftco-footer-widget mb-4 ml-md-4">
              <h2 class="ftco-heading-2">Treatments</h2>
              <ul class="list-unstyled">
{treatment_links}
              </ul>
            </div>
          </div>
          <div class="col-md-4">
            <div class="ftco-footer-widget mb-4">
              <h2 class="ftco-heading-2">Find us</h2>
              <div class="block-23 mb-3">
                <ul>
                  <li><span class="icon icon-map-marker"></span><span class="text">Walkergate Wellness, Walkergate House, Beverley HU17 9ER</span></li>
                  <li><span class="icon icon-map-marker"></span><span class="text">Loft Beauty Co, 4A The Weir, Hessle HU13 0RU</span></li>
                  <li><a href="tel:{tel}"><span class="icon icon-phone"></span><span class="text">{phone}</span></a></li>
                  <li><a href="mailto:{email}"><span class="icon icon-envelope"></span><span class="text">{email}</span></a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12 text-center">
            <p>
              Copyright &copy;<script>document.write(new Date().getFullYear());</script> {brand} &mdash; {formerly}. All rights reserved.
              &nbsp;|&nbsp; <a href="privacy-policy.html">Privacy Policy</a>
              &nbsp;|&nbsp; <a href="cookie-policy.html">Cookie Policy</a>
              <br><span style="font-size:13px;opacity:.7;">Template made with <i class="icon-heart" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank" rel="noopener">Colorlib</a></span>
            </p>
          </div>
        </div>
      </div>
    </footer>
""".format(
    brand=BRAND, formerly=FORMERLY, instagram=INSTAGRAM, tel=TEL, phone=PHONE, email=EMAIL,
    treatment_links="\n".join(
        '                <li><a href="%s" class="py-2 d-block">%s</a></li>' % (slug, label)
        for slug, label in TREATMENT_NAV[:7]),
)


TAIL = """
  <!-- loader -->
  <div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#a3878b"/></svg></div>

  <a href="{booking}" target="_blank" rel="noopener" class="rr-fab" id="rrFab" data-book="floating-button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9h18M8 2.5v4M16 2.5v4"/></svg>Book
  </a>
  <div class="rr-mbar" id="rrMbar">
    <a href="tel:{tel}" data-book="mobile-call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L20 13l1 4v3a1 1 0 0 1-1 1A16 16 0 0 1 3 5a1 1 0 0 1 1-1z"/></svg>Call</a>
    <a class="book" href="{booking}" target="_blank" rel="noopener" data-book="mobile-bar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9h18M8 2.5v4M16 2.5v4"/></svg>Book Now</a>
  </div>

  <script src="js/jquery.min.js"></script>
  <script src="js/jquery-migrate-3.0.1.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/jquery.easing.1.3.js"></script>
  <script src="js/jquery.waypoints.min.js"></script>
  <script src="js/jquery.stellar.min.js"></script>
  <script src="js/owl.carousel.min.js"></script>
  <script src="js/jquery.magnific-popup.min.js"></script>
  <script src="js/aos.js"></script>
  <script src="js/jquery.animateNumber.min.js"></script>
  <script src="js/bootstrap-datepicker.js"></script>
  <script src="js/jquery.timepicker.min.js"></script>
  <script src="js/scrollax.min.js"></script>
  <script src="js/main.js"></script>
  <script src="js/header-tone.js"></script>
  <script src="js/booking.js"></script>
</body>
</html>
""".format(booking=BOOKING, tel=TEL)


def page(slug, title, description, heading, body, breadcrumb=None, hero_image=None,
         ld_extra=None, sub=None, home=False, cta=True, robots=None, hero_compact=False):
    trail = [("Home", "index.html")] + [(n, h) for n, h in (breadcrumb or [])]
    blocks = [ORGANISATION_LD if home else None]
    if not home:
        blocks.append(breadcrumb_ld(trail))
    else:
        blocks.append(None)
    if ld_extra:
        blocks.extend(ld_extra if isinstance(ld_extra, list) else [ld_extra])

    crumb_links = [(n, h if h and h != slug else None) for n, h in trail]
    if not home:
        crumb_links[-1] = (crumb_links[-1][0], None)

    html = head(title, description, slug, ld_script(*blocks), image=hero_image, robots=robots)
    html += hero(heading, sub=sub, breadcrumb=crumb_links, image=hero_image, home=home,
                 compact=hero_compact)
    html += nav(slug) + "\n\n"
    html += body
    if cta:
        html += CTA_BAND
    html += FOOTER + TAIL

    with open(os.path.join(HERE, slug), "w") as fh:
        fh.write(html)
    return slug


# --------------------------------------------------------------------------
# Reusable body helpers
# --------------------------------------------------------------------------
def section(inner, cls="ftco-section", extra=""):
    return '    <section class="%s"%s>\n      <div class="container">\n%s\n      </div>\n    </section>\n\n' % (
        cls, extra, inner)


def heading_block(title, lead=None, eyebrow=None, width=8):
    parts = ['        <div class="row justify-content-center mb-5 pb-3">',
             '          <div class="col-md-%d heading-section ftco-animate text-center">' % width]
    if eyebrow:
        parts.append('            <span class="eyebrow">%s</span>' % eyebrow)
    parts.append('            <h2 class="mb-4">%s</h2>' % title)
    if lead:
        parts.append('            <p>%s</p>' % lead)
    parts += ['          </div>', '        </div>']
    return "\n".join(parts)


def price_list(items):
    """items: list of dicts with name, sub (optional), price (optional), body (optional)."""
    out = ['        <div class="row justify-content-center">',
           '          <div class="col-lg-9 ftco-animate">',
           '            <ul class="price-list">']
    for it in items:
        sub = ('<span class="price-sub">%s</span>' % it["sub"]) if it.get("sub") else ""
        tag = ('<span class="price-tag">%s</span>' % it["price"]) if it.get("price") else ""
        body = ('<p>%s</p>' % it["body"]) if it.get("body") else ""
        out.append("""              <li class="price-item">
                <div class="price-head"><h3>%s</h3>%s</div>%s
                %s
              </li>""" % (it["name"], tag, sub, body))
    out += ['            </ul>', '          </div>', '        </div>']
    return "\n".join(out)


def rate_cards(cards):
    out = ['        <div class="row">']
    for c in cards:
        rows = "\n".join(
            '                <li><span>%s</span><strong>%s</strong></li>' % (n, p)
            for n, p in c["rows"])
        out.append("""          <div class="col-md-6 col-lg-3 mb-4 ftco-animate">
            <div class="rate-card">
              <h3>%s</h3>
              <span class="rate-note">%s</span>
              <ul>
%s
              </ul>
            </div>
          </div>""" % (c["title"], c["note"], rows))
    out.append('        </div>')
    return "\n".join(out)


def treatment_cards(cards):
    out = ['        <div class="row">']
    for c in cards:
        out.append("""          <div class="col-md-6 col-lg-4 mb-4 d-flex ftco-animate">
            <a class="tcard" href="%s">
              <img src="%s" alt="%s" loading="lazy" width="800" height="600">
              <div class="tcard-body">
                <h3>%s</h3>
                <p>%s</p>
                <span class="tcard-more">Learn more</span>
              </div>
            </a>
          </div>""" % (c["href"], c["img"], c["alt"], c["title"], c["text"]))
    out.append('        </div>')
    return "\n".join(out)


def intro_split(img, alt, title, paras, cta_label=None, cta_href=None, reverse=False):
    text = "\n".join('            <p>%s</p>' % p for p in paras)
    btn = ('\n            <p class="mt-4"><a href="%s" class="btn btn-primary py-3 px-4">%s</a></p>'
           % (cta_href, cta_label)) if cta_label else ""
    img_col = """          <div class="col-md-6 d-flex ftco-animate">
            <img src="%s" alt="%s" class="img-fluid align-self-stretch" style="width:100%%;object-fit:cover;border-radius:3px;" loading="lazy">
          </div>""" % (img, alt)
    txt_col = """          <div class="col-md-6 %s ftco-animate">
            <h2 class="mb-4">%s</h2>
%s%s
          </div>""" % ("pr-md-5" if reverse else "pl-md-5", title, text, btn)
    cols = (txt_col + "\n" + img_col) if reverse else (img_col + "\n" + txt_col)
    return '        <div class="row d-flex align-items-center">\n%s\n        </div>' % cols
