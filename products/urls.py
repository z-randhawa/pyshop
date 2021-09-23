from django.urls import path
from . import views


# /products (root)

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]