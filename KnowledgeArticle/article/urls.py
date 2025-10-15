from django.urls import path
from .views import ListArticlesView, CreateArticleView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    path('list-articles', ListArticlesView.as_view(), name='article'),
    path('create-article', CreateArticleView.as_view(), name='article'),
    path('update-article/<int:pk>', UpdateArticleView.as_view(), name='article'),
    path('delete-article/<int:pk>', DeleteArticleView.as_view(), name='article')
]