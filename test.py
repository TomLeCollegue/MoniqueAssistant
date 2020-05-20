from gtts import gTTS 
import playsound
import speech_recognition as sr
import os 
import random
import webbrowser as wb 

r = sr.Recognizer()
language = "fr"
call_assistant = "Monique"


def record_audio():
    with sr.Microphone() as source:
        print('Ecoute ...')
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="fr-FR")
        except sr.RequestError:
            print('Deso pas dispo')
        except sr.UnknownValueError:
            print('deso pas compris')
        return voice_data


def google_speak(audio_string):
    tts = gTTS(text=audio_string, lang = language)
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(response):
    if 'météo' in response:
        url = 'https://www.google.com/search?q=meteo'
        wb.get().open(url)
        google_speak('Voila la météo')
    if 'ferme ta gueule' in response:
        google_speak('Désolé monsieur je me tais promis')
    if 'non rien' in response:
        google_speak('D\'accord')
    if 'merci' in response: 
        google_speak('avec plaisir!')


while 1:
    call = record_audio()
    if call_assistant in call:
        playsound.playsound('trigger_monique.mp3')
        response = record_audio()
        print(response)
        respond(response)
    if 'au revoir' in call:
        playsound.playsound('jingle_exit.mp3')
        exit()
    

