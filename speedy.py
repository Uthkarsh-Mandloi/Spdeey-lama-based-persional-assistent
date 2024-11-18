import pyttsx3
import os
import bs4, requests, datetime, webbrowser, GoogleNews
import speech_recognition as sr
import random
import datetime
import time
import colorama  # Import colorama module for cross-platform colored output
from colorama import Fore
import pyautogui
from pyautogui import *
import pywhatkit as kit # pip install pywhatkit -> cmd
import speedtest # pip install speedtest-cli -> cmd
# import chr
import wikipedia
os.environ['GROQ_API_KEY'] = "enter your  own APIkey" 
from groq import Groq


engine = pyttsx3.init('sapi5')
vocies = engine.getProperty('voices')
print(vocies[0].id)
engine.setProperty('voices',vocies[1].id)

def speak(audio):
    engine.setProperty("rate", 200)
    print("")
    engine.say(audio)
    print("")
    engine.runAndWait()

def takecommand():
    # command1=input("text : ")
    command1 = sr.Recognizer()
    standby_count = 0  # Counter for standby mode
    standby_threshold = 3  # Number of times to repeat "I didn't understand" before standby

    with sr.Microphone() as source:
        print("")
        print('Listening......')
        print("")
        command1.pause_threshold = 0.5
        audio = command1.listen(source,phrase_time_limit=4)

        try:
            print("")
            print('recognizing......')
            command = command1.recognize_google(audio,language='en-in')
            print(f"usersaid:{command}\n")
            return command

        except Exception as e:
            print(e)
            standby_count += 1
            if standby_count >= standby_threshold:
                standby_count = 0  # Reset standby count
                speak("I didn't understand anything. Entering standby mode.")
                time.sleep(2)  # Give a short pause before entering standby
                standby_mode()

            print("say that again please....")
    return command1


client = Groq()

def chatbot(prompt):
  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content":prompt,
          }
      ],
      model="llama3-8b-8192",
      stream=False,
  )
  return chat_completion.choices[0].message.content

def standby_mode():
    standby_name = "Speedy"  # Replace with the wake word or name you want
    command1 = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            command1.pause_threshold = 0.5
            audio = command1.listen(source,phrase_time_limit=3)

            try:
                print("Recognizing wake word...")
                wake_word = command1.recognize_google(audio, language='en-in')
                print(f"Wake word said: {wake_word}\n")

                if standby_name.lower() in wake_word.lower():
                    speak("Standby mode deactivated. How can I help you?")
                    return
            except Exception as e:
                print(e)
       
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12 :
        speak("Good Mornig!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")

    speak("Hello! I am Speedy in your service. How can I help you?")

# Program execution


def close_program(program_name):
    try:
        os.system(f"taskkill /im {program_name}.exe /f")
        speak(f"{program_name} band ho gaya hai.")
    except Exception as e:
        speak("Kuch gadbad ho gayi, program nahi band hua.")

def continue_after_break():
    colorama.init(autoreset=True)  # Initialize colorama for cross-platform colored output
    
    speak("Do you want to continue? (yes/no): ")
    response = takecommand().lower()
    if response == "no":
        speak("Okay, taking a break. For how many minutes would you like to pause?")
        break_time = int(takecommand())
        remaining_time = break_time * 60
        speak(f"Sure! I'll be back after {break_time} minutes. Take your time!")

        while remaining_time > 0:
            # Provide reminder during the last 1 minute and 10 seconds
            if remaining_time == 70:
                speak("Just 1 minute and 10 seconds left.")

            # Change color to red during the last 10 seconds
            if remaining_time == 10:
                speak("Only 10 seconds remaining. Get ready to resume!")

            time.sleep(1)  # Sleep for 1 second
            remaining_time -= 1
            
        speak("Break time is over. I'm back!")
        return True
        
    elif "yes" in response  or "continue" in response:
        return True
    elif "close" in response:
        speak("Okay! Closing the program. See you next time.")
        return False
    else:
        speak("Sorry, I didn't understand that. Do you want to continue? (yes/no): ")
        return continue_after_break()

#main function
    

