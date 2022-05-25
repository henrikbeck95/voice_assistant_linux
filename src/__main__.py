#!/usr/bin/env python3

#Import system libraries
import time

#Import external libraries
import speech_recognition

#Import internal classes
from Utils import Utils

class __main__:
    def main():
        #Make sure that shell script file has executable permission
        Utils.shellScriptCommandRun("chmod +x ./src/speaking.sh")
        #Utils.shellScriptCommandSpeak("Hi, my name is Val!")

        #Import VAL settings file
        fileContent = Utils.fileSettingsRead('./src/settings.yml')
        #print(fileContent)

        __main__.controller(fileContent)

    def controller(fileContent):
        #Capture user voice command
        userCommand = __main__.detectUserVoice(fileContent)
        #userCommand = "software terminal"
        print(userCommand)

        #userCommand = userCommand[1:] #Get all elements from list except first - the 'VAL' calling
        #userCommand = "val " + userCommand #Get all elements from list except first - the 'VAL' calling

        userCommand = userCommand.lower() #Transcribe on terminal the user's voice command
        userCommandArray = userCommand.split() #Split all text word into an array
        #print(userCommandArray)
        
        #Check if command exists
        voiceCommandKey = Utils.valCommandValidation(fileContent, userCommandArray[0])

        #Execute asked command
        if voiceCommandKey == True:
            Utils.valCommandExecutionMenu(fileContent, userCommandArray)

    def detectUserVoice(fileContent):
        #print(speech_recognition.Microphone.list_microphone_names())
        print("Listening...")

        try:
            with speech_recognition.Microphone() as source:
                if fileContent.get('settings').get('debug') == 'off':
                    print('Debug option has been turned off')
                    time.sleep(1)
                    return Utils.valCommandDebugOff(fileContent, source)
                elif fileContent.get('settings').get('debug') == 'on': #Debug a the commands from a text command example
                    print('Debug option has been turned on')
                    return Utils.valCommandDebugOn(fileContent)
                else:
                    print('Debug option has not been found')
                    exit()

        except:
            print("Something unexpected has been happened!")
            
            print(fileContent.get('val').get('message_error_microphone'))
            #engine.say(fileContent.get('val').get('message_error_microphone'))

            exit()
    
if __name__ == '__main__':
    __main__.main()