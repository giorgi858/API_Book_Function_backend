from django.urls import path
from .views import api_home_page, book_detail

urlpatterns = [
    path('books/',api_home_page, name='api_homes'),
    path('books/<int:pk>/', book_detail, name='book_detail')
]

