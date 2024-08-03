import os
import json
from helper import load_mistral_api_key
load_mistral_api_key()

from helper import mistral
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from tools import list as tools
from dictionary import names_to_functions

from config import logger
import sys


model = "mistral-large-latest"

client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

chat_history = []

def promptMistral(msg=""):
    response=mistral(msg)    
    return response


def find_flights():
    response = client.chat(
        model=model, messages=chat_history, tools=tools, tool_choice="auto"
    )
    print(response)
    if response.choices[0].message.tool_calls is None:
        print(response.choices[0].message.content)
    else: 
        tool_fn = response.choices[0].message.tool_calls[0].function
        #logger.debug(tool_fn)
        args = json.loads(tool_fn.arguments)
        result = names_to_functions[tool_fn.name](**args)
        logger.info("-------Result--------")
        logger.info(result)
        final = promptMistral("You are a flight agent. Provide the available flights based on user requirements" + json.dumps(result))
        logger.info("-------FINAL--------")
        logger.info(final)
        print(final)
     
while True:
    query = input('Prompt: ')
    #To exit: use 'exit', 'quit', 'q', or Ctrl-D.",
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        logger.info("Exiting")
        sys.exit()
    chat_message = ChatMessage(role="user", content=query)
    chat_history.append(chat_message)
    find_flights()




# Example:
#promptMistral("hello, what can you do?")

# import sys
# import os
# #print(sys.path)
# print(os.__file__);
