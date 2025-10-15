from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from .models import Article
from .serializers import ArticleSerializer
from user.permissions import IsAdminUser, IsEditorUser, IsViewerUser, IsAdminOrEditorUser

class ListArticlesView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CreateArticleView(CreateAPIView):
    permission_classes = [IsAdminOrEditorUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class UpdateArticleView(UpdateAPIView):
    permission_classes = [IsAdminOrEditorUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class DeleteArticleView(DestroyAPIView):
    permission_classes = [IsAdminOrEditorUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

