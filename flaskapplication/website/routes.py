# Task 6: Import the request module
from flask import Blueprint, render_template

# Task 6: Import markdown
import markdown

# Task 1: Get Gemini API
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load variables from .env

api_key = os.getenv("Gemini_api_key")

routes = Blueprint('routes', __name__)

# Task 5: Add the ask function
client = genai.Client(api_key=api_key)

def ask(question):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=question
    )
    return response.text.strip()

# Task 3, 6, 9: Change the code below
historyData = []

@routes.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        query = request.args.get('query')
        if query:
            response = ask(query)
            formatted_response = markdown.markdown(response)
            queryMessage = {"messagetype": "other-message", "message": query}
            responseMessage = {"messagetype": "my-message", "message": formatted_response}
            historyData.append(queryMessage)
            historyData.append(responseMessage)
            return render_template('response_view.html', results=[queryMessage, responseMessage])
        return render_template('response_view.html')
    else:
        return render_template('history.html', results=historyData)