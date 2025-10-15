from django.urls import path
from .views import KnowledgeView, CreateKnowledgeView, EditKnowledgeView, DeleteKnowledgeView

urlpatterns = [
    path('list-knowledge', KnowledgeView.as_view(), name='knowledge'),
    path('create-knowledge', CreateKnowledgeView.as_view(), name='knowledge'),
    path('edit-knowledge/<int:pk>', EditKnowledgeView.as_view(), name='knowledge'),
    path('delete-knowledge/<int:pk>', DeleteKnowledgeView.as_view(), name='knowledge')
]
