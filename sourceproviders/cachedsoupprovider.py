import hashlib
import pathlib
from http.client import HTTPResponse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from sourceproviders.soupprovider import SoupProvider


class CachedSoupProvider(SoupProvider):

    def __init__(self):
        self.cache_folder: pathlib.Path = pathlib.Path("data/cache/")

    def get_soup(self, url: str, headers: {}) -> BeautifulSoup:
        self.cache_folder.mkdir(parents=True, exist_ok=True)
        file = self.__url_to_file(url)
        if file.exists():
            print(f"Reading HTML from file {file.absolute()}")
            with open(file, "r") as reader:
                html = reader.read()
            return BeautifulSoup(html, "html.parser")
        else:
            print(f"Downloading HTML from {url} and saving it into file {file.absolute()}")
            html = self.__download_html_from_web(url, headers)
            with open(file, "w") as writer:
                writer.write(html)
            return BeautifulSoup(html, 'html.parser')

    @staticmethod
    def __download_html_from_web(url: str, headers: {}) -> str:
        request = Request(url, data=None, headers=headers)
        page: HTTPResponse = urlopen(request)
        html_bytes: bytes = page.read()
        html: str = html_bytes.decode("utf-8")
        return html

    def __url_to_file(self, url: str) -> pathlib.Path:
        return pathlib.Path(self.cache_folder, hashlib.sha1(url.encode("utf-8")).hexdigest() + ".html")
