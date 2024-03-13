from typing import Optional

from article import Article
from implementations.cnnscraper import CnnScraper
from implementations.nytscraper import NytScraper
from implementations.reutersscraper import ReutersScraper
from implementations.washingtonpostscraper import WashingtonPostScraper
from scraperpool import ScraperPool
from sourceproviders.cachedsoupprovider import CachedSoupProvider


def create_article_scraper_pool() -> ScraperPool[Article]:
    soup_provider = CachedSoupProvider()
    scraper_pool = ScraperPool[Article]()
    scraper_pool.register_scrapers([
        NytScraper(soup_provider),
        WashingtonPostScraper(soup_provider),
        CnnScraper(soup_provider),
        ReutersScraper(soup_provider)
    ])
    return scraper_pool


def main():
    url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"
    scraper_pool = create_article_scraper_pool()
    article: Optional[Article] = scraper_pool.process(url)
    if article:
        print('—' * len(article.title))
        print(article.title)
        print('—'*len(article.title))
        print(article.body)
    else:
        print("Could not parse URL. No valid scraper was found.")


if __name__ == '__main__':
    main()
