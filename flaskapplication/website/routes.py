# Task 6: Import the request module
from flask import Blueprint, render_template, request

# Task 6: Import markdown
import markdown

# Task 1: Get Gemini API
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("Gemini_api_key")

if not api_key:
    raise RuntimeError("Gemini_api_key is not set in .env")

# Configure the Gemini SDK (new style, no Client object)
genai.configure(api_key=api_key)

# Create a reusable model instance
model = genai.GenerativeModel("gemini-2.5-flash")
# you could also use: genai.GenerativeModel("gemini-pro")

routes = Blueprint("routes", __name__)

# Task 5: Add the ask function
def ask(question: str) -> str:
    """Send a prompt to Gemini and return the text response."""
    response = model.generate_content(question)
    # response.text can theoretically be None, so be defensive
    return (response.text or "").strip()


# Task 3, 6, 9: Change the code below
historyData = []


@routes.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        query = request.args.get("query")
        if query:
            response = ask(query)
            formatted_response = markdown.markdown(response)

            queryMessage = {"messagetype": "other-message", "message": query}
            responseMessage = {"messagetype": "my-message", "message": formatted_response}

            historyData.append(queryMessage)
            historyData.append(responseMessage)

            return render_template(
                "response_view.html",
                results=[queryMessage, responseMessage],
            )

        # no query yet – just render empty chat UI
        return render_template("response_view.html")
    else:
        # POST: show history page
        return render_template("history.html", results=historyData)
