#Importing libraries internal
import datetime

#Importing libraries external
import speech_recognition as sr
import pyttsx3 

#Calling libraries
audio = sr.Recognizer()
#maquina = pyttsx3.init()

#Coding
try:
    with sr.Microphone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        print(comando)

        if 'val' in comando:
            print(comando)

except:
    print('Microfone nao esta funcionando bem!')

