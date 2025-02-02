import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from playsound import playsound
import os
from flask import Flask, render_template, request, jsonify

app = Flask(name)

# Function to handle voice-to-text translation
def voice_to_text_translator():
    translator = Translator()
    target_language = get_language_choice()
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Say something...")
            audio = recognizer.listen(source, timeout=10)
        
        input_text = recognizer.recognize_google(audio)
        print(f"Recognized: {input_text}")
        translated_text = translator.translate(input_text, dest=target_language).text
        print(f"Translated: {translated_text}")
        return translated_text
    except Exception as e:
        print(f"Error: {e}")
        return "Error during voice recognition."

# Function to handle text-to-voice translation
def text_to_voice_translator():
    translator = Translator()
    target_language = get_language_choice()
    while True:
        text = input("Enter text to translate ('stop' to exit): ").strip()
        if text.lower() == "stop":
            break
        translated_text = translator.translate(text, dest=target_language).text
        print(f"Translated: {translated_text}")
        generate_speech(translated_text, target_language)

# Function to handle text-to-text translation
def text_to_text_translator():
    translator = Translator()
    target_language = get_language_choice()
    while True:
        text = input("Enter text ('change' to switch language, 'stop' to exit): ").strip()
        if text.lower() == "stop":
            break
        if text.lower() == "change":
            target_language = get_language_choice()
        else:
            translated_text = translator.translate(text, dest=target_language).text
            print(f"Translated: {translated_text}")
            return translated_text

# Function to handle voice-to-voice translation
def voice_to_voice_translator():
    translator = Translator()
    target_language = get_language_choice()
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Say something...")
            audio = recognizer.listen(source, timeout=10)
        
        input_text = recognizer.recognize_google(audio)
        print(f"Recognized: {input_text}")
        translated_text = translator.translate(input_text, dest=target_language).text
        print(f"Translated: {translated_text}")
        generate_speech(translated_text, target_language)
    except Exception as e:
        print(f"Error: {e}")

def generate_speech(text, language):
    tts = gTTS(text=text, lang=language)
    audio_file = "output.mp3"
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)

# Helper function to select language
def get_language_choice():
    print("Select language code (default is English): ")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")
    lang_code = input("Enter language code: ").strip().lower()
    return lang_code if lang_code in LANGUAGES else 'en'

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate_text', methods=['POST'])
def translate_text():
    text = request.form['text']
    target_language = request.form['target_language']
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return jsonify({'translated': translation.text})

@app.route('/generate_speech', methods=['POST'])
def generate_speech_route():
    text = request.form['text']
    language = request.form['language']
    generate_speech(text, language)
    return jsonify({'message': 'Speech generated'})

@app.route('/translate_voice', methods=['POST'])
def translate_voice_route():
    target_language = request.form['target_language']
    translated_text = voice_to_text_translator()
    return jsonify({'translated': translated_text})

if name == 'main':
    app.run(debug=True)import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from playsound import playsound
import os
from flask import Flask, render_template, request, jsonify

app = Flask(name)

# Function to handle voice-to-text translation
def voice_to_text_translator():
    translator = Translator()
    target_language = get_language_choice()
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Say something...")
            audio = recognizer.listen(source, timeout=10)
        
        input_text = recognizer.recognize_google(audio)
        print(f"Recognized: {input_text}")
        translated_text = translator.translate(input_text, dest=target_language).text
        print(f"Translated: {translated_text}")
        return translated_text
    except Exception as e:
        print(f"Error: {e}")
        return "Error during voice recognition."

# Function to handle text-to-voice translation
def text_to_voice_translator():
    translator = Translator()
    target_language = get_language_choice()
    while True:
        text = input("Enter text to translate ('stop' to exit): ").strip()
        if text.lower() == "stop":
            break
        translated_text = translator.translate(text, dest=target_language).text
        print(f"Translated: {translated_text}")
        generate_speech(translated_text, target_language)

# Function to handle text-to-text translation
def text_to_text_translator():
    translator = Translator()
    target_language = get_language_choice()
    while True:
        text = input("Enter text ('change' to switch language, 'stop' to exit): ").strip()
        if text.lower() == "stop":
            break
        if text.lower() == "change":
            target_language = get_language_choice()
        else:
            translated_text = translator.translate(text, dest=target_language).text
            print(f"Translated: {translated_text}")
            return translated_text

# Function to handle voice-to-voice translation
def voice_to_voice_translator():
    translator = Translator()
    target_language = get_language_choice()
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Say something...")
            audio = recognizer.listen(source, timeout=10)
        
        input_text = recognizer.recognize_google(audio)
        print(f"Recognized: {input_text}")
        translated_text = translator.translate(input_text, dest=target_language).text
        print(f"Translated: {translated_text}")
        generate_speech(translated_text, target_language)
    except Exception as e:
        print(f"Error: {e}")

def generate_speech(text, language):
    tts = gTTS(text=text, lang=language)
    audio_file = "output.mp3"
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)

# Helper function to select language
def get_language_choice():
    print("Select language code (default is English): ")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")
    lang_code = input("Enter language code: ").strip().lower()
    return lang_code if lang_code in LANGUAGES else 'en'

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate_text', methods=['POST'])
def translate_text():
    text = request.form['text']
    target_language = request.form['target_language']
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return jsonify({'translated': translation.text})

@app.route('/generate_speech', methods=['POST'])
def generate_speech_route():
    text = request.form['text']
    language = request.form['language']
    generate_speech(text, language)
    return jsonify({'message': 'Speech generated'})

@app.route('/translate_voice', methods=['POST'])
def translate_voice_route():
    target_language = request.form['target_language']
    translated_text = voice_to_text_translator()
    return jsonify({'translated': translated_text})

if name == 'main':
    app.run(debug=True)