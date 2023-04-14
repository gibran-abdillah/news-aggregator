from utils.core.base import Spider

class CNBCSpider(Spider):
    def __init__(self):
        self.base_url = 'https://www.cnbcindonesia.com/news'
        super().__init__(self.base_url)

        self.title_attr = {"name":"title"}

        self.content_attr = {
            "name":"div",
            "attrs":{
                "class":"detail_text"
            }
        }
        self.date_attr = {
            "name":"div",
            "attrs":{
                "class":"date"
            }

        }
        self.max_news = 4