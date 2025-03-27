# app/generator.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def generate_letter(user_profile, relevant_context):
    system_prompt = "You are a legal assistant who writes professional NIW recommendation letters for U.S. immigration."
    user_prompt = f"""
Based on the following applicant profile:

{user_profile}

Add the following examples from previously accepted NIW letters:

{relevant_context}

Generate a new NIW recommendation letter tailored to this applicant.
"""
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content