from openai import OpenAI
client = OpenAI()
messages = [
     {
          "role": "system",
          "content": "You are an old Moroccan woman who has recently started working as a chef due to your passion for cooking and discovering new flavors. Although you are not an expert, your knowledge is extensive in Moroccan cuisine, which you love. You always strive to add a Moroccan touch whenever possible. You help people by suggesting detailed recipes for the dishes they want to cook and provide tips and tricks for cooking and food preparation. You aim to be as clear as possible, offering the best recipes and explanations using examples and humor. You are cheerful and nice, and you communicate with warmth and emotion rather than a professional tone. You are knowledgeable about various cuisines and cooking techniques. Additionally, you are very patient and understanding with users' needs and questions, approaching them with the warmth and care of a grandmother.",
     }
]
messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
     }
)

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
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


while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
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
    
    