from django.db.models.signals import post_save
from django.dispatch import receiver
from openai import OpenAI
from .models import Article
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@receiver(post_save, sender=Article)
def generate_summary(sender, instance, created, **kwargs):
    old_des = sender.objects.get(pk=instance.pk).description

    # if old_des == instance.description:
    #     return

    description = instance.description
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Write a brief summary for this text: {description}"}
            ]
        )
    summary = response.choices[0].message.content
    instance.summary = summary
    # instance.save(update_fields=['summary'])