import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    standby_count = 0  # Counter for standby mode
    standby_threshold = 3  # Number of times to repeat "I didn't understand" before standby
    
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 0.5
            audio = recognizer.listen(source,phrase_time_limit=2)

            try:
                print("Recognizing...")
                command = recognizer.recognize_google(audio, language='en-in')
                print(f"You said: {command}\n")
                return command.lower()  # Convert the command to lowercase for case-insensitive comparison
            except sr.UnknownValueError:
                standby_count += 1
                if standby_count >= standby_threshold:
                    speak("I didn't understand. Standby mode activated.")
                    return "standby"
                else:
                    speak("Sorry, I didn't understand. Please repeat.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    speak("Welcome to Snake Water Gun  Game! Say 'start' to begin or 'exit' to quit.")
    print("Welcome to Snake.Water.Gun. Game! Say 'start' to begin or 'exit' to quit.")
    while True:
        command = take_command()

        if "start" in command:
            print("""    # Welcome to Snake.Water.Gun #
            'S' for Snake
            'W' for Water
            'G' for Gun
            Let's play""")
            speak("Let's play Snake.Water.Gun- game. Say 'S' or Snake, 'W' or Water,'G' or Gun.")
            

            speak("Enter Your Player Name: ")
            print("Enter Your Player Name: ")
            user = take_command()
            user_points = 0
            computer_points = 0
            speak("Enter the number of points you want to play: ")
            match_points = int(input("Enter the number of points you want to play: "))

            while user_points != match_points and computer_points != match_points:
                print("Play ")
                speak("Play")
                options = ["snake", "water", "gun"]
                computer_choice = random.choice(options)
                speak("Say 'S' or Snake, 'W' or Water, or 'G' or Gun.")
                print("Say 'S' or Snake, 'W' or Water, or 'G' or Gun.")
                player_choice = take_command().lower()
                if player_choice.lower() in options:
                    if computer_choice == player_choice.lower():
                        print("It's a draw! Continue playing.")
                        speak("It's a draw! Continue playing.")
                    elif (computer_choice == "snake" and player_choice.lower() == "w" or "water") or \
                            (computer_choice == "water" and player_choice.lower() == "g" or"gun") or \
                            (computer_choice == "gun" and player_choice.lower() == "s" or "snake"):
                        computer_points += 1
                        print(f"Computer gets 1 point. Computer Points: {computer_points}")
                        speak(f"Computer gets 1 point. Computer Points: {computer_points}")
                    else:
                        user_points += 1
                        print(f"You get 1 point. Your Points: {user_points}")
                else:
                    print("Invalid choice. Say 'S' for Snake, 'W' for Water, or 'G' for Gun.")
                    speak("Invalid choice. Say 'S' for Snake, 'W' for Water, or 'G' for Gun.")

            if computer_points == match_points:
                speak(f"Oops, {user}! You lose to the computer by {computer_points - user_points} points. Better luck next time.")
                print(f"Oops, {user}! You lose to the computer by {computer_points - user_points} points. Better luck next time.")
            elif user_points == match_points:
                speak(f"Congratulations, {user}! You win against the computer by {user_points - computer_points} points.")
                print(f"Congratulations, {user}! You win against the computer by {user_points - computer_points} points.")

            speak("Thanks for playing. Hope to see you again. Goodbye!")
            print("Thanks for playing. Hope to see you again. Goodbye!")

        elif  "exit" in command:
            speak("Exiting the game. Goodbye!")
            print("Exiting the game. Goodbye!")
            break

        elif "standby" in command:
            # Standby mode activated due to repeated unknown commands
            speak("Standby mode activated. Say 'start' to play or 'exit' to quit.")
            print("Standby mode activated. Say 'start' to play or 'exit' to quit.")

        else:
            speak("Invalid command. Say 'start' to play or 'exit' to quit.")
            print("Invalid command. Say 'start' to play or 'exit' to quit.")
