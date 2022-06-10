import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="personalized email for technical hiring, the  hire is also a woodworker and homebrewer:",
  temperature=0.4,
  max_tokens=160,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)