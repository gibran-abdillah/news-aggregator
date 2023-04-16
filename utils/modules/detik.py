from utils.core.base import Spider 

class DetikSpider(Spider):
    def __init__(self):
        self.base_url = [
            'https://news.detik.com/jabodetabek',
            'https://news.detik.com/internasional',
            'https://news.detik.com/berita'
        ]
        super().__init__(self.base_url)

        self.title_attr = {"name":"h1", "attrs":{"class":"detail__title"}}
        self.content_attr = {"name":"div","attrs":{"class":"detail__body"}}
        self.date_attr = {"name":"div", "attrs":{"class":"detail__date"}}

        
        self.news_card = "article"
        self.max_news = 7
