from django.contrib import admin

# Register your models here.

from .models import Item, Catergory

admin.site.register([Item, Catergory])
