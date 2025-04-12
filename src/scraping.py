# scraping.py

import requests
from bs4 import BeautifulSoup

def obtener_ejemplo():
    url = "https://ejemplo.com"
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    return None
