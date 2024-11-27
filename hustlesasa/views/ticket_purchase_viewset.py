from rest_framework.viewsets import ModelViewSet
from hustlesasa.models import TicketPurchase
from hustlesasa.serializers import TicketPurchaseSerializer


class TicketPurchaseViewSet(ModelViewSet):
    """
    ViewSet for managing Event Tickets
    """
    queryset = TicketPurchase.objects.all()
    serializer_class = TicketPurchaseSerializer