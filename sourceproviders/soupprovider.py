from abc import ABC, abstractmethod

from bs4 import BeautifulSoup


class SoupProvider(ABC):

    @abstractmethod
    def get_soup(self, url: str, headers: {}) -> BeautifulSoup:
        raise NotImplementedError
