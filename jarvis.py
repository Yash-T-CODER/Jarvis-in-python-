import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import pywhatkit as kit
import webbrowser
import os

class Jarvis:
    def __init__(self):
        self.speech = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.pause_threshold = 3
        self.energy_threshold = 400

    def speak(self, text):
        print("Jarvis:", text)
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.speech.pause_threshold = self.pause_threshold
                self.speech.energy_threshold = self.energy_threshold
                self.speech.adjust_for_ambient_noise(source)
                audio = self.speech.listen(source, timeout=20)
                print("Recognizing what you said...")
                command = self.speech.recognize_google(audio)
                print(f"You said:", command)
                return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I could not understand what you said. Please say that again.")
            return ""
        except sr.RequestError:
            self.speak("Sorry, I'm having trouble connecting to the service. Please try again later.")
            return ""
        except sr.WaitTimeoutError:
            time.sleep(10)
            self.speak("You were silent. Do you want to quit the program?")
            return ""

    def open_website(self, command):
        try:
            site = command.replace("open", "").strip().replace(" ", "")
            url = f"https://www.{site}.com"
            webbrowser.open(url)
            self.speak(f"Opening {site} for you, sir.")
        except:
            self.speak("Sorry, I couldn't open that website.")

    def search_google_fallback(self, command):
        query = command.replace("search", "").replace("open", "").strip()
        self.speak(f"Searching {query} on Google...")
        kit.search(query)

    def wish_me(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good morning, sir!")
        elif 12 <= hour < 18:
            self.speak("Good afternoon, sir!")
        else:
            self.speak("Good evening, sir!")
        self.speak("I am your voice assistant, Jarvis. How can I help you today, sir?")

    def run(self):
        self.wish_me()
        time.sleep(1)
        while True:
            command = self.listen()

            if "weather" in command:
                self.speak("Please say your city name.")
                city = self.listen()
                if city:
                    url = f"https://www.google.com/search?q=weather+in+{city}"
                    self.speak(f"Showing weather for {city}")
                    webbrowser.open(url)

            elif "news" in command:
                self.speak("Opening latest news headlines")
                webbrowser.open("https://news.google.com")

            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                self.speak(f"The time is {current_time}")

            elif "date" in command:
                date = datetime.datetime.now().strftime("%B %d, %Y")
                self.speak(f"Today is {date}")

            elif "what is" in command or "who is" in command or "tell me about" in command:
                try:
                    topic = command.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
                    info = wikipedia.summary(topic, sentences=2)
                    self.speak("According to Wikipedia")
                    time.sleep(0.5)
                    print(f"                              {info}")
                    self.engine.say(info)
                    self.engine.runAndWait()
                except wikipedia.exceptions.DisambiguationError:
                    self.speak(f"The topic '{topic}' has multiple meanings on Wikipedia.")
                    self.speak("So, I am searching it on Google for more accurate information.")
                except wikipedia.exceptions.PageError:
                    self.speak(f"Searching for {topic} on Google...")
                    kit.search(topic)

            elif "open" in command:
                try:
                    self.open_website(command)
                except:
                    self.search_google_fallback(command)

            elif "play music" in command:
                self.speak("Playing song, sir.")
                music = "D:\\Academic\\python\\python projects\\jarvis voice assistant\\repo's\\Jarvis-in-python-\\Naina - Crew 320 Kbps (mp3cut.net).mp3"
                os.startfile(music)

            elif "calculate" in command:
                try:
                    command = command.replace("calculate", "").strip()
                    result = eval(command)
                    self.speak(f"The answer is {result}")
                except:
                    self.speak("Sorry, I couldn't calculate that.")

            elif "play" in command:
                song = command.replace("play", "").strip()
                self.speak(f"Playing {song} on YouTube")
                kit.playonyt(song)

            elif "exit" in command or "stop" in command:
                self.speak("Thank you for using me, sir. Have a nice day!")
                break

            else:
                print("")

if __name__ == "__main__":
    assistant = Jarvis()
    assistant.run()


