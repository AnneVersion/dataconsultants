@echo off
cd /d E:\scripts\webscraper\CBSbuurt\dataconsultants
git add -A
git commit -m "Favicon NL-vlag via favicon.ico op alle pagina's"
git push origin main
echo.
echo Klaar. Site ververst binnen ~1 minuut op https://anneversion.github.io/dataconsultants/
pause
