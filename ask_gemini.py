import os
from google import genai
from google.genai import types
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(text):
    prompt = "Find what is needed in this job add - write what web projects are mentioned, give years of experience if there is any mentioned of that, then coding languages in 20 words or less. Write this as a simple text not a markdown."
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=[prompt, text]
    )
   
    return json.dumps(response.text)
