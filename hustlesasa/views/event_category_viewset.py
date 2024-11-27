from rest_framework.viewsets import ModelViewSet
from hustlesasa.models import EventCategory
from hustlesasa.serializers import EventCategorySerializer


class EventCategoryViewSet(ModelViewSet):
    """
    ViewSet for managing Event Categories
    """
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer