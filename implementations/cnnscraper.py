from typing import List
from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from article import Article
from scraper import Scraper


class CnnScraper(Scraper[Article]):
    def can_process_url(self, url: ParseResult) -> bool:
        return url.netloc == "edition.cnn.com"

    def extract(self, soup: BeautifulSoup) -> Article:
        title = soup.find("h1", attrs={"id": "maincontent"}).text
        article_body: List[str] = list(map(lambda p: p.text.strip(), soup.findAll("p", "paragraph")))
        return Article(
            title=title,
            summary='',
            body='\n\n'.join(article_body),
            update_date=None)
