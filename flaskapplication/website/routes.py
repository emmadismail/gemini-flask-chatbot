# Task 6: Import the request module
from flask import Blueprint, render_template

# Task 6: Import markdown

# Task 1: Get Gemini API
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load variables from .env

api_key = os.getenv("Gemini_api_key")

routes = Blueprint('routes', __name__)

# Task 5: Add the ask function


# Task 3, 6, 9: Change the code below
@routes.route('/', methods=['GET', 'POST'])
def home():
    return render_template('response_view.html')