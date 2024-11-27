from rest_framework import serializers
from hustlesasa.models import EventCategory, EventTicket


class NestedRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return str(instance)


class EventTicketSerializer(serializers.ModelSerializer):
    """Serializer for EventTicket"""

    category = NestedRelatedField(queryset=EventCategory.objects.all(), many=True, required=False)

    class Meta:
        model = EventTicket
        fields = ['id', 'name', 'description', 'category',
            'event_type', 'start_date', 'end_date', 'start_time', 'end_time',            
            'venue', 'price', 'created_at', 'updated_at',            
        ]