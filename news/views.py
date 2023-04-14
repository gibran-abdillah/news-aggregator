from rest_framework.response import Response
from news.models import News, Source 
from . import serializers
from rest_framework.decorators import api_view
from .utils import create_pagination
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .documents import NewsDocument
from elasticsearch_dsl import Q

class NewsViewSet(viewsets.ViewSet):
    allowed_methods = ['GET']
    queryset = News.objects.all()

    def list(self, request):
        paginated = create_pagination(self.queryset, serializers.NewsSerializer, request)
        return paginated
    
    def retrieve(self, request, pk):
        object = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.NewsSerializer(object)
        return Response(serializer.data)

class SourceViewSet(viewsets.ViewSet):
    allowed_methods = ['GET']
    queryset = Source.objects.all()

    def list(self, request):
        serializer = serializers.SourceSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(self.queryset, pk=pk)
        news_object = queryset.news_set.all()
        return create_pagination(news_object, serializers.NewsSerializer, request)

@api_view(['GET','POST'])
def search_news(request):
    keyword = request.data.get('keyword')
    
    if not keyword:
        return Response({"success":False, "message":"'keyword' data is missing"})
    
    q = Q(
        'bool',
        should=[ 
            Q('match', content=keyword),
            Q('match', title=keyword)
        ]
    )
    document = NewsDocument().search().query(q)
    result = document.execute()
    
    if not result:
        return Response({"success":False, "message":"can't get news that you search for"})
    
    results_id = [_.id for _ in result.hits if _]
    
    # convert `elasticsearch_dsl.response.Response` to QuerySet and return it to pagination
    queryset = News.objects.filter(id__in=results_id)
    paginated = create_pagination(queryset, serializers.NewsSerializer, request)
    
    return paginated 
