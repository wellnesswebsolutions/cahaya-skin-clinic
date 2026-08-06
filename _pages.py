#!/usr/bin/env python3
"""Page definitions for Skin, Slim & Laser Solutions.

Run `python3 _pages.py` to regenerate every HTML file, sitemap.xml and robots.txt.
Shared chrome (head, nav, hero, CTA, footer, schema) lives in _build.py.

All copy, prices and clinic details are taken from the clinic's own site
(thecahayaskinclinic.co.uk) — nothing here is invented.
"""

import datetime
import json
import os

from _build import (BOOKING, BRAND, BRAND_PLAIN, EMAIL, FORMERLY, HERE, IG_HANDLE,
                    IMG, INSTAGRAM, LOCATIONS, ORIGIN, PHONE, TEL, TREATMENT_NAV,
                    heading_block, intro_split, page, price_list, rate_cards,
                    section, service_ld, treatment_cards)

BUILT = []


def add(*args, **kwargs):
    BUILT.append(page(*args, **kwargs))


# ==========================================================================
# Shared fragments
# ==========================================================================
def location_cards(show_notes=False):
    cols = []
    for loc in LOCATIONS:
        note = ('\n              <p style="font-size:14.5px;line-height:1.8;color:#8a8078;margin-top:1em;">%s</p>'
                % loc["note"]) if show_notes else ""
        cols.append("""          <div class="col-md-4 mb-4 d-flex ftco-animate">
            <div class="loc-card">
              <span class="loc-pin"><span class="icon-map-marker"></span></span>
              <h3>%s</h3>
              <address>%s<br>%s</address>
              <span class="loc-tag">%s</span>%s
            </div>
          </div>""" % (loc["name"], loc["venue"], "<br>".join(loc["lines"]), loc["tag"], note))
    return '        <div class="row">\n%s\n        </div>' % "\n".join(cols)


CONSULT_NOTE = """        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <div class="notice">
              <h3>Every treatment starts with a consultation</h3>
              <p>We are a proactive clinic, not a conveyor belt. Before anything is booked in we talk through your skin, your concerns and your goals, so you leave understanding how your skin works and which active ingredients will actually help. If a treatment will not give you a tangible result, we will tell you and suggest something that will.</p>
              <p>We are strictly an appointment-only clinic. Prices shown are the clinic's standard rates and are confirmed at consultation.</p>
            </div>
          </div>
        </div>"""


def treatment_cta(text="Book a consultation"):
    return """    <section class="ftco-section ftco-discount img" style="background-image: url({img});">
      <div class="overlay" style="background: rgba(255,255,255,0.55);"></div>
      <div class="container">
        <div class="row justify-content-end">
          <div class="col-md-5 discount ftco-animate">
            <h3 style="color:#111;">Not sure where to start?</h3>
            <h2 class="mb-4" style="color:#111;">{text}</h2>
            <p class="mb-4" style="color:#111;">Our in-depth consultations are where every treatment plan begins. We will assess your skin, explain your options honestly and build a plan around your concerns, your budget and your time.</p>
            <p>
              <a href="{booking}" target="_blank" rel="noopener" class="btn px-4 py-3" style="color:#fff;background:#111;border:2px solid #111;" data-book="treatment-band">Book Beverley Online</a>
            </p>
          </div>
        </div>
      </div>
    </section>

""".format(img=IMG["flatlay"], text=text, booking=BOOKING)


# ==========================================================================
# Home
# ==========================================================================
PILLARS = [
    ("Advanced Skin", IMG["treatment"],
     "Microneedling, peels, algae bio-needling, radio frequency and vitamin infusion &mdash; delivered by advanced skin practitioners.",
     "advanced-skin-treatments.html"),
    ("Laser Hair Removal", IMG["flatlay"],
     "The strongest triple wavelength diode laser available, in the hands of British Medical Laser Association members.",
     "laser-hair-removal.html"),
    ("Fat Loss &amp; Body", IMG["ba_body"],
     "Cryolipolysis fat freezing, cavitation, shockwave and radio frequency for stubborn fat, cellulite and loose skin.",
     "fat-loss.html"),
    ("Wellness &amp; Drainage", IMG["gift"],
     "Pressotherapy, manual lymphatic drainage, oxygen therapy and vitamin injections to support you from the inside out.",
     "body-wellness.html"),
]


def build_home():
    pillars = "\n".join("""          <div class="col-lg-3 col-md-6 d-flex mb-4 ftco-animate">
            <div class="staff">
              <div class="img mb-4" style="background-image: url(%s);"></div>
              <div class="info text-center">
                <h3><a href="%s" style="color:inherit;">%s</a></h3>
                <span class="position">%s</span>
                <div class="text"><p>%s</p></div>
              </div>
            </div>
          </div>""" % (img, href, title, "Beverley &middot; Hessle", text)
        for title, img, text, href in PILLARS)

    body = section(
        heading_block(
            "Offering holistic skin solutions",
            "&ldquo;Cahaya&rdquo; is Indonesian for &ldquo;glow&rdquo; &mdash; and that is the aim of "
            "Skin, Slim &amp; Laser Solutions: for our patients to leave glowing. As highly regarded skin "
            "and non-surgical experts, we use medical grade technology to deliver safe, modern treatments "
            "that are genuine alternatives to injectables.",
            eyebrow="Beverley &middot; Hessle", width=9) + "\n        <div class=\"row\">\n" + pillars + "\n        </div>",
        cls="ftco-section bg-light")

    body += section(intro_split(
        IMG["menu"], "Treatment menu at Skin, Slim & Laser Solutions in Beverley",
        "Peptides? Retinol? Antioxidants? Microneedling?",
        ["We know it can be a bit of a minefield out there &mdash; knowing which skin treatment to have "
         "and which skincare to use. That is where we come in.",
         "It is our job to guide you along your treatment journey, so you leave feeling educated about "
         "your own skin type, your concern, your treatment and your skincare. Our in-depth consultations "
         "give you a thorough understanding of how your skin works and which ingredients will work for you.",
         "We only offer results-orientated, medical grade skincare regimes built on corrective and "
         "preventative active ingredients &mdash; and we only use industry leading technology that is "
         "clinically validated. If a treatment doesn't offer tangible results, we simply do not offer it."],
        cta_label="Explore our treatments", cta_href="treatments.html", reverse=True))

    body += section(
        heading_block("Treatments", "Skin, laser, body and wellness &mdash; all under one roof, "
                                    "all delivered by qualified advanced practitioners.",
                      eyebrow="What we do") + "\n" +
        treatment_cards([
            {"href": "facials.html", "img": IMG["treatment"], "alt": "Advanced facial treatment in progress at the Beverley clinic",
             "title": "Facials", "text": "Bespoke, results-driven facials from &pound;85, using pharmaceutical grade products only."},
            {"href": "advanced-skin-treatments.html", "img": IMG["ba_skin"], "alt": "Before and after results from advanced skin treatments",
             "title": "Advanced Skin Treatments", "text": "Microneedling with polynucleotides and exosomes, algae peel, RF and vitamin infusion."},
            {"href": "chemical-peels.html", "img": IMG["products"], "alt": "Medical grade skincare and peel products",
             "title": "Chemical Peels", "text": "Pharmaceutical grade peels from &pound;70 for breakouts, tone and fine lines."},
            {"href": "laser-hair-removal.html", "img": IMG["flatlay"], "alt": "The Cahaya Skin Clinic treatment room styling",
             "title": "Laser Hair Removal", "text": "Triple wavelength diode laser, safe for all skin types. Courses of six from &pound;150."},
            {"href": "fat-loss.html", "img": IMG["ba_body"], "alt": "Before and after body contouring results",
             "title": "Fat Loss &amp; Non-Surgical Lipo", "text": "Fat freezing, cavitation, shockwave and the Slim Suit for stubborn fat and cellulite."},
            {"href": "body-wellness.html", "img": IMG["gift"], "alt": "Wellness treatments and supplements at the clinic",
             "title": "Body &amp; Wellness", "text": "Lymphatic drainage, pressotherapy, oxygen therapy, menopause massage and vitamin injections."},
        ]))

    body += treatment_cta("Book an in-depth skin consultation")

    body += """    <section class="ftco-section ftco-counter img" id="section-counter" style="background-image: url({counter_img});">
      <div class="overlay"></div>
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-10">
            <div class="row">
              <div class="col-md-6 col-lg-3 d-flex justify-content-center counter-wrap ftco-animate">
                <div class="block-18 text-center"><div class="text">
                  <div class="icon"><span class="flaticon-flower"></span></div>
                  <span>Clinics in East Yorkshire</span>
                  <strong class="number" data-number="2">0</strong>
                </div></div>
              </div>
              <div class="col-md-6 col-lg-3 d-flex justify-content-center counter-wrap ftco-animate">
                <div class="block-18 text-center"><div class="text">
                  <div class="icon"><span class="flaticon-flower"></span></div>
                  <span>Up to % fat loss per treated area</span>
                  <strong class="number" data-number="40">0</strong>
                </div></div>
              </div>
              <div class="col-md-6 col-lg-3 d-flex justify-content-center counter-wrap ftco-animate">
                <div class="block-18 text-center"><div class="text">
                  <div class="icon"><span class="flaticon-flower"></span></div>
                  <span>Facial muscles worked in a CACI lift</span>
                  <strong class="number" data-number="32">0</strong>
                </div></div>
              </div>
              <div class="col-md-6 col-lg-3 d-flex justify-content-center counter-wrap ftco-animate">
                <div class="block-18 text-center"><div class="text">
                  <div class="icon"><span class="flaticon-flower"></span></div>
                  <span>Treatments in every skin health package</span>
                  <strong class="number" data-number="6">0</strong>
                </div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

""".format(counter_img=IMG["treatment"])

    body += section(intro_split(
        IMG["flatlay"], "The Cahaya Skin Clinic branding and AlumierMD medical grade skincare",
        "From Australia to Beverley. Then Hessle.",
        ["Formerly The Cahaya Skin Clinic, we started our journey in Australia. Inspired by the advanced, "
         "pioneering treatments being offered down under, our founder decided to bring those advancements "
         "home to East Yorkshire.",
         "Following a career change, our founder Lucy-Anne moved from practising law to being a student "
         "once more &mdash; making sure she holds all of the necessary, recognised qualifications, licences "
         "and board memberships, so that she is not only as qualified as possible but that her clients are "
         "as safe as possible.",
         "We pride ourselves on an honest, judgement-free and confidential approach."],
        cta_label="More about the clinic", cta_href="about.html"))

    body += section(
        heading_block("Two clinics in East Yorkshire",
                      "Beverley takes online bookings. Hessle is arranged by email or phone.",
                      eyebrow="Where to find us") + "\n" + location_cards(),
        cls="ftco-section bg-champagne")

    body += """    <section class="ftco-section pt-0">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-10 text-center ftco-animate">
            <h2 class="mb-3">Follow our work</h2>
            <p class="mb-4"><a href="{ig}" target="_blank" rel="noopener" style="color:#8a7355;font-weight:600;letter-spacing:.06em;">{handle}</a></p>
            <div class="ba-grid">
              <a class="ba-tile" href="{ig}" target="_blank" rel="noopener"><img src="{i1}" alt="Skin treatment before and after results at the Beverley clinic" loading="lazy"></a>
              <a class="ba-tile" href="{ig}" target="_blank" rel="noopener"><img src="{i2}" alt="Body contouring before and after results" loading="lazy"></a>
              <a class="ba-tile" href="{ig}" target="_blank" rel="noopener"><img src="{i3}" alt="The Cahaya Skin Clinic gift packaging and AlumierMD products" loading="lazy"></a>
            </div>
          </div>
        </div>
      </div>
    </section>

""".format(ig=INSTAGRAM, handle=IG_HANDLE, i1=IMG["ba_skin"], i2=IMG["ba_body"], i3=IMG["flatlay"])

    add("index.html",
        "Skin Clinic Beverley &amp; Hessle | Skin, Slim &amp; Laser Solutions",
        "Advanced skin, laser and non-surgical body clinic in Beverley and Hessle. "
        "Medical grade facials, chemical peels, microneedling, laser hair removal and fat loss. "
        "Call 07479 686312.",
        "Advanced Skin, Laser &amp; Non-Surgical Body Clinic",
        body,
        sub="Beverley &middot; Hessle &mdash; " + FORMERLY,
        home=True)


