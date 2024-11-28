from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from engine.services import ContentBasedRecommender
from hustlesasa.serializers import EventTicketSerializer


class RecommendationView(APIView):
    
    def get(self, request):
        """
        Get personalized event ticket recommendations
        
        Required Query Parameters:
        - user_id: Specify a user ID to get recommendations for
        """
        # Get user_id from query parameters
        user_id = request.query_params.get('user_id')
        
        # Validate user_id is present
        if not user_id:
            return Response({
                'error': 'user_id parameter is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            target_user = User.objects.get(id=user_id)
    
            # Get recommendations for the target user
            recommendations = ContentBasedRecommender.recommend_tickets(target_user)
            serializer = EventTicketSerializer(recommendations, many=True)
            
            return Response({
                'user_id': target_user.id,
                'recommendations': serializer.data
            })
        
        except User.DoesNotExist:
            return Response({
                'error': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)