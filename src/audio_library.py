#Import system libraries
import platform

#Import external libraries
import pyttsx3

class AudioLibrary:
    def speechEngineSelection():
        if platform.system() == "Darwin":
            return pyttsx3.init('nsss')
        elif platform.system() == "Linux":
            return pyttsx3.init('espeak')
        elif platform.system() == "Windows":
            return pyttsx3.init('sapi5')
        else:
            return pyttsx3.init()

    def speechEngineSpeedPercentage(engine, fileContent):
        if fileContent.get('settings').get('speech_speed') == "low":
            engine.setProperty('rate', 118)
        elif fileContent.get('settings').get('speech_speed') == "normal":
            engine.setProperty('rate', 178)
        elif fileContent.get('settings').get('speech_speed') == "fast":
            engine.setProperty('rate', 278)

    def speechEngineVolumePercentage(engine, fileContent):
        #Speech percent volume (0-1)
        if fileContent.get('settings').get('speech_volume') == "low":
            engine.setProperty('volume', 0.5)
        elif fileContent.get('settings').get('speech_volume') == "normal":
            engine.setProperty('volume', 0.7)
        elif fileContent.get('settings').get('speech_volume') == "high":
            engine.setProperty('volume', 1)