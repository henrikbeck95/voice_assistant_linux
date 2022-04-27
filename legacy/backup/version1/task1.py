import os
import pyttsx3 as psy
import speech_recognition as sr
import webbrowser
import smtplib
import wikipedia

print('''
Commands Available:
1. Open Notepad
2. Open Windows Media player
3. Open MS Excel
4. Open Chrome Browser
5. Open Vscode
6. Open Firefox
7. Open Microsoft word
8. Play Music
9. Send Email
10. Open website like (Wikipedia, linkedin)
''')

psy.speak("Welcome to Python Automation program")
#os.system("sleep 1")
psy.speak("Choose option from above menu")

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Start Speaking!")
        psy.speak("Star Speaking.")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("Working on it")
        psy.speak("Working on it.")

        try:    
            text = r.recognize_google(audio, language="en-in")
            print("You said  {}".format(text))
        except:
            psy.speak("Sorry Unable to recognize your voice please try again!")        
    
    p = text.lower()
  
    if("run " in p) or ("open " in p):
        if("exit" in p) or ("do not " in p) or ("don't " in p):
            exit()
        else:
            if ("Notepad" in p) or ("notepad" in p):
                psy.speak("Here is you Notepad")
                os.system("notepad")

            elif("wmplayer" in p) or ("Windows Media player" in p):
                psy.speak("opening Windows Media Player")
                os.system("wmplayer")

            elif("Excel" in p) or ("excel" in p):
                psy.speak("opening Microsoft Excel")
                os.system("EXCEL")

            elif("chrome" in p) or ("browser" in p):
                psy.speak("opening Google Chrome: Your internet browser")
                os.system("chrome")

            elif("code" in p) or ("vscode" in p) or ("visual studio code" in p):
                psy.speak("opening Code Blocks: Your C compiler")
                os.system("code")

            elif("Word" in p) or ("word" in p):
                psy.speak("opening Microsoft Word")
                os.system("WINWORD")

            elif("Mozilla Firefox" in p) or ("mozilla firefox" in p) or ("firefox" in p):
                psy.speak("opening Mozilla Firefox: Your internet browser")
                os.system("firefox")

            elif("music" in p) or ("Play Music" in p) or ("play music" in p):
                psy.speak("Playing Music")
                music_dir = os.path.join(os.environ['USERPROFILE'], "Music")
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif("send email" in p) or ("Send Email" in p) or ("Email" in p):
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('youremail@gmail.com', 'your-password')
                    psy.speak("What should I say?")
                    content = text
                    to = "anyone@gmail.com"
                    server.sendmail('youremail@gmail.com', to, content)
                    psy.speak("Email has been sent!")
                    server.close()
                    
                except Exception as e:
                    print(e)
                    psy.speak("Unable to send email please try again")

            elif ("wikipedia") in p:
                psy.speak('Searching Wikipedia...')
                query = p.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                psy.speak("According to Wikipedia")
                print(results)
                psy.speak(results)

            elif ("youtube" in p):
                psy.speak("Opening youtube what would you like to watch")
                query = text
                webbrowser.open(
                    "http://www.youtube.com")                          

            elif ("google search" in p):
                psy.speak("Opening google what would you like to search")
                query = text
                webbrowser.open("https://google.com")

    elif("close" in p) or ("stop" in p) or ("exit"in p):
        psy.speak("Bye Have a Great Day")
        exit()

    elif("hi" in p) or ("hello" in p) or ("hey"in p):
        psy.speak("Hello How can I help you")
        Commands()
    else:
        psy.speak("Unable to run your command please try again")
