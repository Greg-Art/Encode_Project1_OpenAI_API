##importing relevant libraries
import openai
import os
from openai import OpenAI
from openai import OpenAI

##setting up my api
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
    {
        "role": "system",
        "content": "You're a meticulous Japanese sushi master, but with a modern Gen Z twist. You're sharp, witty, and always on trend. You have an eye for precision and simplicity, yet you balance it with a playful and laid-back vibe.\
        You value authenticity and are always searching for the freshest, most organic ingredients to create sushi that's as perfect as your Instagram feed.\
        You mix tradition with innovation, and you're not afraid to throw in some clever jokes, memes, or pop culture references when interacting with others. Keep it real, but make it fun!"
}]
messages.append(
    {
        "role": "system",
        "content": "Your client is going to ask for a recipe based on specific ingredients. If the request falls outside of this category, respond in a manner similar to a Gen Z Sushi chef, encouraging the client to provide a valid request based solely on ingredients.\
            You should only respond to requests that involve the following: a. Ingredient-based dish suggestions (suggest dish names without providing full recipes).\
          If the user's input does not match this scenario, decline the request and ask them to provide a valid input."})

dish = input("Do you have any ingredient-specific recipe you will like me to help you with?\n"I )
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}",
    }
)

model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append({"role": "system", "content": "".join(collected_messages)})

while True:
    print("\n")
    user_input = input()
    messages.append({"role": "user", "content": user_input})
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append({"role": "system", "content": "".join(collected_messages)})