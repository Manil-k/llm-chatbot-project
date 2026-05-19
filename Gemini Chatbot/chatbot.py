import google.generativeai as genai
import pathlib
import textwrap
from IPython.display import display, Markdown
from google.colab import userdata
GOOGLE_API_KEY=userdata.get('gemini_api_key')
genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
  return Markdown(textwrap.indent(text, prefix="> ", predicate= lambda _: True))

model = genai.GenerativeModel('gemini-2.5-flash')

'''
NOTE: for various models list, run
for m in genai.list_models():
  print(m.name)
'''

while True:
  user = input("You: ")
  if user.lower() == "exit":
    print("Chat Ended!")
    break
  
  response = model.generate_content(user)
  print("Gemini: ")
  display(to_markdown(response.text))
