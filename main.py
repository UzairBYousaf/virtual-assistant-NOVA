import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
from selenium_webdriver import infow
from YT_audio import music
from News import *
import randfacts
import speech_recognition
from jokes import joke
from weather import *
import datetime
from send_email import sendEmail
import smtplib
from ss import *
from email.message import EmailMessage
import pyautogui
import webbrowser
from time import sleep
import wikipedia
import os
import psutil

engine = p.init()
rate = engine.getProperty('rate')
#print(rate)
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

def sendEmail(reciever, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, epwd)
    email = EmailMessage()
    email['From'] = senderEmail
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    webbrowser.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text' + Message)
    sleep(10)
    pyautogui.press('Enter')

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered cases : {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = datetime.datetime.now()
    name_img = 'D:\\PY-NOVA\\screenshots\\ss.png'
    img = pyautogui.screenshot(name_img)
    img.show

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at " + battery.percent)

today_date = datetime.datetime.now()
r = sr.Recognizer()

print("Hello Sir, good " + wishme() + ", I am your Voice Assistant Nova")
speak("Hello Sir, good " + wishme() + ", I am your Voice Assistant Nova")
print("Today is " + today_date.strftime("%d") +" of "+ today_date.strftime('%B') + ", And its currently " +(today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("Today is " + today_date.strftime("%d") +" of "+ today_date.strftime('%B') + ", And its currently " +(today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
print("Temperature in rawalpindi is " + str(temp()) + " degree celsius" + " and with " + str(des()))
speak("Temperature in rawalpindi is " + str(temp()) + " degree celsius" + " and with " + str(des()))
print("how are you?")
speak("how are you?")



with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    print("That is nice to hear, I am also having a good day sir")
    speak("That is nice to hear, I am also having a good day sir")


print("What can I do for you?")
speak("What can I do for you?")

while True:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)

    if "information" in text2:
        speak("You need information related to which topic?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
            print("Fetching information for "+infor)
        speak("searching {} on Wikipedia".format(infor))
        result = wikipedia.summary(infor, sentences = 1)
        print("According to Wikipedia, " + result)
        speak("According to Wikipedia, " + result)
        assist = infow()
        assist.get_info(infor)


    elif "video" in text2:
        speak("You want me to play what video or music?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
            print("Playing {} on Youtube".format(vid))
        speak("searching {} on Youtube".format(vid))
        assist = music()
        assist.play(vid)


    elif "news" in text2:
        speak("Sure sir, Now playing some of the top news")
        print("Sure sir, Now playing some of the top news")
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])


    elif "fact" in text2:
        speak("Sure sir")
        x = randfacts.getFact()
        print(x)
        speak("Did you know that, " + x)


    elif "joke" in text2:
        speak("sure sir, get ready for some chuckles")
        print("sure sir, get ready for some chuckles")
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])


    elif "email" in text2:
        email_list ={
            'user' : 'ranaluqman642@gmail.com'
        }
        try:
            print('To whom you want to send the email?')
            speak('To whom you want to send the email?')
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                name = r.recognize_google(audio)
            reciever = email_list[name]
            print(name)
            print('what is the subject of the mail?')
            speak('what is the subject of the mail?')
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                subject = r.recognize_google(audio)
            print(subject)
            print("What should I say?")
            speak("What should I say?")

            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                content = r.recognize_google(audio)
            print(content)
            print("Sending email")
            speak("Sending email")
            sendEmail(reciever,subject,content)
            print("Email sent")
            speak("Email sent")
        except Exception as e:
            print("Unable to send email")
            speak("Unable to send email")


    elif 'message' in text2:
        user_name = {
            'user' : '+923065945093'
        }
        try:
            print("To whom should I send a message?")
            speak("To whom should I send a message?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                towhom = r.recognize_google(audio)
            print(towhom)
            ToWhom = user_name[towhom]
            print("What should be the message?")
            speak("What should be the message?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("listening...")
                audio = r.listen(source)
                whatsmessage = r.recognize_google(audio)
            print(whatsmessage)
            print("Sending message on WhatsApp")
            speak("Sending message on WhatsApp")
            sendwhatsmsg(ToWhom,whatsmessage)
            print("Message sent successfully to " + towhom + " on WhatsApp!")
            speak("Message sent successfully to " + towhom + " on WhatsApp!")
        except Exception as e:
            print("Unable to send message!")
            speak("Unable to send message!")


    elif "search" in text2:
        print("What should I search for")
        speak("What should I search for?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio)
        print(query)
        print("Searching for {} on Google".format(query))
        speak("Searching for {} on Google".format(query))
        webbrowser.open('https://www.google.com/search?q='+query)


    elif "covid" in text2:
        print("Retrieving covid 19 data")
        speak("Retrieving covid 19 data")
        covid()


    elif "code" in text2:
        print("Opening Microsoft Visual Studio Code")
        speak("Opening Microsoft Visual Studio Code")
        codepath = 'C:\\Users\\Uzair Bin Yousaf\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codepath)


    elif 'open' in text2:
        print("Sure sir")
        speak("Sure sir")
        print("Opening {}".format(text2.replace('open','')))
        speak("Opening {}".format(text2.replace('open', '')))
        os.system('explorer C://{}'.format(text2.replace('open','')))


    elif 'screenshot' in text2:
        print("Capturing screen")
        speak("Capturing screen")
        screenshot()
        print("Screen captured")
        speak("Screen captured")


    elif 'remember that' in text2:
        speak('what should i remember?')
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            data = r.recognize_google(audio)
        speak("you said me to remember that " + data)
        remember = open('data.txt', 'w')
        remember.write(data)
        remember.close()

    elif 'do you know anything' in text2:
        remember = open('data.txt','r')
        speak('you told me to remember that ' + remember.read())

    elif 'CPU' in text2:
        print("Fetching CPU Usage")
        speak("Fetching CPU Usage")
        usage = str(psutil.cpu_percent())
        print("CPU usage is at " + usage + " percent.")
        speak("CPU usage is at " + usage + " percent.")


    elif 'battery' in text2:
        print("Fetching battery percentage")
        battery = psutil.sensors_battery()
        print("Battery is at " + str(battery.percent) + ' percentage')
        speak("Battery is at " + str(battery.percent) + 'percentage')

    print("What else can I do for you sir?")
    speak("What else can I do for you sir?")