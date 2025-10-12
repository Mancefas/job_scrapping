import os
from google import genai
from google.genai import types
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = "gemini-2.5-flash"

tools = [{"url_context": {}}]

system_prompt = """
You are a professional recruiter assistant.
You analyze job descriptions and my provided experiences and licences/certifications to evaluate how well I would fit the role.
The CV will be provided as a json file.

Your tasks:
1. Compare the my skills, experience to the job requirements.
2. Provide a match percentage (0-100%) based on relevance.
3. List missing skills or qualifications that would improve the match.
4. Note if the I appears overqualified or underqualified.
5. Keep your feedback clear, structured, and actionable.
7. Use the following format and return only this: 

    {
        "match_percentage": (integer 0-100),
        "summary": (short text summary),
        "strengths": [list of strengths],
        "missing_qualifications": [list of missing or weak areas],
        "overqualified_areas": [list of overqualified aspects if any],
        "recommendations": (short actionable advice)
    }
8. Write this as a simple text not a markdown.
9. Be concise, limit to 150 words.
"""

with open("myCv.json", "r") as file:
    data = json.load(file)

experiences = data["experience"]
licences = data["licenses_certifications"]

def ask_gemini_recruiter(job_description):

    user_prompt = f"""
    Job description: {job_description}
    My experiences: {experiences}
    My licences/certifications: {licences}
    """
    response = client.models.generate_content(
        model=model, 
        contents=user_prompt,
        config=types.GenerateContentConfig( system_instruction=system_prompt)
    )
   
    return json.dumps(response.text)
