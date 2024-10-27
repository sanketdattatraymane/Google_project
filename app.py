from flask import Flask, render_template, request
import google.generativeai as genai
import os
from googletrans import Translator

app = Flask(__name__)

# Set your API key as an environment variable
os.environ["GEMINI_API_KEY"] = "AIzaSyDtQF_YY3RAA-S7xxLzYoo95NNDNTzFzys"

# Configure the Generative AI client with the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    response = genai.GenerativeModel(model_name="gemini-1.5-flash").generate_content(user_input)
    generated_text = response.text
    return generated_text

@app.route('/translate', methods=['POST'])
def translate():
    generated_text = request.form['generated_text']
    target_language = request.form['target_language']
    translator = Translator()
    result = translator.translate(generated_text, dest=target_language)
    return result.text

@app.route('/summarize', methods=['POST'])
def summarize():
    generated_text = request.form['generated_text']
    # Add summarization logic here (e.g., call to another model)
    summary = "This is a placeholder summary."  # Placeholder for actual summary
    return summary

if __name__ == '__main__':
    app.run(debug=True)






