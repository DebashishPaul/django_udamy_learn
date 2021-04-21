from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    #/food/1
    path('<int:item_id>', views.details, name='details'),
    path('item/', views.foodList, name='item'),
]