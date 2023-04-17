from django.db import models
from datetime import datetime


class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    

class News(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.today)

    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True)

    
    def save(self, **kwargs) -> None:
    
        if not self.source:
            source = Source.objects.get_or_create(name='unkown')
            s, created = source 
            self.source = s
        
        return super().save(**kwargs)
    
    def __str__(self):
        return self.title 
    