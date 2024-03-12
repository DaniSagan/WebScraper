from article import Article
from implementations.nytscraper import NytScraper
from sourceproviders.cachedsoupprovider import CachedSoupProvider


def do_stuff():
    scraper = NytScraper(CachedSoupProvider())
    article: Article = scraper.process("https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html?action=click&module=Opinion&pgtype=Homepage")
    print(article.body)


if __name__ == '__main__':
    do_stuff()
