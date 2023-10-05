import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Open the microphone and capture audio
with sr.Microphone() as source:
    print("Please start speaking...")
    audio = recognizer.listen(source)

try:
    # Use Google Web Speech API to recognize the speech
    text = recognizer.recognize_google(audio, language='en-US')
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print(f"Sorry, there was an error with the speech recognition service: {e}")