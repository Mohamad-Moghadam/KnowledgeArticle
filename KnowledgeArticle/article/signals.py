from django.db.models.signals import post_save
from django.dispatch import receiver
from openai import OpenAI
from .models import Article
from dotenv import load_dotenv
import os
from django.db.models.signals import pre_save
from .tasks import get_openai_info

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@receiver(post_save, sender=Article)
def generate_summary(sender, instance, created, **kwargs):
    get_openai_info.delay(instance.pk)