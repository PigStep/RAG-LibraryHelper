from google import genai
from dotenv import load_dotenv
import os

load_dotenv() # Get enviromental variabls (API key)
API_KEY = os.getenv("API_KEY")