import uuid
from django.db import models
from django.contrib.auth.models import User
from hustlesasa.models import EventTicket


class TicketPurchase(models.Model):
    """Model for Ticket Purchases"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    ticket = models.ForeignKey(EventTicket, on_delete=models.SET_NULL, related_name='event_tickets', null=True)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)