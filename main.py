from implementations.nytscraper import NytScraper
from sourceproviders.cachedsoupprovider import CachedSoupProvider


def do_stuff():
    scraper = NytScraper(CachedSoupProvider())
    print(scraper.process("https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html?action=click&module=Opinion&pgtype=Homepage"))


if __name__ == '__main__':
    do_stuff()
