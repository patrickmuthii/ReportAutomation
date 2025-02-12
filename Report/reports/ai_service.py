import openai
from django.conf import settings

def generate_ai_remarks(report):
    """
    Uses OpenAI API to generate AI-powered remarks based on the report content.
    """
    openai.api_key = settings.OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant that provides insightful report summaries."},
            {"role": "user", "content": f"Generate a remark for this report: {report.content}"}
        ]
    )

    return response["choices"][0]["message"]["content"]
