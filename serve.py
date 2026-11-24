"""Data Consultants website, poort 8087.

Statische bestanden, plus een bewaarpunt voor de teksten van de beginpagina (24-11-2026, Anne: "maak een admingedeelte
waar ik de teksten kan aanpassen"): admin.html stuurt POST /api/teksten en dit script schrijft teksten.json.
Dat kan alleen vanaf deze computer (loopback); op GitHub Pages en op de server worknomads bestaat deze route niet,
daar is admin.html alleen te lezen en gaat een wijziging via git (develop, dan main).
"""
import http.server
import json
import os

PORT = 8087
MAP = os.path.dirname(os.path.abspath(__file__))
os.chdir(MAP)
TEKSTEN = os.path.join(MAP, "teksten.json")
LOOPBACK = ("127.0.0.1", "::1", "::ffff:127.0.0.1")


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def _json(self, code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/api/teksten":
            return self._json(404, {"ok": False, "fout": "onbekende route"})
        if self.client_address[0] not in LOOPBACK:
            return self._json(403, {"ok": False, "fout": "opslaan kan alleen vanaf deze computer"})
        try:
            lengte = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(lengte).decode("utf-8"))
            data.pop("sleutel", None)          # het beheerwachtwoord is voor de live site (contactdienst); lokaal niet bewaren
            for sleutel in ("site", "menu", "begin", "secties", "contact", "voet"):
                if sleutel not in data:
                    raise ValueError(f"veld ontbreekt: {sleutel}")
            tekst = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
            with open(TEKSTEN, "w", encoding="utf-8", newline="\n") as f:
                f.write(tekst)
            self._json(200, {"ok": True, "bytes": len(tekst.encode("utf-8"))})
        except (ValueError, json.JSONDecodeError) as e:
            self._json(400, {"ok": False, "fout": str(e)})


if __name__ == "__main__":
    print(f"Data Consultants website: http://localhost:{PORT}  (beheer: /admin.html)")
    http.server.ThreadingHTTPServer(("", PORT), Handler).serve_forever()
