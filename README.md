# 🚀 Krypto Miner Live-Dashboard

Ein leichtgewichtiges, lokales Web-Dashboard zur Überwachung von Solo- und Pool-Minern (z.B. NerdOctaxe, Bitaxe, etc.). Das Dashboard sammelt die Daten direkt über die lokale IP-Adresse der Miner und stellt sie in einer modernen, automatisch aktualisierenden Oberfläche dar.

## ✨ Features

* **Live-Updates:** Automatische Aktualisierung alle 5 Sekunden ohne Seiten-Reload.
* **Profi-Metriken:** Berechnet live die Effizienz (J/TH) und wandelt Sekunden in lesbare Uptime (h/m) um.
* **Smart Sorting:** Alle Tabellenspalten (Hashrate, Strom, Uptime, Best Diff, etc.) lassen sich durch Klick auf den Tabellenkopf auf- und absteigend sortieren.
* **100% Lokal & Privat:** Keine Cloud-Anbindung nötig. Das Skript läuft komplett in deinem eigenen Netzwerk.
* **Zwei Kategorien:** Getrennte Tabellen für Solo-Miner (Fokus auf Best Diff & Blöcke) und Pool-Miner (Fokus auf Accepted/Rejected Shares).

---

## 🛠️ Installation & Setup (Lokaler PC)

### 1. Repository klonen
Lade den Code auf deinen Rechner herunter und wechsle in den Ordner:
```bash
git clone [https://github.com/DEIN_GITHUB_NAME/Krypto_Dashboard.git](https://github.com/DEIN_GITHUB_NAME/Krypto_Dashboard.git)
cd Krypto_Dashboard
```
### 2. Virtuelle Umgebung erstellen & aktivieren
Es wird empfohlen, das Projekt in einer eigenen Python-Umgebung auszuführen:

Windows (Git Bash / PowerShell):

```Bash
python -m venv venv
source venv/Scripts/activate
```
Linux / Mac:

```Bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Abhängigkeiten installieren
```Bash
pip install -r requirements.txt
```
### 4. Konfiguration anlegen (WICHTIG)
Deine privaten Miner-IPs werden aus Sicherheitsgründen nicht auf GitHub hochgeladen.

Kopiere die Datei config.example.json und nenne die Kopie config.json.

Öffne die neue config.json und trage die Namen, IPs und Coins deiner eigenen Miner ein.

### 5. Dashboard starten
Starte den lokalen Webserver mit folgendem Befehl:

```Bash
python app.py
```
Öffne nun deinen Browser und rufe http://localhost:5000 auf! 🎉

## 📂 Projektstruktur
```
Krypto_Dashboard/
├── app.py                     # Der Flask-Webserver (Einstiegspunkt)
├── miner_funktionen.py        # Logik für API-Abfragen & Datenverarbeitung
├── config.json                # DEINE PRIVATEN DATEN (wird von Git ignoriert)
├── config.example.json        # Vorlage für andere Nutzer / GitHub
├── requirements.txt           # Liste der Python-Pakete (Flask, requests)
├── README.md                  # Dokumentation & Installationsanleitung
├── .gitignore                 # Verhindert Upload von venv/ und config.json
├── venv/                      # Deine lokale virtuelle Umgebung (unsichtbar)
├── static/                    # Statische Dateien (Frontend-Logik)
│   ├── style.css              # Das Design (Dark Mode, Tabellen-Layout)
│   └── main.js                # JavaScript für Live-Updates & Sortierung
└── templates/                 # HTML-Vorlagen
    └── dashboard.html         # Das Grundgerüst der Webseite
```
