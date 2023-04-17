from newsaggregator.celery import app
from utils.scrape import main as scrape_main
from news.models import News, Source

def scrape_news():
    results = scrape_main()

    total = 0 

    for result in results:
        for r in result:
            if not News.objects.filter(title=r.get('title')):
                total += 1 

                title = r.get('title')
                content = r.get('content')
                date = r.get('date')
                source = r.get('source')

                n = News(title=title, content=content, date=date)
                n.save()

                s = Source.objects.filter(name=source) 
                if s:
                    
                    s = s[0]
                    s.news_set.add(n)
                    s.save()

                if not s:
                    created = Source.objects.create(name=source)
                    if created:
                        print(f'created news source with name {source}')
                        
                        s = Source.objects.get(name=source)
                        s.news_set.add(n)
                        s.save()

                    else:
                        print(f'could not create a new source {source}')
            else:
                print(f'{r.get("title")}({r.get("source")}) has added to database')
                
        
    return f'saved {total}'
