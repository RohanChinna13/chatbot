from openai import OpenAI
import openai
client = OpenAI()

openai.api_key = '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'

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)


