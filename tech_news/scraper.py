import time

import requests


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    for _ in range(3):
        try:
            response = requests.get(
                url, headers={"User-Agent": "Fake user-agent"}, timeou=3
            )
            responseStatusCode = response.status_code
            responseText = response.text
            time.sleep(1)
            if responseStatusCode != 200:
                return None
            return responseText
        except requests.ReadTimeout:
            return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
