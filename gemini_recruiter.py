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

experiences = [
    {
      "title": "Web Developer (Front-End Focus / Full Stack Exposure)",
      "company": "Hotelston",
      "employment_type": "Full-time",
      "duration": "Feb 2024 - Present (1 yr 9 mos)",
      "location": "Vilnius, Vilniaus, Lithuania · Hybrid",
      "responsibilities": [
        "Implement and optimize front-end interfaces for performance, scalability, and user experience.",
        "Collaborate with cross-functional teams to deliver high-quality software solutions.",
        "Develop and maintain responsive web applications using React, Redux, Java, Springboot, Primefaces, and PostgreSQL.",
        "Continuously improve code quality through reviews, testing, and best practices.",
        "Initially joined as part of the IT support team before transitioning into a development role, leveraging a strong foundation in system support and problem-solving."
      ],
      "skills": ["React.js", "Redux.js" , "Typescript", "Java", "PostgreSQL", "Spring Boot", "PrimeFaces", "Front-End Development", "Full-Stack Development"]
    },
    {
      "title": "Junior Frontend Developer",
      "company": "noblesnipe",
      "employment_type": "Full-time",
      "duration": "Apr 2023 - Aug 2023 (5 mos)",
      "location": "Kaunas, Kaunas, Lithuania · On-site",
      "skills": ["Bitbucket", "Agile Project Management", "React Native", "REST APIs", "Templating", "Git", "Typescript", "Code Review", "Mobile Application Development" ]
    },
    {
      "title": "Customs Specialist",
      "company": "Nordcarrier Baltic, UAB",
      "employment_type": "Full-time",
      "duration": "2014 - Mar 2023 (9 yrs 3 mos)",
      "location": "Kaunas, Kaunas, Lithuania",
      "skills": ["Business Planning", "Import/Export Operations"]
    },
    {
      "title": "Sourcery Academy for Front-End Developers",
      "company": "Cognizant",
      "employment_type": "Internship",
      "duration": "Nov 2022 - Jan 2023 (3 mos)",
      "location": "Kaunas, Kaunas, Lithuania · Hybrid",
      "skills": ["Bitbucket", "Figma", "Storybook", "Front-End Development"]
    },
    {
      "title": "Freelancer on Upwork",
      "company": "Upwork",
      "employment_type": "Freelance",
      "duration": "Dec 2021 - Sep 2022 (10 mos)",
      "focus": "Front-End Development"
    }
  ]

licences = [
    {
      "name": "CS50’s Introduction to Databases with SQL",
      "issuer": "CS50",
      "issued_date": "Aug 2024",
      "skills": ["SQLite", "SQL", "Databases", "SQL database design"]
    },
    {
      "name": "CS50’s Introduction to Cybersecurity",
      "issuer": "CS50",
      "issued_date": "Dec 2023",
      "skills": [
        "Virtual Private Network (VPN)",
        "App Store",
        "Password Management",
        "Cryptography",
        "Hypertext Transfer Protocol Secure (HTTPS)",
        "Cookies",
        "Fingerprinting",
        "Hashing",
        "Two-factor Authentication",
        "DDoS",
        "SQL Injection"
      ]
    },
    {
      "name": "Computer Science 50: Harvard University’s Programming with Python",
      "issuer": "CS50",
      "issued_date": "Oct 2023",
      "skills": ["Python (Programming Language)", "Object-Oriented Programming (OOP)", "Regular Expressions"]
    },
    {
      "name": "Computer Science 50: Harvard University’s Introduction to Computer Science",
      "issuer": "CS50",
      "issued_date": "Sep 2023",
      "skills": ["Python (Programming Language)", "SQLite", "Algorithms", "Flask"]
    },
    {
      "name": "JavaSript Unit Testing",
      "issuer": "Udemy",
      "issued_date": "May 2022",
      "skills": []
    },
    {
      "name": "Next.js & React.js",
      "issuer": "Udemy",
      "issued_date": "Feb 2022",
      "skills": ["Front-End Development"]
    },
    {
      "name": "React - The Complete Guide (incl Hooks, React Router, Redux)",
      "issuer": "Udemy",
      "issued_date": "Dec 2021",
      "skills": ["Redux.js", "Front-End Development"]
    },
    {
      "name": "Learn React Course",
      "issuer": "Codecademy",
      "issued_date": "Oct 2021",
      "skills": []
    },
    {
      "name": "The Complete JavaScript Course 2021",
      "issuer": "Udemy",
      "issued_date": "Sep 2021",
      "skills": []
    },
    {
      "name": "Google Ads For Beginners 2021",
      "issuer": "Udemy",
      "issued_date": "Aug 2021",
      "skills": []
    },
    {
      "name": "Agile in Everyday Practice",
      "issuer": "Danske UNI",
      "issued_date": "Jul 2021",
      "skills": []
    },
    {
      "name": "Building Interactive JavaScript Websites Course",
      "issuer": "Codecademy",
      "issued_date": "Mar 2021",
      "skills": []
    },
    {
      "name": "Learn JavaScript Course",
      "issuer": "Codecademy",
      "issued_date": "Mar 2021",
      "skills": []
    },
    {
      "name": "Responsive Web Design",
      "issuer": "freeCodeCamp",
      "issued_date": "Feb 2021",
      "skills": []
    },
    {
      "name": "Fundamentals of digital marketing",
      "issuer": "Google Digital Garage",
      "issued_date": "Sep 2020",
      "skills": []
    }
  ]

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
