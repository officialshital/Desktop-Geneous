import email
import operator
import smtplib
import tkinter as tk
from tkinter import messagebox

import openai
from PIL import ImageTk, Image
import threading
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import subprocess
import os
import requests
import random
import pywhatkit
import pyautogui
import time

from index import recognize_spelled_text


class DesktopGenius:
    def __init__(self, master):
        self.master = master
        master.geometry("650x750+600+68")
        master.title("Desktop Genius")
        master.resizable(False, False)

        img_path1 = '1LOGO VANSHU.png'
        logo = Image.open(img_path1)
        pixels_x, pixels_y = 98, 98
        resized_image = logo.resize((pixels_x, pixels_y))
        self.img1 = ImageTk.PhotoImage(resized_image)

        self.label = tk.Label(master, image=self.img1)
        self.label.image = self.img1
        self.label.place(x=270, y=40)

        self.nameLabel = tk.Label(master, fg="#6600CC", text="Dekstop Genius", font=('Cascadia Code', 14))
        self.nameLabel.place(x=210, y=134)

        self.listen_button = tk.Button(master, font=('times', 11), text="Listen", width=5, height=1,
                                       command=self.listen)
        self.listen_button.place(x=565, y=687)

        self.command_label = tk.Label(master, text="Commands:")
        self.command_label.place(x=12, y=465)

        self.command_textbox = tk.Text(master, height=10, width=45)
        self.command_textbox.place(x=12, y=506)

        self.effect_thread = None

    def speak_effect(self):
        self.nameLabel.config(fg="blue")
        self.master.update()
        self.master.after(1000, self.reset_effect)

    def reset_effect(self):
        self.nameLabel.config(fg="black")
        self.master.update()

    def listen(self):
        self.speak_effect()
        self.listen_button.config(state="disabled")
        threading.Thread(target=self.assistant_thread).start()

    def assistant_thread(self):
        greeting()
        try:
            while True:
                query = takeCommand().lower()
                self.command_textbox.insert(tk.END, query + "\n")

                if "hello" in query:
                    speak("Hello!  My Name is DesktopGenius")
                elif "thanks" in query:
                    speak("You're welcome!")
                elif "bye" in query:
                    speak("Goodbye! Have a nice day!")
                    break

                elif "search on google" in query:
                    search_query1 = query.replace("search on google", "").strip()
                    webbrowser.open(f"https://www.google.com/search?q={search_query1}")

                elif "who is" in query:
                    search_query2 = query.replace("search", "").strip()
                    webbrowser.open(f"https://www.google.com/search?q={search_query2}")

                elif 'search on youtube' in query:
                    query = query.replace("search on youtube", "")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

                elif 'close browser' in query:
                    os.system("taskkill /f /im msedge.exe")

                elif 'open youtube' in query:
                    speak("Here you go to Youtube\n")
                    webbrowser.open("https://www.youtube.com/")
                    speak("what you will like to watch on youtube ?")
                    queryy = takeCommand().lower()
                    pywhatkit.playonyt(f"{queryy}")

                elif 'open google' in query:
                    speak("Here you go to Google\n")
                    webbrowser.open("https://www.google.com")
                elif 'open stackoverflow' in query:
                    speak("Here you go to Stack Over flow.Happy coding")
                    webbrowser.open("https://www.stackoverflow.com")
                elif 'open spotify' in query:
                    speak("Here you go to Spotify")
                    webbrowser.open("https://www.spotify.com")
                elif 'play music' in query:
                    speak("Here you go with music")
                    play_music()

                elif "open notepad" in query:
                    speak("opening notepad")
                    os.system("start notepad")
                elif "open calculator" in query:
                    speak("opening calculator")
                    os.system("start calc")
                elif "open microsoft edge" in query:
                    speak("opening microsoft edge")
                    os.system("start msedge")
                elif "open chrome" in query:
                    speak("opening chrome")
                    os.system("start chrome")
                elif "open file explorer" in query:
                    speak("opening file explorer")
                    os.system("start explorer")
                elif "open word" in query:
                    speak("opening word")
                    os.system("start winword")
                elif "open powerpoint" in query:
                    speak("opening powerpoint")
                    os.system("start powerpnt")
                elif "open excel" in query:
                    speak("opening excel")
                    os.system("start excel")
                elif "open firefox" in query:
                    speak("opening firefox")
                    os.system("start firefox")
                elif "open camera" in query:
                    speak("opening camera")
                    open_camera()
                elif "open cmd" in query:
                    speak("opening cmd")
                    os.system("start cmd")

                elif "open college website" in query:
                    speak("Opening College Website ")
                    webbrowser.open("https://dbatu.ac.in/")
                elif "which day it is" in query:
                    day = datetime.datetime.today().weekday() + 1
                    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                                7: 'Sunday'}
                    if day in Day_dict.keys():
                        day_of_the_week = Day_dict[day]
                        speak(f"Today is {day_of_the_week}")
                elif "tell me the time" in query:
                    time = str(datetime.datetime.now())
                    hour = time[11:13]
                    min = time[14:16]
                    speak(f"The time is {hour} hours and {min} minutes")
                elif "tell me about" in query:
                    query = query.replace("tell me about", "")
                    try:
                        result = wikipedia.summary(query, sentences=4)
                        speak("According to Wikipedia")
                        print(result)
                        speak(result)
                    except Exception as e:
                        print(e)
                        speak("Sorry, I couldn't find information on this topic.")
                elif "how is your day" in query:
                    speak("My day going great, thank for ask me !")
                elif "tell me your name" in query:
                    speak("I am your Assistant. How can I assist you?")
                # Information for Know
                elif "who is your creators" in query:
                    msg = "My creators are Vanshika, Shital, Vaishnavi and their mentor was Prof. Karan Korpe Sir."
                    print(msg)
                    speak(msg)
                elif "who is your mentor" in query:
                    msg1 = "My mentor is Prof. Karan Korpe Sir.."
                    print(msg1)
                    speak(msg1)
                elif "tell me today's weather" in query:
                    weather()
                elif "send whatsapp message" in query:
                    send_whatsapp_message()

                elif "type" in query:
                    query = query.replace("type", "")
                    pyautogui.typewrite(f"{query}", 0.1)

                elif 'open new tab' in query:
                    pyautogui.hotkey('ctrl', 't')
                elif 'close current tab' in query:
                    pyautogui.hotkey('ctrl', 'w')

                elif 'select all' in query:
                    pyautogui.hotkey('ctrl', 'a')
                elif 'undo' in query:
                    pyautogui.hotkey('ctrl', 'z')
                elif 'redo' in query:
                    pyautogui.hotkey('ctrl', 'y')
                elif 'copy data' in query:
                    pyautogui.hotkey('ctrl', 'c')
                elif 'cut data' in query:
                    pyautogui.hotkey('ctrl', 'x')
                elif 'paste data' in query:
                    pyautogui.hotkey('ctrl', 'v')

                elif 'volume up' in query:
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")

                elif 'volume down' in query:
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")

                elif 'shut down laptop' in query:
                    os.system("shutdown /r /t 5")

                elif 'lock the laptop' in query:
                    os.system("rundll32.exe powrprof.dll, SetSuspendState 0, 1, 0")

                elif "go to the sleep system" in query:
                    os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

                # College Information
                elif "Information about IT Department" in query:
                    webbrowser.open("https://dbatu.ac.in/department-of-information-technology-2/")
                elif "Information about computer department" in query:
                    webbrowser.open("https://cse.dbatu.ac.in/")

                # Department Information
                elif 'Who is the HOD of IT Department' in query:
                    print("Dr. Shivajirao Jadhav Sir")
                    speak("Dr. Shivajirao Jadhav Sir")
                elif 'please tell me all professor names of IT department' in query:
                    print("Dr. S. M. Jadhav Sir, Dr. S. R. Sutar Sir, Dr. V. J. Kadam Sir, Dr. A. R. Babhulgaonkar Sir, Prof. S. V Bharad Mam, Prof. S. S. Barphe Mam, Prof. H. R. Hivre Mam, Prof. E. G. Meshram Mam, Prof. P. P. Jadhav Mam, Prof. S. K. Thakur Mam, Prof. K. R. Korpe Sir")
                    speak("Dr. S. M. Jadhav Sir, Dr. S. R. Sutar Sir, Dr. V. J. Kadam Sir, Dr. A. R. Babhulgaonkar Sir, Prof. S. V Bharad Mam, Prof. S. S. Barphe Mam, Prof. H. R. Hivre Mam, Prof. E. G. Meshram Mam, Prof. P. P. Jadhav Mam, Prof. S. K. Thakur Mam, Prof. K. R. Korpe Sir")


                # Vaishnavi
                elif "take screenshot" in query:
                    speak('Tell me a name for the file')
                    name = takeCommand().lower()
                    img = pyautogui.screenshot()
                    file_path = r"D:\screenshot\\" + name + ".png"
                    img.save(file_path)
                    speak("Screenshot saved as " + name)

                # Change this to the directory you want to save the screenshots in
                elif "calculate" in query:
                    print(calculator(query))

                elif "what is my ip address" in query:
                    speak("Checking")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        speak("your ip adress is")
                        speak(ipAdd)
                    except Exception as e:
                        speak("network is weak, please try again some time later")
                elif "write gmail" in query:
                    GmailAutomation()

                elif 'maximize this window' in query:
                    pyautogui.hotkey('alt', 'space')
                    # time.sleep(1)
                    pyautogui.press('x')
                elif 'open incognito window' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'n')
                elif 'minimise this window' in query:
                    pyautogui.hotkey('alt', 'space')
                    # time.sleep(1)
                    pyautogui.press('n')

                elif 'previous google tab' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'tab')
                elif 'open next tab' in query:
                    pyautogui.hotkey('ctrl', 'tab')
                elif 'close window' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'w')
                elif 'clear browsing history' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'delete')

                # Shital
                elif "open history" in query:
                    pyautogui.hotkey('ctrl', 'h')
                elif "open downloads" in query:
                    pyautogui.hotkey('ctrl', 'j')
                elif "find" in query:
                    pyautogui.hotkey('ctrl', 'f')
                elif "open menu" in query:
                    pyautogui.hotkey('Alt', 'f')
                elif "add to favourite" in query:
                    pyautogui.hotkey('ctrl', 'd')
                elif "open help center" in query:
                    pyautogui.press('F1')
                elif "open new window" in query:
                    pyautogui.hotkey('ctrl', 'n')
                elif "open new tab" in query:
                    pyautogui.hotkey('ctrl', 't')
                elif "jump to next open tab" in query:
                    pyautogui.hotkey('ctrl', 'tab')
                elif "jump to previous open tab" in query:
                    pyautogui.hotkey('ctrl', 'shift')
                    pyautogui.hotkey('alt', 'Home')
                elif "open developers tool" in query:
                    pyautogui.hotkey('ctrl', 'Shift', 'j')

                # elif 'online bot' in query:
                #     chat_with_gpt()
                elif "close software" in query:
                    close_software()

                else:
                    speak("Sorry, I am still learning and I couldn't understand your request.")

        except Exception as e:
            print(e)

