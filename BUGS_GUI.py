from tkinter import *
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    talk("Hello, My name is Bugzsnax, you can call me Bugs. Click on my icon to start the program")


def take_command(ask=False):
    try:
        command = ""
        with sr.Microphone() as source:
            if ask:
                talk(ask)
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if there_exists(["Bugs"]):
                command = command.replace('bugs', '')
                print(command)
    except:
        pass
    return command


class person:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True






def run_Bugzz():
    talk("So what do you want me to do")
    
      

    def there_is(terms):
        for term in terms:
            if term in incommand:
                return True

    while(1):
        voice_data = take_command()
        print(voice_data)
        if there_exists(['hello'], voice_data):
            greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
            greet = greetings[random.randint(0, 4)]
            talk(greet)
    
        elif there_exists(["what is your name", "what's your name", "tell me your name"], voice_data):
            if person_obj.name:
                talk("my name is Bugzsnax")
            else:
                talk("my name is Bugzsnax.")
                talk("what is your name")
                print("Enter your name by saying 'my name is %your name%' ")
    
        elif there_exists(["my name is"], voice_data):
            person_name = voice_data.split("is")[-1].strip()
            talk(f"okay, i will remember that {person_name}")
            person_obj.setName(person_name)
        elif there_exists(["how are you", "how are you doing"], voice_data):
            talk(f"I'm very well, thanks for asking {person_obj.name}")
    
        elif 'play' in voice_data:
            try:
                song = voice_data.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song, use_api=True)
            except:
                print("Connection refused, please try again later")
        elif there_exists(["search for", "google"], voice_data) and 'youtube' not in voice_data:

            search_term = voice_data.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            talk(f'Here is what I found for {search_term} on google')
# youtube search: Example: Youtube explain semiconductor
        elif there_exists(["youtube"], voice_data):
            search_term = voice_data.split("youtube")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            talk(f'Here is what I found for {search_term} on youtube')
        elif 'time' in voice_data:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        # search in wikipedia, example wiki salman khan
        elif there_exists(["wiki", "wikipedia"], voice_data):
            try:
                wiki_term = voice_data.split("wiki")[-1]
            # ,2) means we get 2 lines of text from wiki
                info = wikipedia.summary(wiki_term, 2)
                print(info)
                talk(info)
            except:
                    print("There is no such page available on wikipedia")
                    talk("There is no such page available on wikipedia")
        elif 'joke' in voice_data:
            talk(pyjokes.get_joke())
        elif there_exists(["exit", "quit", "goodbye", "shut down", "duck"], voice_data):
            talk("going offline")
            exit()
        elif there_exists(["change", "text", "terminal"], voice_data):
            talk("text mode initiated")
            incommand = input("press enter and then enter commands")
            def run_textBugzz(incommand):

                if there_is(['hello']):
                    greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
                    greet = greetings[random.randint(0, 4)]
                    talk(greet)

                elif there_is(["what is your name", "what's your name", "tell me your name"]):
                    if person_obj.name:
                        talk("my name is Bugzsnax")
                    else:
                        talk("my name is Bugzsnax.")
                        talk("what is your name")
                        print("Enter your name with 'my name is %your name%' ")

                elif there_is(["my name is"]):
                    person_name = incommand.split("is")[-1].strip()
                    talk(f"okay, i will remember that {person_name}")
                    person_obj.setName(person_name)

                elif there_is(["how are you", "how are you doing"]):
                    talk(f"I'm very well, thanks for asking {person_obj.name}")

                elif 'play' in incommand:
                    try:
                        song = incommand.replace('play', '')
                        talk('playing ' + song)
                        pywhatkit.playonyt(song, use_api=True)
                    except:
                        print("Connection denied, please try again later")

                elif there_is(["search for", "google"]) and 'youtube' not in incommand:
                    search_term = incommand.split("for")[-1]
                    url = f"https://google.com/search?q={search_term}"
                    webbrowser.get().open(url)
                    talk(f'Here is what I found for {search_term} on google')

# youtube search: Example: Youtube chemistry lectures
                elif there_is(["youtube"]):
                    search_term = incommand.split("youtube")[-1]
                    url = f"https://www.youtube.com/results?search_query={search_term}"
                    webbrowser.get().open(url)
                    talk(f'Here is what I found for {search_term} on youtube')

                elif 'time' in incommand:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    talk('Current time is ' + time)
        # search in wikipedia, example wiki world war 2

                elif there_is(["wiki", "wikipedia"]):
                    try:
                        wiki_term = incommand.split("wiki")[-1]
                        info = wikipedia.summary(wiki_term, 2)
                        print(info)
                        talk(info)
                    except:
                        print("There is no such page available on wikipedia")
                        talk("There is no such page available on wikipedia")

                elif 'joke' in incommand:
                    talk(pyjokes.get_joke())

                elif there_is(["exit", "quit", "goodbye", "shut down", "duck"]):
                    talk("going offline")
                    exit()    

                elif there_is(["voice"]):
                    talk("voice mode initiated")
                    return 1

                elif there_is(["why though", "why", "why thou"]):
                    talk("Never ask a man his salary, a woman her age and me why I can not do something")  
                    print("Thanks for understanding")

                else:
                    print("I am unable to process that")
                    talk("I am unable to process that")
                
            while(1):
                incommand = input()
                b = run_textBugzz(incommand)  
                if b == 1:
                    break

        else:
            talk('Please say the command again.')

person_obj = person()        


def main_screen():

      global screen
      screen = Tk()
      screen.title("Bugs")
      screen.geometry("300x450")
      screen.iconbitmap('BUGS.ico')


      name_label = Label(text = "BUGSNAX",width = 300, bg = "black", fg="white", font = ("Calibri", 13))
      name_label.pack()


      microphone_photo = PhotoImage(file = "assistant_logo2.png")
      microphone_button = Button(image=microphone_photo, command = run_Bugzz)
      microphone_button.pack(pady=10)

     # settings_photo = PhotoImage(file = "settings.png")
    #  settings_button = Button(image=settings_photo, command = change_name_window)
    #  settings_button.pack(pady=10)
       
      info_button = Button(text ="About Me", command = wishMe)
      info_button.pack(pady=10)

      name_label = Label(text = "Say or type 'quit/exit' to close",width = 300, bg = "grey", fg="white", font = ("Calibri", 10))
      name_label.pack()

      screen.mainloop()


main_screen()



#while(1):
 #   voice_data = take_command()
  #  print(voice_data)
  #  main_screen(voice_data)

