# models/gemini.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env into os.environ
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def query_gemini(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text