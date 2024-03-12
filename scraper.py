from http.client import HTTPResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Scraper(ABC):
    def __init__(self):
        pass

    @staticmethod
    def __get_source(url: str) -> BeautifulSoup:
        page: HTTPResponse = urlopen(url)
        html_bytes: bytes = page.read()
        html: str = html_bytes.decode("utf-8")
        soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
        return soup

    @abstractmethod
    def can_process_url(self, url: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def extract(self, soup: BeautifulSoup) -> str:
        raise NotImplementedError

    def process(self, url: str) -> str:
        if not self.can_process_url(url):
            raise ValueError("URL cannot be processed.")
        return self.extract(self.__get_source(url))
