from utils.core.base import Spider 

class DetikSpider(Spider):
    def __init__(self):
        self.base_url = 'https://news.detik.com'
        super().__init__(self.base_url)

        self.title_attr = {"name":"h1", "attrs":{"class":"detail__title"}}
        self.content_attr = {"name":"div","attrs":{"class":"detail__body"}}
        self.date_attr = {"name":"div", "attrs":{"class":"detail__date"}}

        
        self.news_card = "article"
        self.max_news = 7

    def initRequest(self):
        soup = self.getSoup(self.base_url, stream=True)
        column_12 = soup.find_all('a', {'dtr-evt':'box berita utama'})
        return self.parseInit(column_12)
    
    def parseInit(self, soup):
        return [a.get('href') for a in soup]

