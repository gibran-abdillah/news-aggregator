from django_elasticsearch_dsl import Document 
from django_elasticsearch_dsl.registries import registry
from .models import News 

# setting up the document 
# source : https://django-elasticsearch-dsl.readthedocs.io/en/latest/quickstart.html

@registry.register_document
class NewsDocument(Document):

    class Index:
        name = 'news'
        settings = {
            'number_of_shards':1,
            'number_of_replicas':0
        }
    
    class Django:
        model = News

        fields = [
            'content',
            'title',
            'id',
        ]
