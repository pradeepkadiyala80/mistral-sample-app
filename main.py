import os
import json
from helper import load_mistral_api_key
load_mistral_api_key()

from helper import mistral
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from tools import list as tools
from dictionary import names_to_functions

model = "mistral-large-latest"

client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

# ChatMessage(role="user", content="Find flight from AUS to SAN. I will be traveling on 2024-05-11 and will return on 2024-05-17")
chat_history = [    
    ChatMessage(role="user", content="Find flight from AUS to SAN. I will be traveling on 2024-06-11 and will return on 2024-06-17")
]



def promptMistral(msg=""):
    response=mistral(msg)    
    return response


def find_flights():
    response = client.chat(
        model=model, messages=chat_history, tools=tools, tool_choice="auto"
    )
    print(response)
    tool_fn = response.choices[0].message.tool_calls[0].function
    print(tool_fn)
    args = json.loads(tool_fn.arguments)
    result = names_to_functions[tool_fn.name](**args)
    print("-------Result--------")
    print(result)
    final = promptMistral("Get the best flights from " + json.dumps(result))
    print("-------FINAL--------")
    print(final)
     

find_flights()




# Example:
#promptMistral("hello, what can you do?")

# import sys
# import os
# #print(sys.path)
# print(os.__file__);
