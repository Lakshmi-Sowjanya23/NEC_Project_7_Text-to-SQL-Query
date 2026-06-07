import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hello")

print(response.text)