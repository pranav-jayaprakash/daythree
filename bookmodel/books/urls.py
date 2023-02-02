from django.urls import path

from books import  views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('authors/',views.AuthorList.as_view(), name='authors'),
    path('create/',views.CreateBook.as_view(), name='create_book'),
    path('detail/<int:pk>/',views.ViewBook.as_view(), name='detail_book'),
    path('update/<int:pk>/', views.UpdateBook.as_view(),name='update_book'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(),name='delete_book'),
]