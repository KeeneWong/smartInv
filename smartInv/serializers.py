from rest_framework import serializers
from .models import Item, Catergory


class ItemSerializer(serializers.ModelSerializer):
    # catergory = serializers.HyperlinkedRelatedField(
    #     view_name='catergory_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Item
        fields = ('id', 'name', 'describtion', 'quantity',
                  'image_url', 'prize', 'alive', 'catergory')


class CatergorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catergory
        fields = ('title', 'image_url')
