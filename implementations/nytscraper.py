from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from article import Article
from scraper import Scraper


class NytScraper(Scraper[Article]):

    def can_process_url(self, url: ParseResult) -> bool:
        return url.netloc == "www.nytimes.com"

    def extract(self, soup: BeautifulSoup) -> Article:
        article = soup.find("article")
        header = article.find("header")
        title = header.find("h1")
        return Article(
            title=title.text,
            body='',
            update_date=None)
