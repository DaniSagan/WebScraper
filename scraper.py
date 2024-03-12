from http.client import HTTPResponse
from urllib.parse import ParseResult, urlparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

from sourceproviders.soupprovider import SoupProvider


class Scraper(ABC):

    def __init__(self, soup_provider: SoupProvider):
        self.soup_provider = soup_provider

    def __get_source(self, url: str) -> BeautifulSoup:
        request = Request(url, data=None, headers=self.get_headers())
        page: HTTPResponse = urlopen(request)
        html_bytes: bytes = page.read()
        html: str = html_bytes.decode("utf-8")
        soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
        return soup

    @staticmethod
    def get_headers() -> {}:
        return {'User-Agent': 'MyApp/1.0'}

    @abstractmethod
    def can_process_url(self, url: ParseResult) -> bool:
        raise NotImplementedError

    @abstractmethod
    def extract(self, soup: BeautifulSoup) -> str:
        raise NotImplementedError

    def process(self, url: str) -> str:
        if not self.can_process_url(urlparse(url)):
            raise ValueError("URL cannot be processed.")
        return self.extract(self.soup_provider.get_soup(url, self.get_headers()))
