from celery import shared_task
from openai import OpenAI
from .models import Article
from dotenv import load_dotenv
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@shared_task(queue='default')
def get_openai_info(article_id):
    article = Article.objects.get(id=article_id)
    if not article or not article.description:
        return
    
    description = article.description
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Write a brief summary for this text: {description}"}
            ]
        )
    summary = response.choices[0].message.content
    article.summary = summary
    article.save()