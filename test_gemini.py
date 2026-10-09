from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What is 25 multiplied by 4? Reply with the answer only."
)

print(response.text)