#Import system libraries
import os
import time

#Import external libraries
import speech_recognition
import yaml

#Loading the libraries functions as variables
t = time.localtime()
audio = speech_recognition.Recognizer()

class ValSpeechSettings:
    def fileSettingsRead():
        with open('./src/settings.yml') as fileSettings:
            return yaml.load(fileSettings, Loader=yaml.FullLoader)

    def commandDebugOn(fileContent):
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

    def commandDebugOff(fileContent, source):
        #???
        audio.adjust_for_ambient_noise(source)
        print(fileContent.get('val').get('message_running'))
        
        #Save the user's voice recording as an external file
        with open(fileContent.get('user').get('file_recording'), 'wb') as file_external:
            voz = audio.listen(source)
            file_external.write(voz.get_wav_data())

        #Load the user's voice recording
        return audio.recognize_google(voz, language=fileContent.get('settings').get('language'))

    def commandValidation(fileContent, userCommandArray):
        if userCommandArray in fileContent:
            print(fileContent.get('val').get('message_success_command_listed'))
            return True
        else:
            print(fileContent.get('val').get('message_error_command_not_listed'))
            return False

    #MUST BE TESTED
    def commandExecution(fileContent, engine, userCommandArray):
        print("User command: {}".format(userCommandArray))

        if 'software' in userCommandArray[0] or 'open' in userCommandArray[0] or 'abrir' in userCommandArray[0]:
            commandExecutionSoftware(fileContent, engine, userCommandArray)
        elif 'system' in userCommandArray[0] or 'sistema' in userCommandArray[0]:
            commandExecutionSystem(fileContent, engine, userCommandArray)

    #MUST BE TESTED
    def commandExecutionSoftware(fileContent, engine, userCommandArray):
        if 'firefox' in userCommandArray[1]:
            os.system(fileContent.get('software').get('firefox'))
        
        elif 'menu' in userCommandArray[1]:
            os.system(fileContent.get('software').get('menu'))
        
        elif 'nautilus' in userCommandArray[1]:
            os.system(fileContent.get('software').get('nautilus'))

        elif 'spotify' in userCommandArray[1]:
            os.system(fileContent.get('software').get('spotify'))

        elif 'terminal' in userCommandArray[1]:
            os.system(fileContent.get('software').get('terminal'))

        else:
            engine.say(fileContent.get('val').get('message_error_command_not_listed'))

    #MUST BE TESTED
    #MUST BE FIXED
    def commandExecutionSystem(fileContent, engine, userCommandArray):
        if 'brightness' in userCommandArray[1]:
            if 'up' in userCommandArray[2]:
                os.system(fileContent.get('system').get('brightness').get('up'))
            elif 'down' in userCommandArray[2]:
                os.system(fileContent.get('system').get('brightness').get('down'))
            else:
                engine.say(fileContent.get('val').get('message_error_command_not_listed'))

        elif 'volume' in userCommandArray[1]:
            if 'up' in userCommandArray[2]:
                os.system(fileContent.get('system').get('volume').get('up'))
            elif 'down' in userCommandArray[2]:
                os.system(fileContent.get('system').get('volume').get('down'))
            else:
                engine.say(fileContent.get('val').get('message_error_command_not_listed'))

        elif 'window' in userCommandArray[1]:
            if 'close' in userCommandArray[2]:
                os.system(fileContent.get('system').get('window').get('close'))
            elif 'floating' in userCommandArray[2]:
                os.system(fileContent.get('system').get('window').get('floating'))
            elif 'full' in userCommandArray[2]:
                os.system(fileContent.get('system').get('window').get('full_screen'))
            elif 'stick' in userCommandArray[2]:
                os.system(fileContent.get('system').get('window').get('stick'))
            elif 'focus' in userCommandArray[2]:
                if 'up' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('focus').get('up'))
                elif 'left' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('focus').get('left'))
                elif 'right' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('focus').get('right'))
                elif 'down' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('focus').get('down'))
                else:
                    engine.say(fileContent.get('val').get('message_error_command_not_listed'))
            elif 'move' in userCommandArray[2]:
                if 'up' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('move').get('up'))
                elif 'left' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('move').get('left'))
                elif 'right' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('move').get('right'))
                elif 'down' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('window').get('move').get('down'))
                else:
                    engine.say(fileContent.get('val').get('message_error_command_not_listed'))
            else:
                engine.say(fileContent.get('val').get('message_error_command_not_listed'))

        elif 'workspace' in userCommandArray[1]:
            if 'go' in userCommandArray[2]:
                if 'last' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('go').get('last'))
                elif 'number' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('go').get('number'))
                elif 'next' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('go').get('next'))
                elif 'previous' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('go').get('prev'))
                else:
                    engine.say(fileContent.get('val').get('message_error_command_not_listed'))
            elif 'move' in userCommandArray[2]:
                if 'last' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('move').get('last'))
                elif 'number' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('move').get('number'))
                elif 'next' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('move').get('next'))
                elif 'previous' in userCommandArray[3]:
                    os.system(fileContent.get('system').get('workspace').get('move').get('prev'))
                else:
                    engine.say(fileContent.get('val').get('message_error_command_not_listed'))

        #if 'terminal' in userCommandArray[1]:
        #    os.system(fileContent.get('software').get('terminal'))
        else:
            engine.say(fileContent.get('val').get('message_error_command_not_listed'))