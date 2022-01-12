from django.urls import path
from .views import FoodView
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('foods/', FoodView.as_view({'get': 'list'})),
]