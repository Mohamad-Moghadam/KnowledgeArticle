from rest_framework.serializers import ModelSerializer
from .models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'summary': {'required': False, 'read_only': False}, 'creator': {'read_only': True}}