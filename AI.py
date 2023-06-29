
import speech_recognition as sr
from datetime import *
from time import sleep
import wikipedia
import webbrowser
import os
import openai
from dotenv import load_dotenv
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from googletrans import Translator
from AppOpener import run
import randfacts
import pywhatkit


Chrome_options = Options()
Chrome_options.add_argument('--log-level=3')
Chrome_options.add_argument('headless')
Chrome_options.add_argument('window-size=1200x600')
Path = r"C:\\SHAIELSH\\PYTHON CODS\\SLP project\\DATA BASE\\chromedriver.exe"


driver = webdriver.Chrome(Path, options=Chrome_options)


driver.maximize_window()
Chrome_options.add_experimental_option("detach", True)
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
website = r"https://ttsmp3.com/text-to-speech/British%20English/"
try:
    driver.get(website)
    ButtonSelection = Select(driver.find_element(
        by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
    ButtonSelection.select_by_visible_text('British English / Brian')
except:
    print(" !!!! Internet not avelible !!!! ")

fileopen = open("C:\\SHAIELSH\\PYTHON CODS\\SLP project\\DATA BASE\\API_key.txt")
API = fileopen.read()
fileopen.close()

openai.api_key = API
load_dotenv()
completion = openai.Completion()


def Brain(question, chat_log=None):

    Filelog = open("DATA BASE\\chat_log.txt", "r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log} You :{question} \n jarvis:'
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0)

    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + \
        f" \n You :{question} \n jarvis: {answer}"
    Filelog = open("DATA BASE\\chat_log.txt", "w")
    Filelog.write(str(chat_log_template_update))
    Filelog.close()
    return answer


def takeinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
       

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi")

    except:
        return "None"

    query = str(query).lower()
    return query


def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text

    if len(data) <= 3:
        return data
    else:
        print(f"You : {data}.")
        return data


def MicExecution():
    query = takeinput()
    data = TranslationHinToEng(query)
    return data


def speak(text):
    lengthoftext = len(str(text))

    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"AI : {text} ")
        print("")
        Data = str(text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(
            By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(
            By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthoftext < 8:
            sleep(5)
        else:
            stop_execution(lengthoftext)


def stop_execution(lengthoftext):
    wait = (lengthoftext//10)
    sleep(wait)


def launchBrowser():
    chrome_options = Options()
    chrome_options.binary_location = "../Google Chrome"
    chrome_options.add_argument("disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    while (True):
        driver.get("http://www.google.com/")
        pass


def google_search(search_string):
    search_string = search_string.replace('search', '')
    search_string = search_string.replace('google', '')
    search_string = search_string.replace('open', '')
    search_string = search_string.replace('what is', '')
    search_string = search_string.replace('who is', '')
    search_string = search_string.replace(' ', '+')
    Chrome_options = Options()
    Chrome_options.add_argument('--log-level=3')
    browser = webdriver.Chrome('chromedriver')

    matched_elements = browser.get("https://www.google.com/search?q=" +
                                   search_string + "&start=" + str(1))


def Open_website(search_string):

    search_string = search_string.replace('open', '')
    search_string = search_string.replace(' ', '+')
    browser = webdriver.Chrome(
        desired_capabilities=caps, executable_path='chromedriver')

    matched_elements = browser.get("https://www.google.com/search?q=" +
                                   search_string + "&start=" + str(1))
    browser.maximize_window()
    ButtonSelection = browser.find_element(By.CLASS_NAME, "iUh30").click()


def play_song(search_string):
    search_string = search_string.replace('song', '')
    search_string = search_string.replace('play', '')
    if "stop"not in qurey:
        try:
            speak(" search for your song please wait")
            search_string = str(search_string)
            Chrome_options.add_experimental_option("detach", True)
            Path = "C:\\SHAIELSH\\PYTHON CODS\\SLP project\\DATA BASE\\chromedriver.exe"
            global browser
            browser = webdriver.Chrome(Path, options=Chrome_options)
            browser.maximize_window()
            browser.get("https://www.jiosaavn.com/")
            browser.implicitly_wait(10)
            search = browser.find_element(
                by=By.XPATH, value="//input[@role='combobox']").send_keys(search_string)
            random = browser.find_elements(
                by=By.XPATH, value="/html[1]/body[1]/div[1]/div[2]/header[1]/aside[1]/div[2]/div[1]/div[1]/div[1]")
            browser.find_element(
                by=By.XPATH, value="/html[1]/body[1]/div[1]/div[2]/header[1]/aside[1]/div[2]/div[1]/div[3]/h5[1]/div[1]/a[1]").click()
            browser.find_element(
                by=By.XPATH, value="/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/ol[1]/li[1]/div[1]/article[1]/div[2]/figure[1]/div[1]").click()
        except:
            speak(
                "sorry sir, your song not found can you try again with different song name ?")
            print("song not found")
            sleep(5)
        try:
            singers = browser.find_element(
                by=By.XPATH, value="(//p[@class='u-centi u-ellipsis u-color-js-gray u-margin-right@sm u-margin-right-none@lg'])[14]")
            speak(f"playing {search_string} sing by {str(singers.text)}")
            print(f"playing {search_string} sing by {str(singers.text)}")
        except:
            pass
    else:
        speak("ok song paused")
        browser.find_element(
            by=By.XPATH, value="(//span[@id='player_play_pause'])[1]").click()


def wishme():
    hour = int(datetime.now().hour)

    if hour >= 1 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 13 and hour <= 16:
        speak("Good Afternoon!")
    elif hour > 16 and hour <= 19:
        speak("Good Evenning!")
    else:
        speak("Good night!")
    speak("let me introduce my self,i am jarvis an artificial intelligence robot and I'm here to complete your task as best as I can")


def hotword():
    result = MicExecution()
    if "jarvis" in result:
        speak(Brain(result))
        return
    else:
        hotword()


if __name__ == "__main__":
    speak("Booting up system, please wait")
    try:
        playsound(r"C:\SHAIELSH\PYTHON CODS\SLP project\music\bootingsound1.mp3")
    except:
        pass
    wishme()
    while (True):

        qurey = MicExecution()
        qurey = qurey.lower()
        count = str(qurey)

        if len(count) < 5:
            pass
        elif 'random fact' in qurey or 'fact' in qurey:
            fact = randfacts.get_fact()
            speak(fact)

        elif 'website' in qurey or ' open website' in qurey:
            Open_website(qurey)

        elif 'open' in qurey or 'open app' in qurey:

            qurey = qurey.replace('open', '')
            qurey = qurey.replace('open app', '')
            speak(f"Search for {qurey} application on leptop")

            temp = run(qurey)
            if 'NOT FOUND...' in qurey:
                speak(f"can not find {qurey}")

        elif 'google' in qurey or ' google search' in qurey:
            google_search(qurey)

        elif 'shutdown' in qurey or 'poweroff' in qurey:
            speak("are you sure , Do you want to shutdown of your device")
            confirm = input(
                "are you sure , Do you want to shutdown your device (y/n)?")
            if 'y' in confirm.lower():
                os.system("shutdown /s")
            else:
                print("ok not shutdown pc")

        elif 'logout' in qurey or 'switch user' in qurey:
            speak("are you sure , Do you want to switch user  of your device")
            confirm = input("are you sure , Do you want to switch user(y/n)?")
            if 'y' in confirm.lower():
                os.system("shutdown /l")
            else:
                print("ok not sswitch user")

        elif 'restart' in qurey or 'reboot' in qurey:
            speak("are you sure , Do you want to restart your device")
            confirm = input(
                "are you sure , Do you want to restart your device (y/n)?")
            if 'y' in confirm.lower():
                os.system("shutdown /r")
            else:
                print("ok not sswitch user")

        elif 'play video' in qurey or 'on youtube' in qurey:

            qurey = qurey.replace('play video', '')
            qurey = qurey.replace('on youtube', '')
            speak(f"Search for {qurey} on youtube")
            try:
                speak("playing video on youtube ")
                pywhatkit.playonyt(qurey)
            except:
                speak("can not find video on youtube")

        elif 'play song' in qurey or 'song' in qurey:
            play_song(qurey)

        elif 'sleep' in qurey or 'rest' in qurey:
            speak("ok sir as your wish,let me know if you need any help")
            hotword()

        elif 'time' in qurey:
            time_now = datetime.now()
            current_time = time_now.strftime("%I:%M %p")
            speak(f"the current time is {current_time}")
            print(f" jarvus : the current time is {current_time}")

        elif 'reminder' in qurey:
            reminder = open("DATA BASE\\reminder.txt")
            things = fileopen.read()
            reminder.close()
            rem = []
            current_time = time_now.strftime("%I:%M %p")
            speak(f"the current time is {current_time}")
            print(f" jarvus : the current time is {current_time}")

        else:
            result = Brain(qurey)
            speak(result)
