from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from electronics.models import Contact, TradeNetwork
from electronics.serializers import ContactSerializer, ProductSerializer, TradeNetworkSerializer
from users.permissions import ActiveUser


class ContactViewSet(viewsets.ModelViewSet):

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [ActiveUser]


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Contact.objects.all()
    permission_classes = [ActiveUser]



class TradeNetworkCreateAPIView(generics.CreateAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated, ActiveUser]


class TradeNetworkListAPIView(generics.ListAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated, ActiveUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['contact__country']


class TradeNetworkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated, ActiveUser]

class TradeNetworkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated, ActiveUser]


class TradeNetworkDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated, ActiveUser]