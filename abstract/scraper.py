from http.client import HTTPResponse
from typing import TypeVar, Generic
from urllib.parse import ParseResult, urlparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

from sourceproviders.soupprovider import SoupProvider


T = TypeVar("T")


class Scraper(Generic[T], ABC):

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
        """
        Returns the headers to use when requesting the web site.
        :return:
        """
        return {'User-Agent': 'MyApp/1.0'}

    @abstractmethod
    def can_process_url(self, url: ParseResult) -> bool:
        """
        Returns True if the scraper can process the URL.
        :param url: URL of the web page to process.
        :return: True if the scraper can process the web page.
        """
        raise NotImplementedError

    @abstractmethod
    def extract(self, soup: BeautifulSoup) -> T:
        raise NotImplementedError

    def process(self, url: str) -> T:
        if not self.can_process_url(urlparse(url)):
            raise ValueError("URL cannot be processed.")
        return self.extract(self.soup_provider.get_soup(url, self.get_headers()))
