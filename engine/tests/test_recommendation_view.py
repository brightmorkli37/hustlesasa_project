import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from hustlesasa.models import EventTicket, TicketPurchase, EventCategory
from datetime import date, time, timedelta


@pytest.mark.django_db
class TestRecommendationView:
    """Test View for testing the various recommendation outcomes"""

    def setup_method(self):
        """
        Setup method to create test data before each test
        """
        self.client = APIClient()
        
        # Create test users
        self.user1 = User.objects.create_user(
            username='testuser1', 
            email='testuser1@example.com'
        )
        self.user2 = User.objects.create_user(
            username='testuser2', 
            email='testuser2@example.com'
        )
        
        # Create test event category
        self.category = EventCategory.objects.create(name='Music')
        
        # Create test event ticket1
        self.ticket1 = EventTicket.objects.create(
            name='Concert A',
            description='Rock concert',
            event_type='single',
            venue='Stadium X',
            price=50.00,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            start_time=time(19, 0),
            end_time=time(22, 0),
        )
        self.ticket1.category.add(self.category)
        
        # Create test event ticket2
        self.ticket2 = EventTicket.objects.create(
            name='Concert B',
            description='Jazz performance',
            event_type='single',
            venue='Hall Y',
            price=75.00,
            start_date=date.today() + timedelta(days=7),
            end_date=date.today() + timedelta(days=8),
            start_time=time(20, 0),
            end_time=time(23, 0),
        )
        self.ticket2.category.add(self.category)
        
        # Create a ticket purchase for user
        TicketPurchase.objects.create(
            user=self.user1, 
            ticket=self.ticket1
        )


    def test_get_recommendations_success(self):
        """
        Test successful ticket recommendations
        """
        url = f'/api/v1/user/recommendations/?user_id={self.user1.id}'
        
        # Use patch to mock the recommendation method
        with patch('engine.services.ContentBasedRecommender.recommend_tickets') as mock_recommend:
            mock_recommend.return_value = [self.ticket2]
            
            response = self.client.get(url)
            
            assert response.status_code == status.HTTP_200_OK
            assert len(response.data['recommendations']) > 0
            assert response.data['user_id'] == self.user1.id

    def test_recommendations_missing_user_id(self):
        """
        Test API response when user_id is not provided
        """
        url = '/api/v1/user/recommendations/'
        
        response = self.client.get(url)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'user_id parameter is required' in str(response.data)

    def test_recommendations_nonexistent_user(self):
        """
        Test API response for a non-existent user
        """
        # Use an id that does not exist
        nonexistent_user_id = 999
        url = f'/api/v1/user/recommendations/?user_id={nonexistent_user_id}'
        
        response = self.client.get(url)
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert 'User not found' in str(response.data)

    def test_recommendations_no_purchase_history(self):
        """
        Test recommendations for a user with no purchase history
        """
        url = f'/api/v1/user/recommendations/?user_id={self.user2.id}'
        
        # Use patch to verify the fallback to most recent tickets
        with patch('engine.services.ContentBasedRecommender.recommend_tickets') as mock_recommend:
            mock_recommend.return_value = [self.ticket1, self.ticket2]
            
            response = self.client.get(url)
            
            assert response.status_code == status.HTTP_200_OK
            assert len(response.data['recommendations']) > 0

@pytest.fixture(scope='module')
def django_db_setup():
    """Optional database setup configuration"""
    pass