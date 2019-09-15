from django.conf import settings
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Catergory(models.Model):
    title = models.CharField(default="other", max_length=50, null=False)
    image_url = models.TextField(null=False)

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(default="", max_length=30, null=False)
    describtion = models.CharField(default="", max_length=100)
    quantity = models.IntegerField(default=1, null=False)
    image_url = models.TextField(null=True)
    prize = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=False)
    alive = models.BooleanField(default=True, null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False)
    catergory = models.ForeignKey(
        Catergory, on_delete=models.SET_NULL, related_name='items', null=True
    )

    def __str__(self):
        return self.name
