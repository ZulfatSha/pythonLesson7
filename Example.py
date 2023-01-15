def generate_mp3():
    mp3fileName = ''

    import pyttsx3 as tts

    engine = tts.init()

    engine.save_to_file(mp3fileName)

    engine.runAndWait()

    return mp3fileName

import speech_recognition as sr
engine = sr.Recognizer()

mp3fileName = generate_mp3()
with sr.AudioFile(mp3fileName) as source:
    print('Файл анализируется...')
    audio = engine.record(source)

try:
    text = engine.recognize_google(audio)
    print(f'Text: {text}')
    txtFile = open('textFromMP3.txt', 'a')
    txtFile.writelines(text)
except:
    print('Warning...')

