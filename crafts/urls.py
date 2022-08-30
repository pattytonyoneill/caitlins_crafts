from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_crafts, name='crafts'),
    path('<int:craft_id>/', views.craft_detail, name='craft_detail'),
    path('add/', views.add_craft, name='add_craft'),
    path('edit/<int:craft_id>/', views.edit_craft, name='edit_craft'),
]
