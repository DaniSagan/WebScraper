from article import Article
from implementations.cnnscraper import CnnScraper
from implementations.nytscraper import NytScraper
from implementations.washingtonpostscraper import WashingtonPostScraper
from sourceproviders.cachedsoupprovider import CachedSoupProvider


def do_stuff():
    url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
    scraper = CnnScraper(CachedSoupProvider())
    article: Article = scraper.process(url)
    print(article.body)


if __name__ == '__main__':
    do_stuff()
