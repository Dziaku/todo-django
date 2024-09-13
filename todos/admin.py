from django.contrib import admin

# Register your models here.
from .models import Item, List


admin.site.register(List)
admin.site.register(Item)