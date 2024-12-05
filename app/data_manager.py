import requests
from app.utils import *

ENDPOINTS = ["countries", "materials", "products"]


def fetch_data(url) -> json:
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None


def update_data() -> None:
    for endpoint in ENDPOINTS:
        data = fetch_data(f"https://ecobalyse.beta.gouv.fr/api/textile/{endpoint}")
        if data:
            save_json(data, f"data/{endpoint}.json")


def get_data() -> dict:
    data = {}
    for endpoint in ENDPOINTS:
        data[endpoint] = load_json(f"data/{endpoint}.json")
    return data
