# Import libraries/API key
import os
import openai
import tkinter as tk
from tkinter import simpledialog
from openai_config.fitness_presets import parameters, job, concision

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

"""
These specifications function ask the user activity-specific
questions to feed into the system instructions.
"""


def lifting_specified(root):
    experience = simpledialog.askstring("Input","How many years of experience do you have lifting?", parent=root)
    limitations = simpledialog.askstring("Input","Any movements you don't want to or cannot do?", parent=root)
    goal = simpledialog.askstring("Input",
        "What is your primary goal with lifting (e.g. getting stronger, "
        "building muscle, more flexible)", parent=root)
    output = f'''
        Lifting specifications:
        Experience level: {experience}
        Limitations: include alternative movements - {limitations}
        Primary goal: {goal}'''

    return output


def calisthenics_specified(root):
    experience = simpledialog.askstring("Input",
        "How many years of experience do you "
        "have with bodyweight fitness?", parent=root)
    skillset = simpledialog.askstring("Input",
        "What movements can you do currently "
        "for 5-10 repetitions? e.g. Pull-ups, push-ups, squats.", parent=root)
    goal = simpledialog.askstring("Input",
        "What is your primary goal with calisthenics? For "
        "example, you could say 'I want to do a one-arm pull-up', "
        "or 'I want to get stronger overall'.", parent=root)

    output = f'''
        Calisthenics specifications:
        Experience level: {experience}
        Limitations: include alternative movements - {skillset}
        Primary goal: {goal}'''

    return output


def yoga_specified(root):
    experience = simpledialog.askstring("Input",
        "Have you done yoga before? If so, how long have you been doing it?", parent=root)
    skills = simpledialog.askstring("Input","How flexible are you?", parent=root)
    goal = simpledialog.askstring("Input",
        "What is your primary goal with yoga? For example, you could "
        "say 'I want to be more flexible', or 'I want to get stronger'.", parent=root)

    output = f'''
        Yoga specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def jogging_specified(root):
    experience = simpledialog.askstring("Input","How much experience do you have with jogging "
                       "on a plan or regularly (2 or more times per week)?", parent=root)
    skills = simpledialog.askstring("Input","How long can you jog before you need to "
                   "walk or take a break?", parent=root)
    goal = simpledialog.askstring("Input","What is your primary goal for focusing on "
                 "running - speed, endurance, weight loss, overall "
                 "improvement, fun, something else?", parent=root)
    output = f'''
        Jogging/running specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def hiking_specified(root):
    experience = simpledialog.askstring("Input","How much experience do you have with hiking?", parent=root)
    skills = simpledialog.askstring("Input","How comfortable are you with elevation gain?", parent=root)
    goal = simpledialog.askstring("Input","What is your primary goal with hiking - "
                 "more time in nature, endurance, weight loss, "
                 "overall health, fun, something else?", parent=root)
    output = f'''
        Hiking specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def walking_specified(root):
    current_activity_level = simpledialog.askstring("Input","About how many steps per day "
                                   "or miles per day do you walk?", parent=root)
    limitations = simpledialog.askstring("Input","Do you have any limitations with walking "
                        "exercise - past injuries, stairs, steep downward "
                        "slopes, etc.?", parent=root)
    goal = simpledialog.askstring("Input","What is your primary goal with walking?", parent=root)
    output = f'''
        Walking specifications:
        Current activity level: {current_activity_level}
        Limitations: {limitations}
        Primary goal: {goal}'''

    return output


def swimming_specified(root):
    experience = simpledialog.askstring("Input","How much experience do you have with swimming?", parent=root)
    skills = simpledialog.askstring("Input","What strokes can you currently or want "
                   "to swim? (freestyle, backstroke, butterfly, "
                   "or breaststroke)", parent=root)
    goal = simpledialog.askstring("Input","What is your primary goal with swimming?", parent=root)
    output = f'''
        Swimming specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def sport_climbing_specified(root):
    experience = simpledialog.askstring("Input","How much experience do you have with "
                       "sport climbing/top roping?", parent=root)
    skills = simpledialog.askstring("Input","What climbing grade are you comfortable doing?", parent=root)
    goal = simpledialog.askstring("Input","What is your primary goal with sport climbing?  "
                 "Remember, having fun is a valid reason!", parent=root)
    output = f'''
        Sport climbing specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def bouldering_specified(root):
    experience = simpledialog.askstring("Input","How much experience do you have with bouldering?", parent=root)
    skills = simpledialog.askstring("Input","What climbing grade are you comfortable doing?", parent=root)
    goal = simpledialog.askstring("Input","What is your primary goal with bouldering? "
                 "Remember, having fun is a valid reason!", parent=root)
    output = f'''
        Bouldering specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def rowing_specified(root):
    experience = simpledialog.askstring("Input","How much experience do you have with rowing?", parent=root)
    skills = simpledialog.askstring("Input","What climbing grade are you comfortable doing?", parent=root)
    goal = simpledialog.askstring("Input","What is your primary goal with rowing? For example, "
                 "you could say 'lose weight' or 'get in better shape'.", parent=root)
    output = f'''
        Rowing specifications:
        Experience level: {experience}
        Limitations: {skills}
        Primary goal: {goal}'''

    return output


