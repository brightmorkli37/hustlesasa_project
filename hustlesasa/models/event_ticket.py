import uuid
from django.db import models
from hustlesasa.models import EventCategory


class EventTicket(models.Model):
    """Event Ticket Model"""

    EVENT_TYPE_CHOICES = (
        ('group', 'Group'),
        ('single', 'Single'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(EventCategory, blank=True, related_name='categories')
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES, default='single')
    
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    venue = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name