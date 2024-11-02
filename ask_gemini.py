import os
import google.generativeai as genai
import json
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(text):

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        ["Find what is needed in this job add - write what web projects are mentioned, give years of experience if there is any mentioned of that, then coding languages in 20 words or less. Write this as a simple text not a markdown.", text])
    return json.dumps(response.text)
