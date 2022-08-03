from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_crafts, name='crafts')
]
