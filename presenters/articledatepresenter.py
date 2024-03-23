from article import Article
from abstract.presenterbase import PresenterBase


class ArticleDatePresenter(PresenterBase[Article]):
    def present(self, obj: Article) -> str:
        res: str = str(obj.update_date)
        return res
