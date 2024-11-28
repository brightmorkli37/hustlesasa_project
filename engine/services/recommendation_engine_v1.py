import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.db.models import Q
from django.contrib.auth.models import User
from hustlesasa.models import EventTicket, TicketPurchase, EventCategory


class ContentBasedRecommender:
    @classmethod
    def prepare_ticket_features(cls):
        """
        Prepare feature matrix for all event tickets
        
        Returns:
            tuple: (feature_matrix, ticket_ids, vectorizer)
        """
        # Fetch all tickets
        tickets = EventTicket.objects.all()
        
        # Prepare feature text
        def prepare_feature_text(ticket):
            # Combine relevant fields into a single text feature
            categories = ' '.join(ticket.category.values_list('name', flat=True))
            return f"{ticket.name} {ticket.description} {categories} {ticket.event_type} {ticket.venue} {str(ticket.price)}"
        
        # Prepare features
        feature_texts = [prepare_feature_text(ticket) for ticket in tickets]
        
        # Create TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words='english')
        feature_matrix = vectorizer.fit_transform(feature_texts)
        
        # Store ticket IDs for reference
        ticket_ids = list(tickets.values_list('id', flat=True))
        
        return feature_matrix, ticket_ids, vectorizer

    @classmethod
    def get_user_ticket_profile(cls, user_id):
        """
        Create a profile of tickets purchased by the user
        
        Args:
            user_id (UUID): The user ID to profile
        
        Returns:
            numpy.ndarray or None: User's ticket profile
        """
        # Get user's purchased tickets
        purchased_tickets = TicketPurchase.objects.filter(user_id=user_id).values_list('ticket_id', flat=True)
        
        if not purchased_tickets:
            return None
        
        # Prepare feature matrix
        feature_matrix, ticket_ids, vectorizer = cls.prepare_ticket_features()
        
        # Find indices of purchased tickets
        purchased_indices = [ticket_ids.index(ticket_id) for ticket_id in purchased_tickets]
        
        # Compute user profile as average of purchased ticket features
        # Convert to dense numpy array and compute mean
        user_profile = np.asarray(feature_matrix[purchased_indices].mean(axis=0)).flatten()
        
        return user_profile

    @classmethod
    def recommend_tickets(cls, user_id, limit=5):
        """
        Recommend tickets based on user's purchase history
        
        Args:
            user_id (UUID): The user ID to recommend tickets for
            limit (int): Maximum number of recommendations
        
        Returns:
            QuerySet: Recommended event tickets
        """
        # Prepare feature matrix
        feature_matrix, ticket_ids, vectorizer = cls.prepare_ticket_features()
        
        # Get user's ticket profile
        user_profile = cls.get_user_ticket_profile(user_id)
        
        # If no purchase history, return most recent tickets
        if user_profile is None:
            return EventTicket.objects.order_by('-created_at')[:limit]
        
        # Ensure user_profile is a 2D array for cosine_similarity
        user_profile_2d = user_profile.reshape(1, -1)
        
        # Convert feature matrix to dense array
        feature_matrix_dense = feature_matrix.toarray()
        
        # Compute similarity between user profile and all tickets
        similarities = cosine_similarity(user_profile_2d, feature_matrix_dense)[0]
        
        # Exclude already purchased tickets
        purchased_tickets = TicketPurchase.objects.filter(user_id=user_id).values_list('ticket_id', flat=True)
        
        # Get top similar ticket indices
        similar_indices = similarities.argsort()[::-1]
        
        # Filter and collect recommendations
        recommended_ticket_ids = []
        for idx in similar_indices:
            ticket_id = ticket_ids[idx]
            if ticket_id not in purchased_tickets:
                recommended_ticket_ids.append(ticket_id)
                if len(recommended_ticket_ids) == limit:
                    break
        
        # Return recommended tickets, preserving order
        return EventTicket.objects.filter(id__in=recommended_ticket_ids)