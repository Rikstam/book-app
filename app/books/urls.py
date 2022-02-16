from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("book/<slug:slug>/", views.book_detail, name="book-detail"),
    path("author/<pk>/", views.create_book, name="create-book"),
    path("htmx/create-book-form/", views.create_book_form, name="create-book-form"),
    path("htmx/book/<pk>/", views.detail_book, name="detail-book")
]
