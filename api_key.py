from dotenv import load_dotenv
import os

load_dotenv() # Get enviromental variables (API key)
API_KEY = os.getenv("API_KEY")

DB_KEY= os.getenv("DB_KEY")
DB_URL= os.getenv("DB_URL")

print(f"LLM API key '{API_KEY}' have been setted")
print(f"DB API key '{DB_KEY}' have been setted")
print(f"DB URL '{DB_KEY}' have been setted")