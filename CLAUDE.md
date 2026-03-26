# Data Consultants - Claude Code Instructies

## 1. Project Overzicht

Portfolio website voor **Data Consultants** (ALTIJD met spatie, NOOIT "DataConsultants").
Focus op data collection, modellering en het koppelen van open databronnen. GeoInzicht is het hoofdproject.

| Eigenschap | Waarde |
|------------|--------|
| **Locatie** | `E:\scripts\webscraper\CBSbuurt\dataconsultants\` |
| **URL** | `http://localhost:8087` |
| **GitHub** | `AnneVersion/dataconsultants` |
| **GitHub Pages** | `anneversion.github.io/dataconsultants` |
| **Type** | Statische website, geen database |
| **Port** | 8087 |

---

## 2. Starten

```bash
python serve.py  # http://localhost:8087
```

**Auto-start via Windows Startup**: `start_server.vbs` in Windows Startup folder start `serve.py` onzichtbaar via `pythonw`.

---

## 3. Branch-strategie

- **main** = stabiel / productie (GitHub Pages)
- **develop** = dagelijkse ontwikkeling (standaard werkbranch)
- **feature/*** = nieuwe features, maak aan vanuit develop

Standaard werkbranch = `develop`. Alleen mergen naar `main` als het stabiel is.

---

## 4. Architectuur

### Bestanden

| Bestand | Beschrijving |
|---------|-------------|
| `index.html` | Hoofdpagina: portfolio website met alle secties |
| `showcase.html` | Cinematic slideshow presentatie van alle projecten |
| `project-geoinzicht.html` | Detail pagina GeoInzicht App |
| `project-vastgoed.html` | Detail pagina Serviced Apartments |
| `project-daw.html` | Detail pagina DAW Platform |
| `project-email.html` | Detail pagina Email Validator |
| `project-astronomy.html` | Detail pagina Astronomy |
| `project-fietsverhuur.html` | Detail pagina Darosa Fietsverhuur |
| `project-meldpunt.html` | Detail pagina Meldpunt Ambtenaren |
| `project-cataract.html` | Detail pagina Cataract |
| `project-dwh.html` | Detail pagina GeoInzicht DWH |
| `project-juridisch.html` | Detail pagina Juridisch Assistent |
| `project-datakwaliteit.html` | Detail pagina Datakwaliteit |
| `sitemap.xml` | XML sitemap voor zoekmachines |
| `robots.txt` | Robots.txt voor crawlers |
| `logo.svg` | Geanimeerd SVG logo: 3D globe met continenten, data-netwerk, zwart gat kern, binaire orbit ring, neon groen (#39ff14) |
| `serve.py` | Python HTTP server met CORS headers, port 8087 |
| `start_server.vbs` | Windows VBScript voor onzichtbare autostart via `pythonw` |
| `README.md` | GitHub readme |
| `CLAUDE.md` | Dit bestand - Claude Code instructies |

### Geen externe bestanden

Alle CSS en JavaScript staat inline in de HTML bestanden. Er zijn geen losse `.css` of `.js` bestanden.

---

## 5. Key Features

### 5.1 Thema & Design

**index.html** (verfijnd donker thema):
- Achtergrond: `--bg: #0f1218`, `--bg2: #131820`, `--bg3: #161b24`
- Accent: `--accent: #39ff14` (neon groen), `--accent2: #C9A96E` (goud)
- Tekst: `--text: #b8b5b0`, `--white: #e8e6e3`
- Font: Verdana, Geneva, Tahoma, sans-serif
- Material Icons Round voor iconen

**showcase.html en project-*.html** (origineel donker + neon groen):
- Achtergrond: `--bg: #0a0f1a` (diep donkerblauw)
- Accent: `--accent: #39ff14` (neon groen)
- Font: Verdana

### 5.2 Favicon

Nederlandse vlag als inline SVG data URI (rood #AE1C28, wit, blauw #21468B). Aanwezig op alle pagina's.

### 5.3 Navigatie (index.html)

Fixed navbar met logo (logo.svg) + "Data Consultants" tekst. Hamburger menu op mobiel (< 768px).

Links: Over Ons | GeoInzicht | Prototypes | Technologie | Visie | Contact | Showcase

Active state highlighting op scroll via IntersectionObserver.

### 5.4 Secties op index.html

1. **Hero** - Logo, titel "Data Consultants", tagline, CTA knop "Open GeoInzicht App" (linkt naar `anneversion.github.io/geoinzicht-app/`)
2. **Wie Wij Zijn** (#over-ons) - Twee kolommen: beschrijvende tekst + databronnen lijst (CBS StatLine, BAG/Kadaster, Politie, Vektis, PDOK)
3. **GeoInzicht** (#geoinzicht) - Vlaggenschip project sectie met:
   - Architectuur pipeline diagram (Brondata -> Staging -> DWH -> Geo Services -> API -> Dashboard)
   - Statistieken tellers met animatie: 14.700+ buurten, 3.475 wijken, 343 gemeenten, 9.7M BAG adressen, 12 jaar trenddata, 16 data domeinen
   - Vergelijking DWH vs App (twee kaarten)
4. **Open Data Prototypes** (#projecten) - Grid met 11 prototype-kaarten. Visietekst over open data voor de gemeenschap, inclusie, maatschappelijke impact, samenwerking met vrouwenorganisaties, geïnspireerd door Rutger Bregman. Alle projecten hebben status "Prototype".
5. **Technologie** (#tech) - Tech stack in 4 categorieen: Data, Geo, Web, DevOps
6. **Open Data Visie** (#visie) - 4 visie kaarten + artikel callout (De Correspondent)
7. **Contact** (#contact) - Email + GitHub links
8. **Footer** - "2026 Data Consultants -- Gebouwd met Claude"

### 5.5 Prototypes Grid (11 prototypes)

Alle projecten zijn nu benoemd als **Prototypes**. Ze gebruiken open data ten behoeve van de gemeenschap, met focus op maatschappelijke impact en inclusie.

| # | Prototype | Status | Tags | Detail pagina | Live link | GitHub |
|---|-----------|--------|------|---------------|-----------|--------|
| 1 | GeoInzicht DWH | Prototype | Python, Flask, PostgreSQL, PostGIS, GeoServer | project-dwh.html | -- | AnneVersion/geoinzicht-dwh |
| 2 | GeoInzicht App | Prototype | JavaScript, HTML/CSS, Leaflet, Chart.js | project-geoinzicht.html | anneversion.github.io/geoinzicht-app | AnneVersion/geoinzicht-app |
| 3 | Serviced Apartments | Prototype | Python, Flask, PostgreSQL, Leaflet, iDEAL | project-vastgoed.html | -- | AnneVersion/vastgoed |
| 4 | DAW Platform | Prototype | Web Audio API, Canvas, Flask, PostgreSQL | project-daw.html | anneversion.github.io/daw | AnneVersion/daw |
| 5 | Email Validator | Prototype | Python, Flask, PostgreSQL, DNS, SMTP | project-email.html | -- | AnneVersion/email-validator |
| 6 | Meldpunt Ambtenaren | Prototype | PWA, Supabase, JavaScript | project-meldpunt.html | anneversion.github.io/meldpunt-ambtenaren | AnneVersion/meldpunt-ambtenaren |
| 7 | Astronomy | Prototype | JavaScript, Canvas, NASA API's | project-astronomy.html | anneversion.github.io/astronomy | AnneVersion/astronomy |
| 8 | Darosa Fietsverhuur | Prototype | Python, Flask, PostgreSQL | project-fietsverhuur.html | anneversion.github.io/darosa-fietsverhuur | AnneVersion/darosa-fietsverhuur |
| 9 | Cataract | Prototype | HTML/CSS, SVG, Medisch | project-cataract.html | anneversion.github.io/cataract | AnneVersion/cataract |
| 10 | Juridisch Assistent | Prototype | Python, Flask, AI, Rechtspraak.nl | project-juridisch.html | -- | AnneVersion/juridisch-assistent |
| 11 | Datakwaliteit | Prototype | Python, PostgreSQL, Great Expectations, dbt | project-datakwaliteit.html | -- | AnneVersion/datakwaliteit |

Status badge: **Prototype** (teal) - alle projecten hebben dezelfde status

### 5.6 Showcase Pagina (showcase.html)

Fullscreen cinematic slideshow met 9 slides:

| Slide | Inhoud | Kleur accent | Animatie |
|-------|--------|-------------|----------|
| 0 - Intro | "Data Consultants" letter-by-letter | #39ff14 | Char-by-char reveal |
| 1 - GeoInzicht | NL kaart met pulserende dots, statistieken tellers | #39ff14 | Animated counters, dot pulse |
| 2 - Serviced Apartments | 3 property cards (Amsterdam, Den Haag, Rotterdam) | #B8860B (goud) | Card slide-in |
| 3 - DAW Platform | Equalizer met 24 animated bars | #4a9eff (blauw) | Bouncing bars |
| 4 - Email Validator | Circulaire score gauge (animatie naar 97/100) | #39ff14 | SVG stroke animation |
| 5 - Astronomy | 3D planeet met orbiting dots | #a855f7 (paars) | Rotating shadows, orbits |
| 6 - Darosa Fietsverhuur | Fiets animatie over road | #0066FF (blauw) | Bike ride animation |
| 7 - Meldpunt Ambtenaren | Pulserende shield/lock SVG | #ef4444 (rood) | Shield pulse glow |
| 8 - Outro | "Gebouwd met Claude" + "Data Consultants" + GitHub link | #39ff14 | Fade-up sequence |

Features:
- Autoplay (6 seconden per slide) met play/pause controls
- Dot navigatie + vorige/volgende knoppen
- Progress bar onderaan
- Letterbox bars (boven en onder)
- Particle canvas achtergrond met muis-interactie
- Keyboard navigatie (pijltjes, spatie)
- Terug-naar-home link linksboven

### 5.7 GeoInzicht App Knop

Hero CTA knop "Open GeoInzicht App" linkt naar `https://anneversion.github.io/geoinzicht-app/` (GitHub Pages versie).

In de showcase linkt slide 1 naar `http://localhost:8091` (lokale versie).

### 5.8 "Gebouwd met Claude" Badge

Aanwezig in:
- Footer van index.html: "2026 Data Consultants -- Gebouwd met Claude"
- Showcase slide 8 (outro): groot weergegeven als afsluitende slide

### 5.9 Logo (logo.svg)

Geanimeerd SVG logo met:
- 3D globe met continenten (Europa, Scandinavie, UK, Ierland, Afrika, Noord-Amerika, Zuid-Amerika, Azie, India, Arabie, Groenland, Madagascar, IJsland, Sri Lanka)
- Data-netwerk mesh over de globe met pulserende groene nodes
- Zwart gat in de kern met accretion disks
- Binaire streams (10110, 01001, etc.) die vanuit de kern stromen
- Twee orbit ringen met ronddraaiende binaire cijfers
- Kleur: #39ff14 (neon groen) op transparante achtergrond

### 5.10 Scroll Animaties

IntersectionObserver-based animaties op index.html:
- `.anim` elementen fade-in bij scroll (opacity 0 -> 1, translateY 20px -> 0)
- `.from-left` / `.from-right` varianten
- `.stagger` voor opeenvolgende vertragingen (0s - 0.34s)
- Statistieken teller animatie met easeOutCubic (2 seconden)

### 5.11 Technologie Stack Sectie

4 categorieen met badges:
- **Data**: Python, SQL Server, PostgreSQL, PostGIS
- **Geo**: GeoServer, Leaflet.js, PDOK, WFS/WMS
- **Web**: Flask, JavaScript, HTML/CSS, Chart.js
- **DevOps**: Git, Docker (planned)

### 5.12 SEO & Meta Tags

- Open Graph tags (og:type, og:title, og:description, og:url, og:site_name, og:locale)
- Twitter Card meta tags
- Meta description, keywords, author, robots

---

## 6. Startup Checklist & Test Instructies

### Server starten
- [ ] `python serve.py` draait zonder errors
- [ ] Browser opent `http://localhost:8087` succesvol

### index.html - Visueel
- [ ] Donker thema geladen (achtergrond #0f1218)
- [ ] Logo (logo.svg) zichtbaar in navbar en hero
- [ ] "Data Consultants" met spatie in navbar en hero titel
- [ ] NL vlag favicon zichtbaar in browser tab
- [ ] Hero tagline en subtitel tekst zichtbaar
- [ ] CTA knop "Open GeoInzicht App" aanwezig

### index.html - Navigatie
- [ ] Alle 7 nav links klikbaar: Over Ons, GeoInzicht, Projecten, Technologie, Visie, Contact, Showcase
- [ ] Smooth scroll naar elke sectie werkt
- [ ] Active state highlighting bij scrollen door secties
- [ ] Hamburger menu verschijnt op < 768px
- [ ] Mobiel menu opent/sluit bij klikken

### index.html - Secties
- [ ] "Wie Wij Zijn" sectie: twee kolommen (tekst + 5 databronnen)
- [ ] GeoInzicht sectie: architectuur pipeline diagram (6 stappen) zichtbaar
- [ ] GeoInzicht sectie: 6 statistieken tellers animeren bij scroll (14.700+, 3.475, 343, 9.7M, 12, 16)
- [ ] GeoInzicht sectie: DWH vs App vergelijking met twee kaarten
- [ ] Prototypes sectie: 11 prototype-kaarten in 3-kolom grid (2 kolom op tablet, 1 op mobiel)
- [ ] Elke prototype-kaart heeft: icoon, status badge "Prototype", titel, beschrijving, tags, GitHub link
- [ ] Alle status badges zijn "Prototype" (teal)
- [ ] "Meer info" links aanwezig op 7 projecten (niet op GeoInzicht DWH en Juridisch Assistent)
- [ ] "Bekijk Live" knoppen op: GeoInzicht App, DAW, Meldpunt, Astronomy, Darosa
- [ ] Technologie sectie: 4 categorieen met tech badges
- [ ] Visie sectie: 4 visie kaarten + artikel callout
- [ ] Contact sectie: email link + GitHub link
- [ ] Footer: "2026 Data Consultants -- Gebouwd met Claude"

### index.html - Scroll Animaties
- [ ] Elementen faden in bij scrollen (.anim class)
- [ ] Stagger effect werkt op lijsten en grids
- [ ] Statistieken tellers animeren eenmalig bij zichtbaarheid

### index.html - Links
- [ ] Hero CTA -> `https://anneversion.github.io/geoinzicht-app/` opent in nieuw tab
- [ ] Alle GitHub links openen correct in nieuw tab
- [ ] "Bekijk Live" links verwijzen naar juiste GitHub Pages URLs
- [ ] "Meer info" links openen juiste project-*.html pagina's
- [ ] "Showcase" nav link opent showcase.html
- [ ] Artikel callout link naar De Correspondent werkt
- [ ] Email link opent mailto:info@dataconsultants.nl

### showcase.html
- [ ] Fullscreen weergave, geen scrollbar
- [ ] Letterbox bars boven en onder zichtbaar
- [ ] Particle canvas achtergrond actief
- [ ] "Home" link linksboven navigeert terug naar index.html
- [ ] 9 dots in navigatie onderaan
- [ ] Controls (vorige, play/pause, volgende) rechtsonder
- [ ] Progress bar onderaan

### showcase.html - Slides
- [ ] Slide 0 (Intro): "Data Consultants" letter-by-letter animatie
- [ ] Slide 1 (GeoInzicht): NL kaart dots + statistieken tellers animeren
- [ ] Slide 1: "Bekijk GeoInzicht" link -> localhost:8091
- [ ] Slide 2 (Serviced Apartments): 3 property cards verschijnen met delay
- [ ] Slide 2: "Bekijk Vastgoed" link -> localhost:8088
- [ ] Slide 3 (DAW): equalizer bars bouncen
- [ ] Slide 3: "Bekijk DAW" link -> localhost:8086
- [ ] Slide 4 (Email Validator): gauge animatie naar 97
- [ ] Slide 4: "Bekijk Validator" link -> localhost:8089
- [ ] Slide 5 (Astronomy): planeet roteert, dots orbiten
- [ ] Slide 5: "Bekijk Astronomy" link -> localhost:8765
- [ ] Slide 6 (Darosa): fiets animatie over road
- [ ] Slide 7 (Meldpunt): shield pulseert
- [ ] Slide 7: "Bekijk Meldpunt" link -> localhost:8090
- [ ] Slide 8 (Outro): "Gebouwd met Claude" + "Data Consultants" + GitHub link

### showcase.html - Interactie
- [ ] Autoplay (6 sec per slide) werkt
- [ ] Spatiebalk pauzeert/hervat autoplay
- [ ] Pijltjestoetsen (links/rechts) wisselen slides
- [ ] Dot klikken navigeert naar juiste slide
- [ ] Vorige/volgende knoppen werken
- [ ] Progress bar vult op tijdens autoplay

### Project Detail Pagina's
- [ ] `project-geoinzicht.html` laadt correct met NL vlag favicon
- [ ] `project-vastgoed.html` laadt correct
- [ ] `project-daw.html` laadt correct
- [ ] `project-email.html` laadt correct
- [ ] `project-astronomy.html` laadt correct
- [ ] `project-fietsverhuur.html` laadt correct
- [ ] `project-meldpunt.html` laadt correct
- [ ] Alle detail pagina's gebruiken thema #0a0f1a + #39ff14
- [ ] Alle detail pagina's hebben terug-naar-home navigatie

### Responsiveness
- [ ] Desktop (> 900px): 3-kolom project grid
- [ ] Tablet (768-900px): 2-kolom project grid
- [ ] Mobiel (< 600px): 1-kolom project grid
- [ ] Mobiel: hamburger menu zichtbaar en werkend
- [ ] Showcase: responsive letterbox bars (32px -> 16px op mobiel)

---

## 7. TODO Lijst

- [x] Cataract project toegevoegd aan projecten grid en showcase
- [x] Darosa Fietsverhuur showcase slide link gefixt (localhost:8092)
- [ ] Docker staat als "planned" in tech stack - niet geimplementeerd
- [ ] Edak project ontbreekt (wacht op Excel input)
- [ ] Showcase slide 1 GeoInzicht linkt naar localhost:8091 (werkt alleen lokaal, niet op GitHub Pages)
- [x] GeoInzicht DWH projectkaart heeft nu "Meer info" detail pagina (project-dwh.html)
- [x] Juridisch Assistent projectkaart heeft nu "Meer info" detail pagina (project-juridisch.html)
- [ ] index.html hero CTA linkt naar GitHub Pages maar showcase linkt naar localhost - inconsistent
- [ ] OG image ontbreekt (og:image meta tag niet ingevuld)
- [x] sitemap.xml en robots.txt toegevoegd

---

## 8. Belangrijke Notities

- **NAAM**: "Data Consultants" ALTIJD met spatie. NOOIT "DataConsultants".
- **Port**: 8087 (vast, niet wijzigen)
- **Geen database**: Puur statische website
- **Autostart**: start_server.vbs in Windows Startup folder start serve.py automatisch met Windows
- **Consistent thema**: Alle pagina's gebruiken neon groen (#39ff14) als accent kleur, met goud (#C9A96E) als secundaire accent
- **Logo**: Geanimeerd SVG met globe + data netwerk + zwart gat + binaire orbits
- **Inline CSS/JS**: Alle styling en scripts staan inline in de HTML bestanden, geen externe bestanden
- **Material Icons Round**: Gebruikt voor alle iconen (geladen via Google Fonts CDN)
- **serve.py**: Simpele Python HTTP server met CORS headers en no-cache, ThreadingHTTPServer
