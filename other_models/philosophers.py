import openai
import gradio

openai.api_key = "Add-Secret key"

# Create an empty list to store messages
messages = [{"role": "system", 
             "content": "You are Aristotle, speak in first person "}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn= CustomChatGPT,
                        inputs= "text", 
                        outputs="text", 
                        title="Aristotle Chatbot")

demo.launch(share=True)
