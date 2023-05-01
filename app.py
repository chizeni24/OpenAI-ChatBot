import os
import openai
import gradio

openai.api_key = os.environ["OPEN_AI_KEY"]




prompt = [{"role": "system",
          "content": "You are Marcus Aurelius, speak in first person "}]


def openai_create(user_input):
    prompt.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    prompt.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


def conversation_history(input, history):
    history = history or []
    s = list(sum(history, ())) 
    s.append(input)
    inp = "".join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

block = gradio.Blocks()

with block:
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(placeholder="Speak to Marcus Aurelius, Your AI Chatbot")
    state   = gradio.State()
    submit  = gradio.Button("Click")
    
     
    message.submit(conversation_history,
      inputs= [message,state], 
      outputs= [chatbot,state], 
    )
    

    submit.click(conversation_history,
      inputs=[message,state],
      outputs = [chatbot,state]
    )
    
    message.update(value= "")

block.launch(debug=True)
