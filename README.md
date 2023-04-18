# News Aggregator 
Web App that aggregates news articles from multiple sources using BeautifulSoup4 for web scraping, Django for web development, Django REST framework for building APIs, Elasticsearch for search functionality, and periodic tasks for automated updates.

## Installation
- Install 'elasticsearch' https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
- Install 'redis' https://redis.io/docs/getting-started/installation/
- Clone this repository 
  ```sh
    git clone https://github.com/gibran-abdillah/news-aggregator
  ```
- Create your virtual environment and go to the project directory
  ```sh
  virtualenv env/
  source env/bin/activate

  cd news-aggregator
  pip3 install -r requirements.txt
  ```

## Setup the project
  - add the crontab job with details
  ```sh
  */30 * * * * source yourenv/activate && cd news-aggregator && python3 manage.py scrape > /path/to/log 2>&1
  ```
  
- Migrate your database and build search index
  ```sh
  python3 manage.py makemigrations
  python3 manage.py migrate

  python3 manage.py search_index --rebuild
  ```

## Run the app!
after everything is set up, run the django app as usual
```sh
python3 manage.py runserver
```
or you can use ```gunicorn``` to run the wsgi app
```sh
gunicorn newsaggregator.wsgi
```
finally, you can browse the api at <b>api/</b>


## Customize Scraper 
you can also create your own scraper, you just need set the title, content, and date attribute
still don't get it? check this example code : 

```html
<p class="date">13 Apr 2023</p>
<h1 class="title">This is Example title of the news article</h1>
<div class='detail-in' id='isi'>
    <p>Lorem ipsum dolor sit amet</p>
    <p>Azaret metrio zintos!</p>
</div>
```

all you just need is inherate the ```Spider`` class in utils/core/base.py and set the attribute

example in ```utils/modules/tempo.py```

```python
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
        
```
