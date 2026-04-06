# install langchain and langchain-google-genai
from langchain.chat_models import init_chat_model
GOOGLE_API_KEY = "AIzaSyDGW611tHmX3gGI9-7dJSfjJtVrC_YlgA8"

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY)

with open('wood.txt') as file:
    wood = file.read()

response = model.invoke(f"Which wood is best for making furniture: {wood}")
print(response.content[0]['text'])