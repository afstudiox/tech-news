from datetime import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_by_title]


# Requisito 7
def search_by_date(date):
    try:
        inverse_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news_by_date = search_news({"timestamp": inverse_date})
        return [(news["title"], news["url"]) for news in news_by_date]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_by_tag = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_by_tag]

# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
