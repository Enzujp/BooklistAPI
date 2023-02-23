from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name="books"),
    #need to add another path 
]