# ==========================================================================
# About
# ==========================================================================
def build_about():
    body = section(intro_split(
        IMG["treatment"], "Advanced skin practitioner treating a client at the Beverley clinic",
        "Honest, judgement-free, results-driven skin care",
        ["Skin, Slim &amp; Laser Solutions &mdash; formerly The Cahaya Skin Clinic &mdash; is an advanced "
         "skin, laser and non-surgical body clinic with sites in Beverley and Hessle.",
         "&ldquo;Cahaya&rdquo; is Indonesian for &ldquo;glow&rdquo;. That is the aim: for our patients to "
         "leave glowing. As highly regarded skin and non-surgical experts, you can feel safe in the "
         "knowledge that your skin will receive the utmost care and personalised attention. Our medical "
         "grade technology means patients receive safe, modern treatments that are real alternatives to "
         "injectables.",
         "We pride ourselves on an honest, judgement-free, confidential approach."],
        cta_label="See our treatments", cta_href="treatments.html"))

    body += section(
        heading_block("From Australia to East Yorkshire", eyebrow="Our story", width=9) + """
        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <p>Our journey started in Australia. Inspired by the advanced, pioneering treatments being offered down under, our founder decided to bring those advancements home to East Yorkshire.</p>
            <p>Following a career change, our founder <strong>Lucy-Anne</strong> transitioned from practising law to being a student once more &mdash; making sure she holds all of the necessary, recognised qualifications, licences and board memberships. Not only to be as qualified as possible, but so that her clients are as safe as possible. As proud members of the <strong>British Medical Laser Association</strong>, we are highly qualified, highly experienced practitioners who endeavour to follow licensing requirements and professional standards.</p>
            <p>As advanced skin and laser practitioners, the clinic is able to support clients in achieving their aesthetic goals. By offering truly tailored packages, we can make sure that all skin concerns and skin types are catered for.</p>
            <p>Every treatment offered here is results driven, clinically validated and backed by science. <strong>If a treatment doesn't offer tangible results, we simply do not offer it.</strong></p>
          </div>
        </div>""", cls="ftco-section bg-light")

    steps = [
        ("1. In-depth consultation", "flaticon-flower",
         "We talk through your skin, your concerns and your history before anything is booked in. No pressure, no judgement."),
        ("2. A plan you understand", "flaticon-shampoo",
         "You leave knowing how your skin works, what your treatment does and which active ingredients are worth your money."),
        ("3. The treatment", "flaticon-curl",
         "Delivered by advanced practitioners using clinically validated, medical grade technology only."),
        ("4. Aftercare &amp; review", "flaticon-cosmetics",
         "Prescriptive homecare, before and after photographs where relevant, and a review of how your skin is responding."),
    ]
    step_html = "\n".join("""          <div class="col-md-6 col-lg-3 ftco-animate">
            <div class="media d-block text-center block-6 services">
              <div class="icon d-flex mb-3"><span class="%s"></span></div>
              <div class="media-body">
                <h3 class="heading">%s</h3>
                <p>%s</p>
              </div>
            </div>
          </div>""" % (icon, title, text) for title, icon, text in steps)

    body += section(
        heading_block("What a visit looks like",
                      "No surprises and no upselling &mdash; just a clear plan before anything starts.",
                      eyebrow="Our approach") + "\n" + step_html)

    body += section(
        heading_block("Education, not guesswork", eyebrow="Skin seminars", width=9) + """
        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <div class="notice">
              <p>We are a proactive service and run skin seminars with our patients to educate them on their skin concerns. Empowering patients with knowledge, and allowing them to gain an understanding of the science of their own skin, enhances their results and increases how long those results last.</p>
              <p>Thorough skincare consultations are offered as standard, because we believe in targeting the root of a concern rather than the symptom. Our <a href="skin-health-packages.html">skin health packages</a> take that further, treating the skin from the inside out with award-winning supplements alongside professional treatments.</p>
            </div>
          </div>
        </div>""", cls="ftco-section bg-champagne")

    body += section(
        heading_block("Two clinics, one standard of care",
                      "Beverley takes online bookings. Hessle is arranged by email or phone.",
                      eyebrow="Where to find us") + "\n" + location_cards())

    add("about.html",
        "About Us | Advanced Skin &amp; Laser Clinic in Beverley",
        "Meet Skin, Slim & Laser Solutions, formerly The Cahaya Skin Clinic. Founded by Lucy-Anne, "
        "an advanced skin and laser practitioner and British Medical Laser Association member, with "
        "clinics in Beverley and Hessle.",
        "About the Clinic",
        body,
        breadcrumb=[("About", "about.html")], hero_compact=True)


# ==========================================================================
# Treatments hub
# ==========================================================================
TREATMENT_INDEX = [
    ("facials.html", "Facials", IMG["treatment"],
     "Advanced facial treatment being delivered at the Beverley clinic",
     "Bespoke, results-driven yet relaxing facials from &pound;85, delivered by an advanced skin scientist using pharmaceutical grade products only."),
    ("advanced-skin-treatments.html", "Advanced Skin Treatments", IMG["ba_skin"],
     "Before and after results from advanced skin treatments",
     "Microneedling with polynucleotides and exosomes, algae bio-needling, fractional radio frequency and vitamin infusion therapy."),
    ("chemical-peels.html", "Chemical Peels", IMG["products"],
     "Medical grade skincare and chemical peel products",
     "A bespoke range of pharmaceutical grade peels from &pound;70, for breakout-prone skin, uneven tone and fine lines."),
    ("non-surgical-lifting.html", "Non-Surgical Lifting", IMG["menu"],
     "Facial treatment menu at the clinic",
     "CACI microcurrent facials and no-needle rejuvenation &mdash; lifting and tightening without injectables."),
    ("aesthetic-treatments.html", "Aesthetic Treatments", IMG["gift"],
     "Clinic product and gift styling",
     "Anti-wrinkle injections, Profhilo, polynucleotides, Sunekos, Lumi Eyes and Plasma Pen, from an experienced injector."),
    ("laser-hair-removal.html", "Laser Hair Removal", IMG["flatlay"],
     "The Cahaya Skin Clinic styling and branding",
     "The strongest triple wavelength diode laser available, safe for all skin types. Courses of six from &pound;150."),
    ("fat-loss.html", "Fat Loss &amp; Non-Surgical Liposuction", IMG["ba_body"],
     "Before and after body contouring and cellulite results",
     "Cryolipolysis fat freezing, cavitation, shockwave therapy, the Slim Suit and fat dissolving injections."),
    ("body-wellness.html", "Body &amp; Wellness Treatments", IMG["products"],
     "Wellness products at the clinic",
     "Pressotherapy, manual lymphatic drainage, wood therapy, menopause and post-op massage, oxygen therapy and vitamin injections."),
    ("skin-health-packages.html", "Skin Health Packages", IMG["flatlay"],
     "Skincare and supplement packages from the clinic",
     "Four-month partnership packages for acne, ageing, pigmentation, psoriasis, eczema and pregnancy &mdash; treating skin inside and out."),
    ("medical-grade-skincare.html", "Medical Grade Skincare", IMG["gift"],
     "AlumierMD medical grade skincare products",
     "Prescriptive, results-orientated regimes built on corrective and preventative active ingredients."),
]


