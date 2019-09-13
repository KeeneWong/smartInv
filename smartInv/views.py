from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemSerializer, CatergorySerializer, UserSerializer, UserSerializer, GroupSerializer
from .models import Item, Catergory
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class ItemList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_queryset(self):
        userid = self.kwargs['userid']
        queryset = Item.objects.filter(user=userid)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CatergoryList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Catergory.objects.all()
    serializer_class = CatergorySerializer


class CatergoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Catergory.objects.all()
    serializer_class = CatergorySerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet2(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
