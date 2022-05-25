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
        if fileContent.get('settings').get('debug') == 'off':
            userCommand = __main__.detectUserVoice(fileContent)
        elif fileContent.get('settings').get('debug') == 'on':
            userCommand = Utils.valCommandDebugOn(fileContent)
        else:
            #codeError = fileContent.get('val').get('message_error_microphone')
            codeError = "A debug value on settings file must be defined to procedure"
            
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)
            exit()

        #print(userCommand)

        #Format the voice command transcription
        #userCommand = userCommand[1:] #Get all elements from list except first - the 'VAL' calling
        #userCommand = "val " + userCommand #Get all elements from list except first - the 'VAL' calling
        userCommand = userCommand.lower() #Convert all the characters to lower case
        userCommandArray = userCommand.split() #Split all text word into an array

        #Transcribe on terminal the user's voice command
        #print(userCommandArray)
        print("User command: {}".format(userCommandArray))
        
        #Check if command exists
        voiceCommandKey = Utils.valCommandValidation(fileContent, userCommandArray[0])

        #Execute asked command
        if voiceCommandKey == True:
            codeError = codeError = fileContent.get('val').get('message_error_command_not_listed')
            Utils.valCommandExecutionMenu(fileContent, userCommandArray, codeError)

    def detectUserVoice(fileContent):
        print("Listening...")
        Utils.shellScriptCommandSpeak("Listening...")

        #List all available microphones
        #print(speech_recognition.Microphone.list_microphone_names())

        try:
            with speech_recognition.Microphone() as source:
                time.sleep(1)
                return Utils.valCommandRecording(fileContent, source)

        except:
            codeError = fileContent.get('val').get('message_error_microphone')

            print("Something unexpected has been happened!")
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)
            #exit()
    
if __name__ == '__main__':
    #while True:
    __main__.main()