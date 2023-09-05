# Import libraries/API key
import os
import openai
from openai_config.fitness_presets import parameters, job, concision

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

"""
These specifications function ask the user activity-specific
questions to feed into the system instructions.
"""


def lifting_specified():
    experience = input("How many years of experience do you have lifting? ")
    limitations = input("Any movements you don't want to or cannot do? ")
    goal = input(
        "What is your primary goal with lifting (e.g. getting stronger, "
        "building muscle, more flexible) ")
    output = f'''
        Lifting specifications:
        Experience level: {experience}
        Limitations: include alternative movements - {limitations}
        Primary goal: {goal}'''

    return output


def calisthenics_specified():
    experience = input(
        "How many years of experience do you "
        "have with bodyweight fitness? ")
    skillset = input(
        "What movements can you do currently "
        "for 5-10 repetitions? e.g. Pull-ups, push-ups, squats. ")
    goal = input(
        "What is your primary goal with calisthenics? For "
        "example, you could say 'I want to do a one-arm pull-up', "
        "or 'I want to get stronger overall'. ")

    output = f'''
        Calisthenics specifications:
        Experience level: {experience}
        Limitations: include alternative movements - {skillset}
        Primary goal: {goal}'''

    return output


def yoga_specified():
    experience = input(
        "Have you done yoga before? If so, how long have you been doing it? ")
    skills = input("How flexible are you? ")
    goal = input(
        "What is your primary goal with yoga? For example, you could "
        "say 'I want to be more flexible', or 'I want to get stronger'. ")

    output = f'''
        Yoga specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def jogging_specified():
    experience = input("How much experience do you have with jogging "
                       "on a plan or regularly (2 or more times per week)? ")
    skills = input("How long can you jog before you need to "
                   "walk or take a break? ")
    goal = input("What is your primary goal for focusing on "
                 "running - speed, endurance, weight loss, overall "
                 "improvement, fun, something else? ")
    output = f'''
        Jogging/running specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def hiking_specified():
    experience = input("How much experience do you have with hiking? ")
    skills = input("How comfortable are you with elevation gain? ")
    goal = input("What is your primary goal with hiking - "
                 "more time in nature, endurance, weight loss, "
                 "overall health, fun, something else? ")
    output = f'''
        Hiking specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def walking_specified():
    current_activity_level = input("About how many steps per day "
                                   "or miles per day do you walk? ")
    limitations = input("Do you have any limitations with walking "
                        "exercise - past injuries, stairs, steep downward "
                        "slopes, etc.? ")
    goal = input("What is your primary goal with walking? ")
    output = f'''
        Walking specifications:
        Current activity level: {current_activity_level}
        Limitations: {limitations}
        Primary goal: {goal}'''

    return output


def swimming_specified():
    experience = input("How much experience do you have with swimming? ")
    skills = input("What strokes can you currently or want "
                   "to swim? (freestyle, backstroke, butterfly, "
                   "or breaststroke) ")
    goal = input("What is your primary goal with swimming? ")
    output = f'''
        Swimming specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def sport_climbing_specified():
    experience = input("How much experience do you have with "
                       "sport climbing/top roping? ")
    skills = input("What climbing grade are you comfortable doing?  ")
    goal = input("What is your primary goal with sport climbing?  "
                 "Remember, having fun is a valid reason! ")
    output = f'''
        Sport climbing specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def bouldering_specified():
    experience = input("How much experience do you have with bouldering? ")
    skills = input("What climbing grade are you comfortable doing? ")
    goal = input("What is your primary goal with bouldering? "
                 "Remember, having fun is a valid reason! ")
    output = f'''
        Bouldering specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def rowing_specified():
    experience = input("How much experience do you have with rowing? ")
    skills = input("What climbing grade are you comfortable doing?  ")
    goal = input("What is your primary goal with rowing? For example, "
                 "you could say 'lose weight' or 'get in better shape'. ")
    output = f'''
        Rowing specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def other_specified():
    clarifier = input("You said you want to practice another activity. "
                      "What is it? ")
    skills = input("Please explain your level of experience in this "
                   "activity? ")
    goal = input("What are your goals or reasoning for pursuing this "
                 "activity? ")

    output = f'''
        Other specifications:
        Activity: {clarifier}
        Skills: {skills}
        Primary goal: {goal}'''

    return output


# Sports switches
activities_dict = {
    'lifting': ['Weight lifting', 0],
    'calisthenics': ['Calisthenics (body weight strength)', 0],
    'yoga': ['Yoga', 0],
    'jogging': ['Jogging/running', 0],
    'hiking': ['Hiking', 0],
    'walking': ['Walking', 0],
    'swimming': ['Swimming', 0],
    'sport_climbing': ['Climbing (top-roping, lead climbing)', 0],
    'bouldering': ['Bouldering', 0],
    'rowing': ['Rowing', 0],
    'other': ['Other (please specify)', 0]
}


def choose_sports(activities_dict=activities_dict):
    '''
    Asks the user to input what sports or activities they want to focus on.
    When specified, the system will ask activity-specific questions.
    '''
    keys = list(activities_dict.keys())  # creates a list of the keys
    items = list(activities_dict.values())  # creates a list of the values
    activities = []
    bools = []
    for item in items:
        activities.append(item[0])  # Create a list of  activity names
        bools.append(item[1])  # Create a list of booleans for each activity

    print(
        "Please select one to three of the listed sports "
        "from the following list. Type 'done' if you want "
        "to focus on only one or two activites.")
    for i, activity in enumerate(activities):
        print(f"{i+1}: {activity}")

    selected_sports = []
    while len(selected_sports) < 3:
        selection = input("Enter the number of the sport you want "
                          "to select, or 'done' if you are finished: ")
        if selection.lower() == 'done':
            break
        elif selection.isdigit() and 1 <= int(selection) <= len(activities):
            selected_sport = activities[int(selection) - 1]
            if selected_sport not in selected_sports:
                selected_sports.append(selected_sport)
                activities_dict[keys[int(selection) - 1]][1] = 1
            else:
                print("You've already selected that sport. "
                      "Please choose a different one.")
        else:
            print("Invalid selection. Please enter a number from the "
                  "list, or 'done' if you are finished.")

    selected_keys = [
        key for key, value in activities_dict.items() if value[1] == 1
        ]

    return selected_keys


def ask_questions(selected_keys=choose_sports()):
    outputs = []
    print(f"You selected {selected_keys}. I'm now going to ask you "
          "some specific questions about your selections.")
    print("In your responses, include as much information as you'd like.")
    for key in selected_keys:
        if key == 'lifting':
            lifting_output = lifting_specified()
            outputs.append(lifting_output)
        elif key == 'calisthenics':
            calisthenics_output = calisthenics_specified()
            outputs.append(calisthenics_output)
        elif key == 'yoga':
            yoga_output = yoga_specified()
            outputs.append(yoga_output)
        elif key == 'jogging':
            jogging_output = jogging_specified()
            outputs.append(jogging_output)
        elif key == 'hiking':
            hiking_output = hiking_specified()
            outputs.append(hiking_output)
        elif key == 'walking':
            walking_output = walking_specified()
            outputs.append(walking_output)
        elif key == 'swimming':
            swimming_output = swimming_specified()
            outputs.append(swimming_output)
        elif key == 'sport_climbing':
            sport_climbing_output = sport_climbing_specified()
            outputs.append(sport_climbing_output)
        elif key == 'bouldering':
            bouldering_output = bouldering_specified()
            outputs.append(bouldering_output)
        elif key == 'rowing':
            rowing_output = rowing_specified()
            outputs.append(rowing_output)
        elif key == 'other':
            other_output = other_specified()
            outputs.append(other_output)

    final_output = "\n".join(outputs)
    return final_output


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
