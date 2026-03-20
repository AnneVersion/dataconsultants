# Data Consultants - Claude Code Instructies

## Project
Portfolio website voor Data Consultants. Focus op data collection, modellering en het koppelen van open data. GeoInzicht is het hoofdproject.
Locatie: `E:\scripts\webscraper\CBSbuurt\dataconsultants\`
GitHub: AnneVersion/dataconsultants
GitHub Pages: anneversion.github.io/dataconsultants

## Starten
```bash
python serve.py  # http://localhost:8087
```

Auto-start via Windows Startup: `start_server.vbs` (in Startup folder)

## Branch-strategie
- **main** = stabiel/productie
- **develop** = dagelijkse ontwikkeling (standaard werkbranch)
- **feature/*** = nieuwe features, maak aan vanuit develop

## Key Files
- `index.html` - Portfolio website (donker thema, neon groen)
- `showcase.html` - Showcase pagina met project details
- `serve.py` - Python HTTP server
- `start_server.vbs` - Windows auto-start script

## Features (maart 2026)
- **Thema**: Donker (#0a0f1a), neon groen (#39ff14), Verdana lettertype
- **Favicon**: NL vlag
- **Projecten sectie**: 8 projecten met status badges (Actief/Beta/POC) + GitHub links
- **GeoInzicht knop**: opent localhost:8091 (de app)
- **Showcase pagina**: showcase.html met uitgebreide project details
- **"Gebouwd met Claude"**: badge op de website
- **Inhoud**: Data verzameling & modellering, open data koppelen

## Let op
- Port 8087
- Statische website, geen database
- Start automatisch mee met Windows via start_server.vbs
- **BELANGRIJK**: "Data Consultants" met SPATIE, NOOIT "DataConsultants"
