#Import system libraries
import os
import platform
import subprocess
import time
#import webbrowser

#Import external libraries
import pyttsx3
import speech_recognition as sr
import yaml

#Import settings file
with open('settings.yml') as file_settings:
    content = yaml.load(file_settings, Loader=yaml.FullLoader)
    #print(content)

#Loading the libraries functions as variables
t = time.localtime()
audio = sr.Recognizer()

#############################
#VAL speech settings
#############################

#Speech engine
#engine = pyttsx3.init()
if platform.system() == "Darwin":
    engine = pyttsx3.init('nsss')
elif platform.system() == "Linux":
    engine = pyttsx3.init('espeak')
elif platform.system() == "Windows":
    engine = pyttsx3.init('sapi5')

#Speech percent speed
if content.get('settings').get('speech_speed') == "low":
    engine.setProperty('rate', 118)
elif content.get('settings').get('speech_speed') == "normal":
    engine.setProperty('rate', 178)
elif content.get('settings').get('speech_speed') == "fast":
    engine.setProperty('rate', 278)

#Speech percent volume (0-1)
if content.get('settings').get('speech_volume') == "low":
    engine.setProperty('volume', 0.5)
elif content.get('settings').get('speech_volume') == "normal":
    engine.setProperty('volume', 0.7)
elif content.get('settings').get('speech_volume') == "high":
    engine.setProperty('volume', 1)

engine.say(content.get('val').get('message_welcome')) #Speech sentence
engine.runAndWait()
engine.stop()

#############################
#Functions
#############################

def main():
    if content.get('settings').get('debug') == "on":
        detectUserVoice()
    else:
        while True:
            detectUserVoice()

def detectUserVoice():
    try:
        with sr.Microphone() as source:
            if content.get('settings').get('debug') == "on":
                #Debug a the commands from a text command example
                userCommand = commandExample()
            else:
                #???
                audio.adjust_for_ambient_noise(source)
                print(content.get('val').get('message_running'))
                
                #Save the user's voice recording as an external file
                with open(content.get('user').get('file_recording'), 'wb') as file_external:
                    voz = audio.listen(source)
                    file_external.write(voz.get_wav_data())

                #Load the user's voice recording
                userCommand = audio.recognize_google(voz, language=content.get('settings').get('language'))
                time.sleep(1)

            #Transcribe on terminal the user's voice command
            userCommand = userCommand.lower()
            print(userCommand)

            #Split all text word into an array
            userCommandArray = userCommand.split()
            
            #Check if command exists
            voiceCommandKey = commandValidation(userCommandArray[0])

            #Execute asked command
            if voiceCommandKey == True:
                commandExecution(userCommandArray)

    except:
        #print(userCommand)
        print(userCommandArray)
        print(content.get('val').get('message_error_microphone'))
        engine.say(content.get('val').get('message_error_microphone'))

def commandExample():
    #Debugging commands for softwares
    #return "software firefox"
    #return "software menu"
    #return "software nautilus"
    #return "software spotify" #Not working
    return "software terminal"

    #Debugging commands for system
    #return "system brightness up"
    #return "system brightness down"
    #return "system volume up"
    #return "system volume down"
    #return "system window close"
    #return "system window floating"
    #return "system window stick"
    #return "system window full screen"
    #return "system window focus up"
    #return "system window focus left"
    #return "system window focus right"
    #return "system window focus down"
    #return "system window move up"
    #return "system window move left"
    #return "system window move right"
    #return "system window move down"
    #return "system workspace go last"
    #return "system workspace go number" #Not working
    #return "system workspace go next"
    #return "system workspace go previous"
    #return "system workspace move last"
    #return "system workspace move number" #Not working
    #return "system workspace move next"
    #return "system workspace move previous"

def commandValidation(userCommandArray):
    if userCommandArray in content:
        print(content.get('val').get('message_success_command_listed'))
        return True
    else:
        print(content.get('val').get('message_error_command_not_listed'))
        return False

def commandExecution(userCommandArray):
    print("Comando do usuário: {}".format(userCommandArray))

    if 'software' in userCommandArray[0] or 'open' in userCommandArray[0] or 'abrir' in userCommandArray[0]:
        commandExecution_software(userCommandArray)
    elif 'system' in userCommandArray[0] or 'sistema' in userCommandArray[0]:
        commandExecution_system(userCommandArray)

def commandExecution_software(userCommandArray):
    if 'firefox' in userCommandArray[1]:
        os.system(content.get('software').get('firefox'))
    
    elif 'menu' in userCommandArray[1]:
        os.system(content.get('software').get('menu'))
    
    elif 'nautilus' in userCommandArray[1]:
        os.system(content.get('software').get('nautilus'))

    elif 'spotify' in userCommandArray[1]:
        os.system(content.get('software').get('spotify'))

    elif 'terminal' in userCommandArray[1]:
        os.system(content.get('software').get('terminal'))

    else:
        engine.say(content.get('val').get('message_error_command_not_listed'))

#Must be fixed
def commandExecution_system(userCommandArray):
    if 'brightness' in userCommandArray[1]:
        if 'up' in userCommandArray[2]:
            os.system(content.get('system').get('brightness').get('up'))
        elif 'down' in userCommandArray[2]:
            os.system(content.get('system').get('brightness').get('down'))
        else:
            engine.say(content.get('val').get('message_error_command_not_listed'))

    elif 'volume' in userCommandArray[1]:
        if 'up' in userCommandArray[2]:
            os.system(content.get('system').get('volume').get('up'))
        elif 'down' in userCommandArray[2]:
            os.system(content.get('system').get('volume').get('down'))
        else:
            engine.say(content.get('val').get('message_error_command_not_listed'))

    elif 'window' in userCommandArray[1]:
        if 'close' in userCommandArray[2]:
            os.system(content.get('system').get('window').get('close'))
        elif 'floating' in userCommandArray[2]:
            os.system(content.get('system').get('window').get('floating'))
        elif 'full' in userCommandArray[2]:
            os.system(content.get('system').get('window').get('full_screen'))
        elif 'stick' in userCommandArray[2]:
            os.system(content.get('system').get('window').get('stick'))
        elif 'focus' in userCommandArray[2]:
            if 'up' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('focus').get('up'))
            elif 'left' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('focus').get('left'))
            elif 'right' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('focus').get('right'))
            elif 'down' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('focus').get('down'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))
        elif 'move' in userCommandArray[2]:
            if 'up' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('move').get('up'))
            elif 'left' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('move').get('left'))
            elif 'right' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('move').get('right'))
            elif 'down' in userCommandArray[3]:
                os.system(content.get('system').get('window').get('move').get('down'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))
        else:
            engine.say(content.get('val').get('message_error_command_not_listed'))

    elif 'workspace' in userCommandArray[1]:
        if 'go' in userCommandArray[2]:
            if 'last' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('go').get('last'))
            elif 'number' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('go').get('number'))
            elif 'next' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('go').get('next'))
            elif 'previous' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('go').get('prev'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))
        elif 'move' in userCommandArray[2]:
            if 'last' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('move').get('last'))
            elif 'number' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('move').get('number'))
            elif 'next' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('move').get('next'))
            elif 'previous' in userCommandArray[3]:
                os.system(content.get('system').get('workspace').get('move').get('prev'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))

    #if 'terminal' in userCommandArray[1]:
    #    os.system(content.get('software').get('terminal'))
    else:
        engine.say(content.get('val').get('message_error_command_not_listed'))

main()