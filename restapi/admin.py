from django.contrib import admin
from .models import Food, FoodCategory


admin.site.register(FoodCategory)
admin.site.register(Food)
