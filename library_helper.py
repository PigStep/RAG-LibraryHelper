from api_key import API_KEY
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-r1-0528-qwen3-8b:free",
  messages=[
    {
      "role": "user",
      "content": "Say hi to my project! In russian"
    }
  ]
)
print(completion.choices[0].message.content)