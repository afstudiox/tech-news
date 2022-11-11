import time

import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    for _ in range(5):
        try:
            response = requests.get(
                url, headers={"User-Agent": "Fake user-agent"}, timeout=3
            )
            time.sleep(1)
            if response.status_code != 200:
                return None
            return response.text
        except requests.ReadTimeout:
            return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("h2.entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
