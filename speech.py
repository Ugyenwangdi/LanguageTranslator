import googletrans  # In order to use google trans library
from googletrans import Translator

# from gtts import gTTS
# import os
import pyttsx3  # to speak the text 
import speech_recognition as sr
recognizer = sr.Recognizer()

engine = pyttsx3.init()  # Python text to speech initialize

# # Check the voices
# for voice in engine.getProperty('voices'):
#     print(voice)

voices = engine.getProperty('voices')  # Get all the voices
engine.setProperty('voice', voices[1].id)  # set it to second voice

# Store all the supported languages in a variable
supported_langs = googletrans.LANGUAGES   # This will be a python dictionary
t = Translator()


# with sr.AudioFile('audio.mp3') as source:
#     audio_data = recognizer.record(source)
#     speech = recognizer.recognize_google(audio_data, language='ja')

# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_speech():
    try:
        with sr.Microphone() as source:
            speak('Hello. Please Say something ')
            print("Speak now..")    
            engine.runAndWait()
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice)
            print(f'Recognised as: {text}')
            translated = t.translate(text)
            print(f'Translated text: {translated.text}')

            
            speak('spoken in english as: ')
            speak(translated.text)

            # speak the translated text in english
            # tts = gTTS(translated.text, lang='en')
            # tts.save("good.mp3")   # save as good.mp3
            # os.system("start good.mp3")  # play the recorded voice

            # # write audio to a WAV file
            # with open("microphone-results.wav", "wb") as f:
            #     f.write(voice.get_wav_data())
            

    except:
        pass


def get_supported_langs():
    # Print all the languages in 
    print('Supported languages: ')
    speak('This are list of all the supported languages: ')
    for key, value in supported_langs.items():
        # speak(value)
        print(key, ':', value)

# Get the source language
def get_source():
    speak('Enter the source language that you want to translate')
    source_lang = input('Source language: ')

    # is source_lang in lanuguage keys
    if source_lang in supported_langs.keys():
        return source_lang

    # Check if it is present in language values
    for key, value in supported_langs.items():
        if source_lang == value:   # Check if the value is in 
            return key
            
    else:
        return ''

# Get destination language
def get_dest():
    speak('Enter the target language you want to translate to')
    dest_lang = input('Translate to: ')    

    # if dest_lang in language key
    if dest_lang in supported_langs.keys():
        return dest_lang

    # Check if it is present in language values
    for key, value in supported_langs.items():
        if dest_lang == value:   # Check if the value is in 
            return key

    else:
        return ''

def translate():
    get_supported_langs()
    print('Choose language from the supported languages')
    speak('Choose the language from the supported languages')
    source_lang = get_source()
    # print(source_lang)
    
    dest_lang = get_dest()
    # print(dest_lang)

    speak('Enter your text')
    text = input("Enter your Text: ")
    
    print("Text to be translated: "+ text)
    speak(f'Entered text: {text}')

    # Let's print the language of input text
    input_text = t.translate(text)
    s = input_text.src
    print('Entered text is in:', s) 
    speak(f'Entered text is in: {supported_langs[s]}')

    # We can obtain the attributes with following
    # print(result.src)
    # print(result.dest)
    # print(result.origin)
    # print(result.text)
    # print(result.pronunciation)


    # The get_source() or get_dest() returns null means inputs are invalid which means the language is unsupported
    if source_lang == '' or dest_lang == '':
        print("Invalid input...")
        speak('Invalid input')
        pass

    try:
        if source_lang and dest_lang:  
            # Using translate() method which requires
            # three arguments, 1st the sentence which needs to be translated 
            # 2nd source language
            # and 3rd to which we need to translate in
            result = t.translate(text, src=source_lang, dest=dest_lang)   # Translate the text 

            # Ensure the input to be entered using the language specified
            if source_lang == s:
                print(f'Translated text to {supported_langs[dest_lang]}: {result.text}')
                speak(f'Translated to {supported_langs[dest_lang]}')
                # speak(result.text)

                print(f"Pronunciation in {supported_langs[dest_lang]}: {result.pronunciation}")
                speak(f'Pronounced in {supported_langs[dest_lang]} as {result.pronunciation}')

            else:
                print('Enter in ', supported_langs[source_lang])
                speak(f'Could not translate. Please enter in: {supported_langs[source_lang]}')

    except:
        print("Unable to understand the input...")
        speak(f'Unable to understand the input...')

if __name__=='__main__':
    get_speech()
    translate()  # Run it continuously
    while True:
        speak(f'Do you want to continue? enter y for yes or n for no ')
        q = input('Do you want to continue? (y/n): ')
        if q == 'n':
            break
        else:
            translate()
        