import ollama
import pyttsx3
import re


rx = re.compile(r'_{2,}')
voice = pyttsx3.init()
voice.setProperty('rate', 180)

def HeyLlama():
    prompt = input("What do you want ? \n")

    response = ollama.chat(model='tinyllama', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])
      
    resp = response['message']['content']

    resp2 = [rx.sub(r"_", i).replace("\\","").replace('"',"") for i in resp]

    print(response['message']['content'])

    mapped = map(str, resp2)
    EditedResponse = ''.join(mapped)
    #print(SEditedResp)



    #print(EditedResponse)

    voice.say(EditedResponse)
    voice.save_to_file(str, 'Response.mp3')
    voice.runAndWait()

HeyLlama()


     

    
