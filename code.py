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


