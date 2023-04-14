from django.urls import path
from news import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', views.NewsViewSet)
router.register('source',views.SourceViewSet)

urlpatterns = [
    path('search', views.search_news)
] + router.urls 


