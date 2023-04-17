from django.core.management import BaseCommand
from utils.scrape import main

from news.models import News, Source
class Command(BaseCommand):
    help = "Scrape news from modules"

    def handle(self, *args, **kwargs):
        result = main()
        if not result:
            self.stdout.write("No data to add.")
            return 1 
        
        for x in result:
            for r in x:

                sumber = r.get('source')
                title = r.get('title')
                content = r.get('content')
                date = r.get('date')

                source, created = Source.objects.get_or_create(name=sumber)
                
                n = News.objects.filter(title=title)
                
                if not n:
                    
                    n = News.objects.create(title=title, content=content, date=date)
                    source.news_set.add(n)

                else:
                    print(f'{title} has added to database ')
                    
        return "OK"