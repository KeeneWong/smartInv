from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Item, Catergory
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'describtion', 'quantity',
                  'image_url', 'prize', 'alive', 'catergory', 'user')


class CatergorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catergory
        fields = ('id', 'title', 'image_url')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
