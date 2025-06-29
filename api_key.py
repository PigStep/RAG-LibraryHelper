from dotenv import load_dotenv
import os

load_dotenv() # Get enviromental variables (API key)
API_KEY = os.getenv("API_KEY")


print(f"LLM API key '{API_KEY}' have been setted")