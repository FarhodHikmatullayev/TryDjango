from django.urls import path
from .views import article_list, article_detail, article_create_view, article_create_form_view, \
    article_edit_form, article_delete_view

app_name = "articles"

urlpatterns = [
    path('', article_list, name='list'),
    path('article/detail/<slug:slug>/', article_detail, name='detail'),
    path('article/create/', article_create_view, name='create'),
    path('article/create/form/', article_create_form_view, name='create_form'),
    path('article/edit/<slug:slug>/', article_edit_form, name='edit'),
    path('article/delete/<slug:slug>/', article_delete_view, name='delete'),
]
