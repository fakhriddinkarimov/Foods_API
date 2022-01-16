from django.urls import path
from .views import FoodwView
urlpatterns = [
    path('foods/',FoodwView.as_view(),name='foods-list'),
    path('foods/<int:pk>/',FoodwView.as_view(),name='food-one')
]