def other_specified(root):
    clarifier = simpledialog.askstring("Input","You said you want to practice another activity. "
                      "What is it?", parent=root)
    skills = simpledialog.askstring("Input","Please explain your level of experience in this "
                   "activity?", parent=root)
    goal = simpledialog.askstring("Input","What are your goals or reasoning for pursuing this "
                 "activity?", parent=root)

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


def choose_sports(root, activities_dict=activities_dict):
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

    activities_str = "\n".join([f"{i+1}: {activity}" for i, activity in enumerate(activities)])
    activities_str += "\nPlease select one to three of the listed sports from the above list. Type 'done' if you want to focus on only one or two activities."

    selected_sports = []
    while len(selected_sports) < 3:
        selection = simpledialog.askstring("Input", activities_str, parent=root)
        if selection.lower() == 'done':
            break
        elif selection.isdigit() and 1 <= int(selection) <= len(activities):
            selected_sport = activities[int(selection) - 1]
            if selected_sport not in selected_sports:
                selected_sports.append(selected_sport)
                activities_dict[keys[int(selection) - 1]][1] = 1
            else:
                tk.messagebox.showinfo("Info", "You've already selected that sport. Please choose a different one.")
        else:
            tk.messagebox.showinfo("Info", "Invalid selection. Please enter a number from the list, or 'done' if you are finished.")

    selected_keys = [
        key for key, value in activities_dict.items() if value[1] == 1
        ]

    return selected_keys


def ask_questions(root, selected_keys=None):
    if selected_keys is None:
        selected_keys = choose_sports(root)

    outputs = []
    for key in selected_keys:
        if key == 'lifting':
            lifting_output = lifting_specified(root)
            outputs.append(lifting_output)
        elif key == 'calisthenics':
            calisthenics_output = calisthenics_specified(root)
            outputs.append(calisthenics_output)
        elif key == 'yoga':
            yoga_output = yoga_specified(root)
            outputs.append(yoga_output)
        elif key == 'jogging':
            jogging_output = jogging_specified(root)
            outputs.append(jogging_output)
        elif key == 'hiking':
            hiking_output = hiking_specified(root)
            outputs.append(hiking_output)
        elif key == 'walking':
            walking_output = walking_specified(root)
            outputs.append(walking_output)
        elif key == 'swimming':
            swimming_output = swimming_specified(root)
            outputs.append(swimming_output)
        elif key == 'sport_climbing':
            sport_climbing_output = sport_climbing_specified(root)
            outputs.append(sport_climbing_output)
        elif key == 'bouldering':
            bouldering_output = bouldering_specified(root)
            outputs.append(bouldering_output)
        elif key == 'rowing':
            rowing_output = rowing_specified(root)
            outputs.append(rowing_output)
        elif key == 'other':
            other_output = other_specified(root)
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
