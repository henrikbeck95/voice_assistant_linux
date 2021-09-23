#Import testing libraries
import os

#Import system libraries
import subprocess
import time
import webbrowser

#Import external libraries
import pyttsx3
import speech_recognition as sr

#Declaring variables
OPERATING_SYSTEM_TERMINAL = "alacritty"
OPERATING_SYSTEM_BROWSER = "firefox"
OPERATING_SYSTEM_GRAPHICAL_INTERFACE = "i3"
OPERATING_SYSTEM_SPOTIFY = "spotify"
OPERATING_SYSTEM_FILE_BROWSER = "nautilus"

SYSTEM_FILE_USER_VOICE = "voice_user.wav"
SYSTEM_LANGUAGE = "pt-BR"
SYSTEM_MESSAGE_RUNNING = "VAL is listenning..."
SYSTEM_MESSAGE_ERROR = "An error has occurred. Your microphone device might not be correctly configured. Please, check it out before try again."

VAL_WELCOME = "VAL here!"
#VAL_WELCOME = "'Olá, eu sou a VAL'"

VAL_INTRODUCTION = "How can I help you!?"

'''
GRAPHICAL_INTERFACE_WINDOW_MOVE_UP
GRAPHICAL_INTERFACE_WINDOW_MOVE_LEFT
GRAPHICAL_INTERFACE_WINDOW_MOVE_RIGHT
GRAPHICAL_INTERFACE_WINDOW_MOVE_DOWN
GRAPHICAL_INTERFACE_WORKSPACE_GO_TO_WKS
GRAPHICAL_INTERFACE_WORKSPACE_MOVE_TO_WKS
GRAPHICAL_INTERFACE_WORKSPACE_
GRAPHICAL_INTERFACE_
GRAPHICAL_INTERFACE_
GRAPHICAL_INTERFACE_
GRAPHICAL_INTERFACE_
GRAPHICAL_INTERFACE_
GRAPHICAL_INTERFACE_
GRAPHICAL_INTERFACE_
OPERATING_SYSTEM_
OPERATING_SYSTEM_
USER_ = ""
USER_ = ""
USER_ = ""
USER_ = ""
USER_ = ""
USER_ = ""
VAL_LISTENNING = ""
VAL_ = ""
VAL_ = ""
VAL_ = ""
VAL_ = ""
VAL_ = ""
VAL_ = ""
'''

#Loading the libraries functions as variables
t = time.localtime()
audio = sr.Recognizer()
audio2 = sr.Recognizer()
audio3 = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say(VAL_WELCOME)
maquina.runAndWait()
maquina.stop()

def virtualAssistantExecuting():
    try:
        with sr.Microphone() as source:
            audio.adjust_for_ambient_noise(source)
            print(SYSTEM_MESSAGE_RUNNING)
            
            #Save the user's voice recording as an external file
            with open(SYSTEM_FILE_USER_VOICE, 'wb') as file_external:
                voz = audio.listen(source)
                file_external.write(voz.get_wav_data())

            #Load the user's voice recording
            user_command = audio.recognize_google(voz, language=SYSTEM_LANGUAGE)
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
                os.system(OPERATING_SYSTEM_TERMINAL)
                #user_command = user_command.split('navegador ')
                #x = ('https://'+"".join(user_command))
                #webbrowser.open(x, new=2)
                #print(x)

    except:
        print(user_command)
        print(SYSTEM_MESSAGE_ERROR)

virtualAssistantExecuting()