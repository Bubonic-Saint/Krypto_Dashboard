# 🚀 Krypto Miner Live-Dashboard

Ein leichtgewichtiges, lokales Web-Dashboard zur Überwachung von Solo- und Pool-Minern (z.B. NerdOctaxe, Bitaxe, etc.). Das Dashboard sammelt die Daten direkt über die lokale IP-Adresse der Miner und stellt sie in einer modernen, automatisch aktualisierenden Oberfläche dar.

## ✨ Features

* **Live-Updates:** Automatische Aktualisierung alle 5 Sekunden ohne Seiten-Reload.
* **Profi-Metriken:** Berechnet live die Effizienz (J/TH) und wandelt Sekunden in lesbare Uptime (h/m) um.
* **Smart Sorting:** Alle Tabellenspalten (Hashrate, Strom, Uptime, Best Diff, etc.) lassen sich durch Klick auf den Tabellenkopf auf- und absteigend sortieren.
* **100% Lokal & Privat:** Keine Cloud-Anbindung nötig. Das Skript läuft komplett in deinem eigenen Netzwerk.
* **Zwei Kategorien:** Getrennte Tabellen für Solo-Miner (Fokus auf Best Diff & Blöcke) und Pool-Miner (Fokus auf Accepted/Rejected Shares).
* **Nachtwächter-Modus:** Ein Hintergrund-Thread prüft alle 60 Sekunden den Status.
* **Discord-Alarme:**
  * Sofortige Benachrichtigung bei Block-Fund (Solo-Miner).
  * Alarmierung, wenn ein Miner länger als 10 Minuten offline ist.
* **Headless-Betrieb:** Optimiert für den Raspberry Pi Zero 2 W.
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

Für die Benachrichtigungen über Discord musst du zusätzlich die Webhook-URL deines Discord-Kanals eintragen.

```Bash
{
  "SOLO_MINERS": [
    {"name": "Mein_Erster_Miner", "ip": "192.168.1.100", "coin": "BTC"}
  ],
  "POOL_MINERS": [
    {"name": "Mein_Pool_Miner", "ip": "192.168.1.101", "coin": "BTC"}
  ],
  "DISCORD_WEBHOOK_URL": "YOUR_DISCORD_WEBHOOK_URL_HERE"
}
```

### 5. Dashboard starten
Starte den lokalen Webserver mit folgendem Befehl:

```Bash
python app.py
```
Öffne nun deinen Browser und rufe http://localhost:5000 auf! 🎉

## 🖥️ Setup auf dem Raspberry Pi (Headless)
### 1. Vorbereitung
Verbinde dich per SSH mit deinem Pi und installiere die notwendigen System-Pakete:

```Bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### 2. Repository klonen & Setup
Klone das Repository und erstelle eine virtuelle Python-Umgebung, um Konflikte mit System-Paketen zu vermeiden:
```Bash
git clone https://github.com/DEIN_USER/Krypto_Dashboard.git
cd Krypto_Dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Konfiguration anlegen
Da die config.json nicht im Git-Repository liegt, erstelle sie manuell auf dem Pi:
```Bash
nano config.json
```

### 4. Autostart einrichten (24/7 Betrieb)
Damit das Dashboard nach jedem Neustart automatisch startet und im Hintergrund läuft, erstellen wir einen System-Service:

#### 1. Erstelle die Service-Datei:
```Bash
sudo nano /etc/systemd/system/krypto_dashboard.service
```
#### 2. Füge folgenden Inhalt ein (passe den Pfad zu deinem Projekt an):
```ini
[Unit]
Description=Krypto Miner Dashboard 24/7 Service
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/Krypto_Dashboard
ExecStart=/home/pi/Krypto_Dashboard/venv/bin/python app.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```
#### 3. Service aktivieren und starten:
```Bash
sudo systemctl daemon-reload
sudo systemctl enable minerdashboard.service
sudo systemctl start minerdashboard.service
```

## 📂 Projektstruktur
```
Krypto_Dashboard/
├── app.py                     # Der Flask-Webserver & Startpunkt des Nachtwächters
├── nachtwaechter.py           # Logik für Hintergrund-Überwachung & Discord-Alarme
├── miner_funktionen.py        # Logik für API-Abfragen & Datenverarbeitung
├── config.json                # PRIVAT: Deine Miner-IPs & Webhook (wird von Git ignoriert)
├── config.example.json        # Vorlage für GitHub (ohne echte Daten)
├── requirements.txt           # Liste der Python-Pakete (Flask, requests)
├── README.md                  # Dokumentation & Installationsanleitung
├── .gitignore                 # Verhindert Upload von venv/ und config.json
├── venv/                      # Lokale virtuelle Umgebung (wird von Git ignoriert)
├── static/                    # Frontend-Dateien
│   ├── style.css              # Das Design (Dark Mode, Tabellen-Layout)
│   └── main.js                # JavaScript für Live-Updates (Frontend-Seite)
└── templates/                 # HTML-Vorlagen
    └── dashboard.html         # Das Grundgerüst der Webseite
```
