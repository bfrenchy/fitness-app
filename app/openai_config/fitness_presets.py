import os
import openai

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

# Workout routine completion parameters
parameters = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.6,
    "max_tokens": 1000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

# System role will depend on what activities the user likes and can do.
job = '''
    You are a fitness professional. Provide the user with a structured,
    daily, personalized, and specific routine.
    '''

concision = '''
    Be concise and provide the routine and each workout regime in table format.
    '''
