import gzip
import hashlib
import pathlib
import urllib
from http.cookiejar import CookieJar
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
            try:
                with open(file, "r") as reader:
                    html = reader.read()
            except UnicodeDecodeError:
                with open(file, "r", encoding="utf-8") as reader:
                    html = reader.read()
            return BeautifulSoup(html, "html.parser")
        else:
            print(f"Downloading HTML from {url} and saving it into file {file.absolute()}")
            html = self.__download_html_from_web(url, headers)
            try:
                with open(file, "w") as writer:
                    writer.write(html)
            except UnicodeDecodeError:
                with open(file, "w", encoding="utf-8") as writer:
                    writer.write(html)
            return BeautifulSoup(html, 'html.parser')

    @staticmethod
    def __download_html_from_web(url: str, headers: {}) -> str:
        request = Request(url, data=None, headers=headers)
        cookie_jar = CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
        page = opener.open(request)
        html_bytes: bytes = page.read()
        encoding = page.info()['content-encoding']
        if encoding == 'gzip':
            html: str = gzip.decompress(html_bytes).decode("utf-8")
        else:
            html: str = html_bytes.decode("utf-8")
        return html

    def __url_to_file(self, url: str) -> pathlib.Path:
        return pathlib.Path(self.cache_folder, hashlib.sha1(url.encode("utf-8")).hexdigest() + ".html")
