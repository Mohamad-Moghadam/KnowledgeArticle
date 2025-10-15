from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from .serializers import KnowledgeSerializer
from .models import Knowledge
from user.permissions import IsAdminUser

class KnowledgeView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer

class CreateKnowledgeView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer

class EditKnowledgeView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer

class DeleteKnowledgeView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer