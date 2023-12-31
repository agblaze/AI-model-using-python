!pip install -q -U google-generativeai


import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=('AIzaSyA3MqQJb9KtaSEfKb2xwYxZcuvpR1EkLWQ') #key changeable

genai.configure(api_key=GOOGLE_API_KEY)


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)   #from the list of models choose your desired model


model = genai.GenerativeModel('gemini-pro')


#so I created a chatbot using a function to call itself SKY

def SKY(input_text):

  response =model.generate_content(input_text)

  # Return the output of the AI bot.
  return to_markdown(response.text)


SKY("Hi Sky whats the mass of Earth?")

