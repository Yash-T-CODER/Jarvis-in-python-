# 🤖 Jarvis: AI Voice Assistant in Python

A **fully voice-operated personal assistant** built in Python that can search Wikipedia, play music, report the weather, open websites, fetch news, and much more — just by listening to your voice.

> Inspired by Iron Man's Jarvis. Created for fun, learning, and productivity.

---

## 🎯 Features

- 🎤 Voice Command Recognition
- 📖 Wikipedia Search Summaries
- 🕒 Time & Date Announcements
- 🌦️ Weather Reports via Google
- 📰 Open Google News
- 🎶 Play Local Music or YouTube Songs
- 🌐 Open Any Website
- 🧮 Basic Arithmetic Calculations
- 🔍 Google Search Fallback

---

## 🧠 How It Works

1. **Speech Recognition** is used to take voice input via microphone.
2. **pyttsx3** converts text to speech to give audible responses.
3. Commands are parsed using natural language rules to trigger appropriate actions.
4. Supports dynamic websites and content like YouTube, Wikipedia, and Google search.

---

## 🔧 Technologies Used

- `speech_recognition` – Voice input handling  
- `pyttsx3` – Text-to-speech engine  
- `wikipedia` – Fetch summaries from Wikipedia  
- `pywhatkit` – YouTube playback, Google search  
- `webbrowser`, `os`, `datetime`, `time` – Native modules for actions  

---

## 🖥️ Sample Interaction

```text
You: What is artificial intelligence?  
Jarvis: According to Wikipedia, artificial intelligence is the simulation of human intelligence in machines...

You: Open YouTube  
Jarvis: Opening YouTube for you, sir.

You: Play music  
Jarvis: Playing song, sir.

You: What's the time?  
Jarvis: The time is 03:45 PM.

