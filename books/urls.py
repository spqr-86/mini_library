from django.urls import path
from .views import IndexView, BookDetailView, BookNew, BookUpdate, BookDelete

urlpatterns = [
    path('',
         IndexView.as_view(),
         name='index'),
    path('book/<int:pk>',
         BookDetailView.as_view(),
         name='book_detail'),
    path('book-new/',
         BookNew.as_view(),
         name='book_new'),
    path('book-edit/<str:username>/<int:pk>/',
         BookUpdate.as_view(),
         name='book_edit'),
    path('book-delete/<str:username>/<int:pk>/',
         BookDelete.as_view(),
         name='book_delete'),
]
