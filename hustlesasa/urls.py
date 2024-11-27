from rest_framework.routers import DefaultRouter
from hustlesasa.views import (
    EventCategoryViewSet, EventTicketViewSet, 
    TicketPurchaseViewSet, UserViewSet,
)

router = DefaultRouter()
router.register(r'event-categories', EventCategoryViewSet, basename='eventcategory')
router.register(r'event-tickets', EventTicketViewSet, basename='eventticket')
router.register(r'ticket-purchase', TicketPurchaseViewSet, basename='ticketpurchase')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls

