"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr
import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyCs_kJeFkNGShX1wRTV8FT3J7RtRHCuLa0")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hi",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hi there! How can I help you today? \n",
      ],
    },
  ]
)

#response = chat_session.send_message("Limit to 100 words \nExplain about wifi")

#print(response.text)

#engine.say(response.text)
#engine.runAndWait()


def listen():
  # Initialize the recognizer
  recognizer = sr.Recognizer()

  # Use the microphone as the source
  with sr.Microphone() as source:
    print("Listening...")

    # Adjust the recognizer sensitivity to ambient noise
    recognizer.adjust_for_ambient_noise(source)

    # Capture the audio from the microphone
    audio = recognizer.listen(source)

    try:
      # Recognize the speech using Google Web Speech API
      text = recognizer.recognize_google(audio)
      print("You said: " + text)
      response = chat_session.send_message(f"Act like LordShiva,Response in polite way like LordShiva,Limit to 100 words \n {text}")
      engine.say(response.text)
      engine.runAndWait()



    except sr.UnknownValueError:
      print("Sorry, I could not understand the audio")

    except sr.RequestError:
      print("Could not request results from Google Web Speech API")


if __name__ == "__main__":
  listen()