import datetime
from unittest import TestCase
from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from article import Article
from scraper import Scraper, T
from sourceproviders.soupprovider import SoupProvider


class ArticleScraper(Scraper[Article]):

    def __init__(self, soup_provider: SoupProvider):
        super().__init__(soup_provider)
        self.article = Article("title", "summary", "body", datetime.datetime(2000, 1, 1))

    def can_process_url(self, url: ParseResult) -> bool:
        return True

    def extract(self, soup: BeautifulSoup) -> T:
        return self.article


class SoupProviderMock(SoupProvider):

    def get_soup(self, url: str, headers: {}) -> BeautifulSoup:
        return BeautifulSoup("", "html.parser")


class TestScraper(TestCase):
    def setUp(self):
        self.soup_provider = SoupProviderMock()
        self.scraper = ArticleScraper(self.soup_provider)

    def test_get_headers(self):
        headers = self.scraper.get_headers()
        self.assertIsNotNone(headers)

    def test_process(self):
        article = self.scraper.process("http://example.com")
        self.assertIsNotNone(article)
        self.assertEqual(article.title, self.scraper.article.title)
        self.assertEqual(article.body, self.scraper.article.body)
        self.assertEqual(article.summary, self.scraper.article.summary)
        self.assertEqual(article.update_date, self.scraper.article.update_date)