def build_treatments():
    cards = treatment_cards([
        {"href": h, "img": img, "alt": alt, "title": t, "text": txt}
        for h, t, img, alt, txt in TREATMENT_INDEX])

    body = section(
        heading_block(
            "Every treatment we offer",
            "From wrinkle reduction and skin tightening to microneedling, laser hair removal and "
            "non-surgical body contouring. Everything below is clinically validated and delivered by "
            "qualified advanced practitioners &mdash; if a treatment doesn't offer tangible results, "
            "we don't offer it.",
            eyebrow="Treatments", width=9) + "\n" + cards)

    body += section(CONSULT_NOTE, cls="ftco-section bg-light pt-0 pb-5",
                    extra=' style="padding-top:0;"')
    body += treatment_cta()

    add("treatments.html",
        "Treatments | Skin, Laser &amp; Body Clinic, Beverley",
        "Full treatment list at Skin, Slim & Laser Solutions: facials, chemical peels, microneedling, "
        "CACI, aesthetics, laser hair removal, fat freezing, lymphatic drainage and skin health packages.",
        "Treatments",
        body,
        breadcrumb=[("Treatments", "treatments.html")],
        hero_compact=True)


# ==========================================================================
# Individual treatment pages
# ==========================================================================
def treatment_page(slug, nav_title, h1, title, description, lead, items,
                   hero_image=None, extra_top="", extra_bottom="", ld_name=None):
    body = section(heading_block(h1, lead, eyebrow="Treatments", width=9) + "\n" + price_list(items))
    if extra_top:
        body += extra_top
    body += section(CONSULT_NOTE, cls="ftco-section bg-light")
    if extra_bottom:
        body += extra_bottom
    body += treatment_cta()

    offers = [{"name": i["name"].replace("&amp;", "&"), "price": i.get("ld_price")} for i in items]
    add(slug, title, description, h1, body,
        breadcrumb=[("Treatments", "treatments.html"), (nav_title, slug)],
        hero_image=hero_image or IMG["treatment"],
        ld_extra=service_ld(ld_name or nav_title.replace("&amp;", "&"), description, offers, slug),
        hero_compact=True)


def build_facials():
    items = [
        {"name": "The Refresh", "price": "&pound;85", "ld_price": "85",
         "sub": "Signature skin detox",
         "body": "The ultimate skin detox. A deep clean, soothing oxygen therapy and skin purification modalities. The perfect prep and post treatment &mdash; you even get a sneak peek of the impurities your skin was harbouring."},
        {"name": "The Renew", "price": "&pound;95", "ld_price": "95",
         "sub": "Tuned to your skin",
         "body": "The Skin Renew package tunes into what <em>your</em> skin needs. Using a variety of advanced treatment programs, the Renew is the facial that works specifically for you."},
        {"name": "The Rewind", "price": "&pound;135", "ld_price": "135",
         "sub": "Rejuvenating signature facial",
         "body": "Incorporating our signature cleanse and a wealth of rejuvenating modalities, this facial will have you feeling relaxed but still reaping the rewards in the weeks to come."},
    ]
    extra = section(
        heading_block("The technology behind your facial",
                      "Each facial is delivered by an advanced skin scientist using pharmaceutical grade "
                      "products only. Your practitioner will build your treatment from the modalities below.",
                      eyebrow="Modalities", width=9) + """
        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <ul class="contra-list">
              <li>Dermalux LED light therapy</li>
              <li>CACI Microlift</li>
              <li>Radio frequency skin tightening</li>
              <li>Microneedling</li>
              <li>Hydradiamond exfoliation</li>
              <li>Sculpting facial massage</li>
              <li>Oxygen therapy</li>
              <li>Skin purification and deep cleansing</li>
            </ul>
            <p class="mt-4" style="font-size:15px;color:#8a8078;">Facials are delivered in partnership with <strong>@The_Facialist_Beverley</strong>.</p>
          </div>
        </div>""", cls="ftco-section bg-champagne")

    treatment_page(
        "facials.html", "Facials", "Facials",
        "Facials in Beverley | Medical Grade Facial Treatments",
        "Results-driven facials in Beverley from £85. The Refresh, Renew and Rewind, delivered by an "
        "advanced skin scientist using Dermalux LED, CACI, radio frequency, microneedling and oxygen therapy.",
        "Offering a range of technologies and modalities, our facials are a bespoke, results-driven yet "
        "relaxing experience. Each facial is delivered by an advanced skin scientist, using pharmaceutical "
        "grade products only.",
        items, hero_image=IMG["menu"], extra_top=extra)


def build_peels():
    items = [
        {"name": "Chemical peel", "price": "from &pound;70", "ld_price": "70",
         "sub": "Pharmaceutical grade",
         "body": "A chemical peel is a solution applied to the skin to remove dead skin cells. The peeling solution lowers the skin's natural pH so that dead surface cells can be removed safely. The name implies an extremely invasive treatment &mdash; that is not the case, and we make sure every patient is completely comfortable."},
    ]
    extra = section(
        heading_block("What a peel can treat", eyebrow="Concerns", width=9) + """
        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <p>Our bespoke range of pharmaceutical grade peels means we can treat a multitude of skin concerns &mdash; from helping clients with breakout-prone skin, to improving skin tone, to helping reduce fine lines and wrinkles.</p>
            <ul class="contra-list mt-4">
              <li>Breakout and blemish-prone skin</li>
              <li>Congestion and enlarged pores</li>
              <li>Uneven skin tone and pigmentation</li>
              <li>Fine lines and wrinkles</li>
              <li>Dull, tired-looking skin</li>
              <li>Textural irregularity</li>
            </ul>
            <p class="mt-4">Peels pair well with our <a href="advanced-skin-treatments.html">advanced skin treatments</a> and with a prescriptive <a href="medical-grade-skincare.html">medical grade skincare</a> routine at home.</p>
          </div>
        </div>""", cls="ftco-section bg-champagne")

    treatment_page(
        "chemical-peels.html", "Chemical Peels", "Chemical Peels",
        "Chemical Peels Beverley | From &pound;70 | Skin, Slim &amp; Laser",
        "Pharmaceutical grade chemical peels in Beverley from £70. Safely resurface the skin to treat "
        "breakouts, uneven tone, congestion and fine lines. In-depth consultation included.",
        "A bespoke range of pharmaceutical grade peels, matched to your skin at consultation.",
        items, hero_image=IMG["products"], extra_top=extra)


ADVANCED_ITEMS = [
    {"name": "Algae Peel", "price": "&pound;85", "ld_price": "85", "sub": "Bio microneedling",
     "body": "The revolutionary algae peel has taken the industry by storm. A form of bio microneedling, this peel has an improved ingredient delivery system, enhances skin renewal and offers improved structural support for the skin. A must for all skin types and concerns."},
    {"name": "Vitamin Infusion Therapy", "price": "&pound;90", "ld_price": "90", "sub": "Mesotherapy with NCTF 135HA",
     "body": "This procedure incorporates microneedling with NCTF 135. The micro-punctures created during microneedling allow for a deeper infusion of the 24 amino acids, 12 vitamins and 6 mineral ingredients that make up the award-winning collagen bio-stimulator, NCTF 135HA."},
    {"name": "Microneedling Remodelling", "price": "&pound;85", "ld_price": "85",
     "sub": "With polynucleotides &amp; exosomes",
     "body": "Microneedling uses a medical device to create tiny wounds in the target area. By fabricating a minor injury, the body's healing process awakens, igniting the production of collagen and elastin &mdash; and a more youthful complexion. It can also minimise the effects of scarring and stretch marks, reduce pore size and reduce wrinkle depth. What sets our microneedling apart is the incorporation of salmon DNA and exosome therapy to accelerate results and stimulate cell-to-cell communication. Every microneedling treatment includes a complimentary skin-healing oxygen and LED light treatment."},
    {"name": "Fractional Radiofrequency", "price": "&pound;85", "ld_price": "85", "sub": "Lift and tighten",
     "body": "Fractional radio frequency tightens over-stretched collagen fibres for an instant lift, and plays a huge role in helping your skin create more collagen and elastin &mdash; helping you to age backwards, naturally."},
    {"name": "Radiofrequency with Microneedling", "price": "Face &pound;120 &middot; Eyes &pound;80",
     "ld_price": "120", "sub": "The ultimate lift and tighten",
     "body": "This combination couples the benefits of radio frequency with the advantages of microneedling. Radio frequency machinery sends radio waves to selectively target and heat the deep layer of your skin, stimulating the fibroblast cells to contract and produce new elastin and collagen fibres."},
    {"name": "Hair Growth Restoration Therapy", "price": "from &pound;85", "ld_price": "85",
     "sub": "Scalp microneedling",
     "body": "Hair growth stimulators are applied to the scalp using microneedling technology. The hair-restoring ingredients penetrate individual hair follicles and initiate growth through the tiny channels made by the microneedling. A popular treatment for those with thinning hair, or anyone wanting to encourage growth and volume."},
]


