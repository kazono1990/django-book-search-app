from django.urls import path
from .views import book_search

urlpatterns = [
    path('', book_search, name='book_search'),
]

