from article import Article
from abstract.presenterbase import PresenterBase


class FullArticlePresenter(PresenterBase[Article]):
    def present(self, obj: Article) -> str:
        res: str = '-' * min(len(obj.title), 50) + "\n"
        res += obj.title + "\n"
        if obj.update_date:
            res += str(obj.update_date) + "\n"
        res += '-' * min(len(obj.title), 50) + "\n"
        res += obj.body
        return res
