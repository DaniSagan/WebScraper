from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from scraper import Scraper


class NytScraper(Scraper):

    def can_process_url(self, url: ParseResult) -> bool:
        return url.netloc == "www.nytimes.com"

    def extract(self, soup: BeautifulSoup) -> str:
        article = soup.find("article")
        header = article.find("header")
        title = header.find("h1")
        return title.text
