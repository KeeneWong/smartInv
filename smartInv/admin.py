from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

from .models import Item, Catergory, User

admin.site.register([Item, Catergory])