# openai.api_key = "3bb323fe1c8ebcd25deb3b7923e8bae7"
# def chat_with_gpt(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150
#     )
#     message = response.choices[0].text.strip()
#     return message


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        speak('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing...")
            speak("recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("You Said: ", Query)
        except Exception as e:
            print(e)
            print("Say That Again")
            return "None"
        return Query

def greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I'm DesktopGenius, how can I help you today?")

def send_whatsapp_message():
    speak("Do you want to send a WhatsApp message?")
    msg = int(input("For Person - Press 1, To end - Press 0: "))

    if msg == 1:
        speak("Enter the phone number:")
        phone = input("Enter the phone number: ")

        speak("What is the message?")
        message = input("Enter your message: ")

        speak("Enter the hour to send the message:")
        time_hour = int(input("Enter hour (24-hour format): "))

        speak("Enter the minute to send the message:")
        time_minute = int(input("Enter minute: "))

        pywhatkit.sendwhatmsg(phone, message, time_hour, time_minute)
        speak("Message scheduled.")

        pyautogui.press('enter')

    elif msg == 0:
        speak("Okay, ending the process.")
    else:
        speak("Invalid choice. Please try again.")

def close_software(close=None):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Which software would you like to close?")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            software_name = r.recognize_google(audio, language='en-in').lower()
            print(f"You said: {software_name}")
            close(software_name)
            speak(f"Closing {software_name}")
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't understand which software to close. Please try again.")

def weather():
    api = "3bb323fe1c8ebcd25deb3b7923e8bae7"
    baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
    r = sr.Recognizer()
    with sr.Microphone() as source:
        city_call = "Your city name"
        print(city_call)
        speak(city_call)
        audio = r.listen(source)
        try:
            city = r.recognize_google(audio, language='en-in').lower()
            print(city)
            result = baseURL + city + "&appid=" + api
            response = requests.get(result)
            data = response.json()
            temp = "Current Temperature", data["main"]["temp"]
            feels_like = "Feels Like Temperature", data["main"]["feels_like"]
            temp_min = "Minimum Temperature", data["main"]["temp_min"]
            temp_max = "Maximum Temperature", data["main"]["temp_max"]
            print(temp, "\n", feels_like, "\n", temp_min, "\n", temp_max, "\n")
            speak(temp)
            speak(feels_like)
            speak(temp_min)
            speak(temp_max)
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't understand, Please try again.")


def open_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)

def play_music():
    try:
        music_dir = "C:\\Users\\vansh\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, random.choice(songs)))
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't open the default music player.")


# Vaishnavi
def send_email(receiver_email, subject, body):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "Vaishnavidhekare2002@gmail.com"  # Enter your email address
    password = "rvpn etfx obqp dkbc"  # Enter your app password

    try:
        # Log in to the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)

        # Construct the email
        msg = email.message.EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Send the email
        server.send_message(msg)

        # Quit the server
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def GmailAutomation():
    speak("Please spell out the receiver's email address, starting with the username.")
    print("Please spell out the receiver's email address, starting with the username.")
    receiver_username = recognize_spelled_text().replace(" ", "")
    speak("Now, please spell out the domain name.")
    print("Now, please spell out the domain name.")
    receiver_domain = recognize_spelled_text().replace(" ", "")
    speak("And finally, please spell out the top-level domain.")
    print("And finally, please spell out the top-level domain.")
    receiver_tld = recognize_spelled_text().replace(" ", "")
    receiver_email = receiver_username + "@" + receiver_domain + "." + receiver_tld
    print("Receiver's email:", receiver_email)
    speak("Please say the subject of the email: ")

    subject = recognize_spelled_text()
    speak("Please say the body of the email: ")

    body = recognize_spelled_text()

    send_email(receiver_email, subject, body)
    print("Email sent successfully!")
    speak("Email sent successfully!")

# Calling the function
def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }[op]

def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


def calculator(query):
    if "calculate" in query:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Ready")
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
        my_string = my_string.replace('x', '*')
        result = eval_binary_expr(*(my_string.split()))
        speak("Your result is " + str(result))
        os.system('calc')
        time.sleep(2)
        # Typing the result on the calculator

        pyautogui.typewrite(str(int(result)), interval=0.1)
        pyautogui.press('enter')
        return "Your result is " + str(result)


root = tk.Tk()
my_gui = DesktopGenius(root)
root.mainloop()
