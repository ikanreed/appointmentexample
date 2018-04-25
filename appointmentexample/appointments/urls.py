from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.onlypage, name="index"),
    ]
