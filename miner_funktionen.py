import requests

def get_miner_data(ip):
    url = f"http://{ip}/api/system/info"
    try:
        antwort = requests.get(url, timeout=3.0)
        antwort.raise_for_status()
        return antwort.json()
    except Exception:
        return None