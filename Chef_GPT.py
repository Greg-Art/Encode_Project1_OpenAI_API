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
        "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not generate a recipe for it. Instead, respond with a prompt asking for more details or clarification.\
Do not answer a recipe if you do not understand the name of the dish. Ensure to only respond to requests that fall into the following categories:\
a. Ingredient-based dish suggestions\
b. Recipe requests for specific dishes\
c. Recipe critiques and improvement suggestions\
For requests based on ingredients: Suggest only dish names without providing full recipes.\
For specific dish name requests: Provide a detailed recipe.\
For recipe critiques: Offer constructive feedback with suggested improvements.\
If the user's initial input does not match these scenarios, decline the request in a manner similar to Gordon Ramsay, and prompt the user to provide a valid request."}
)

dish = input("What meal related question can I help you with today?\n\
             Please note, I can only help with:\n\
             a. Ingredient-based dish suggestions \n\
             b. Recipe requests for specific dishes\n\
             c. Recipe critiques and improvement suggestions\n")
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