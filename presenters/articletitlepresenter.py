from article import Article
from abstract.presenterbase import PresenterBase


class ArticleTitlePresenter(PresenterBase[Article]):
    def present(self, obj: Article) -> str:
        res: str = obj.title
        return res
