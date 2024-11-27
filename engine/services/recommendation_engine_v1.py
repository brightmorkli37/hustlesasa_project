from django.db.models import Count
from hustlesasa.models import EventTicket, TicketPurchase


class ContentBasedRecommender:
    @classmethod
    def get_user_category_preferences(cls, user):
        """
        Calculate user's category preferences based on their ticket purchases
        
        Args:
            user (User): The user to analyze
        
        Returns:
            dict: A dictionary of category preferences with their weights
        """
        # Get all ticket purchases for the user
        purchases = TicketPurchase.objects.filter(user=user)
        
        # Calculate category preferences
        category_weights = {}
        total_tickets = purchases.count()
        
        for purchase in purchases:
            ticket = purchase.ticket
            for category in ticket.category.all():
                category_weights[category.name] = category_weights.get(category.name, 0) + 1
        
        # Normalize weights
        normalized_weights = {
            category: count / total_tickets 
            for category, count in category_weights.items()
        }
        
        return normalized_weights

    @classmethod
    def recommend_tickets(cls, user, limit=5):
        """
        Recommend event tickets based on user's past purchases
        
        Args:
            user (User): The user to recommend tickets for
            limit (int): Maximum number of recommendations
        
        Returns:
            QuerySet: Recommended event tickets
        """
        # Get user's category preferences
        user_preferences = cls.get_user_category_preferences(user)
        
        if not user_preferences:
            # If no purchase history, return popular tickets
            return EventTicket.objects.annotate(
                purchase_count=Count('event_tickets')
            ).order_by('-purchase_count')[:limit]
        
        # Find tickets with matching categories
        recommended_tickets = EventTicket.objects.filter(
            category__name__in=user_preferences.keys()
        ).exclude(
            # Exclude tickets user has already purchased
            id__in=TicketPurchase.objects.filter(user=user).values_list('ticket_id', flat=True)
        ).annotate(
            category_match_score=Count('category', filter=models.Q(
                category__name__in=user_preferences.keys()
            ))
        ).order_by('-category_match_score')[:limit]
        
        return recommended_tickets