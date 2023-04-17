import openai

openai.api_key = "Add-Secret key"

# Create an empty list to store messages
messages = []

# Ask what type of assistance is needed
system_msg =  input("What type of chatbot will you like to create?")

# Append the input to messages specifing the role as system 
messages.append({"role": "system", "content": system_msg})

# responds with the a reply 
print("Say Hello to your new assistant!")

while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
