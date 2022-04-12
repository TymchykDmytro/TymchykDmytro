import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
#import pywhatkit
def talk(words):
    print(words)
    engine= pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk("Здраствуйте, мой повелитель")
def command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio= r.listen(source)
    try:
        spech=r.recognize_google(audio, language="ru-RU").lower()

    except sr.UnknownValueError:
        talk("Я не понимаю, что вы сказали ")
        talk("Повторите, пожалуйста, команду....")
        spech=command()
    return spech
def maker(spech):
    if 'открой курс' in spech:
        talk("Уже открываю...")
        url='https://www.coursera.org'
        webbrowser.open(url)
    elif 'открой дулинго' in spech:
        talk("Уже открываю...")
        url='https://www.duolingo.com/learn'
        webbrowser.open(url)
    elif 'открой работу' in spech:
        talk("Уже открываю...")
        url='https://www.upwork.com'
        webbrowser.open(url)
    elif 'открой справку' in spech:
        talk("Уже открываю...")
        url='https://docs.python.org/3/library/functions.html'
        webbrowser.open(url)
    elif 'открой учебник' in spech:
        talk("Уже открываю...")
        url='https://python-scripts.com/install-django'
        webbrowser.open(url)
    elif 'открой атом' in spech:
        talk("Уже открываю...")
        os.system('C:/Users/Администратор.ASPIRELIKEFIRE/AppData/Local/atom/atom.exe')

    #elif 'ютуб' in spech:
        #talk("Уже открываю...")
        #kit.plyonyt('Elon Mask')

    elif 'список команд' in spech:
        talk('Вот доступный список команд:')
        print('1.Открой учебник.')
        print('2.Открой курс')
        print('3.Открой справку')
        print('4.Открой работу')
        print('5.Открой Дулинго')
        print('6.Давай поговорим')
        print('7.Создатель')
        print('8.Открой атом')
        print('9.Стоп')
    elif 'давай поговорим' in spech:
        talk('Про что бы вы хотели поговорить?')
    elif 'как тебя зовут' in spech:
        talk('Меня зовут, Ланселот ')
    elif 'создатель' in spech:
        talk('Мой создатель и повелитель Тымчик  Дмитро')
    elif 'стоп' in spech:
        talk('Да,как прикажете,мой господин')
        sys.exit()
while True:
    maker(command())
input()
