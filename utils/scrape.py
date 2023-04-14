from .core.utils import get_scaraper
import json 

def main():
    scrapers = get_scaraper()
    
    data = []
    
    total = 0 

    for scraper in scrapers:
        cls = scraper()
        result = cls.main()
        if result:
            total += len(result)
            data.append(result)
    
    return data 
