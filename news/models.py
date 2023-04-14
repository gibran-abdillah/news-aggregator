from django.db import models
from datetime import datetime


class Source(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name 
    

class News(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.today)

    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title 
    