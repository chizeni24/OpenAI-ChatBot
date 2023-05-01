# Import all the libraries
import openai
import os
# post the API key 

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
      {"role": "user", "content": "write an essay about love"}
    ]
)

print(completion.choices[0].message)
