from datetime import datetime
from typing import Optional


class Article:
    def __init__(self, title: str, summary: str, body: str, update_date: Optional[datetime]):
        self.title: str = title
        self.summary: str = summary
        self.body: str = body
        self.update_date: Optional[datetime] = update_date
