from rest_framework.serializers import ModelSerializer
from .models import Knowledge

class KnowledgeSerializer(ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'