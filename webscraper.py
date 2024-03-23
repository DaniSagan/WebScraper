from argparse import ArgumentParser, Namespace

from article import Article
from implementations.cnnscraper import CnnScraper
from implementations.nytscraper import NytScraper
from implementations.reutersscraper import ReutersScraper
from implementations.washingtonpostscraper import WashingtonPostScraper
from abstract.scraperpool import ScraperPool
from presenters.fullarticlepresenter import FullArticlePresenter
from presenters.articletitlepresenter import ArticleTitlePresenter
from sourceproviders.cachedsoupprovider import CachedSoupProvider
from sourceproviders.soupprovider import SoupProvider
from webscrapersettings import WebScraperSettings


def create_article_scraper_pool(soup_provider: SoupProvider) -> ScraperPool[Article]:
    scraper_pool = ScraperPool[Article]()
    scraper_pool.register_scrapers([
        NytScraper(soup_provider),
        WashingtonPostScraper(soup_provider),
        CnnScraper(soup_provider),
        ReutersScraper(soup_provider)
    ])
    return scraper_pool


class WebScraper:
    def __init__(self):
        self.soup_provider = CachedSoupProvider()
        self.scraper_pools = {
            'article': create_article_scraper_pool(self.soup_provider)
        }
        self.presenters = {
            'fullarticle': FullArticlePresenter(),
            'title': ArticleTitlePresenter()
        }
        self.settings: WebScraperSettings = WebScraperSettings()

    def parse_args(self, args: Namespace):
        self.settings.url = args.url
        if args.type is not None:
            self.settings.type = args.type
        if args.presenter is not None:
            self.settings.presenter = args.presenter

    def execute(self) -> None:
        result = self.scraper_pools[self.settings.type].process(self.settings.url)
        print(self.presenters[self.settings.presenter].present(result))


def create_parser(web_scraper: WebScraper) -> ArgumentParser:
    parser = ArgumentParser(
        prog='WebScraper',
        description='A python web scraper',
        epilog='Text at the bottom of help')
    parser.add_argument('url', help='URL of the resource to scrape.')
    parser.add_argument('-t', '--type', help='Scraper type', choices=list(web_scraper.scraper_pools.keys()))
    parser.add_argument('-p', '--presenter', help='Scraper type', choices=list(web_scraper.presenters.keys()))
    return parser


def main():
    web_scraper = WebScraper()
    parser = create_parser(web_scraper)
    args: Namespace = parser.parse_args()
    web_scraper.parse_args(args)
    web_scraper.execute()


if __name__ == '__main__':
    main()
