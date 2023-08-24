"""
This module is to test calling the OpenAI API.
"""

import os
import openai
from openai_config.fitness_presets import parameters, job, concision

api_key = os.getenv("OPENAI_KEY")


# Check API key found
if api_key:
    print("OpenAI API key found.")
    print("")
    openai.api_key = api_key
else:
    print("OpenAI API key not found.")


def generate_response(user_input, model_name='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=parameters['model'],
        messages=[
            {"role": "system", "content": job+concision},
            {"role": "user", "content": user_input}
        ],
        temperature=parameters['temperature'],
        max_tokens=parameters['max_tokens'],
        top_p=parameters['top_p'],
        frequency_penalty=parameters['frequency_penalty'],
        presence_penalty=parameters['presence_penalty'],
    )
    return response.choices[0].message['content'].strip()


user_input = '''
    I want a fitness plan for weight loss.
    I like swimming and want to do weight lifting to get toned too.
    I can't do deadlifts."
'''
output = generate_response(user_input)
print(output)
