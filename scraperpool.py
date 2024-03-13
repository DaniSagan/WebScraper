from typing import List, TypeVar, Generic, Optional, Iterable
from urllib.parse import urlparse

from scraper import Scraper


T = TypeVar("T")


class ScraperPool(Generic[T]):

    def __init__(self):
        self.scrapers: List[Scraper[T]] = []

    def register_scraper(self, scraper: Scraper[T]):
        self.scrapers.append(scraper)

    def register_scrapers(self, scrapers: Iterable[Scraper[T]]):
        self.scrapers.extend(scrapers)

    def process(self, url: str) -> Optional[T]:
        for scraper in self.scrapers:
            if scraper.can_process_url(urlparse(url)):
                return scraper.process(url)
        return None
