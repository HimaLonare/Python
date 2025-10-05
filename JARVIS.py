import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open instagram" in c.lower():
      webbrowser.open("https://instagram.com") 

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True :
        r = sr.Recognizer()

        print("recognizing..")
        try:
          with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=3, phrase_time_limit=4)
          word = r.recognize_google(audio)
          if(word.lower() == "jarvis"):
               speak("Konichiiwa")
               with sr.Microphone() as source:
                  print("How Can I help You ?")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)

                  processCommand(command)
        except sr.UnknownValueError:
            print("Jarvis could not understand audio")
        except sr.WaitTimeoutError:
            continue