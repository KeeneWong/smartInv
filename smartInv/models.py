from django.db import models
import datetime

# Create your models here.


class Catergory(models.Model):
    title = models.CharField(default="other", max_length=50)
    image_url = models.TextField(null=False)

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(default="", max_length=30)
    describtion = models.CharField(default="", max_length=100)
    quantity = models.IntegerField(default=0)
    image_url = models.TextField(null=True)
    prize = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    alive = models.BooleanField(default=True)
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='items')
    catergory = models.ForeignKey(
        Catergory, on_delete=models.SET_NULL, related_name='items2', null=True
    )

    def __str__(self):
        return self.name
