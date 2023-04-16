from utils.core.base import Spider

class TempoSpider(Spider):
    def __init__(self):

        self.base_url = [
            'https://www.tempo.co',
            'https://nasional.tempo.co',
            'https://gaya.tempo.co',
            'https://dunia.tempo.co'
            ]
        
        super().__init__(self.base_url)

        self.title_attr = {
            "name":"h1",
            "attrs":{
                "class":"title"
            }
        }
        
        self.content_attr = {
            "name":"div",
            "attrs":{
                "class":"detail-in",
                "id":"isi"
            }
        }
        self.date_attr = {
            "name":"p",
            "attrs":{
                "class":"date"
            }
        }
        