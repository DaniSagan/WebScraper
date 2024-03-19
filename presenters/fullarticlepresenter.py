from article import Article
from presenterbase import PresenterBase, T


class FullArticlePresenter(PresenterBase[Article]):
    def present(self, obj: Article) -> str:
        res: str = obj.title
        res += '-' * min(len(obj.title), 30)
        res += obj.body
        return res
