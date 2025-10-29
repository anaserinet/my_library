from django.contrib import admin
from django.urls import path
from loans import views

urlpatterns = [
    path('', views.welcome, name='home'),       # 👈 for root URL
    path('welcome/', views.welcome, name='welcome'),
    path('books/', views.books, name='books'),
    # matched anything of the form book/(any integer)
    # ex: http://127.0.0.1:8000/book/1
    path('book/<int:book_id>', views.get_book, name='get_book'),
    path('book/<int:book_id>/foobar/<int:foo>',
         # ex: http://127.0.0.1:8000/book/1/foobar/2/3
         views.get_book2, name='get_book2'),
    path('create_book/', views.create_book, name='create_book'),
    path('admin/', admin.site.urls),
]
