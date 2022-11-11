import time

import requests
from parsel import Selector

from tech_news.database import create_news


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
def scrape_novidades(html_content):  # link da noticia
    selector = Selector(html_content)
    return selector.css("h2.entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):  # link da proxima pagina
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
# Impotância da canonical TAG https://rockcontent.com/br/blog/canonical-tag/
def scrape_noticia(html_content):
    selector = Selector(html_content)
    comments = selector.css("div.post-comments h5::text").get()
    summary = selector.css("div.entry-content > p:nth-of-type(1) *::text")
    tags = selector.css("a[rel=tag]::text").getall()
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count": comments.split()[0] if comments else 0,
        "summary": "".join(summary.getall()).strip(),
        "tags": tags if tags else [],
        "category": selector.css("a.category-style span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    urls = []

    while len(urls) <= amount:
        content = fetch(url)
        news = scrape_novidades(content)

        for new in news:
            urls.append(scrape_noticia(fetch(new)))
        url = scrape_next_page_link(content)
    create_news(urls[:amount])
    return urls[:amount]
