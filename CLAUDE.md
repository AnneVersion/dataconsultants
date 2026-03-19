# Data Consultants - Claude Code Instructies

## Project
Portfolio website voor Data Consultants. Focus op data collection, modellering en het koppelen van open data. GeoInzicht is het hoofdproject.
Locatie: `E:\scripts\webscraper\CBSbuurt\dataconsultants\`

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
- `index.html` - Portfolio website
- `serve.py` - Python HTTP server
- `start_server.vbs` - Windows auto-start script

## Let op
- Port 8087
- Statische website, geen database
- Start automatisch mee met Windows via start_server.vbs