def build_advanced():
    treatment_page(
        "advanced-skin-treatments.html", "Advanced Skin Treatments", "Advanced Skin Treatments",
        "Microneedling &amp; Advanced Skin Treatments, Beverley",
        "Advanced skin treatments in Beverley: microneedling with polynucleotides and exosomes from £85, "
        "algae peel, vitamin infusion mesotherapy, fractional radiofrequency and hair growth restoration.",
        "Clinically validated, results-driven treatments using medical grade devices. Advanced and express "
        "treatments can be performed as stand-alone appointments or added on to any other treatment.",
        ADVANCED_ITEMS, hero_image=IMG["ba_skin"])


def build_lifting():
    items = [
        {"name": "CACI Facial", "price": "&pound;65", "ld_price": "65", "sub": "Non-surgical microcurrent lift",
         "body": "CACI (Computer Aided Cosmetology Instrument) facials have been at the forefront of non-invasive aesthetic treatment systems for over 25 years. CACI uses electrical pulses to stimulate all 32 muscles in your face. These non-surgical facials combine LED light therapy with a microcurrent, and that simultaneous energy helps tissue regeneration and the production of collagen."},
    ] + [dict(i) for i in ADVANCED_ITEMS[:5]]
    treatment_page(
        "non-surgical-lifting.html", "Non-Surgical Lifting", "Non-Surgical Lifting &amp; No-Needle Rejuvenation",
        "Non-Surgical Face Lifting &amp; CACI in Beverley",
        "Non-surgical lifting in Beverley: CACI microcurrent facials from £65, plus algae peel, "
        "mesotherapy, microneedling and radiofrequency. Lift and tighten without injectables.",
        "Lifting, tightening and rejuvenation without needles or surgery &mdash; using microcurrent, LED, "
        "radio frequency and bio-needling technology.",
        items, hero_image=IMG["menu"], ld_name="Non-Surgical Lifting")


def build_aesthetics():
    items = [
        {"name": "Anti-Wrinkle Injections", "price": "&pound;150 &middot; &pound;170 &middot; &pound;185",
         "ld_price": "150", "sub": "One, two or three areas",
         "body": "Using only FDA approved toxins, you can feel safe in the knowledge that our wrinkle-reducing injections are industry leading products. Relaxing the muscles reduces movement and softens lines and wrinkles. Every patient receives a thorough consultation and leaves with a solid understanding of their treatment, aftercare and what to expect. The procedure takes roughly 30 minutes with no downtime &mdash; you can return to work the same day. Our injector is highly experienced and has practised in the field for many years."},
        {"name": "Polynucleotides", "price": "from &pound;100", "ld_price": "100", "sub": "Salmon DNA rejuvenation",
         "body": "We offer a range of polynucleotide options and bespoke these to your needs and concerns. The rejuvenating properties of salmon DNA are considerable. These treatments are trending as a result of their success, but we have offered them here for over three years &mdash; we pride ourselves on being completely up to date with skin advancements, and are almost always the first to offer them."},
        {"name": "Profhilo", "price": "&pound;200", "ld_price": "200", "sub": "Skin booster",
         "body": "Arguably the best skin boosting treatment on the market. Tiny injections of hyaluronic acid in the surface layers of the skin, intended to treat fine lines, skin laxity, elasticity and firmness. Two treatments are required and results typically last between six and nine months. Ideal for the face, neck, d&eacute;collet&eacute; and hands. Pain free, with no downtime."},
        {"name": "Jalupro", "price": "&pound;125", "ld_price": "125", "sub": "Dermal biorevitaliser",
         "body": "This skin booster acts as a dermal biorevitaliser, using a combination of hyaluronic acid and amino acids to improve skin texture and the first signs of ageing or skin damage. With no downtime involved, this is a perfect lunchtime refresher."},
        {"name": "Lumi Eyes", "price": "&pound;90", "ld_price": "90", "sub": "Under-eye booster",
         "body": "A skin booster just for the under-eye area. With its dermal filler mimicking properties, this treatment offers the benefits of tear trough filler but without the risks. Lumi Eyes helps to alleviate hollow eyes and reduce the appearance of dark circles and wrinkles. Around 30 minutes, and completely comfortable."},
        {"name": "Sunekos", "price": "&pound;200", "ld_price": "200", "sub": "Targeted rejuvenation",
         "body": "Similar to Jalupro, this skin booster can be used in targeted areas around the face and body to help alleviate the signs of ageing. Great when coupled with anti-wrinkle injections for clients who have deeper, static lines."},
        {"name": "Plasma Pen", "price": "&pound;200", "ld_price": "200", "sub": "Upper eyelids only",
         "body": "This revolutionary treatment is a catalyst for collagen production, and is one of the only treatments available that is safe to treat the upper eyelids outside of surgery. It helps to tighten the skin, reduce the appearance of fine lines and wrinkles, and can help to lift the eyelid area."},
    ]
    treatment_page(
        "aesthetic-treatments.html", "Aesthetic Treatments", "Aesthetic Treatments",
        "Anti-Wrinkle Injections &amp; Skin Boosters, Beverley",
        "Aesthetic treatments in Beverley: anti-wrinkle injections from £150, Profhilo £200, "
        "polynucleotides from £100, Jalupro, Lumi Eyes, Sunekos and Plasma Pen. Experienced injector, "
        "full consultation included.",
        "Injectable treatments delivered by a highly experienced injector, always after a thorough "
        "consultation. Prices are per session.",
        items, hero_image=IMG["gift"])


def build_laser():
    cards = rate_cards([
        {"title": "Face &amp; Neck", "note": "Course of 6",
         "rows": [("Upper lip", "&pound;175"), ("Chin", "&pound;175"), ("Cheeks", "&pound;300"),
                  ("Male beard", "&pound;500"), ("Centre brow", "&pound;150"), ("Neck", "&pound;300"),
                  ("Top-ups &amp; single sessions", "from &pound;29")]},
        {"title": "Legs &amp; Arms", "note": "Course of 6",
         "rows": [("Half leg", "&pound;400"), ("Three-quarter leg", "&pound;500"), ("Full leg", "&pound;650"),
                  ("Feet &amp; toes", "&pound;300"), ("Underarms", "&pound;225"), ("Half arms", "&pound;300"),
                  ("Full arms", "&pound;380"), ("Top-ups &amp; single sessions", "from &pound;37.50")]},
        {"title": "Body", "note": "Course of 6",
         "rows": [("Basic bikini", "&pound;320"), ("Hollywood bikini", "&pound;400"),
                  ("Centre line buttocks", "&pound;350"), ("Buttocks", "&pound;400"),
                  ("Buttocks with centre line", "&pound;550"), ("Chest", "&pound;350"),
                  ("Chest &amp; abdomen", "&pound;700"), ("Abdomen", "&pound;400"),
                  ("Full back", "&pound;700"), ("Lower back", "&pound;450")]},
        {"title": "Offers", "note": "Course of 6",
         "rows": [("Underarms", "&pound;225"), ("Half leg", "&pound;350"),
                  ("Bikini, underarm &amp; half leg", "&pound;585")]},
    ])

    body = section(
        heading_block("Laser Hair Removal",
                      "Laser hair removal is the most effective method of hair removal. Unlike shaving and "
                      "waxing, laser treatments offer long-lasting, more permanent results.",
                      eyebrow="Treatments", width=9) + """
        <div class="row justify-content-center mb-5">
          <div class="col-lg-9 ftco-animate">
            <p>As proud members of the <strong>British Medical Laser Association</strong>, we are highly qualified and highly experienced practitioners who endeavour to follow licensing requirements and professional standards.</p>
            <p>We use the strongest triple wavelength diode laser available to tackle hair reduction, ensuring maximum efficiency and safety for all skin types. Laser hair removal uses light energy to damage and destroy active, individual hair follicles. Treatments are quick and comfortable &mdash; you can expect to feel some warmth, but our Ice Laser has its own cooling system so surface tissue stays cool while the laser works deep within the follicle.</p>
          </div>
        </div>
""" + cards)

    body += section(
        heading_block("How many sessions will I need?", eyebrow="What to expect", width=9) + """
        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <div class="faq-item mb-4">
              <h3>How many treatments does it take?</h3>
              <p>The number of sessions needed depends on your skin tone and hair thickness. On average patients need between 8 and 12 treatments to optimise the permanency of the hair removal. Results do vary &mdash; some people see results after a single session, others not until treatment three or four.</p>
            </div>
            <div class="faq-item mb-4">
              <h3>How far apart are appointments?</h3>
              <p>Appointments are usually spaced four to six weeks apart, depending on the treatment area and your individual response to the laser. It is important for your clinician to monitor your hair growth cycle during the course, to make sure the follicles are active at the time of treatment.</p>
            </div>
            <div class="faq-item mb-4">
              <h3>Do I need a patch test?</h3>
              <p>Yes. A patch test is always required before a course of laser treatments begins.</p>
            </div>
            <div class="faq-item">
              <h3>Is it safe for my skin type?</h3>
              <p>Our triple wavelength diode laser is suitable for all skin types, and every course starts with a consultation and patch test so your practitioner can set the correct parameters for you.</p>
            </div>
          </div>
        </div>""", cls="ftco-section bg-champagne")

    body += section(CONSULT_NOTE, cls="ftco-section bg-light")
    body += treatment_cta("Book a patch test and consultation")

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How many laser hair removal treatments will I need?",
             "acceptedAnswer": {"@type": "Answer", "text": "On average patients need between 8 and 12 treatments to optimise the permanency of the hair removal. Results vary — some people see results after one session, others not until treatment three or four."}},
            {"@type": "Question", "name": "How far apart are laser hair removal appointments?",
             "acceptedAnswer": {"@type": "Answer", "text": "Appointments are usually spaced four to six weeks apart, depending on the treatment area and individual response to the laser."}},
            {"@type": "Question", "name": "Do I need a patch test before laser hair removal?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. A patch test is always required before a course of laser treatments begins."}},
        ],
    }

    offers = [{"name": "Laser hair removal, course of 6 (upper lip)", "price": "175"},
              {"name": "Laser hair removal, course of 6 (underarms)", "price": "225"},
              {"name": "Laser hair removal, single session", "price": "29"}]

    add("laser-hair-removal.html",
        "Laser Hair Removal Beverley &amp; Hessle | BMLA Members",
        "Laser hair removal in Beverley and Hessle using the strongest triple wavelength diode laser, "
        "safe for all skin types. Courses of six from £150. British Medical Laser Association members.",
        "Laser Hair Removal",
        body,
        breadcrumb=[("Treatments", "treatments.html"), ("Laser Hair Removal", "laser-hair-removal.html")],
        hero_image=IMG["flatlay"],
        ld_extra=[service_ld("Laser Hair Removal",
                             "Triple wavelength diode laser hair removal in Beverley and Hessle, East Yorkshire.",
                             offers, "laser-hair-removal.html"), faq_ld])


