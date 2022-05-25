#Import system libraries
import os
import subprocess
import time

#Import external libraries
import speech_recognition
import yaml

#Loading the libraries functions as variables
t = time.localtime()
audio = speech_recognition.Recognizer()

class Utils:
    def checkIfFileExists(pathFile):
        if os.path.isfile(pathFile):
            return True
        else:
            return False
    
    def fileSettingsRead(filepath):
        try:
            with open(filepath) as fileSettings:
                data = yaml.load(fileSettings, Loader=yaml.FullLoader)
                #data = yaml.load(fileSettings, Loader=yaml.BaseLoader)
                #return yaml.load(fileSettings, Loader=yaml.BaseLoader)
        
        except yaml.YAMLError as exc:
            print("Failed to read {}".format(filepath))
            print("Error: {}".format(exc))
            return None
        
        else:
            return data

    def shellScriptCommandRun(command):
        aux = 'bash -c "%s"' %(command)
        stdout = subprocess.getoutput(aux)
        print(stdout)
    
    def shellScriptCommandSpeak(voiceSpeech):
        fileSpeaking = './src/speaking.sh'

        if Utils.checkIfFileExists(fileSpeaking) == True:
            command = "source " + fileSpeaking + " && voice_assistant_speech_text_val " + "'" + voiceSpeech + "'"
            #print(f"Testing: {command}")
            Utils.shellScriptCommandRun(command)
        else:
            print("Shell script has not been found")
    
    def valCommandExecutionMenu(fileContent, userCommandArray):
        print("User command: {}".format(userCommandArray))

        match userCommandArray[0]:
            case "abrir" | "open" | "software":
                Utils.valCommandExecutionSoftware(fileContent, userCommandArray)
            case "sistema" | "system":
                Utils.valCommandExecutionSystem(fileContent, userCommandArray)
            case _:
                print("")
                #engine.say(fileContent.get('val').get('message_error_command_not_listed'))
        
    def valCommandExecutionSoftware(fileContent, userCommandArray):
        match userCommandArray[1]:
            case "firefox":
                os.system(fileContent.get('software').get('firefox'))
            case "menu":
                os.system(fileContent.get('software').get('menu'))
            case "nautilus":
                os.system(fileContent.get('software').get('nautilus'))
            case "spotify":
                os.system(fileContent.get('software').get('spotify'))
            case "terminal":
                os.system(fileContent.get('software').get('terminal'))
            case _:
                print("")
                #engine.say(fileContent.get('val').get('message_error_command_not_listed'))

    def valCommandExecutionSystem(fileContent, userCommandArray):
        match userCommandArray[1]:
            case "brightness":
                match userCommandArray[2]:
                    case "up":
                        os.system(fileContent.get('system').get('brightness').get('up'))
                    case "down":
                        os.system(fileContent.get('system').get('brightness').get('down'))
                    case _:
                        print("")
                        #engine.say(fileContent.get('val').get('message_error_command_not_listed'))

            case "volume":
                match userCommandArray[2]:
                    case "up":
                        os.system(fileContent.get('system').get('volume').get('up'))
                    case "down":
                        os.system(fileContent.get('system').get('volume').get('down'))
                    case _:
                        print("")
                        #engine.say(fileContent.get('val').get('message_error_command_not_listed'))

            case "window":
                match userCommandArray[2]:
                    case "close":
                        os.system(fileContent.get('system').get('window').get('close'))
                    case "floating":
                        os.system(fileContent.get('system').get('window').get('floating'))
                    case "full":
                        os.system(fileContent.get('system').get('window').get('full_screen'))
                    case "stick":
                        os.system(fileContent.get('system').get('window').get('stick'))
                    case "focus":
                        match userCommandArray[3]:
                            case "up":
                                os.system(fileContent.get('system').get('window').get('focus').get('up'))
                            case "left":
                                os.system(fileContent.get('system').get('window').get('focus').get('left'))
                            case "right":
                                os.system(fileContent.get('system').get('window').get('focus').get('right'))
                            case "down":
                                os.system(fileContent.get('system').get('window').get('focus').get('down'))
                            case _:
                                print("")
                                #engine.say(fileContent.get('val').get('message_error_command_not_listed'))
                    case "move":
                        match userCommandArray[3]:
                            case "up":
                                os.system(fileContent.get('system').get('window').get('move').get('up'))
                            case "left":
                                os.system(fileContent.get('system').get('window').get('move').get('left'))
                            case "right":
                                os.system(fileContent.get('system').get('window').get('move').get('right'))
                            case "down":
                                os.system(fileContent.get('system').get('window').get('move').get('down'))
                            case _:
                                print("")
                                #engine.say(fileContent.get('val').get('message_error_command_not_listed'))
                    case _:
                        print("")
                        #engine.say(fileContent.get('val').get('message_error_command_not_listed'))
                
            case "workspace":
                match userCommandArray[2]:
                    case "go":
                        match userCommandArray[3]:
                            case "last":
                                os.system(fileContent.get('system').get('workspace').get('go').get('last'))
                            case "number":
                                os.system(fileContent.get('system').get('workspace').get('go').get('number'))
                            case "next":
                                os.system(fileContent.get('system').get('workspace').get('go').get('next'))
                            case "previous":
                                os.system(fileContent.get('system').get('workspace').get('go').get('prev'))
                            case _:
                                print("")
                                #engine.say(fileContent.get('val').get('message_error_command_not_listed'))
                    case "move":
                        match userCommandArray[3]:
                            case "last":
                                os.system(fileContent.get('system').get('workspace').get('move').get('last'))
                            case "number":
                                os.system(fileContent.get('system').get('workspace').get('move').get('number'))
                            case "next":
                                os.system(fileContent.get('system').get('workspace').get('move').get('next'))
                            case "previous":
                                os.system(fileContent.get('system').get('workspace').get('move').get('prev'))
                            case _:
                                print("")
                                #engine.say(fileContent.get('val').get('message_error_command_not_listed'))
                    case _:
                        print("")
                        #engine.say(fileContent.get('val').get('message_error_command_not_listed'))
            case _:
                print("")
                #engine.say(fileContent.get('val').get('message_error_command_not_listed'))

    def valCommandValidation(fileContent, userCommandArray):
        if userCommandArray in fileContent:
            print(fileContent.get('val').get('message_success_command_listed'))
            return True
        else:
            print(fileContent.get('val').get('message_error_command_not_listed'))
            return False

    def valCommandDebugOff(fileContent, source):
        #???
        audio.adjust_for_ambient_noise(source)
        print(fileContent.get('val').get('message_running'))
        
        #Save the user's voice recording as an external file
        with open(fileContent.get('user').get('file_recording'), 'wb') as file_external:
            voz = audio.listen(source)
            file_external.write(voz.get_wav_data())

        #Load the user's voice recording
        return audio.recognize_google(voz, language=fileContent.get('settings').get('language'))

    def valCommandDebugOn(fileContent):
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