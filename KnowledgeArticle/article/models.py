from django.db import models
from knowledge.models import Knowledge
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(validators=[MinLengthValidator(50)])
    summary = models.TextField()
    knowledge = models.ForeignKey(Knowledge, on_delete=models.CASCADE, related_name="Knowledge")
    creator = models.ForeignKey(User , on_delete=models.CASCADE, related_name="Creator")