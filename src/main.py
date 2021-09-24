#Import system libraries
import os
import subprocess
import time
#import webbrowser

#Import external libraries
import pyttsx3
import speech_recognition as sr

#Import settings file
import yaml

with open('settings.yml') as file_settings:
    content = yaml.load(file_settings, Loader=yaml.FullLoader)
    #print(content)

#Loading the libraries functions as variables
t = time.localtime()
audio = sr.Recognizer()

#VAL speech settings
#engine = pyttsx3.init()
engine = pyttsx3.init('espeak') #Speech engine

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

def main():
    #Stand voice assistant up
    if content.get('settings').get('debug') == "on":
        virtualAssistantExecuting()
    else:
        while True:
            virtualAssistantExecuting()

def virtualAssistantExecuting():
    try:
        with sr.Microphone() as source:
            if content.get('settings').get('debug') == "on":
                #Debug a the commands from a text command example
                user_command = commandExample()
            else:
                #???
                audio.adjust_for_ambient_noise(source)
                print(content.get('val').get('message_running'))
                
                #Save the user's voice recording as an external file
                with open(content.get('user').get('file_recording'), 'wb') as file_external:
                    voz = audio.listen(source)
                    file_external.write(voz.get_wav_data())

                #Load the user's voice recording
                user_command = audio.recognize_google(voz, language=content.get('settings').get('language'))
                time.sleep(1)

            #Transcribe on terminal the user's voice command
            user_command = user_command.lower()
            print(user_command)

            #Split all text word into an array
            user_command_array = user_command.split()
            
            #Check if command exists
            voiceCommandKey = validateVoiceCommand(user_command_array[0])

            #Execute asked command
            if voiceCommandKey == True:
                executeVoiceCommand(user_command_array)

    except:
        #print(user_command)
        print(user_command_array)
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

def validateVoiceCommand(user_command_array):
    if user_command_array in content:
        print(content.get('val').get('message_success_command_listed'))
        return True
    else:
        print(content.get('val').get('message_error_command_not_listed'))
        return False

def executeVoiceCommand(user_command_array):
    print("Comando do usuário: {}".format(user_command_array))

    if 'software' in user_command_array[0] or 'open' in user_command_array[0] or 'abrir' in user_command_array[0]:
        executeVoiceCommand_software(user_command_array)
    elif 'system' in user_command_array[0] or 'sistema' in user_command_array[0]:
        executeVoiceCommand_system(user_command_array)

def executeVoiceCommand_software(user_command_array):
    if 'firefox' in user_command_array[1]:
        os.system(content.get('software').get('firefox'))
    
    elif 'menu' in user_command_array[1]:
        os.system(content.get('software').get('menu'))
    
    elif 'nautilus' in user_command_array[1]:
        os.system(content.get('software').get('nautilus'))

    elif 'spotify' in user_command_array[1]:
        os.system(content.get('software').get('spotify'))

    elif 'terminal' in user_command_array[1]:
        os.system(content.get('software').get('terminal'))

    else:
        engine.say(content.get('val').get('message_error_command_not_listed'))

#Must be fixed
def executeVoiceCommand_system(user_command_array):
    if 'brightness' in user_command_array[1]:
        if 'up' in user_command_array[2]:
            os.system(content.get('system').get('brightness').get('up'))
        elif 'down' in user_command_array[2]:
            os.system(content.get('system').get('brightness').get('down'))
        else:
            engine.say(content.get('val').get('message_error_command_not_listed'))

    elif 'volume' in user_command_array[1]:
        if 'up' in user_command_array[2]:
            os.system(content.get('system').get('volume').get('up'))
        elif 'down' in user_command_array[2]:
            os.system(content.get('system').get('volume').get('down'))
        else:
            engine.say(content.get('val').get('message_error_command_not_listed'))

    elif 'window' in user_command_array[1]:
        if 'close' in user_command_array[2]:
            os.system(content.get('system').get('window').get('close'))
        elif 'floating' in user_command_array[2]:
            os.system(content.get('system').get('window').get('floating'))
        elif 'full' in user_command_array[2]:
            os.system(content.get('system').get('window').get('full_screen'))
        elif 'stick' in user_command_array[2]:
            os.system(content.get('system').get('window').get('stick'))
        elif 'focus' in user_command_array[2]:
            if 'up' in user_command_array[3]:
                os.system(content.get('system').get('window').get('focus').get('up'))
            elif 'left' in user_command_array[3]:
                os.system(content.get('system').get('window').get('focus').get('left'))
            elif 'right' in user_command_array[3]:
                os.system(content.get('system').get('window').get('focus').get('right'))
            elif 'down' in user_command_array[3]:
                os.system(content.get('system').get('window').get('focus').get('down'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))
        elif 'move' in user_command_array[2]:
            if 'up' in user_command_array[3]:
                os.system(content.get('system').get('window').get('move').get('up'))
            elif 'left' in user_command_array[3]:
                os.system(content.get('system').get('window').get('move').get('left'))
            elif 'right' in user_command_array[3]:
                os.system(content.get('system').get('window').get('move').get('right'))
            elif 'down' in user_command_array[3]:
                os.system(content.get('system').get('window').get('move').get('down'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))
        else:
            engine.say(content.get('val').get('message_error_command_not_listed'))

    elif 'workspace' in user_command_array[1]:
        if 'go' in user_command_array[2]:
            if 'last' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('go').get('last'))
            elif 'number' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('go').get('number'))
            elif 'next' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('go').get('next'))
            elif 'previous' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('go').get('prev'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))
        elif 'move' in user_command_array[2]:
            if 'last' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('move').get('last'))
            elif 'number' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('move').get('number'))
            elif 'next' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('move').get('next'))
            elif 'previous' in user_command_array[3]:
                os.system(content.get('system').get('workspace').get('move').get('prev'))
            else:
                engine.say(content.get('val').get('message_error_command_not_listed'))

    #if 'terminal' in user_command_array[1]:
    #    os.system(content.get('software').get('terminal'))
    else:
        engine.say(content.get('val').get('message_error_command_not_listed'))

main()