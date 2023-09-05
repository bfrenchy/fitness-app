from flask import Flask, request, render_template
import os
import openai
from functions import ask_questions, generate_response

app = Flask(__name__)
api_key = os.getenv("OPENAI_KEY")


# Check API key
if api_key:
    openai.api_key = api_key
else:
    print("OpenAI API key not found.")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = ask_questions()
        output = generate_response(user_input)
        return render_template('index.html', output=output)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
