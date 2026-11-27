# modelos_gratis.py
import json
import urllib.request

with urllib.request.urlopen("https://openrouter.ai/api/v1/models") as respuesta:
    modelos = json.load(respuesta)["data"]

gratis = [m["id"] for m in modelos if m["id"].endswith(":free")]
for modelo in sorted(gratis):
    print(modelo)