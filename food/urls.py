from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('item/', views.foodList, name='item'),
]