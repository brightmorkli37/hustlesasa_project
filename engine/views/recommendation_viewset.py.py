from rest_framework.views import APIView
from rest_framework.response import Response
from engine.services import ContentBasedRecommender
from hustlesasa.serializers import EventTicketSerializer


class RecommendationViewSet(APIView):
    
    def get_queryset(self, request):
        """
        Get personalized event ticket recommendations
        """
        recommendations = ContentBasedRecommender.recommend_tickets(request.user)
        serializer = EventTicketSerializer(recommendations, many=True)
        
        return Response({
            'recommendations': serializer.data
        })