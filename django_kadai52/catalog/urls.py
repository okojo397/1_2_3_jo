from django.urls import path
from .views import BookList
app_name = 'catalog'
urlpatterns = [ path('', BookList.as_view(), name='book_list') ]
