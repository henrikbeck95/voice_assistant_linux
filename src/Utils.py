#Import system libraries
import os
import subprocess
import time

#Import external libraries
import speech_recognition
import yaml

#Loading the libraries functions as variables
audio = speech_recognition.Recognizer()

class Utils:
    #Auxiliary lists for improving voice detection with their possibilities
    AUX_WORD_BRIGHTNESS = ["brightness"]
    AUX_WORD_CLOSE = ["close"]
    AUX_WORD_DOWN = ["down"]
    AUX_WORD_FLOAT = ["float", "floor"]
    AUX_WORD_FOCUS = ["focus"]
    AUX_WORD_FULL = ["full", "full-screen", "full", "you", "boom", "who", "bookoo", "foo", "poo", "pool"]
    AUX_WORD_GO = ["go"]
    AUX_WORD_LAST = ["last"]
    AUX_WORD_LEFT = ["left"]
    AUX_WORD_MOVE = ["move"]
    AUX_WORD_NEXT = ["next"]
    AUX_WORD_PREVIOUS = ["previous"]
    AUX_WORD_RIGHT = ["right"]
    AUX_WORD_SOFTWARE = ["software", "open"]
    AUX_WORD_STICK = ["stick"]
    #AUX_WORD_SYSTEM = ["system", "systems", "c-span", "eastern", "casement", "easton", "easter", "cstep", "houston", "sister", "piston", "assistant"]
    AUX_WORD_SYSTEM = listWordDictionary(pathDirectory, testWord)
    AUX_WORD_UP = ["up"]
    AUX_WORD_VOLUME = ["volume"]
    AUX_WORD_WINDOW = ["window", "windows"]
    AUX_WORD_WORKSPACE = ["workspace", "wordspace"]
    #ZZZZZZZZZZZ_NUMBER #Replace it content for a number value

    def checkIfFileExists(pathFile):
        if os.path.isfile(pathFile):
            return True
        else:
            return False

    def fileDictionaryAppend(pathFile, userCommand):
        try:
            fileObject = open(pathFile, mode='a', encoding='utf-8')
            #fileObject.write(userCommand)
            EachStringNewLine = userCommand.replace(' ', '\n')
            fileObject.write('\n' + EachStringNewLine)
        finally:
            fileObject.close()

    def fileDictionaryClear(pathFile):
        try:
            fileObject = open(pathFile, mode='w', encoding='utf-8')
            fileObject.write('')

        finally:
            fileObject.close()

    def fileDictionaryLoadAsList(pathFile):
        try:
            fileObject = open(pathFile, mode='r', encoding='utf-8')
            listContent = fileObject.readlines()

            #print (f'VARIABLES: {listContent}')

            #Remove '\n' from string
            listContentAux = []

            for i in listContent:
                listContentAux.append(i.replace("\n", ""))

            #print (f'VARIABLES2: {listContentAux}')
            return listContentAux

        finally:
            fileObject.close()
    
    def fileDictionaryPath(pathDirectory, testWord):
        #print(f'PATH DIRECTORY: {pathDirectory}')
        pathFile = pathDirectory + "/dictionary_" + testWord + ".txt"

        return pathFile
    
    def listWordDictionary(pathDirectory, testWord):
        filePathDictionary = Utils.fileDictionaryPath(pathDirectory, testWord)
        listWordDictionary = Utils.fileDictionaryLoadAsList(filePathDictionary)
        
        return listWordDictionary
    
    def fileDictionaryRead(pathFile):
        try:
            fileObject = open(pathFile, mode='r', encoding='utf-8')
            fileContent = fileObject.read()
            print(f'The content from {pathFile}:\n{fileContent}')

        finally:
            fileObject.close()
    
    def fileDictionaryRemoveAllBlankLine(pathFile):
        try:
            fileObject = open(pathFile, mode='r+', encoding='utf-8')

            lines = fileObject.readlines()
            fileObject.seek(0)
            fileObject.writelines(line for line in lines if line.strip())
            fileObject.truncate()

        finally:
            fileObject.close()

    def fileDictionaryWrite(pathFile, userCommand):
        try:
            fileObject = open(pathFile, mode='w', encoding='utf-8')
            #fileObject.write(userCommand)
            EachStringNewLine = userCommand.replace(' ', '\n')
            fileObject.write(EachStringNewLine)

        finally:
            fileObject.close()
    
    #Filter the external file to store only unique values
    def fileDictionarySort(pathFile):
        #Get all values        
        listContentValuesAll = Utils.fileDictionaryLoadAsList(pathFile)

        #Get only unique values
        setContentValuesUnique = set(listContentValuesAll)
        #print(f'UNIQUE: {setContentValuesUnique}')

        #Convert set to list
        listContentValuesUnique = list(setContentValuesUnique)

        #Sort the values
        listContentValuesUnique.sort()
        #print(f'SORTED: {listContentValuesUnique}')
        
        #Clear old file content
        Utils.fileDictionaryClear(pathFile)

        #Overwrite
        try:
            fileObject = open(pathFile, mode='w', encoding='utf-8')

            for i in range(len(listContentValuesUnique)):
                fileObject.write('\n')
                fileObject.write(listContentValuesUnique[i])
                fileObject.write('\n')

        finally:
            fileObject.close()
        '''
        '''

        Utils.fileDictionaryRemoveAllBlankLine(pathFile)

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
        #aux = 'bash -c "%s"' %(command)
        aux = 'sh -c "%s"' %(command)
        stdout = subprocess.getoutput(aux)
        print(stdout)
    
    def shellScriptCommandSpeak(voiceSpeech):
        #Get user home directory path
        pathHomeUser = os.path.expanduser('~')

        #Shell Script Library file location
        fileShellScriptLibrary = ''

        if Utils.checkIfFileExists('/usr/local/bin/shell-script-library') == True:
            fileShellScriptLibrary = '/usr/local/bin/shell-script-library'
        elif Utils.checkIfFileExists(f'{pathHomeUser}/.local/bin/shell-script-library') == True:
            fileShellScriptLibrary = f'{pathHomeUser}/.local/bin/shell-script-library'
        else:
            print("Shell Script Library is not installed on operating system.")
            exit(0)

        if Utils.checkIfFileExists(fileShellScriptLibrary) == True:
            #command = "source " + fileShellScriptLibrary + " && system_sound_voice_speech_text_complex " + "'" + voiceSpeech + "'"
            command = "source " + fileShellScriptLibrary + " && system_sound_voice_speech_text_simple " + "'" + voiceSpeech + "'"
            Utils.shellScriptCommandRun(command)
        else:
            print("Shell script has not been found")

    #MUST BE FIXED
    def urlGenerateGoogle(query):
        return "google.com/search?q=your+query"

    #MUST BE FIXED
    def urlGenerateMaps(query):
        return "http://maps.google.com/?q=your+query"

    #MUST BE FIXED
    def urlGenerateYoutube(query):
        return "https://www.youtube.com/results?search_query=your+query"

    def valCommandDetectUserVoice(fileContent):
        commandListening = fileContent.get('val').get('message_running')

        print(commandListening)
        Utils.shellScriptCommandSpeak(commandListening)

        #List all available microphones
        #print(speech_recognition.Microphone.list_microphone_names())

        try:
            #with speech_recognition.Microphone(device_index=7) as source:
            with speech_recognition.Microphone() as source:
                time.sleep(1)
                return Utils.valCommandRecording(fileContent, source)

        except:
            codeError = fileContent.get('val').get('message_error_microphone')

            print("Something unexpected has been happened!")
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)
            #exit()

    def valCommandRecording(fileContent, source):
        #Inspect audio file for removing some ambient noise
        audio.adjust_for_ambient_noise(source)
        
        '''
        audio.energy_threshold = 1932
        audio.dynamic_energy_threshold = True
        audio.pause_threshold=1.2
        '''

        print(fileContent.get('val').get('message_running'))
        
        #Save the user's voice recording as an external file
        pathFileValUserVoice = fileContent.get('user').get('file_recording')

        with open(pathFileValUserVoice, 'wb') as file_external:
            userVoiceTranscription = audio.listen(source)
            file_external.write(userVoiceTranscription.get_wav_data())



        try:
            #Load the user's voice recording
            result = audio.recognize_google(userVoiceTranscription, language=fileContent.get('settings').get('language'))
        except audio.UnknownValueError:
            print("Could not understand audio")
        except audio.RequestError as e:
            print("Could not request results {0}".format(e))



        #Remove the user's voice recording file if exists
        if Utils.checkIfFileExists(pathFileValUserVoice) == True:
            command = "rm " + pathFileValUserVoice
            Utils.shellScriptCommandRun(command)
        else:
            print(pathFileValUserVoice + " file has not been found")

        return result
    
    def valCommandExecutionMenu(fileContent, userCommandArray, codeError):
        if userCommandArray[0] in Utils.AUX_WORD_SOFTWARE:
            Utils.valCommandExecutionSoftware(fileContent, userCommandArray, codeError)
        elif userCommandArray[0] in Utils.AUX_WORD_SYSTEM:
            Utils.valCommandExecutionSystem(fileContent, userCommandArray, codeError)
        else:
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)

    #Check this out
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
        if userCommandArray[1] in Utils.AUX_WORD_BRIGHTNESS:
            print()
            if userCommandArray[2] in Utils.AUX_WORD_UP:
                os.system(fileContent.get('system').get('brightness').get('up'))
            elif userCommandArray[2] in Utils.AUX_WORD_DOWN:
                os.system(fileContent.get('system').get('brightness').get('down'))
            else:
                print(codeError)
                Utils.shellScriptCommandSpeak(codeError)
        
        elif userCommandArray[1] in Utils.AUX_WORD_VOLUME:
            print()
            if userCommandArray[2] in Utils.AUX_WORD_UP:
                os.system(fileContent.get('system').get('volume').get('up'))
            elif userCommandArray[2] in Utils.AUX_WORD_DOWN:
                os.system(fileContent.get('system').get('volume').get('down'))
            else:
                print(codeError)
                Utils.shellScriptCommandSpeak(codeError)

        elif userCommandArray[1] in Utils.AUX_WORD_WINDOW:
            if userCommandArray[2] in Utils.AUX_WORD_CLOSE:
                os.system(fileContent.get('system').get('window').get('close'))
            elif userCommandArray[2] in Utils.AUX_WORD_FLOAT:
                os.system(fileContent.get('system').get('window').get('floating'))
            elif userCommandArray[2] in Utils.AUX_WORD_FULL:
                os.system(fileContent.get('system').get('window').get('full_screen'))
            elif userCommandArray[2] in Utils.AUX_WORD_STICK:
                os.system(fileContent.get('system').get('window').get('stick'))
            elif userCommandArray[2] in Utils.AUX_WORD_FOCUS:
                if userCommandArray[3] in Utils.AUX_WORD_UP:
                    os.system(fileContent.get('system').get('window').get('focus').get('up'))
                elif userCommandArray[3] in Utils.AUX_WORD_LEFT:
                    os.system(fileContent.get('system').get('window').get('focus').get('left'))
                elif userCommandArray[3] in Utils.AUX_WORD_RIGHT:
                    os.system(fileContent.get('system').get('window').get('focus').get('right'))
                elif userCommandArray[3] in Utils.AUX_WORD_DOWN:
                    os.system(fileContent.get('system').get('window').get('focus').get('down'))
                else:
                    print(codeError)
                    Utils.shellScriptCommandSpeak(codeError)

            elif userCommandArray[2] in Utils.AUX_WORD_MOVE:
                if userCommandArray[3] in Utils.AUX_WORD_UP:
                    os.system(fileContent.get('system').get('window').get('move').get('up'))
                elif userCommandArray[3] in Utils.AUX_WORD_LEFT:
                    os.system(fileContent.get('system').get('window').get('move').get('left'))
                elif userCommandArray[3] in Utils.AUX_WORD_RIGHT:
                    os.system(fileContent.get('system').get('window').get('move').get('right'))
                elif userCommandArray[3] in Utils.AUX_WORD_DOWN:
                    os.system(fileContent.get('system').get('window').get('move').get('down'))
                else:
                    print(codeError)
                    Utils.shellScriptCommandSpeak(codeError)
            
        elif userCommandArray[1] in Utils.AUX_WORD_WORKSPACE:
            if userCommandArray[2] in Utils.AUX_WORD_GO:
                if userCommandArray[3] in Utils.AUX_WORD_LAST:
                    os.system(fileContent.get('system').get('workspace').get('go').get('last'))
                elif userCommandArray[3] in Utils.ZZZZZZZZZZZ_NUMBER:
                    os.system(fileContent.get('system').get('workspace').get('go').get('number'))
                elif userCommandArray[3] in Utils.AUX_WORD_NEXT:
                    os.system(fileContent.get('system').get('workspace').get('go').get('next'))
                elif userCommandArray[3] in Utils.AUX_WORD_PREVIOUS:
                    os.system(fileContent.get('system').get('workspace').get('go').get('prev'))
                else:
                    print(codeError)
                    Utils.shellScriptCommandSpeak(codeError)

            elif userCommandArray[2] in Utils.AUX_WORD_MOVE:
                if userCommandArray[3] in Utils.AUX_WORD_LAST:
                    os.system(fileContent.get('system').get('workspace').get('move').get('last'))
                elif userCommandArray[3] in Utils.ZZZZZZZZZZZ_NUMBER:
                    os.system(fileContent.get('system').get('workspace').get('move').get('number'))
                elif userCommandArray[3] in Utils.AUX_WORD_NEXT:
                    os.system(fileContent.get('system').get('workspace').get('move').get('next'))
                elif userCommandArray[3] in Utils.AUX_WORD_PREVIOUS:
                    os.system(fileContent.get('system').get('workspace').get('move').get('prev'))
                else:
                    print(codeError)
                    Utils.shellScriptCommandSpeak(codeError)

            else:
                print(codeError)
                Utils.shellScriptCommandSpeak(codeError)
        
        else:
            print(codeError)
            Utils.shellScriptCommandSpeak(codeError)

    #MUST BE FIXED
    def valCommandValidation(fileContent, userCommandArray):
        print("HERE WE GO: " + userCommandArray)

        '''
        if userCommandArray[1] in Utils.AUX_WORD_SYSTEM:
            userCommandArray = "system"
        '''
        
        '''
        match userCommandArray:
            case "sistema" | "system" | "c-span" | "eastern" | "casement" | "easton" | "easter" | "houston" | "sister" | "piston" | "assistant":
                userCommandArray = "system"
        '''
        
        print("HERE WE GO: " + userCommandArray)
        
        '''
        '''
        if userCommandArray in fileContent:
            print(fileContent.get('val').get('message_success_command_listed'))
            return True
        else:
            print(fileContent.get('val').get('message_error_command_not_listed'))
            return False

    def valCommandDebugOn(fileContent):
        #Debugging commands for softwares
        #userCommand = "software firefox"
        #userCommand = "software menu"
        #userCommand = "software nautilus"
        #userCommand = "software spotify" #Not working
        #userCommand = "software terminal"

        #Debugging commands for system
        #userCommand = "system brightness up"
        #userCommand = "system brightness down"
        #userCommand = "system volume up"
        #userCommand = "system volume down"
        #userCommand = "system window close"
        #userCommand = "system window floating"
        #userCommand = "system window stick"
        userCommand = "system window full screen"
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

        #TRAINING
        #userCommand = "software sowfjoj softwari dgdkkgl"
        userCommand = "lalalala lejgwe ltet"

        return userCommand