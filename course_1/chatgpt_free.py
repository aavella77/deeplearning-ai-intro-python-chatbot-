from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('API_KEY'), base_url="https://api.pawan.krd/v1/")

completion = client.chat.completions.create(
	model="pai-001",
	messages=[
		{"role": "user", "content": "What is the capital of Venezuela?"},
	],
)

print(completion.choices[0].message.content)
