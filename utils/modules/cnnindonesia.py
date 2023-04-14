from utils.core.base import Spider 

class CNNIndoSpider(Spider):
    def __init__(self):
        self.base_url = 'https://www.cnnindonesia.com/nasional'
        super().__init__(self.base_url)
        self.content_attr = {"name":"div","attrs":{"class":"detail_text"}}
        self.date_attr = {"name":"div","attrs":{"class":"date"}}
        


