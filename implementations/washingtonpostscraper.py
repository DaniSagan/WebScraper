from typing import List
from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from article import Article
from scraper import Scraper


class WashingtonPostScraper(Scraper[Article]):
    def can_process_url(self, url: ParseResult) -> bool:
        return url.netloc == "www.washingtonpost.com"

    def extract(self, soup: BeautifulSoup) -> Article:
        """ Currently giving HTTP Error 302 """
        raise NotImplementedError
