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
    scraper_pool.register(NytScraper(soup_provider))
    scraper_pool.register(WashingtonPostScraper(soup_provider))
    scraper_pool.register(CnnScraper(soup_provider))
    scraper_pool.register(ReutersScraper(soup_provider))
    return scraper_pool


def main():
    url = "https://www.reuters.com/technology/us-house-vote-force-bytedance-divest-tiktok-or-face-ban-2024-03-13/"
    scraper_pool = create_article_scraper_pool()
    article: Optional[Article] = scraper_pool.process(url)
    if article:
        print(article.body)
    else:
        print("Could not parse URL. No valid scraper was found.")


if __name__ == '__main__':
    main()
