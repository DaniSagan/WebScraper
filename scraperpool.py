from typing import List, TypeVar, Generic, Optional
from urllib.parse import urlparse

from scraper import Scraper


T = TypeVar("T")


class ScraperPool(Generic[T]):

    def __init__(self):
        self.scrapers: List[Scraper[T]] = []

    def register(self, scraper: Scraper[T]):
        self.scrapers.append(scraper)

    def process(self, url: str) -> Optional[T]:
        for scraper in self.scrapers:
            if scraper.can_process_url(urlparse(url)):
                return scraper.process(url)
        return None
