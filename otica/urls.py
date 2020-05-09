from django.urls import path
from .views import index,contact,store1,store2,store3

urlpatterns = [
    path('', index),
    path('contact', contact),
    path('store1', store1),
    path('store2', store2),
    path('store3', store3),
]
