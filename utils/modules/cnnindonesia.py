from utils.core.base import Spider 

class CNNIndoSpider(Spider):
    def __init__(self):
        self.base_url = [
            'https://www.cnnindonesia.com/nasional',
            'https://www.cnnindonesia.com/otomotif',
            'https://www.cnnindonesia.com/teknologi',
            'https://www.cnnindonesia.com/internasional'
            'https://www.cnnindonesia.com/olahraga'
        ]
        super().__init__(self.base_url)
        self.content_attr = {"name":"div","attrs":{"class":"detail_text"}}
        self.date_attr = {"name":"div","attrs":{"class":"date"}}
        


