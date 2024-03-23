from unittest import TestCase
from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from abstract.scraper import Scraper
from abstract.scraperpool import ScraperPool
from sourceproviders.soupprovider import SoupProvider


class StringScraperPool(ScraperPool[str]):
    pass


class SoupProviderMock(SoupProvider):

    def get_soup(self, url: str, headers: {}) -> BeautifulSoup:
        return BeautifulSoup("", "html.parser")


class StringScraperMock(Scraper[str]):

    def __init__(self, soup_provider: SoupProvider):
        super().__init__(soup_provider)
        self.result = "result"

    def can_process_url(self, url: ParseResult) -> bool:
        return True

    def extract(self, soup: BeautifulSoup) -> str:
        return "result"


class TestScraperPool(TestCase):
    def setUp(self) -> None:
        self.soup_provider = SoupProviderMock()
        self.string_scraper_pool = StringScraperPool()
        self.string_scraper_mock = StringScraperMock(self.soup_provider)
        self.string_scraper_pool.scrapers.append(self.string_scraper_mock)

    def test_process(self):
        result = self.string_scraper_pool.process("http://example.com")
        self.assertIsNotNone(result)
        self.assertEqual(self.string_scraper_mock.result, result)