def build_fat_loss():
    items = [
        {"name": "Cryolipolysis &mdash; Fat Freezing", "price": "Small &pound;100 &middot; Large &pound;140",
         "ld_price": "100", "sub": "Award-winning 3D Lipo",
         "body": "Fat cells are targeted using a combination of electro and cryo technology. Fat pockets are lifted using a vacuum and the fat cells are crystallised, leading to apoptosis &mdash; localised cell death &mdash; as the cells cannot survive the controlled, frozen temperature. The body then disposes of them naturally as waste. Non-invasive, pain-free and completely comfortable, with up to 20&ndash;40% fat loss in the targeted area. Small area covers one cup (upper abdomen, lower abdomen, bingo wings, chin); large area covers two cups (inside or outside thigh, back of thigh, love handles, back fat, upper and lower abdomen)."},
        {"name": "The Power Hour", "price": "from &pound;170", "ld_price": "170", "sub": "Signature fat loss hour",
         "body": "Fat freezing coupled with the Slim Suit and oxygen therapy treatments &mdash; the treatment of all treatments when it comes to non-surgical liposuction."},
        {"name": "The Blitz", "price": "60 min &pound;100 &middot; 90 min &pound;140", "ld_price": "100",
         "sub": "Multidimensional fat reduction",
         "body": "A bespoke fat reduction treatment for the area of your concern. The Blitz uses the full range of 3D Lipo fat reducing and skin tightening technologies, targeting fat cells from a multitude of angles to maximise inch loss."},
        {"name": "4 Month Fat Loss Program", "price": "&pound;150 deposit + &pound;150 &times; 4",
         "ld_price": "150", "sub": "Almost &pound;1,000 worth of treatments",
         "body": "Four months of bespoke fat loss treatments ranging from fat freezing and cavitation therapy to radio frequency and shockwave sessions. Includes a consultation, before and after pictures and nine bespoke treatments using award-winning technology."},
        {"name": "The Slim Suit", "price": "&pound;150", "ld_price": "150", "sub": "Gold standard fat loss",
         "body": "Radio frequency fat melting, skin tightening, cavitation therapy and a pressotherapy slim suit are used in unison with oxygen therapy. By destroying the fat cells in this multimodal way, they can be removed from the body in an accelerated manner using lymphatic drainage and oxygen therapy &mdash; both scientifically proven to remove fat from the body quickly."},
        {"name": "Bioslimming Fat Loss Wraps", "price": "from &pound;85", "ld_price": "85",
         "sub": "Patented formula",
         "body": "Using patented formulas backed by over 3,000 trials proving they remove fat and not water. Incorporating radio frequency, vacuum and pressotherapy technology, this is a great option when preparing for a holiday or event."},
        {"name": "Chin Contour", "price": "from &pound;90", "ld_price": "90", "sub": "Jawline definition",
         "body": "Using a delicate method of clinically backed techniques we can contour the chin, remove fat and tighten the area."},
        {"name": "Lemon Bottle Fat Dissolve Injections", "price": "1 bottle from &pound;100 &middot; 4 from &pound;250",
         "ld_price": "100", "sub": "Injectable fat dissolving",
         "body": "Melting the fat into a liquid state using our state of the art technology, coupled with Lemon Bottle injections, is what sets our treatments apart &mdash; and the results speak for themselves."},
        {"name": "Aqualyx Fat Dissolving Injections", "price": "from &pound;85", "ld_price": "85",
         "sub": "Enzyme fat dissolving",
         "body": "The procedure involves injecting a naturally occurring fat-digesting enzyme into a pocket of fat. The enzyme breaks down the fatty acids from within the fat cell, and the fat is then released from the body in the form of urine."},
        {"name": "Cellulite Reduction Taster Course", "price": "&pound;300 for 3", "ld_price": "300",
         "sub": "Shockwave therapy",
         "body": "Shockwave therapy is a clinically proven way to improve cellulite and reduce circumference around the legs, waist and arms. It works by emitting radial waves through the skin that stimulate the breakdown of fat, collagen synthesis and lymphatic drainage."},
        {"name": "Cellulite &amp; Silhouette Program", "price": "&pound;670 course of 8", "ld_price": "670",
         "sub": "Saving &pound;90, or &pound;200 deposit &amp; &pound;75 per session",
         "body": "Using state of the art technology we can transform your behind."},
        {"name": "Thigh Gap Enhancement", "price": "&pound;95 &middot; course of 8 &pound;630", "ld_price": "95",
         "sub": "Saving &pound;90",
         "body": "This procedure uses medical grade machinery to contour the shape of your thighs. Non-invasive and painless."},
        {"name": "Ultimate Flat Tummy", "price": "&pound;95 &middot; course of 8 &pound;630", "ld_price": "95",
         "sub": "Saving &pound;90",
         "body": "Medical grade technology and a range of suitable techniques to beat the bloat, help with sagging skin, tighten the stomach area and remove stubborn fat. A perfect, non-invasive answer to any &lsquo;mummy tummy&rsquo; concerns."},
        {"name": "Bingo Wing Treatments", "price": "&pound;80 &middot; course of 8 &pound;560", "ld_price": "80",
         "sub": "Saving &pound;80",
         "body": "This procedure uses medical grade machinery to contour the shape of your arms. Non-invasive."},
        {"name": "Radio Frequency Skin Tightening", "price": "from &pound;75", "ld_price": "75",
         "sub": "Face or body",
         "body": "A non-surgical, non-invasive method of tightening your skin. With ageing, elastin proteins and collagen begin to wear down, causing wrinkles, fine lines and sagging. RF sends radio waves to selectively target and heat the deep layer of your skin, causing an immediate contraction of the collagen fibres while increasing the metabolism of the fibroblast cells to accelerate the production of elastin and collagen."},
    ]

    contra = section(
        heading_block("Am I a candidate for fat loss treatments?",
                      "The following conditions prevent treatment with all of our non-surgical liposuction "
                      "treatments. If you are unsure, please raise it at consultation &mdash; some conditions "
                      "need individual advice rather than an outright no.",
                      eyebrow="Safety first", width=9) + """
        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <ul class="contra-list">
              <li>Pregnancy or breastfeeding</li>
              <li>Vascular diseases</li>
              <li>Pacemakers</li>
              <li>Thrombosis or thrombophlebitis</li>
              <li>Heart conditions</li>
              <li>Prescribed anti-coagulant (blood thinner) medications</li>
              <li>Steroid medications</li>
              <li>Low or high blood pressure medicines &mdash; seek advice</li>
              <li>Transplant patients</li>
              <li>Cancer patients</li>
              <li>Tumours</li>
              <li>Users of large metal prosthetics &mdash; seek advice</li>
              <li>Diabetes</li>
              <li>Epilepsy</li>
            </ul>
          </div>
        </div>""", cls="ftco-section bg-champagne")

    treatment_page(
        "fat-loss.html", "Fat Loss &amp; Non-Surgical Lipo",
        "Fat Loss &amp; Non-Surgical Liposuction",
        "Fat Freezing &amp; Non-Surgical Liposuction, Beverley",
        "Non-surgical liposuction in Beverley: cryolipolysis fat freezing from £100, cavitation, "
        "shockwave cellulite therapy, the Slim Suit, radio frequency skin tightening and fat dissolving "
        "injections. Clinically validated 3D Lipo technology.",
        "Using the best medical grade technology in the industry, we offer a range of fat reducing methods "
        "that are clinically validated and scientifically supported.",
        items, hero_image=IMG["ba_body"], extra_bottom=contra,
        ld_name="Non-Surgical Liposuction and Fat Loss")


