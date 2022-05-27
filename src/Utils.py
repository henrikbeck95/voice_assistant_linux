#Import system libraries
import os
import subprocess

#Import external libraries
import speech_recognition
import yaml

#Loading the libraries functions as variables
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

    def generatePathDirectory(pathDirectoryRelative):
        #pathDirectoryCurrent = os.getcwd()
        #pathDirectoryCurrent = __file__
        pathDirectoryCurrent = os.path.dirname(os.path.abspath(__file__))

        #Check if first character from string must be removed
        if pathDirectoryRelative[0] == '.':
            pathDirectoryRelativeAux = pathDirectoryRelative[1:]
        else:
            pathDirectoryRelativeAux = pathDirectoryRelative

        return pathDirectoryCurrent + pathDirectoryRelativeAux

    def shellScriptCommandRun(command):
        aux = 'bash -c "%s"' %(command)
        stdout = subprocess.getoutput(aux)
        print(stdout)
    
    def shellScriptCommandSpeak(voiceSpeech):
        fileSpeaking = './src/speaking.sh'

        if Utils.checkIfFileExists(fileSpeaking) == True:
            command = "source " + fileSpeaking + " && voice_assistant_speech_text_val " + "'" + voiceSpeech + "'"
            Utils.shellScriptCommandRun(command)
        else:
            print("Shell script has not been found")
    
    def valCommandExecutionMenu(fileContent, userCommandArray, codeError):
        match userCommandArray[0]:
            case "abrir" | "open" | "software":
                Utils.valCommandExecutionSoftware(fileContent, userCommandArray, codeError)
            case "sistema" | "system":
                Utils.valCommandExecutionSystem(fileContent, userCommandArray, codeError)
            case _:
                print(codeError)
                Utils.shellScriptCommandSpeak(codeError)
        
    def valCommandExecutionSoftware(fileContent, userCommandArray, codeError):
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
                print(codeError)
                Utils.shellScriptCommandSpeak(codeError)

    def valCommandExecutionSystem(fileContent, userCommandArray, codeError):
        match userCommandArray[1]:
            case "brightness":
                match userCommandArray[2]:
                    case "up":
                        os.system(fileContent.get('system').get('brightness').get('up'))
                    case "down":
                        os.system(fileContent.get('system').get('brightness').get('down'))
                    case _:
                        print(codeError)
                        Utils.shellScriptCommandSpeak(codeError)

            case "volume":
                match userCommandArray[2]:
                    case "up":
                        os.system(fileContent.get('system').get('volume').get('up'))
                    case "down":
                        os.system(fileContent.get('system').get('volume').get('down'))
                    case _:
                        print(codeError)
                        Utils.shellScriptCommandSpeak(codeError)

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
                                print(codeError)
                                Utils.shellScriptCommandSpeak(codeError)

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
                                print(codeError)
                                Utils.shellScriptCommandSpeak(codeError)
                    case _:
                        print(codeError)
                        Utils.shellScriptCommandSpeak(codeError)
                
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
                                print(codeError)
                                Utils.shellScriptCommandSpeak(codeError)

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
                                print(codeError)
                                Utils.shellScriptCommandSpeak(codeError)
                    case _:
                        print(codeError)
                        Utils.shellScriptCommandSpeak(codeError)
            case _:
                print(codeError)
                Utils.shellScriptCommandSpeak(codeError)

    def valCommandValidation(fileContent, userCommandArray):
        if userCommandArray in fileContent:
            print(fileContent.get('val').get('message_success_command_listed'))
            return True
        else:
            print(fileContent.get('val').get('message_error_command_not_listed'))
            return False

    def valCommandRecording(fileContent, source):
        #Inspect audio file for removing some ambient noise
        audio.adjust_for_ambient_noise(source)
        print(fileContent.get('val').get('message_running'))
        
        #Save the user's voice recording as an external file
        pathFileValUserVoice = fileContent.get('user').get('file_recording')

        with open(pathFileValUserVoice, 'wb') as file_external:
            userVoiceTranscription = audio.listen(source)
            file_external.write(userVoiceTranscription.get_wav_data())

        #Load the user's voice recording
        result = audio.recognize_google(userVoiceTranscription, language=fileContent.get('settings').get('language'))

        #Remove the user's voice recording file if exists
        if Utils.checkIfFileExists(pathFileValUserVoice) == True:
            command = "rm " + pathFileValUserVoice
            Utils.shellScriptCommandRun(command)
        else:
            print(pathFileValUserVoice + " file has not been found")

        return result

    def valCommandDebugOn(fileContent):
        #Debugging commands for softwares
        #userCommand = "software firefox"
        #userCommand = "software menu"
        #userCommand = "software nautilus"
        #userCommand = "software spotify" #Not working
        #userCommand = "software terminal"

        #Debugging commands for system
        userCommand = "system brightness up"
        #userCommand = "system brightness down"
        #userCommand = "system volume up"
        #userCommand = "system volume down"
        #userCommand = "system window close"
        #userCommand = "system window floating"
        #userCommand = "system window stick"
        #userCommand = "system window full screen"
        #userCommand = "system window focus up"
        #userCommand = "system window focus left"
        #userCommand = "system window focus right"
        #userCommand = "system window focus down"
        #userCommand = "system window move up"
        #userCommand = "system window move left"
        #userCommand = "system window move right"
        #userCommand = "system window move down"
        #userCommand = "system workspace go last"
        #userCommand = "system workspace go number" #Not working
        #userCommand = "system workspace go next"
        #userCommand = "system workspace go previous"
        #userCommand = "system workspace move last"
        #userCommand = "system workspace move number" #Not working
        #userCommand = "system workspace move next"
        #userCommand = "system workspace move previous"

        return userCommand