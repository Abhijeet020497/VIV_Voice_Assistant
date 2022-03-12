from tkinter import Message
from bs4 import BeautifulSoup
import pyttsx3 # text to speech
import datetime
import speech_recognition as sr #speech recognition
import smtplib
from secrets import senderemail, epwd, to 
from email.message import EmailMessage
import pyautogui
import webbrowser as web
from time import sleep 
import subprocess
import wikipedia
import pywhatkit
import requests

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice==1:
        engine.setProperty('voice',voices[0].id)
        speak('hello this is VIV')
    
    if voice==2:
        engine.setProperty('voice',voices[1].id)
        speak('hello this is VIV')
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak('Current time is ')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('Current date is ')
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back")
    greeting()
    time()
    date()
    speak("VIV online, how can i help you")

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommandCMD():
    query = input("how can i help you?")
    return query

def takeCommandMic():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again..,")
        return "None"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendWhatsAppmsg(phone_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text'+Message)
    sleep(10)
    pyautogui.press('enter')

def searchGoogle():
    speak('What should I search for?')
    search = takeCommandMic()
    web.open('https://google.co.in/search?q='+search)
    
 

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommandMic().lower()
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'exit' in query:
            exit()
        
        elif 'email' in query:
            email_list = {
                'test email':'abhijeetshetty1997@gmail.com'
            }
            try:
                speak('to whom you want to send mail?')
                name = takeCommandMic()
                receiver = email_list[name]
                speak('what is the subject of the mail?')
                subject = takeCommandMic()
                speak('What should I say?')
                content = takeCommandMic()
                sendEmail(receiver,subject,content)
                speak('Email has been send')
            except Exception as e:
                print(e)
                speak('Unable to send the email')

        elif 'message' in query:
            user_name = {
                'viv': '+918452896807'
            }
            try:
                speak('to whom you want to send the WhatsApp msg?')
                name = takeCommandMic()
                phone_no = user_name[name]
                speak('what is the message?')
                message = takeCommandMic()
                sendWhatsAppmsg(phone_no,message)
                speak('Message has been send')
            except Exception as e:
                print(e)
                speak('Unable to send the message')

        elif 'wikipedia' in query:
            speak('searching on wikipedia.... ')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'covid-19 tracker' in query:
            web.open_new_tab(
                "https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen"
            )
            speak("covid-19 tracker is open now")
            
        
        elif "shoping" in query or 'shopping' in query:
            websites = ['amazon', 'flipkart', 'myntra', 'limeroad']
            print('\n'.join(websites))
            speak("nice mood sir!, what do you want to open?")
            user_ip = takeCommandMic().lower().replace(' ', '')

            for website in websites:
                if website in user_ip:
                    web.open(website + '.com')

            speak("here you are sir")

        elif 'online courses' in query or 'course' in query:
            platforms = [
                'coursera', 'udemy', 'edx', 'skillshare', 'datacamp', 'udacity'
            ]
            speak("Select a platform that you prefer : ")
            print("\n".join(platforms))
            query1 = takeCommandMic().lower()
            if query1 == 0:
                continue
            if 'coursera' in query1:
                web.open_new_tab("https://www.coursera.org")
                speak("Coursera is open now")
                sleep(2)
            elif 'udemy' in query1:
                web.open_new_tab("https://www.udemy.com")
                speak("udemy is open now")
                sleep(2)
            elif 'edx' in query1:
                web.open_new_tab("https://www.edx.org/")
                speak("edx is open now")
                sleep(2)
            elif 'skillshare' in query1:
                web.open_new_tab("https://www.skillshare.com")
                speak("skill share is open now")
                sleep(2)
            elif 'datacamp' in query1:
                web.open_new_tab("https://www.datacamp.com")
                speak("datacamp is open now")
                sleep(2)
            elif 'udacity' in query1:
                web.open_new_tab("https://www.udacity.com")
                speak("udacity is open now")
                sleep(2)
            else:
                speak("Sorry we couldn't find your search!!!")
            sleep(3)
        
        elif 'jobs' in query or 'job' in query or 'job recommandation' in query or 'work' in query:
            platforms = [
                'linkedin', 'indeed', 'glassdoor', 'hackerrank', 'naukri',
                'intern shala'
            ]
            speak("Select a platform that you prefer:")
            print('\n'.join(platforms))
            query1 = takeCommandMic().lower()
            if (query1 == 0):
                continue
            if 'linkedIn' in query1:
                web.open_new_tab("https://www.linkedin.com/jobs")
                speak("LinkedIn is open now")
                sleep(2)
            elif 'indeed' in query1:
                web.open_new_tab("https://www.indeed.com/jobs")
                speak("Indeed is open now")
                sleep(2)
            elif 'glassdoor' in query1:
                web.open_new_tab("https://www.glassdoor.com/jobs")
                speak("Glassdoor is open now")
                sleep(2)
            elif 'hackerrank' in query1:
                web.open_new_tab(
                    "https://www.hackerrank.com/jobs/search")
                speak("HackerRank is open now")
                sleep(2)
            elif 'naukri' in query1:
                web.open_new_tab("https://www.naukri.com/jobs")
                speak("Naukri is open now")
                sleep(2)
            elif 'intern shala' in query1:
                web.open_new_tab('internshala.com')
                speak('Intern Shala is open now')
                sleep(2)
            else:
                speak("Sorry we couldn't find your search!!!")
            sleep(3)
        
        elif 'news' in query or 'news headline' in query or 'top news' in query or 'some news' in query:
            speak('Here are some headlines from the India today')

            res = requests.get('https://www.indiatoday.in/top-stories')
            soup = BeautifulSoup(res.text, 'lxml')

            news_box = soup.find('div', {'class': 'top-takes-video-container'})
            all_news = news_box.find_all('p')

            for news in all_news:
                print('\n' + news.text)
                speak(news.text)
                print()
                sleep(6)
            sleep(8)

        elif 'movie ticket booking' in query or 'movie booking' in query or 'movie ticket' in query:
            speak('Here are some top websites for ticket booking')
            web.open_new_tab("https://in.bookmyshow.com/")
            speak(" Book my show website is open now")
            sleep(2)

        elif 'train ticket booking' in query or 'train booking' in query or 'train ticket' in query or 'train ticket' in query:
            speak('Here are some top websites for tarin ticket booking')
            web.open_new_tab("https://www.easemytrip.com/railways/")
            speak(" Ease My trip website is open now, have a good journey !")
            sleep(2)

        elif 'bus ticket booking' in query or 'bus booking' in query or 'bus ticket' in query:
            speak('Here are some top websites for bus ticket booking')
            web.open_new_tab("https://www.redbus.in")
            speak(" Red bus website is open now, have a good journey !")
            sleep(2)

        elif 'airplane ticket booking' in query or 'airplane booking' in query or 'airplane ticket' in query:
            speak('Here are some top websites for airplane ticket booking')
            web.open_new_tab("https://www.goindigo.in")
            speak(" Indigo website is open now, have a good journey !")
            sleep(2)

        elif "hotel" in query or "hotel booking" in query:
            speak('Opening go ibibo .com')
            web.open_new_tab('goibibo.com/hotels')

        elif 'top engineering colleges in india' in query or 'indian engineering college' in query or 'engineering college' in query:
            web.open_new_tab(
                "https://www.shiksha.com/b-tech/ranking/top-engineering-colleges-in-india/44-2-0-0-0"
            )
            speak("Colleges as per NIRF Ranking are open on Shiksha website!")
            sleep(2)

        elif 'top medical colleges in india' in query or 'indian medical college' in query or 'medical college' in query:
            speak('Here are some top Medical Colleges in India')
            web.open_new_tab(
                "https://medicine.careers360.com/colleges/ranking")
            speak("Colleges as per NIRF rankings are opened!")
            sleep(2)

        elif 'top science colleges in india' in query or 'indian science college' in query or 'science college' in query:
            speak('Here are some top website for Science Colleges in India')
            web.open_new_tab(
                "https://collegedunia.com/science-colleges")
            speak(" College Dunia website is opened!")

        elif 'top law colleges in india' in query or 'indian law college' in query or 'law college' in query:
            speak('Here are some top website for law Colleges in India')
            web.open_new_tab(
                "https://www.collegedekho.com/law-humanities/law-colleges-in-india/"
            )
            speak(" College Deko website is opened!")
            sleep(2)

        elif 'top research colleges in india' in query or 'indian research college' in query or 'research college' in query:
            speak('Here are some top website for Research Colleges in India')
            web.open_new_tab(
                "https://www.biotecnika.org/2019/09/top-govt-research-institutes-present-in-india-top-10-list/"
            )
            speak("Biotechnika website is opened!")
            sleep(2)
     
        elif 'search' in query:
            searchGoogle()
            
        elif 'youtube' in query:
            speak('what should i search for on youtube')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
            
        elif 'offline' in query:
            quit() 
        
        elif "sign out" in query:
            speak("Ok , your pc will log off in make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

