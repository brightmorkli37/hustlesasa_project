from django.urls import path
from engine.views import RecommendationViewSet

urlpatterns = [
    path('recommendations/', RecommendationViewSet.as_view(), name='event-recommendations'),
]