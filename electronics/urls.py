from django.urls import path
from rest_framework.routers import SimpleRouter
from electronics.views import ContactViewSet, ProductViewSet, TradeNetworkCreateAPIView, TradeNetworkListAPIView, \
    TradeNetworkRetrieveAPIView, TradeNetworkUpdateAPIView, TradeNetworkDestroyAPIView
from electronics.apps import ElectronicsConfig

app_name = ElectronicsConfig.name

router = SimpleRouter()
router.register('', ContactViewSet, basename='contact')

prod_router = SimpleRouter()
prod_router.register('', ProductViewSet, basename='product')

urlpatterns = [
    path('net_create/', TradeNetworkCreateAPIView.as_view(), name='network_create'),
    path('net_list/', TradeNetworkListAPIView.as_view(), name='network_list'),
    path('net_detail/', TradeNetworkRetrieveAPIView.as_view(), name='network_detail'),
    path('net_update/', TradeNetworkUpdateAPIView.as_view(), name='network_update'),
    path('net_destroy/', TradeNetworkDestroyAPIView.as_view(), name='network_destroy'),

              ] + router.urls + prod_router.urls
