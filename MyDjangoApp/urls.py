from django.urls import path
from MyDjangoApp import views

urlpatterns = [
    path('', views.MyDjangoApp, name='MyDjangoApp'),
]
