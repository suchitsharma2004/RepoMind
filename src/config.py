import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# API keys
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # For GitHub API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# print("GOOGLE_API_KEY:", GOOGLE_API_KEY)  # Debugging line

genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_model(model="gemini-1.5-flash"):
    return genai.GenerativeModel(model)