def build_body_wellness():
    items = [
        {"name": "Pressotherapy", "price": "&pound;70", "ld_price": "70", "sub": "Advanced lymphatic drainage",
         "body": "Our pressotherapy treatment is an advanced form of lymphatic drainage massage. The suit uses specially designed garments that gently inflate to precise, pre-set pressures &mdash; often described as having a team of massage therapists working on the body simultaneously to flush out excess fluid, toxins and metabolic waste. As relaxing as it is, it is the workout equivalent of 20 minutes of intense treadmill activity."},
        {"name": "Lymphatic Drainage Massage", "price": "&pound;80", "ld_price": "80", "sub": "60 minutes, full body",
         "body": "Our full body, 60 minute manual lymphatic drainage massage is customised entirely to you. As we are trained in a number of different drainage and massage techniques, we can design this treatment around your goals. The traditional Vodder method can be used alongside the F&ouml;ldi method to encourage drainage and expel toxins. Wood therapy and Brazilian lymphatic massage techniques can also be used for those wanting more body contouring."},
        {"name": "Wood Therapy Massage", "price": "&pound;90", "ld_price": "90", "sub": "60 minutes, contouring",
         "body": "This 60 minute treatment focuses on body contouring alongside lymphatic drainage, using a range of wooden apparatus to sculpt and define your natural contours. A great pre-event treatment."},
        {"name": "Menopause Massage", "price": "&pound;75", "ld_price": "75", "sub": "Hormonal support",
         "body": "Help yourself to feel lighter, less sluggish, less bloated and more relaxed, with a massage aimed at alleviating some of the discomfort associated with hormonal changes."},
        {"name": "Post-Op Massage", "sub": "Recovery focused",
         "body": "This treatment focuses on healing. Using gentle drainage techniques with red light and oxygen therapy, together with our PEMF mat, you can expect to relax while you recover."},
        {"name": "Body Wraps", "sub": "Total detox",
         "body": "Starting on our vibration plate, we then use castor oil and/or magnesium in conjunction with our PEMF infrared sauna dome &mdash; you can expect to burn up to 300 calories within 30 minutes. This treatment helps remove toxins from the body and helps to ground and re-centre, while being totally relaxing."},
        {"name": "Oxygen Therapy", "price": "&pound;45", "ld_price": "45", "sub": "90%+ oxygen LED dome",
         "body": "Elevate your wellness and deepen cellular activation using our 90%+ oxygen LED light dome. A fantastic option for avid exercisers, or anyone struggling with persistent illness, lack of energy or dull skin &mdash; and a great addition to fat loss treatments. Studies show that breathing a higher concentration of oxygen increases the amount of fat exhaled from the body."},
        {"name": "Vitamin Injections", "price": "B12 &pound;25 &middot; Vit D &pound;30 &middot; Biotin &pound;30 &middot; Glutathione &pound;40",
         "ld_price": "25", "sub": "Directly into the bloodstream",
         "body": "We only offer vitamin injections for vitamins that can be stored in the body and are better absorbed when administered directly into the bloodstream. We understand vitamin interaction and are vastly experienced in the field."},
    ]
    treatment_page(
        "body-wellness.html", "Body &amp; Wellness", "Body &amp; Wellness Treatments",
        "Lymphatic Drainage &amp; Wellness Treatments, Beverley",
        "Wellness treatments in Beverley: manual lymphatic drainage £80, pressotherapy £70, wood therapy, "
        "menopause and post-op massage, oxygen therapy £45 and vitamin injections from £25.",
        "Drainage, recovery and wellness treatments designed to support your body from the inside out.",
        items, hero_image=IMG["products"], ld_name="Lymphatic Drainage and Wellness Treatments")


def build_packages():
    items = [
        {"name": "Acne &amp; Blemish Prone Skin", "price": "&pound;125 &times; 4 months", "ld_price": "125",
         "sub": "Over &pound;950 of skincare and treatments",
         "body": "Medical grade products combined with award-winning supplements for a 100% skincare regime that treats the skin as a whole. Our skin is the largest organ in the body, so it is not enough to treat such a vast matrix from the outside alone with serums and creams. This package takes a holistic approach to your skin's health from home and includes a total of six professional treatments. Saving over &pound;300."},
        {"name": "Rejuvenation &amp; Ageing", "price": "&pound;135 &times; 4 months", "ld_price": "135",
         "sub": "Collagen support inside and out",
         "body": "Four months' supply of a bioavailable, award-winning collagen powder, along with hydrating and rejuvenating supplements clinically proven to enhance skin cell regeneration. The programme includes six professional treatments that specifically target your own collagen production and help alleviate fine lines, skin laxity and uneven tone, plus a choice of medical grade skincare."},
        {"name": "Pigmentation &amp; Uneven Skin Tone", "price": "&pound;125 &times; 4 months", "ld_price": "125",
         "sub": "Inside-out pigment control",
         "body": "Treating discolouration and skin tone from the inside out has proven to be an effective treatment for pigmentation. Includes four months' supply of vital supplements that are triple tested and organically sourced, six professional treatments and an award-winning, prescriptive skincare serum."},
        {"name": "Psoriasis", "price": "&pound;120 &times; 4 months", "ld_price": "120",
         "sub": "Consistent, dual approach",
         "body": "Psoriasis symptoms can be dramatically reduced with a consistent approach that tackles the condition from the inside and the outside. Includes four months of award-winning, organic supplements, a prescriptive topical cream, an intensive course of medically certified treatments and a skin consultation."},
        {"name": "Eczema", "price": "&pound;120 &times; 4 months", "ld_price": "120",
         "sub": "Hydration from within",
         "body": "Designed to help hydrate the skin from the inside out. Includes four months of award-winning, organic supplements, a prescriptive topical cream, a course of medical grade treatments and a skin consultation."},
        {"name": "Pregnancy", "price": "&pound;60 &times; 4 months + deposit", "ld_price": "60",
         "sub": "Safe in pregnancy and postpartum",
         "body": "Our skin undergoes a variety of changes during this special time, and it can be very difficult to navigate what skincare you can and cannot use. This package takes the stress out of pregnancy skincare and nourishes your skin from within, which can reduce your risk of stretch marks, loose skin and pigmentation changes. Also safe postpartum for anyone breastfeeding, with skincare and baby-safe supplements that are triple tested."},
    ]
    extra = section("""        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <div class="notice">
              <h3>How the packages work</h3>
              <p>All packages include a professional skin consultation and an opening deposit, which is deducted from the total cost of the package &mdash; meaning your monthly repayments are reduced.</p>
              <p>Our skin is the last of our organs to receive any nutrients, so we often see skin problems arise from a range of nutritional deficiencies. Treating those concerns with creams and serums alone will never be enough &mdash; which is why every package works on the skin internally and externally.</p>
            </div>
          </div>
        </div>""", cls="ftco-section bg-champagne")

    treatment_page(
        "skin-health-packages.html", "Skin Health Packages", "Skin Health Packages",
        "Skin Health Packages | Acne, Ageing &amp; Pigmentation Plans",
        "Four-month skin health partnership packages in Beverley from £60 per month. Acne, rejuvenation, "
        "pigmentation, psoriasis, eczema and pregnancy plans combining supplements, medical grade skincare "
        "and six professional treatments.",
        "Our expertly curated skin partnership packages are designed to treat the skin both internally and "
        "externally &mdash; making sure your skin works optimally from the inside and glows on the outside.",
        items, hero_image=IMG["flatlay"], extra_top=extra, ld_name="Skin Health Packages")


def build_skincare():
    body = section(intro_split(
        IMG["gift"], "AlumierMD medical grade skincare products at the clinic",
        "Medical grade skincare, prescribed properly",
        ["Peptides? Retinol? Antioxidants? We know it can be a bit of a minefield out there &mdash; knowing "
         "which skin treatment to have and which skincare to actually use.",
         "We only offer results-orientated, medical grade skincare regimes that use corrective and "
         "preventative active ingredients. Your regime is prescribed after an in-depth consultation, so it "
         "targets the root of your concern rather than the symptom &mdash; and so you understand what every "
         "product in it is doing.",
         "Professional treatments and homecare work together. A course of peels or microneedling will always "
         "give a better, longer-lasting result when it is supported by the right actives at home."]))

    body += section(
        heading_block("Register for AlumierMD",
                      "AlumierMD is a professional, prescription-strength skincare range only available "
                      "through registered clinics. Register with us and your products are matched to the "
                      "regime we build for you.",
                      eyebrow="Prescriptive skincare", width=9) + """
        <div class="row justify-content-center">
          <div class="col-lg-9 text-center ftco-animate">
            <p><a href="https://www.alumiermd.co.uk/register" target="_blank" rel="noopener" class="btn btn-primary py-3 px-4">Register with AlumierMD</a></p>
            <p class="mt-3" style="font-size:15px;color:#8a8078;">Not sure which regime is right for you? Book a skin consultation and we will build one around your skin, your budget and your routine.</p>
          </div>
        </div>""", cls="ftco-section bg-champagne")

    body += section(CONSULT_NOTE, cls="ftco-section bg-light")
    body += treatment_cta("Book a skincare consultation")

    add("medical-grade-skincare.html",
        "Medical Grade Skincare &amp; AlumierMD, Beverley",
        "Prescriptive medical grade skincare in Beverley. Results-orientated regimes built on corrective "
        "and preventative active ingredients, prescribed after an in-depth skin consultation. "
        "AlumierMD stockist.",
        "Medical Grade Skincare",
        body,
        breadcrumb=[("Treatments", "treatments.html"), ("Medical Grade Skincare", "medical-grade-skincare.html")],
        hero_image=IMG["gift"],
        ld_extra=service_ld("Medical Grade Skincare Consultation",
                            "Prescriptive medical grade skincare regimes in Beverley, East Yorkshire.",
                            None, "medical-grade-skincare.html"))


