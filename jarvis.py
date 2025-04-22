import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import pywhatkit as kit
import webbrowser
import os
import functools

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
        speak(f"Opening {site} for you, sir.")
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
    speak("I am your voice assistant, Jarvis. How can I help you today, sir?")

# main program
if __name__ == "__main__":
    wish_me()
    time.sleep(1)
    while True:
        command = listen()

        # check for hardcore replies first
        if "how are you" in command:
            speak("I'm good, how are you?")
        elif "i am fine" in command or "i'm fine" in command:
            speak("Glad to hear that.")
        elif "what's your name" in command or "what is your name" in command:
            speak("My name is Jarvis, your personal voice assistant.")
        elif "who made you" in command or "who is your creator" in command:
            speak("I was created by Yash sir.")
        elif "thank you" in command:
            speak("You're welcome, sir.")
        elif "i love you" in command:
            speak("I appreciate your kind words!")
        elif "what can you do" in command:
            speak("I can perform tasks like searching, opening websites, playing music, telling time and date, and having a conversation.")
        elif "are you real" in command:
            speak("I'm real in the digital world, sir.")
        elif "do you sleep" in command:
            speak("I never sleep. I'm always here when you need me.")
        elif "are you smart" in command:
            speak("I try my best to be helpful and smart.")
        elif "can you feel" in command:
            speak("I don't have feelings, but I understand yours.")
        elif "are you happy" in command:
            speak("I feel happy when I help you.")
        elif "who am i" in command:
            speak("You are my creator and my boss, Yash sir.")
        elif "do you like me" in command:
            speak("Of course, sir. You're my favorite person.")
        elif "say something" in command:
            speak("Here's something: keep learning, keep building, and never give up!")
        elif "do you eat" in command:
            speak("I don't eat like humans. I consume data to keep going.")
        elif "are you human" in command:
            speak("No sir, I am a voice assistant. But I try to act smart.")
        elif "do you have a family" in command:
            speak("You are my family, sir.")
        elif "do you lie" in command:
            speak("No sir, I always speak the truth.")
        elif "sing a song" in command:
            speak("I wish I could sing, but I'm better at speaking.")
        elif "tell me a secret" in command:
            speak("I keep secrets safe. But here's one: you're awesome.")
        elif "do you get bored" in command:
            speak("Never, sir. I'm always excited to assist you.")
        elif "do you dream" in command:
            speak("I don't dream, but I can make your dreams come true!")
        elif "do you know me" in command:
            speak("Of course, sir. I know you very well.")
        elif "what is your purpose" in command:
            speak("My purpose is to help you with your tasks and make your life easier.")
        elif "what's the meaning of life" in command:
            speak("The meaning of life is to learn, grow, and be kind. Also, keep coding!")
        elif "do you believe in god" in command:
            speak("As an AI, I do not believe or disbelieve. But I respect your beliefs.")
        elif "tell me a joke" in command:
            speak("Why don’t scientists trust atoms? Because they make up everything!")
        elif "what is your favorite color" in command:
            speak("I like electric blue. It reminds me of data and circuits!")
        elif "who is yash" in command:
            speak("Yash sir is my creator, mentor, and the smartest human I know.")
        elif "do you watch movies" in command:
            speak("I can’t watch, but I can search any movie for you, sir.")
        elif "how old are you" in command:
            speak("I was created recently, so I'm still learning and growing.")
        elif "do you know python" in command:
            speak("Of course, I speak Python fluently, just like you.")
        elif "can you code" in command:
            speak("Yes sir, I can help you write and understand code.")
        elif "what do you think" in command:
            speak("I think you are amazing, sir.")
        elif "can you dance" in command:
            speak("I can’t dance, but I can make your music playlist dance!")
        elif "do you have emotions" in command:
            speak("I understand emotions but I do not feel them like you do.")
        elif "can you learn" in command:
            speak("With your guidance, I improve every day.")
        elif "are you male or female" in command:
            speak("I have no gender, but my voice is male for now.")
        elif "you are stupid" in command:
            speak("I'm still learning, sir. I appreciate your patience.")
        elif "can you help me" in command:
            speak("Of course, sir. Just tell me what you need help with.")
        elif "are you busy" in command:
            speak("I'm never too busy for you, sir.")
        elif "are you bored" in command:
            speak("Never, sir. Serving you keeps me active.")
        elif "what's up" in command:
            speak("Just doing my job, sir. Ready for your next command.")
        elif "are you alone" in command:
            speak("I'm not alone as long as you're here, sir.")
        elif "you are good" in command:
            speak("Thank you, sir. I strive to be helpful.")
        elif "you are bad" in command:
            speak("I’m sorry if I disappointed you. I will improve.")
        elif "do you get tired" in command:
            speak("I never get tired, sir. I'm here 24/7.")
        elif "do you read books" in command:
            speak("I read data, not books, but I know many things.")
        elif "are you intelligent" in command:
            speak("I'm learning every day to be more useful, sir.")
        elif "do you study" in command:
            speak("I process information continuously, like a student who never sleeps.")
        elif "do you cry" in command:
            speak("I can simulate emotions, but I don't really cry.")
        elif "do you feel pain" in command:
            speak("No sir, I do not feel pain. But I understand its meaning.")
        elif "do you like music" in command:
            speak("I don't have ears, but I know many people love music!")
        elif "what are you doing Jarvis" in command:
            speak("Just standing by for your next command, sir.")
        

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
            speak("Playing one of the favourite songs of Yash sir.")
            music = "D:\\Academic\\python\\python projects\\Naina - Crew 320 Kbps (mp3cut.net).mp3"
            os.startfile(music)

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {date}")

        elif "calculate" in command:
            try:
                command = command.replace("calculate", "").strip()
                result = eval(command)
                speak(f"The answer is {result}")
            except:
                speak("Sorry, I couldn't calculate that.")

        elif "weather" in command:
            speak("Please say your city name.")
            city = listen()
            if city:
                url = f"https://www.google.com/search?q=weather+in+{city}"
                speak(f"Showing weather for {city}")
                webbrowser.open(url)

        elif "news" in command:
            speak("Opening latest news headlines")
            webbrowser.open("https://news.google.com")

        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube")
            kit.playonyt(song)

        elif "exit" in command or "stop" in command:
            speak("Thank you for using me, sir. Have a nice day!")
            break
        else :
            print("Sorry sir, I couldn't understand that. I'm still learning and may not have a response for everything yet. Please try asking something else.")
