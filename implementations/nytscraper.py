from typing import List
from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from article import Article
from scraper import Scraper


class NytScraper(Scraper[Article]):

    def can_process_url(self, url: ParseResult) -> bool:
        return url.netloc == "www.nytimes.com"

    def extract(self, soup: BeautifulSoup) -> Article:
        article = soup.find("article", id="story")
        header = article.find("header")
        title = header.find("h1", attrs={"data-testid": "headline"}).text
        summary = header.find("p", attrs={"id": "article-summary"}).text
        article_body: List[str] = list(map(lambda p: p.text, article.findAll("p", "css-at9mc1")))
        return Article(
            title=title,
            summary=summary,
            body='\n'.join(article_body),
            update_date=None)
