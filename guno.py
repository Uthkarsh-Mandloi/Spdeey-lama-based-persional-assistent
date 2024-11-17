import random
import pyttsx3

engine = pyttsx3.init('sapi5')
vocies = engine.getProperty('voices')
print(vocies[0].id)
engine.setProperty('voices',vocies[0].id)

def speak(audio):
    engine.setProperty("rate", 200)
    print("")
    engine.say(audio)
    print("")
    engine.runAndWait()

randNumber = random.randint(1, 100)
userGuess = None
guesses = 0
speak("enter your name")
name =input("enter your name :")
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
        speak("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
            speak("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
            speak("You guessed it wrong! Enter a larger number")

print(f"{name}You guessed the number in {guesses} guesses")
speak(f"{name}You guessed the number in {guesses} guesses")
with open("gunohiscore.txt", "r") as f:
    gunohiscore = int(f.read())

if(guesses<gunohiscore):
    print("{name}You have just broken the high score!")
    speak("{name}You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
