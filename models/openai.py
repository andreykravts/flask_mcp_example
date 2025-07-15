# models/openai.py

import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def query_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }]
    )
    return response.choices[0].message.content