# ==========================================================================
# Gallery
# ==========================================================================
def build_gallery():
    tiles = [
        (IMG["ba_skin"], "Before and after: skin texture, congestion and breakout results at Skin, Slim &amp; Laser Solutions Beverley",
         "Skin clarity and texture &mdash; results from a course of advanced skin treatments."),
        (IMG["ba_body"], "Before and after: cellulite and body contouring results at Skin, Slim &amp; Laser Solutions",
         "Cellulite and silhouette &mdash; results from a course of body contouring treatments."),
        (IMG["ba_extra"], "Treatment results at the Beverley skin clinic",
         "Client results from the clinic."),
        (IMG["treatment"], "Advanced skin practitioner delivering a facial treatment in Beverley",
         "In the treatment room at Walkergate Wellness, Beverley."),
        (IMG["menu"], "The Refresh, Renew and Rewind facial menu",
         "Our signature facial menu: The Refresh, The Renew and The Rewind."),
        (IMG["flatlay"], "The Cahaya Skin Clinic gift styling with AlumierMD products and collagen shots",
         "Gift sets and homecare, with AlumierMD and collagen support."),
        (IMG["gift"], "Clinic product and gift packaging",
         "Prescriptive homecare, packaged for gifting."),
        (IMG["products"], "Medical grade skincare products stocked at the clinic",
         "Medical grade skincare stocked in clinic."),
    ]
    grid = "\n".join(
        """            <figure class="ba-tile ftco-animate">
              <img src="%s" alt="%s" loading="lazy">
              <figcaption>%s</figcaption>
            </figure>""" % (src, alt, cap) for src, alt, cap in tiles)

    body = section(
        heading_block("Results, treatments and the clinic",
                      "Real client results and a look inside the clinic. Every before and after is shared "
                      "with the client's permission. Individual results vary &mdash; your practitioner will "
                      "give you a realistic expectation at consultation.",
                      eyebrow="Gallery", width=9) + """
        <div class="row">
          <div class="col-12">
            <div class="ba-grid">
%s
            </div>
          </div>
        </div>""" % grid)

    body += """    <section class="ftco-section bg-champagne">
      <div class="container">
        <div class="row justify-content-center text-center">
          <div class="col-lg-8 ftco-animate">
            <h2 class="mb-3">More on Instagram</h2>
            <p class="mb-4">We post new results, offers and treatment explainers regularly.</p>
            <p><a href="{ig}" target="_blank" rel="noopener" class="btn btn-primary py-3 px-4">Follow {handle}</a></p>
          </div>
        </div>
      </div>
    </section>

""".format(ig=INSTAGRAM, handle=IG_HANDLE)

    add("gallery.html",
        "Gallery | Before &amp; After Results, Beverley Skin Clinic",
        "Before and after results from Skin, Slim & Laser Solutions in Beverley — skin treatments, "
        "body contouring and cellulite reduction, plus a look inside the clinic.",
        "Gallery",
        body,
        breadcrumb=[("Gallery", "gallery.html")],
        hero_compact=True)


# ==========================================================================
# Contact
# ==========================================================================
CONTACT_FAQ = [
    ("How do I book an appointment?",
     "Beverley appointments can be booked online through our booking system. For Hessle, "
     "please email or call us to arrange an appointment. We are strictly an appointment-only clinic."),
    ("How quickly will you reply?",
     "If you have not heard back from us within five working days, please email us directly at "
     "info@thecahayaskinclinic.co.uk."),
    ("What is your cancellation policy?",
     "Cancellations within five days will incur a £40 fee. During school holidays and December, all "
     "cancellations incur a £40 fee or a £25 rescheduling sum. We hate having to charge these fees — "
     "please see our socials to understand why they are necessary."),
    ("Where do I park in Beverley?",
     "Parking is available at Tesco. The back of our Grade II listed building is directly opposite Tesco. "
     "Follow the footpath around and you will find our black front door, opposite Dog & Duck Lane. Use the "
     "intercom, select Skin & Slim, then the bell — reception is on the first floor."),
    ("Do I need a consultation first?",
     "Yes. Every treatment plan starts with an in-depth consultation so we can assess your skin, explain "
     "your options honestly and make sure the treatment is safe and suitable for you."),
]


def build_contact():
    faq_html = "\n".join(
        """          <div class="col-md-6 ftco-animate mb-4">
            <div class="faq-item">
              <h3>%s</h3>
              <p>%s</p>
            </div>
          </div>""" % (q, a.replace("&", "&amp;").replace("£", "&pound;")) for q, a in CONTACT_FAQ)

    body = """    <section class="ftco-section contact-section">
      <div class="container">
        <div class="row block-9">
          <div class="col-md-5 contact-info ftco-animate">
            <div class="row">
              <div class="col-md-12 mb-4">
                <h2 class="h4">Contact &amp; booking</h2>
                <p>Please get in touch to book an appointment or to discuss your treatment options. Our online booking system for Beverley is linked below. For Hessle, please email to arrange an appointment.</p>
              </div>
              <div class="col-md-12 mb-3">
                <p><span>Phone:</span> <a href="tel:{tel}" data-book="contact-call">{phone}</a></p>
              </div>
              <div class="col-md-12 mb-3">
                <p><span>Email:</span> <a href="mailto:{email}" style="word-break:break-all;">{email}</a></p>
              </div>
              <div class="col-md-12 mb-3">
                <p><span>Instagram:</span> <a href="{ig}" target="_blank" rel="noopener">{handle}</a></p>
              </div>
              <div class="col-md-12 mb-4">
                <p><span>Booking:</span> Beverley online, or enquire for Hessle</p>
              </div>
              <div class="col-md-12">
                <p>
                  <a href="{booking}" target="_blank" rel="noopener" class="btn btn-primary py-3 px-4 mb-2" data-book="contact-primary">Book Beverley Online</a>
                </p>
                <p style="font-size:14.5px;color:#8a8078;">Gift vouchers are available &mdash; <a href="#enquiry">send us an enquiry</a> or call the clinic and we will sort one out for you.</p>
              </div>
            </div>
          </div>
          <div class="col-md-1"></div>
          <div class="col-md-6 ftco-animate">
            <h2 class="h4 mb-4">Send us a message</h2>
            <form id="enquiry" class="contact-form" novalidate>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label class="sr-only" for="cf-name">Your name</label>
                    <input id="cf-name" name="name" type="text" class="form-control" placeholder="Your name" required>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label class="sr-only" for="cf-email">Your email</label>
                    <input id="cf-email" name="email" type="email" class="form-control" placeholder="Your email" required>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label class="sr-only" for="cf-phone">Phone</label>
                    <input id="cf-phone" name="phone" type="tel" class="form-control" placeholder="Phone (optional)">
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <label class="sr-only" for="cf-clinic">Preferred clinic</label>
                    <select id="cf-clinic" name="clinic" class="form-control" required>
                      <option value="">Preferred clinic</option>
                      <option>Beverley</option>
                      <option>Hessle</option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="form-group">
                <label class="sr-only" for="cf-service">What are you interested in?</label>
                <select id="cf-service" name="service" class="form-control" required>
                  <option value="">What are you interested in?</option>
                  <option>Skin consultation</option>
                  <option>Facials</option>
                  <option>Chemical peels</option>
                  <option>Advanced skin treatments / microneedling</option>
                  <option>Non-surgical lifting / CACI</option>
                  <option>Aesthetic treatments</option>
                  <option>Laser hair removal</option>
                  <option>Fat loss / non-surgical liposuction</option>
                  <option>Body &amp; wellness treatments</option>
                  <option>Skin health packages</option>
                  <option>Gift voucher</option>
                  <option>Something else</option>
                </select>
              </div>
              <div class="form-group">
                <label class="sr-only" for="cf-msg">Message</label>
                <textarea id="cf-msg" name="message" cols="30" rows="6" class="form-control" placeholder="Tell us about your skin or your goal, and which days suit you best&hellip;" required></textarea>
              </div>
              <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="cf-consent" name="consent" required>
                <label class="form-check-label" for="cf-consent" style="font-size:14px;color:#8a8078;">I have read the <a href="privacy-policy.html">privacy policy</a> and understand the information provided will be used in accordance with it.</label>
              </div>
              <div class="form-group">
                <input type="submit" value="Send message" class="btn btn-primary py-3 px-5">
              </div>
              <p id="cf-status" role="status" aria-live="polite" class="mt-3 mb-0" style="display:none;font-size:15px;"></p>
            </form>
          </div>
        </div>
      </div>
    </section>

""".format(tel=TEL, phone=PHONE, email=EMAIL, ig=INSTAGRAM, handle=IG_HANDLE, booking=BOOKING)

    body += section(
        heading_block("Our clinics", "Strictly appointment only.", eyebrow="Where to find us") + "\n"
        + location_cards(show_notes=True), cls="ftco-section bg-light")

    body += section("""        <div class="row justify-content-center">
          <div class="col-lg-9 ftco-animate">
            <div class="notice">
              <h3>Cancellation policy</h3>
              <p>Cancellations within five days will incur a &pound;40.00 fee. During school holidays and December, all cancellations will incur a &pound;40.00 fee or a &pound;25.00 rescheduling sum.</p>
              <p>Please be assured that we hate to charge such fees. Please see our <a href="%s" target="_blank" rel="noopener">socials</a> to help understand why they are necessary.</p>
            </div>
          </div>
        </div>""" % INSTAGRAM)

    body += section(
        heading_block("Before you book", eyebrow="Questions") + "\n"
        + '        <div class="row">\n%s\n        </div>' % faq_html,
        cls="ftco-section bg-champagne")

    body += """    <!-- Swap the src below for the clinic's Google Maps embed URL to show a live map. -->
    <iframe title="Skin, Slim &amp; Laser Solutions, Walkergate House, Beverley HU17 9ER"
      src="https://www.google.com/maps?q=Walkergate+House,+Walkergate,+Beverley+HU17+9ER&output=embed"
      width="100%" height="420" style="border:0; display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

"""

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in CONTACT_FAQ
        ],
    }

    add("contact.html",
        "Contact &amp; Booking | Beverley &amp; Hessle",
        "Book your appointment at Skin, Slim & Laser Solutions. Online booking for Beverley, email for "
        "Hessle. Call 07479 686312 or email info@thecahayaskinclinic.co.uk.",
        "Contact &amp; Booking",
        body,
        breadcrumb=[("Contact", "contact.html")],
        ld_extra=faq_ld,
        cta=False)


