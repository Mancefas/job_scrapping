import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_ai(text):
    lt_characters = ["ą", "č", "ę", "ė", "į", "š", "ų", "ū", "ž"]
    if any(letter in lt_characters for letter in text):
        return json.dumps("I don't speek that language")
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Find what is needed in add - give ONLY years of experience, coding languages in max 10 words"
                },
                {"role": "user", "content": text}
            ]
        )
        return json.dumps(completion.choices[0].message["content"])
