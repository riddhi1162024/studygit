
# urls.py (in your app)
from django.urls import path
from .views import book_list,book_detail

urlpatterns =[
    path('book_list/',book_list),
    path('book_detail/<int:pk>/',book_detail)]


