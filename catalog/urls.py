from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog'),
    path('test/', views.BookCreate.as_view(), name='test'),
    path('contact/', views.contact_view, name='contact'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
]
