class WebScraperSettings:
    def __init__(self):
        self.url: str = ''
        self.type: str = 'article'
        self.presenter: str = 'fullarticle'
        self.use_cache = True
