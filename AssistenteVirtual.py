# IMPORTA MODULO PARA EXECUTAR PROGRAMA EM SEGUNDO PLANO E NAO TRAVAR O PYTHON
# NESSE EXEMPLO A  CALCULADORA
import subprocess
import time
import webbrowser

import pyautogui as pyautogui
import pyttsx3
import speech_recognition as sr

t = time.localtime()

#time.sleep(0.5)
audio = sr.Recognizer()
audio2 = sr.Recognizer()
audio3 = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('Olá, eu sou a VAL')
#maquina.say('Como posso ajudar?. Para fazer uma pesquisa diga buscar e aguarde!')
maquina.runAndWait()
maquina.stop()

try:
    with sr.Microphone() as source:

        audio.adjust_for_ambient_noise(source)
        #time.sleep(1)
        print('Ouvindo..')
        voz = audio.listen(source)
        with open('voz.wav', 'wb') as f:
            f.write(voz.get_wav_data())
        comando = audio.recognize_google(voz, language='pt-BR')
        time.sleep(1)
        comando = comando.lower()
        print(comando)
        #print(current_time)

        if 'navegador' in comando:
            #comando = comando.split()
            comando = comando.split('navegador ')
            x = ('https://'+"".join(comando))
            webbrowser.open(x, new=2)
            print(x)

        if 'buscar' in comando:

            maquina.say('Certo. Posso buscar no google. Na wiki e no dicionário.')
            maquina.say('O que você deseja? diga google, wiki ou palavra e a sua pesquisa')
            maquina.runAndWait()
            time.sleep(1)
            print('Ouvindo..')
            voz3 = audio3.listen(source)
            comando3 = audio3.recognize_google(voz3, language='pt-BR')
            time.sleep(1)
            comando3 = comando3.lower()
            print(comando3)
            print("Current Time =", t)

            if 'google' in comando3:
                # comando = comando.split()
                comando3 = comando3.split('google ')
                x = ('https://www.google.com/search?q='"+".join(comando3))
                webbrowser.open(x, new=2)
                print(x)

            if 'wiki' in comando3:
                #comando = comando.split()
                comando3 = comando3.split('wiki ')
                #x = ('https://www.google.com/search?q='"+".join(comando))
                x = ('https://pt.wikipedia.org/wiki/'"_".join(comando3))
                webbrowser.open(x, new=2)
                print(x)

            if 'palavra' in comando3:
                #comando = comando.split()
                comando3 = comando3.split('palavra ')
                #x = ('https://www.google.com/search?q='"+".join(comando))
                x = ('https://pt.wiktionary.org/wiki/'"".join(comando3))
                webbrowser.open(x, new=2)
                print(x)


        if 'calculadora' in comando:
            time.sleep(1)
            print('Ouvindo..')
            voz2 = audio2.listen(source)
            comando2 = audio2.recognize_google(voz2, language='pt-BR')
            time.sleep(1)
            #comando = comando.lower()
            print(comando2)
            subprocess.Popen(["C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_10.2109.54.0_x64__8wekyb3d8bbwe\CalculatorApp.exe"])
            time.sleep(1)
            pyautogui.press("1")
            pyautogui.press("2")
            pyautogui.press("*")
            pyautogui.press("4")
            pyautogui.press("enter")

        if 'horas' in comando:
            #maquina = pyttsx3.init()
            maquina.say('Agora são %d  e %s'% (t.tm_hour,t.tm_min))
            maquina.runAndWait()
            print("Current Time =", t)



except:
   print(comando)
   print('Microfone não está ok')