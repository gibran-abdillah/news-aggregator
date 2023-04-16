import requests, random , os 
from bs4 import BeautifulSoup
from datetime import datetime 
from urllib.parse import urlparse

DAY_REPLACEMENT = {
    'Senin':'Monday',
    'Selasa':'Tuesday',
    'Rabut':'Wednesday',
    'Kamis':'Thursday',
    'Jum\'at':'Friday',
    'Sabtu':'Saturday',
    'Minggu':'Sunday',
    ' WIB':'',
}

class Spider:

    def __init__(self, base_url):
        
        self.base_url = base_url

        self.title_attr = {"name":"title"}

        self.date_attr = {}
        self.content_attr = {}

        self.news_card = "article"

        self.max_news = 20

        # format date that usually used in news article, thx to CHATGPT!
        self.date_formats = [
            '%d %B %Y %H:%M',
            '%A, %d %B %Y %H:%M %Z',
            '%Y-%m-%dT%H:%M:%S%z',
            '%b %d, %Y %I:%M %p',
            '%d %b %Y %H:%M',
            '%d/%m/%Y %I:%M %p',
            '%A, %B %d, %Y %I:%M %p',
            '%B %d, %Y at %I:%M %p',
            '%dth %B %Y, %I:%M %p',
            '%I:%M %p %Z, %d %B %Y',
            '%I:%M %p, %A, %B %d, %Y',
            '%Y/%m/%d %H:%M:%S',
            '%B %d, %Y %H:%M',
            '%m/%d/%Y %I:%M %p',
            '%A, %b %d, %Y %I:%M %p',
            '%d %B %Y %I:%M %p',
            '%I:%M %p %Z on %B %d, %Y',
            '%A %d %B %Y %I:%M %p',
            '%Y-%m-%d %H:%M:%S.%f',
            '%d/%m/%y %I:%M %p',
            '%A, %d %b %Y %H:%M %Z'
            '%A, %d %b %Y %H:%M'
        ]


    
    @property
    def user_agents(self):
        return [_.rstrip() for _ in open('utils/user-agents.txt','r').readlines()]
    
    @property
    def source(self):
        """
        get source name from base_url
        """
        if isinstance(self.base_url, list):
            url = self.base_url[0]
        else:
            url = self.base_url
        return ''.join([x for x in urlparse(url).netloc.split('.') if len(x) > 4])

    def buildSession(self):
        session = requests.Session()
        session.headers['User-Agent'] = random.choice(self.user_agents)
        return session
    
    def getSoup(self, url: str, **kwargs):
        try:
            session = self.buildSession()
            response = session.get(url, **kwargs)
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException:
            return None
        
    def initRequest(self):
        """
        init request and get news from news card
        """
        result = []
        if isinstance(self.base_url, list):
            for base_url in self.base_url:
                soup = self.getSoup(base_url)
                if not soup:
                    return None
                news_card = soup.find_all('article')
                cleaned = self.parseInit(news_card)
                result = result + cleaned
            return result 
        else:
            soup = self.getSoup(self.base_url)
            if not soup:
                return None
            news_card = soup.find_all('article')
            cleaned = self.parseInit(news_card)
            return cleaned
         

    def main(self):
        articles = self.initRequest()
        print(f'added url from ({self.source}): {len(articles)}')
        result = []
        if articles:

            for article in articles:
                soup = self.getSoup(article)
                if not soup:
                    return False

                title = self.parseTitle(soup)
                content = self.parseContent(soup)
                date = self.parseDate(soup)

                data = {
                    "title":title, 
                    "content":content, 
                    "date":date
                }
                if all([title, content, date]):
                    
                    tmp_data = {k:self.clean_text(v) for k, v in data.items()}
                    
                    tmp_data['date'] = self.convert_date(data.get('date'))
                    tmp_data['source'] = self.source

                    result.append(tmp_data)
                else:
                    print([x for x,y in data.items() if not y], article, 'is missing')

            return result
        else:
            print('article missing in ', self.base_url)
    
    def parseInit(self, soup: BeautifulSoup.find_all):
        result = [_.find('a').get('href') for _ in soup if _.find('a') and 'href' in str(_.find('a'))]
        if len(result) >= self.max_news:
            return result[0:self.max_news]
        return result 

        
    def parseContent(self, soup: BeautifulSoup):
        content_tag = soup.find(**self.content_attr)
        return content_tag.text if content_tag else None 

    def parseDate(self, soup: BeautifulSoup):
        date_tag = soup.find(**self.date_attr)
        return date_tag.text if date_tag else None 
    
    def parseTitle(self, soup: BeautifulSoup):
        result = soup.find(**self.title_attr)
        return result.text if result else None
    
    def clean_text(self, text: str):
        return ' '.join(text.split())
    
    def convert_date(self, date: str):
        for day, replace in DAY_REPLACEMENT.items():
            date = date.replace(day, replace)
        
        for format_date in self.date_formats:
            try:
                return datetime.strptime(date, format_date)
            except:
                continue

        return datetime.utcnow()

    