from typing import List
from urllib.parse import ParseResult

from bs4 import BeautifulSoup

from article import Article
from abstract.scraper import Scraper, T


class ReutersScraper(Scraper[Article]):
    def can_process_url(self, url: ParseResult) -> bool:
        return url.netloc == "www.reuters.com"

    def extract(self, soup: BeautifulSoup) -> T:
        title = soup.find("h1", attrs={"data-testid": "Heading"}).text
        article_body: List[str] = list(
            map(
                lambda p: p.text.strip(),
                soup.findAll(
                    "div",
                    {"data-testid": lambda x: x and x.startswith("paragraph-")}
                )
            )
        )
        return Article(
            title=title,
            summary='',
            body='\n\n'.join(article_body),
            update_date=None)

    def get_headers(self) -> {}:
        return {
            'Host': 'www.reuters.com',
            'User-Agent': 'MyApp/1.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.reuters.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }
