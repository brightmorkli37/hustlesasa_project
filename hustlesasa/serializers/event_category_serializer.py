from rest_framework import serializers
from hustlesasa.models import EventCategory
    

class EventCategorySerializer(serializers.ModelSerializer):
    """Serializer for EventCategory"""

    class Meta:
        model = EventCategory
        fields = ['name',]