wishme()
while True:
    command = takecommand().lower()

    # Check if the command contains the word 'open'
    if "open" in command:
        command = command.replace("open","")
        # press("win", "s")
        # sleep(.2)
        # typewrite(command)
        # sleep(.2)
        # press("enter")
        # Simulate pressing Win + S keys together
        pyautogui.hotkey("win", "s")
        
        sleep(0.5)  # Wait for the search bar to open
        
        # Type the command
        pyautogui.typewrite(command)
        
        sleep(0.2)
        pyautogui.press("enter")  # Press Enter to open the application

    elif "game" in command or "play game" in command or "play a game" in command:
        print("great! i have 3 Games for you Would you like to play")
        speak("great! i have 3 Games for you Would you like to play")

        command== "game"

        while command == "game":

            ak=takecommand()
            
            if "yes" in ak:

                while ak == "yes":
                    print("What would you like to play"
                            "Snake Water Gun"
                            "guess the Number"
                            "prices less K.B.C")
                    speak("again great! What would you like to play Snake Water Gun, guess the Number or prices less KBC")
                    gm=takecommand()
                    
                    if "snake" in gm or "water" in gm or "gun" in gm:
                        os.system(f"start vswg.py")
                        standby_mode()

                    elif "guess" in gm or "number" in gm:
                        os.system(f"start guno.py")
                        standby_mode()

                    elif"kbc" in gm or "quize" in gm:
                        os.system(f"start kbc.py")
                        standby_mode()

                    else:
                        print(" i didn't understan speak again pls")
                        speak(" i didn't understan speak again pls")
                        ak="yes"

            elif "no" in ak:
                print("no problem")
                speak("no problem")
                break
            else:
                print(" i didn't understan speak again pls")
                speak(" i didn't understan speak again pls")
                command="game"

    elif "intro" in command or "introduction" in command or "intradus" in command:
        print("Welcome to Speedy - Your Smart AI Assistant!")

        # Introduction
        print("Hey there, I'm Speedy, your trusty AI companion, here to make your digital life a breeze!")
        speak("Hey there, I'm Speedy, your trusty AI companion, here to make your digital life a breeze!")

        speak(" i know you hsve many quetions for me like what i am? no! you know what i am what i can do!,how i work!, what is A I!,why my name speedy! etc")

        print("What I Can Do")
        speak("What I Can Do!")
        print("I can open programs, search the internet, open sites, and offer three entertaining games: Snake Water Gun, Guess the Number, and Prices-Less KBC.")
        speak("I can open programs, search the internet, open sites, and offer three entertaining games: Snake Water Gun, Guess the Number, and Prices-Less KBC.")

        # How I Work
        speak("how i wor!")
        print("I operate on a sophisticated algorithm that analyzes your input and responds with the most fitting reply.")
        speak("I operate on a sophisticated algorithm that analyzes your input and responds with the most fitting reply.")

        # About AI
        speak("What is A I!")
        print("Artificial Intelligence (AI) is not just a buzzword; it's a revolutionary force transforming every aspect of our lives.")
        speak("Artificial Intelligence (AI) is not just a buzzword; it's a revolutionary force transforming every aspect of our lives.")


        # Why Speedy
        speak("why my name is speedy!")
        print("My name might be Speedy, but don't let that fool you—I'm here to bring a touch of humor to your day while being your efficient digital assistant.")
        speak("My name might be Speedy, but don't let that fool you—I'm here to bring a touch of humor to your day while being your efficient digital assistant.")

        # The Future of AI
        print("AI is not just the future; it's the present. From healthcare to finance, education to entertainment, AI is making waves.")
        speak("AI is not just the future; it's the present. From healthcare to finance, education to entertainment, AI is making waves.")

        # Choosing AI
        print("Why choose AI? Because I'm here to simplify your life, make tasks a breeze, and keep you entertained.")
        speak("Why choose AI? Because I'm here to simplify your life, make tasks a breeze, and keep you entertained.")

        #Closing
        speak("So, buckle up, as we embark on this AI-driven journey together. Ready for the future? Let's make it happen, one command at a time!")


    elif "guess" in command or "number" in command:
        os.system(f"start guno.py")
        standby_mode()

    elif"kbc" in command or "quize" in command:
        os.system(f"start kbc.py")
        standby_mode()

    elif "snake" in command or "water" in command or "gun" in command:
        os.system(f"start vswg.py")
        standby_mode()
      
    elif "close" in command:
        # Split the command to extract the program name
        parts = command.split(" ")
        if len(parts) > 1:
            program_name = parts[1]
            if program_name == "mycomputer":
                close_program(r"C:\Windows\explorer.exe")
            elif program_name == "paint":
                close_program(r"C:\Windows\System32\mspaint.exe")
            else:
                close_program(program_name)
        else:
            speak("Program ka naam nahi mila.")
    elif "exit" in command or "bye" in command:
        speak("Alwida! See you next time.")
        break  # Exit the loop and end the program
    elif "exhausted" in command or "tired" in command or "break" in command:
        if not continue_after_break():
            break

    elif "time" in command:
            # time = datetime.datetime.now().strftime("%H:%M:%S %p") # 24 hour format
            time = datetime.datetime.now().strftime("%I:%M:%S %p") # 12 hour format
            print(time)
            speak(time)

    elif "date" in command:
            date = datetime.datetime.now().strftime("%D")
            print(date)
            speak(date)
    elif "day" in command:
            day = datetime.datetime.now().strftime("%A")
            print(day)
            speak(day)

    elif "temperature" in command:
            q = command
            r = requests.get(f"https://www.google.com/search?q={q}")
            data = bs4.BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"the temperature outside is {temp}")
            speak(f"the temperature outside is {temp}")
            
            speak("do you want another place temperature")
            place = takecommand()
            if "yes" in place or  "temperature" in place or "ya" in place:
                speak("tell me the name of the place")
                next = takecommand()
                r = requests.get(f"https://www.google.com/search?q={next}")
                data = bs4.BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                print(f"the temperature outside is {temp}")
                speak(f"the temperature outside is {temp}")
            else:
                speak("no problem!")

    elif "play" in command: 
            command = command.replace("play ","")
            kit.playonyt(command)
            print(f"ok boss, playing {command}")
            speak(f"ok boss, playing {command}")

    elif "website" in command: 
        command = command.replace("website","")
        command = command.replace(" ","") 
        webbrowser.open(f"https://www.{command}.com")
        print(f"ok boss, opening {command}")
        speak(f"ok boss, opening {command}")
        
    elif "search" in command: 
        command = command.replace("search","") or command.replace("","")
        command = command.replace(" ","") 
        webbrowser.open(f"https://www.{command}.com")
        print(f"ok boss, opening {command}")
        speak(f"ok boss, opening {command}")
            
    elif "news of" in command: 
        command = command.replace("news of ","")
        new = GoogleNews.GoogleNews()
        print(f"getting news of {command}")
        speak(f"getting news of {command}")
        new.get_news(command)
        new.result()
        a = new.gettext()
        print(a[1:5])
        speak(a[1:5])
        
    elif "headlines" in command or "headline" in command: 
        new = GoogleNews.GoogleNews()
        print("getting fresh headlines")
        speak("getting fresh headlines")
        new.get_news("headlines")
        new.result()
        a = new.gettext()
        print(a[1:10])
        speak(a[1:10])
    elif "speed test" in command or "test speed" in command:
        speed = speedtest.Speedtest()
        print("checking")
        speak("checking")
        ul = speed.upload()
        ul = int(ul/800000)
        dl = speed.download()
        dl = int(dl/800000)
        print(f"your upload speed is {ul} mbp s and your download speed is {dl} mbp s")
        speak(f"your upload speed is {ul} mbp s and your download speed is {dl} mbp s")

    elif "standby mode" in command or "standby" in command:
        standby_mode()

    elif 'wikipedia' in command or "tell about" in command:
        speak('seraching Wikipedia...')
        command=command.replace("wikipedia","") 
        results =  wikipedia.summary(command,sentences=2)
        speak('According to wikipedia')
        print(results)
        speak(results)

    else:
        # speak(.get_responschre(command))
        # print(chr.get_response(command))  
        print(chatbot(command))
        speak(chatbot(command))      

    # Randomly choose a message instead of always asking "Anything else?"
    random_messages = [
        "Hope my assistance was helpful!","","","","","","",
        "Feel free to ask for more assistance.","","","","","","",
        "Is there anything else I can do for you?","","","","","","",
        "I hope you are enjoying our interaction.","","","","","","",
        "If you have any more questions, feel free to ask.""","","","","","",
    ]
    random_message = random.choice(random_messages)
    
    speak(random_message)

    
