from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from hustlesasa.models import EventTicket
from hustlesasa.serializers import EventTicketSerializer


class EventTicketViewSet(ModelViewSet):
    """
    ViewSet for managing Event Tickets
    """
    queryset = EventTicket.objects.all()
    serializer_class = EventTicketSerializer