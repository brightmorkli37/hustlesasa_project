from django.contrib.auth.models import User
from rest_framework import serializers
from hustlesasa.models import TicketPurchase
from hustlesasa.serializers import UserSerializer, EventTicketSerializer


class TicketPurchaseSerializer(serializers.ModelSerializer):
    """Serializer for Event Ticket Purchase"""

    total_price = serializers.SerializerMethodField() 

    class Meta:
        model = TicketPurchase
        fields = ['user', 'ticket', 'quantity', 'total_price', 'created_at', 'updated_at']

    def get_total_price(self, obj):
        """Calculate total price for the ticket purchase"""

        if obj.ticket and obj.ticket.price is not None:
            return obj.quantity * obj.ticket.price
        return None
    
    def to_representation(self, instance):

        """shows the names of the user and ticket on the data"""
        ret = super().to_representation(instance)
        
        if instance.user:
            ret['user'] = UserSerializer(instance.user).data
        
        if instance.ticket:
            ret['ticket'] = EventTicketSerializer(instance.ticket).data
        
        return ret