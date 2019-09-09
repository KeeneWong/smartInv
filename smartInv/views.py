from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemSerializer, CatergorySerializer
from .models import Item, Catergory


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CatergoryList(generics.ListCreateAPIView):
    queryset = Catergory.objects.all()
    serializer_class = CatergorySerializer


class CatergoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catergory.objects.all()
    serializer_class = CatergorySerializer


# Create your views here.
