import time
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(),override=True)

import google.generativeai as genai
genai.configure(api_key='AIzaSyAA2EkmyT4-qSOPJ3wJvGaveTqvyefLDVo')

#for model in genai.list_models():
    #print(model.name)

# Intiatting the model
model = genai.GenerativeModel('gemini-pro')

# Generating the chat session
chat = model.start_chat(history=[])

# Build an infinite loop for ongoing chat
while True:
    prompt = input('User: ')
    # Setting the exit logic for the chat loop
    if prompt.lower() not in ['exit', 'quit', 'exit']:
        # Sending the chat message to the API
        response = chat.send_message(prompt)

        # Getting the last item from the chat history (the AI Answer)
        print(f"{chat.history[-1].role.capitalize()}: {chat.history[-1].parts[0].text}")
        print('\n' + '=' * 100 +'\n')
    else:
        print('Exiting...')
        time.sleep(2)
        print('Bye!')
        break