#Import system libraries
import time
#import platform
#import subprocess
#import webbrowser

#Import external libraries
import speech_recognition

#Import VAL classes
from val_audio_library import ValAudioLibrary
from val_speech_settings import ValSpeechSettings

class Controller:
    def main():
        #Import VAL settings file
        fileContent = ValSpeechSettings.fileSettingsRead()

        #Engine - Testing
        
        engine = ""
        
        """
        engine = ValAudioLibrary.speechEngineSelection()
        speechEngineSpeedPercentage(engine, fileContent)
        speechEngineVolumePercentage(engine, fileContent)

        engine.say(content.get('val').get('message_welcome')) #Speech sentence
        engine.runAndWait()
        engine.stop()
        """

        #Capture user voice command
        userCommand = detectUserVoice(fileContent, engine)

        #Transcribe on terminal the user's voice command
        userCommand = userCommand.lower()
        print(userCommand)

        #Split all text word into an array
        userCommandArray = userCommand.split()

        print(userCommandArray)
        
        #Check if command exists
        voiceCommandKey = ValSpeechSettings.commandValidation(fileContent, userCommandArray[0])

        #Execute asked command
        if voiceCommandKey == True:
            ValSpeechSettings.commandExecution(fileContent, engine, userCommandArray)

    def detectUserVoice(fileContent, engine):
        try:
            with speech_recognition.Microphone() as source:
                if fileContent.get('settings').get('debug') == 'on':
                    #Debug a the commands from a text command example
                    print('Debug option has been turned on')
                    return ValSpeechSettings.commandDebugOn(fileContent)
                elif fileContent.get('settings').get('debug') == 'off':
                    print('Debug option has been turned off')
                    time.sleep(1)
                    return ValSpeechSettings.commandDebugOff(fileContent, source)
                else:
                    print('Debug option has not been found')
                    exit()

        except:
            print("Something unexpected has been happened!")
            
            print(fileContent.get('val').get('message_error_microphone'))
            #engine.say(fileContent.get('val').get('message_error_microphone'))

            exit()
