import os
from google import genai
from google.genai import types
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
prompt = "Find what is needed in this job add at {url} - write what web projects are mentioned, give years of experience if there is any mentioned of that, then coding languages in 20 words or less. Text can be either in English or Lithuanian languages, so respond with the same language. Write this as a simple text not a markdown."


def ask_gemini(text):

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", 
        contents=[prompt, text],
        config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
    )
   
    return json.dumps(response.text)
