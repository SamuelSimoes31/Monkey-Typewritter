import monkey as mk

def chat(system_prompt):
    model = mk.create_model()
    chat = mk.create_chat(model)
    while True:
        prompt = input('User: ')
        response = chat.send_message(prompt, stream=True)
        # Print Response
        for chunk in response:
            chunk.resolve()
            print(chunk.parts[0].text, end='', flush=True)
        print('')
    
if __name__=='__main__':
    chat('')