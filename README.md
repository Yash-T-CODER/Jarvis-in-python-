# 🤖 Jarvis: AI Voice Assistant in Python

A **fully voice-operated personal assistant** built in Python that can perform a wide range of tasks, such as searching Wikipedia, playing music, reporting the weather, opening websites, fetching news, performing calculations, and much more — all through natural voice commands.

> **Inspired by Iron Man's Jarvis**, this project showcases my skills in Python programming, voice recognition, text-to-speech synthesis, and integrating multiple APIs to create a practical, fun, and interactive assistant.

---

## 🎯 Key Features

* 🎤 **Voice Command Recognition** – Seamless interaction through speech using Python's `speech_recognition` library.
* 📖 **Wikipedia Search Summaries** – Retrieve concise information from Wikipedia using voice commands.
* 🕒 **Time & Date Announcements** – Get the current time and date announced verbally.
* 🌦️ **Weather Reports** – Ask for the weather in any city, and the assistant will fetch live data from Google.
* 📰 **News Headlines** – Stay up-to-date with the latest news via voice command.
* 🎶 **Play Music** – Play local music or stream songs from YouTube directly through voice commands.
* 🌐 **Open Websites** – Access any website instantly by simply saying its name.
* 🧮 **Basic Arithmetic Calculations** – Perform simple calculations directly by voice.
* 🔍 **Google Search Fallback** – Search Google when the assistant doesn't understand the command or requires more details.

---

## 🧠 How It Works

1. **Speech Recognition**: The assistant listens to your voice input through the microphone and converts it into text using the `speech_recognition` library.
2. **Text-to-Speech (TTS)**: It replies verbally using the `pyttsx3` library, providing an interactive experience.
3. **Command Parsing**: Voice commands are parsed using natural language rules to trigger corresponding actions (e.g., opening websites, playing music, fetching information).
4. **Web & Local Interaction**: The assistant uses `webbrowser` for online interactions (like opening websites or searching Google) and `os` to play local files (like music).

---

## 🔧 Technologies Used

* `speech_recognition` – For converting spoken commands into text.
* `pyttsx3` – Text-to-speech engine for vocal responses.
* `wikipedia` – Fetches summaries for queries related to people, places, and topics.
* `pywhatkit` – Performs Google searches, plays YouTube videos.
* `webbrowser` – Opens websites based on voice commands.
* `os` – Plays local music files.
* `datetime` – Provides current time and date.
* `time` – Manages time delays for smoother user interaction.

---

## 💡 Why This Project?

This project demonstrates:

- **End-to-End Voice Assistant**: Full-cycle development of a voice assistant that listens, processes, and responds to commands.
- **Practical Applications**: A blend of useful real-world features like weather updates, news, music, and more.
- **Hands-On Experience**: Working with speech recognition, text-to-speech, and interacting with APIs to build a multi-functional tool.
- **Problem Solving**: Overcoming challenges related to voice command accuracy, error handling, and seamless user interaction.

---

# 🖥️ Sample Interaction

```text
You: What is artificial intelligence?  
Jarvis: According to Wikipedia, artificial intelligence is the simulation of human intelligence in machines...

You: Open YouTube  
Jarvis: Opening YouTube for you, sir.

You: Play music  
Jarvis: Playing song, sir.

You: What's the time?  
Jarvis: The time is 03:45 PM.

You: Weather in Paris  
Jarvis: Showing weather for Paris.
````
---


## 🤝 Let's Connect!

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/yash-goyal-6a8a00343/) or check out my other projects on [GitHub](https://github.com/Yash-T-CODER).


