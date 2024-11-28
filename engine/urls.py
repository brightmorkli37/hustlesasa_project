from django.urls import path
from engine.views import RecommendationView

urlpatterns = [
    path('user/recommendations/', RecommendationView.as_view(), name='event-recommendations'),
]