# ==========================================================================
# Policies
# ==========================================================================
def policy_page(slug, title, h1, description, sections):
    inner = ['        <div class="row justify-content-center">',
             '          <div class="col-lg-9 ftco-animate">']
    for hd, paras in sections:
        if hd:
            inner.append('            <h2 class="h4 mt-5 mb-3">%s</h2>' % hd)
        for p in paras:
            inner.append('            %s' % p)
    inner += ['          </div>', '        </div>']
    body = section("\n".join(inner))
    add(slug, title, description, h1, body,
        breadcrumb=[(h1, slug)], cta=False, robots="noindex, follow", hero_compact=True)


def build_policies():
    updated = datetime.date.today().strftime("%d %B %Y")
    policy_page(
        "privacy-policy.html",
        "Privacy Policy | Skin, Slim &amp; Laser Solutions",
        "Privacy Policy",
        "How Skin, Slim & Laser Solutions collects, uses and protects your personal and health "
        "information under UK GDPR.",
        [
            (None, ["<p><em>Last updated %s. This policy should be reviewed by the clinic before "
                    "publication to confirm it reflects current practice, particularly around clinical "
                    "record retention and any third-party booking or payment providers used.</em></p>" % updated]),
            ("Who we are", [
                "<p>Skin, Slim &amp; Laser Solutions (%s) operates clinics in Beverley and Hessle, "
                "East Yorkshire. We are the data controller for the personal information "
                "described in this policy. You can contact us at <a href=\"mailto:%s\">%s</a> or on "
                "<a href=\"tel:%s\">%s</a>.</p>" % (FORMERLY, EMAIL, EMAIL, TEL, PHONE)]),
            ("What we collect", [
                "<p>When you use this website we may collect your name, email address, telephone number, "
                "preferred clinic, the treatment you are enquiring about and anything else you choose to "
                "include in your message.</p>",
                "<p>When you become a patient we also collect health information relevant to your "
                "treatment &mdash; your medical history, medications, allergies, skin history, consent "
                "forms and, where you agree to it, before and after photographs. This is special category "
                "data and is handled with additional care.</p>"]),
            ("Why we use it and our lawful basis", [
                "<p>We use your information to respond to enquiries, arrange and deliver appointments, "
                "keep accurate clinical records, meet our insurance and professional obligations, and "
                "take payment. Our lawful bases are your consent (for enquiries and marketing), the "
                "performance of a contract (delivering treatment you have booked), our legal obligations, "
                "and Article 9(2)(h) of the UK GDPR for health data processed for the provision of "
                "treatment by a professional bound by a duty of confidentiality.</p>"]),
            ("Photographs", [
                "<p>Before and after photographs are only taken and only shared publicly with your "
                "explicit, separate written consent. You may withdraw that consent at any time by "
                "contacting us, and we will stop using the images going forward.</p>"]),
            ("Who we share it with", [
                "<p>We do not sell your data. We share it only with service providers who help us run the "
                "clinic &mdash; our booking system, email provider, website host and payment processor "
                "&mdash; and with insurers, regulators or medical professionals where we are legally "
                "required to or where it is necessary for your care.</p>"]),
            ("How long we keep it", [
                "<p>Enquiries that do not become appointments are deleted once they are no longer needed. "
                "Clinical records are retained for the period required by our professional and insurance "
                "obligations, after which they are securely destroyed.</p>"]),
            ("Your rights", [
                "<p>You have the right to access the personal data we hold about you, to have inaccurate "
                "data corrected, to request erasure or restriction of processing, to object to processing, "
                "and to data portability. To exercise any of these, email "
                "<a href=\"mailto:%s\">%s</a>. If you are unhappy with how we have handled your data you "
                "can complain to the Information Commissioner's Office at "
                "<a href=\"https://ico.org.uk\" target=\"_blank\" rel=\"noopener\">ico.org.uk</a>.</p>"
                % (EMAIL, EMAIL)]),
            ("Cookies", [
                "<p>Information about the cookies this site uses is set out in our "
                "<a href=\"cookie-policy.html\">cookie policy</a>.</p>"]),
        ])

    policy_page(
        "cookie-policy.html",
        "Cookie Policy | Skin, Slim &amp; Laser Solutions",
        "Cookie Policy",
        "How Skin, Slim & Laser Solutions uses cookies and similar technologies on this website.",
        [
            (None, ["<p><em>Last updated %s. Review this page whenever analytics, advertising or "
                    "embedded third-party tools are added to the site.</em></p>" % updated]),
            ("What cookies are", [
                "<p>Cookies are small text files placed on your device when you visit a website. They are "
                "used to make a site work, to remember your preferences, and to understand how the site "
                "is being used.</p>"]),
            ("Cookies on this site", [
                "<p><strong>Strictly necessary.</strong> This site is a static website and sets no cookies "
                "of its own in order to function.</p>",
                "<p><strong>Analytics.</strong> If Google Analytics is enabled, it sets cookies that help "
                "us understand how many people visit the site and which pages they use. This data is "
                "aggregated and does not identify you personally. Analytics is disabled until a "
                "measurement ID is configured.</p>",
                "<p><strong>Third-party embeds.</strong> Pages that embed Google Maps, or that link out to "
                "our booking system or Instagram, may result in those providers setting their own cookies. "
                "Their use of cookies is governed by their own policies.</p>"]),
            ("Managing cookies", [
                "<p>You can control and delete cookies through your browser settings. Blocking cookies "
                "will not stop this website from working.</p>"]),
            ("Questions", [
                "<p>If you have any questions about how we use cookies, email "
                "<a href=\"mailto:%s\">%s</a>.</p>" % (EMAIL, EMAIL)]),
        ])


# ==========================================================================
# robots.txt / sitemap.xml
# ==========================================================================
def build_meta_files():
    today = datetime.date.today().isoformat()
    priority = {"index.html": "1.0", "treatments.html": "0.9", "contact.html": "0.9"}
    urls = []
    for slug in BUILT:
        if slug in ("privacy-policy.html", "cookie-policy.html"):
            continue
        loc = "%s/%s" % (ORIGIN, "" if slug == "index.html" else slug)
        urls.append("""  <url>
    <loc>%s</loc>
    <lastmod>%s</lastmod>
    <changefreq>monthly</changefreq>
    <priority>%s</priority>
  </url>""" % (loc, today, priority.get(slug, "0.8")))

    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(HERE, "sitemap.xml"), "w") as fh:
        fh.write(sitemap)

    # robots.txt — DEMO build blocks indexing. Flip Disallow to Allow when this
    # site replaces the live one at thecahayaskinclinic.co.uk.
    with open(os.path.join(HERE, "robots.txt"), "w") as fh:
        fh.write("""# Demo build: indexing is blocked so this preview cannot compete with the
# clinic's live site. When this becomes the live site, delete the Disallow line.
User-agent: *
Disallow: /

Sitemap: %s/sitemap.xml
""" % ORIGIN)

    with open(os.path.join(HERE, "_headers"), "w") as fh:
        fh.write("""# Demo build: remove this block when the site goes live.
/*
  X-Robots-Tag: noindex, nofollow
""")


# ==========================================================================
def main():
    build_home()
    build_about()
    build_treatments()
    build_facials()
    build_advanced()
    build_peels()
    build_lifting()
    build_aesthetics()
    build_laser()
    build_fat_loss()
    build_body_wellness()
    build_packages()
    build_skincare()
    build_gallery()
    build_contact()
    build_policies()
    build_meta_files()
    print("Built %d pages:" % len(BUILT))
    for slug in BUILT:
        print("  " + slug)


if __name__ == "__main__":
    main()
