from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_llm(question: str, flight_data: str):
    if not flight_data:
        return "Could not retrieve flight data. Please try again later."
    
    template_path = Path("templates")
    template_file = "draft_template.j2"
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_file)

    system_prompt = template.render(
          question = question,
          flight_data = flight_data,
        )
    
    try:
        response = await openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": system_prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating answer: {str(e)}"