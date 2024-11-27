import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
 
API = os.getenv('GEMINI_API')
genai.configure(
  api_key=API
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

def gemi(prompt):
  
  try:
    response = chat.send_message(prompt)
    return response.text.replace("*","")
  except Exception as error:
    return f"Error occurred: {error}"