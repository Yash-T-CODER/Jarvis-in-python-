import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import pywhatkit as kit
import webbrowser
import os

speech = sr.Recognizer()
robot = pyttsx3.init()

# speak function
def speak(text):
    print("Jarvis:", text)
    robot.say(text)
    robot.runAndWait()

# function to listen from microphone
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            speech.pause_threshold = 3
            speech.energy_threshold = 400
            speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source, timeout=20)
            print("Recognizing what you said...")
            command = speech.recognize_google(audio)
            print(f"You said:", command)
            return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand what you said. Please say that again.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service. Please try again later.")
        return ""
    except sr.WaitTimeoutError:
        time.sleep(10)
        speak("You were silent. Do you want to quit the program?")
        return ""

# open a website
def open_website(command):
    try:
        site = command.replace("open", "").strip().replace(" ", "")
        url = f"https://www.{site}.com"
        webbrowser.open(url)
        speak(f"Opening {site} for you,sir.")
    except:
        speak("Sorry, I couldn't open that website.")

# fallback search on Google
def search_google_fallback(command):
    query = command.replace("search", "").replace("open", "").strip()
    speak(f"Searching {query} on Google...")
    kit.search(query)

# greet the user
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning,sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon,sir!")
    else:
        speak("Good evening,sir!")
    speak("I am your voice assistant,Jarvis. How can I help you today,sir?")

# main program
if __name__ == "__main__":
    wish_me()
    time.sleep(1)
    while True:
        command = listen()

        if "weather" in command:
            speak("Please say your city name.")
            city = listen()
            if city:
                url = f"https://www.google.com/search?q=weather+in+{city}"
                speak(f"Showing weather for {city}")
                webbrowser.open(url)

        elif "news" in command:
            speak("Opening latest news headlines")
            webbrowser.open("https://news.google.com")


        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {date}")

        elif "what is" in command or "who is" in command or "tell me about" in command:
            try:
                topic = command.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
                info = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia")
                time.sleep(0.5)
                print(f"                              {info}")
                robot.say(info)
                robot.runAndWait()
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"The topic '{topic}' has multiple meanings on Wikipedia.")
                speak("So, I am searching it on Google for more accurate information.")
            except wikipedia.exceptions.PageError:
                speak(f"Searching for {topic} on Google...")
                kit.search(topic)

        elif "open" in command:
            try:
                open_website(command)
            except:
                search_google_fallback(command)

        elif "play music" in command:
            speak("Playing song,sir.")
            music = "D:\\Academic\\python\\python projects\\jarvis voice assistant\\repo's\\Jarvis-in-python-\\Naina - Crew 320 Kbps (mp3cut.net).mp3"
            os.startfile(music)

        elif "calculate" in command:
            try:
                command = command.replace("calculate", "").strip()
                result = eval(command)
                speak(f"The answer is {result}")
            except:
                speak("Sorry, I couldn't calculate that.")

        
        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube")
            kit.playonyt(song)

        elif "exit" in command or "stop" in command:
            speak("Thank you for using me, sir. Have a nice day!")
            break
        else :
            print("")
