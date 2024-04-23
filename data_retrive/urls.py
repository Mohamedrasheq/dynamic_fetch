from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.hello,name="hello"),
    path('enter',views.datastore,name="datastore"),
    path('<str:pk>',views.index,name="index"),
    
]