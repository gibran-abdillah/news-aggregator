from rest_framework import serializers

from .models import News, Source

class NewsSerializer(serializers.ModelSerializer):

    source = serializers.CharField(source='source.name')

    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'date',
            'source'
        ]

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source 
        fields = '__all__'

