"""
This module is to test calling the OpenAI API.
"""

import os
import openai
from openai_config.fitness_presets import parameters, job, concision
from openai_config.fitness_presets import ask_questions

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


test_input = ask_questions()
test_output = generate_response(test_input)
print(test_output)

# test_input = '''
#     I want a fitness plan to get faster in swimming sprints.
#     I like swimming and want to do weight lifting to get toned too.
#     I don't want to do deadlifts.
# '''
# output = generate_response(test_input)
# print(output)

# test_response = '''
# Sure! Here's a personalized fitness plan to help you improve your
# swimming sprints and tone your body without including deadlifts:

# Day 1: Swimming Workout

# Exercise | Sets x Reps | Rest
# --- | --- | ---
# Warm-up (freestyle) | 1 x 400 meters |
# Sprint (freestyle) | 10 x 50 meters | 30 seconds
# Rest | 1 minute |
# Kick (with kickboard) | 4 x 100 meters | 20 seconds
# Cool-down (choice of stroke) | 1 x 200 meters |

# Day 2: Weight Training - Upper Body

# Exercise | Sets x Reps | Rest
# --- | --- | ---
# Bench Press | 3 x 8-10 | 1-2 minutes
# Shoulder Press | 3 x 8-10 | 1-2 minutes
# Dumbbell Rows | 3 x 8-10 | 1-2 minutes
# Chest Flyes | 3 x 10-12 | 1-2 minutes
# Tricep Dips | 3 x 10-12 | 1-2 minutes

# Day 3: Rest or Light Cardio

# Day 4: Swimming Workout

# Exercise | Sets x Reps | Rest
# --- | --- | ---
# Warm-up (choice of stroke) | 1 x 400 meters |
# Sprint (choice of stroke) | 6 x 100 meters | 45 seconds
# Rest | 1 minute |
# Pull (using pull buoy) | 4 x 150 meters | 20 seconds
# Cool-down (choice of stroke) | 1 x 200 meters |

# Day 5: Weight Training - Lower Body

# Exercise | Sets x Reps | Rest
# --- | --- | ---
# Squats | 3 x 8-10 | 1-2 minutes
# Lunges | 3 x 10-12 | 1-2 minutes
# Leg Press | 3 x 8-10 | 1-2 minutes
# Calf Raises | 3 x 12-15 | 1-2 minutes
# Glute Bridges | 3 x 10-12 | 1-2 minutes

# Day 6: Rest or Light Cardio

# Day 7: Rest

# Remember to listen to your body and adjust the weights
# and intensity as needed. Stay consistent and gradually
# increase the weights or reps over time to continue
# challenging your muscles and improving your swimming performance.
# '''
