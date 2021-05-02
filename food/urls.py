from . import views
from django.urls import path

#namespace
app_name = 'food'

urlpatterns = [
    path('',views.IndexClassViews.as_view(), name='index'),
    #/food/1
    path('<int:pk>', views.DetailViewClass.as_view(), name='details'),
    path('item/', views.foodList, name='item'),
    #adding an item
    path('create', views.create_item, name='create_item'),
    #update the item
    path('update/<int:id>/', views.update_item, name='update_item'),
    #delete_item
    path('delete/<int:id>/', views.delete_item, name='delete_item'),


]