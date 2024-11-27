from rest_framework import serializers
from hustlesasa.models import EventCategory, EventTicket
from hustlesasa.serializers import EventCategorySerializer

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

    def to_representation(self, instance):
        """Show category name on the data"""

        ret = super().to_representation(instance)
        
        if instance.category.exists():
            ret['category'] = EventCategorySerializer(instance.category.all(), many=True).data
        
        return ret