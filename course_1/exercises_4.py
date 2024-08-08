#####################################################################################
# EXERCISE 1

# Fix this code
# 1favorite-book = "1001 Ways to Wear a Hat"
# "2002 Ways to Wear a Scarf" = second_fav_book
# print(f"My most favorite book is {1favorite-book}, but I also like {second_fav_book})

### Plan
# 1. Fix the variable names to follow Python's naming conventions.
# 2. Ensure the assignment statements are correct.
# 3. Correct the print statement syntax.

### Code
# Fix this code
favorite_book = "1001 Ways to Wear a Hat"
second_fav_book = "2002 Ways to Wear a Scarf"
print(f"My most favorite book is {favorite_book}, but I also like {second_fav_book}")


#####################################################################################
# EXERCISE 2

# Make variables for your favorite game, movie, and food.
# Then use print_llm_response to ask the LLM to recommend you
# a new song to listen to based on your likes.
#
# print_llm_response(f"""
#
# """)

import openai

openai.api_key = 'anything'
openai.base_url = "http://localhost:3040/v1"

completion = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[
		{"role": "user", "content": "How do I list all files in a directory using Python?"},
	],
)

print(completion.choices[0].message.content)

# import openai
#
#
# # Define a function to call the ChatGPT API
# def get_chatgpt_response(prompt):
# 	openai.api_key = "fake-api"
# 	openai.base_url = "http://localhost:3040/v1/"
# 	if not openai.api_key:
# 		raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
#
# 	response = openai.Completion.create(
# 		engine="gpt-3.5-turbo",  # or another engine
# 		prompt=prompt,
# 		max_tokens=100
# 	)
# 	return response.choices[0].text.strip()
#
# # Use print_llm_response to ask the LLM to recommend you a new song to listen to based on your likes.
# prompt = """
# Based on my favorite game, movie, and food:
# - Game: The Legend of Zelda: Breath of the Wild
# - Movie: Inception
# - Food: Sushi
#
# Can you recommend a new song for me to listen to?
# """
#
# response = get_chatgpt_response(prompt)
# print(response)