#!/usr/bin/env python3

#Import system library
import os

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




        #MUST CHECK THESE BLOCKS OUT
        #Generate the configuration without having a copy of the settings.yml file

        #Only for becoming easier the debugging process
        if Utils.checkIfFileExists(pathSettingsSystemFile) == True:
            Utils.shellScriptCommandRun(f'rm {pathSettingsSystemFile}')

        #Generate VAL settings file if not exists
        if Utils.checkIfFileExists(pathSettingsSystemFile) == False:
            Utils.shellScriptCommandRun(f'mkdir -p {pathSettingsSystemDirectory}')
            Utils.shellScriptCommandRun(f'ln -sf {pathSettingsLocalFile} {pathSettingsSystemFile}')
        '''
            Utils.shellScriptCommandRun(f'cp {pathSettingsLocalFile} {pathSettingsSystemFile}')
        '''




        #Import VAL settings file
        fileContent = Utils.fileSettingsRead(pathSettingsSystemFile)

        #Display the settings.yml file content only if debug mode is turned on
        if fileContent.get('settings').get('debug') == 'on':
            print(fileContent)

        #while True:
        Main.controller(fileContent)

    def controller(fileContent):
        if fileContent.get('settings').get('training').get('mode') == 'off':
            Main.runningModeNormal(fileContent)

        #Training feature
        elif fileContent.get('settings').get('training').get('mode') == 'on':
            Main.runningModeTraining(fileContent)

        else:
            #codeError = fileContent.get('val').get('message_error_microphone')
            codeError = "Debug mode must be defined"
            
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)
            exit()

    def runningModeNormal(fileContent):
        #Capture user voice command
        if fileContent.get('settings').get('debug') == 'on':
            userCommand = Utils.valCommandDebugOn(fileContent)
        elif fileContent.get('settings').get('debug') == 'off':
            userCommand = Utils.valCommandDetectUserVoice(fileContent)
        else:
            #codeError = fileContent.get('val').get('message_error_microphone')
            codeError = "A debug value on settings file must be defined to procedure"
            
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)
            #exit()

        '''
        if 'val' in userCommand:
            print(userCommand)
        '''

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

    def runningModeTraining(fileContent):
        #Declaring variables
        pathDirectory = fileContent.get('settings').get('dictionary')
        testWord = fileContent.get('settings').get('training').get('word')

        pathFile = Utils.fileDictionaryPath(pathDirectory, testWord)
        
        print(f'Path from dictionary file: {pathFile}')
        print(f'Training the {testWord} command...')

        #Capture user voice command
        if fileContent.get('settings').get('debug') == 'on':
            userCommand = Utils.valCommandDebugOn(fileContent)
        elif fileContent.get('settings').get('debug') == 'off':
            userCommand = Utils.valCommandDetectUserVoice(fileContent)
        else:
            #codeError = fileContent.get('val').get('message_error_microphone')
            codeError = "A debug value on settings file must be defined to procedure"
            
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)
            #exit()

        #Format the voice command transcription
        userCommand = userCommand.lower() #Convert all the characters to lower case
        userCommandArray = userCommand.split() #Split all text word into an array

        #Transcribe on terminal the user's voice command
        print("User command: {}".format(userCommandArray))
        
        #Command test example
        #["system", "system", "system"]

        #Write on a external file as append
        Utils.fileDictionaryAppend(pathFile, userCommand)
        Utils.fileDictionarySort(pathFile)