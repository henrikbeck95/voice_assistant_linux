#!/usr/bin/env python3

#Import system libraries
import os
import time

#Import external libraries
import speech_recognition

#Import internal classes
from Utils import Utils

class Main:
    def main():
        #Make sure that shell script file has executable permission
        #pathFileSpeaking = Utils.generatePathDirectory('./speaking.sh')
        #Utils.shellScriptCommandRun(f'chmod +x {pathFileSpeaking}')
        #Utils.shellScriptCommandSpeak("Hi, my name is Val!")

        #Get user home directory path
        pathHomeUser = os.path.expanduser('~')

        #Declaring variables to VAL settings file
        fileSettingsBothName = 'settings.yml'
        pathSettingsLocalFile = Utils.generatePathDirectory(f'./{fileSettingsBothName}')
        pathSettingsSystemDirectory = f'{pathHomeUser}/.config/voice_assistant_linux'
        pathSettingsSystemFile = f'{pathSettingsSystemDirectory}/{fileSettingsBothName}'

        #Only for becoming easier the debugging process
        if Utils.checkIfFileExists(pathSettingsSystemFile) == True:
            Utils.shellScriptCommandRun(f'rm {pathSettingsSystemFile}')

        #Generate VAL settings file if not exists
        if Utils.checkIfFileExists(pathSettingsSystemFile) == False:
            Utils.shellScriptCommandRun(f'mkdir -p {pathSettingsSystemDirectory}')
            Utils.shellScriptCommandRun(f'cp {pathSettingsLocalFile} {pathSettingsSystemFile}')
            #Utils.shellScriptCommandRun(f'ln -sf {pathSettingsLocalFile} {pathSettingsSystemFile}')
            #Utils.shellScriptCommandRun(f'ls -lah {pathSettingsSystemFile} && echo -e "\n"')
        
        #Import VAL settings file
        fileContent = Utils.fileSettingsRead(pathSettingsSystemFile)
        print(fileContent)

        Main.controller(fileContent)

    def controller(fileContent):
        #Capture user voice command
        if fileContent.get('settings').get('debug') == 'off':
            userCommand = Main.detectUserVoice(fileContent)
        elif fileContent.get('settings').get('debug') == 'on':
            userCommand = Utils.valCommandDebugOn(fileContent)
        else:
            #codeError = fileContent.get('val').get('message_error_microphone')
            codeError = "A debug value on settings file must be defined to procedure"
            
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)
            exit()

        #Format the voice command transcription
        #userCommand = userCommand[1:] #Get all elements from list except first - the 'VAL' calling
        #userCommand = "val " + userCommand #Get all elements from list except first - the 'VAL' calling
        userCommand = userCommand.lower() #Convert all the characters to lower case
        userCommandArray = userCommand.split() #Split all text word into an array

        #Transcribe on terminal the user's voice command
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
    
'''
if __name__ == 'Main':
    #while True:
    Main.main()
'''