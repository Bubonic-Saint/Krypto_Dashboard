import requests
from nachtwaechter import DISCORD_WEBHOOK_URL

print("Sende direkte Anfrage an Discord...")

# Wir schicken die Anfrage und speichern die Antwort von Discord
antwort = requests.post(DISCORD_WEBHOOK_URL, json={"content": "🛠️ **TEST:** Direkter Netzwerk-Test!"})

# Jetzt zwingen wir Python, uns exakt zu sagen, was Discord geantwortet hat:
print(f"HTTP Status-Code: {antwort.status_code}")
print(f"Antwort von Discord: {antwort.text}")