# from flask import Flask, request, render_template
import tkinter as tk
from tkinter import scrolledtext
import os
import openai
from functions import ask_questions, generate_response

api_key = os.getenv("OPENAI_KEY")


# Check API key
if api_key:
    openai.api_key = api_key
else:
    print("OpenAI API key not found.")


def ask_questions_gui():
    root = tk.Tk()
    root.withdraw()  # hides the main window

    user_input = ask_questions(root)

    return user_input


def main():
    user_input = ask_questions_gui()
    output = generate_response(user_input)

    root = tk.Tk()
    root.title("Fitness Planning App")

    output_text = scrolledtext.ScrolledText(root, width=80, height=20)
    output_text.pack()

    output_text.insert(tk.END, output)

    root.mainloop()


if __name__ == "__main__":
    main()
