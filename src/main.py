#Import system libraries
import os
import subprocess
import time
import webbrowser

#Import external libraries
import pyttsx3
import speech_recognition as sr

#Import settings file
import yaml

with open('settings.yml') as file_settings:
    content = yaml.load(file_settings, Loader=yaml.FullLoader)
    print(content)

#Loading the libraries functions as variables
t = time.localtime()
audio = sr.Recognizer()
audio2 = sr.Recognizer()
audio3 = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say(content.get('val').get('message_welcome'))
maquina.runAndWait()
maquina.stop()

def virtualAssistantExecuting():
    try:
        with sr.Microphone() as source:
            audio.adjust_for_ambient_noise(source)
            print(content.get('system').get('message_running'))
            
            #Save the user's voice recording as an external file
            with open(content.get('user').get('file_recording'), 'wb') as file_external:
                voz = audio.listen(source)
                file_external.write(voz.get_wav_data())

            #Load the user's voice recording
            user_command = audio.recognize_google(voz, language=content.get('system').get('language'))
            time.sleep(1)

            #Transcribe on terminal the user's voice command
            user_command = user_command.lower()
            print(user_command)

            #Check if VAL has been called
            #if 'val' in user_command:
            #    print(VAL_INTRODUCTION)
            #    maquina.say(VAL_INTRODUCTION)
            #    time.sleep(3)

            if 'terminal' in user_command:
                os.system(content.get('software').get('terminal'))
                #user_command = user_command.split('navegador ')
                #x = ('https://'+"".join(user_command))
                #webbrowser.open(x, new=2)
                #print(x)

    except:
        print(user_command)
        print(content.get('system').get('message_error'))

virtualAssistantExecuting()