import pyttsx3
import speech_recognition as sr
import random

from keyboard import press
from keyboard import press_and_release
import cv2
from matplotlib.pyplot import cla
import datetime
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys
import os
from face3 import  Ui_Face
import webbrowser as web



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty("rate",176)

#cap=cv2.VideoCapture("lela.mp4")

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")
def wish():
         
        cmd=("I am your Assistant, How can i help you?")

        
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            Speak("Good Morning Sir !"+cmd)
    
        elif hour>= 12 and hour<18:
            Speak("Good Afternoon Sir !"+cmd)  
    
        else:
            Speak("Good Evening Sir !"+cmd) 
    

        

class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()
    def run(self):
        self.TaskExe()
        
    def TakeCommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print(": Listening....")

            r.pause_threshold = 1

            audio = r.listen(source)

        try:

            print(": Recognizing...")

            query = r.recognize_google(audio, language='en-in')

            print(f": Your Command : {query}\n")

        except:
            return ""

        return query.lower()
 

    def TaskExe(self):
        wish()
       

        while True:
            self.query=self.TakeCommand()
            query=self.query
           
            if 'search' in query:
                Query = query.replace("search", "")
                query = Query.replace("play", "")
                from features import GoogleSearch
                GoogleSearch(query)

            elif 'play' in query:
                Query = query.replace("service", "")
                query = Query.replace("play", "")
                from features import YoutubeSearch
                YoutubeSearch(query)
            
            elif 'open' in query:

                name = query.replace("open ", "")

                NameA = str(name)

                if 'youtube' in NameA:

                    web.open("https://www.youtube.com/")

                elif 'instagram' in NameA:

                    web.open("https://www.instagram.com/")

                else:

                    string = "https://www." + NameA + ".com"

                    string_2 = string.replace(" ", "")

                    web.open(string_2)

                           
            elif 'close tab' in self.query:
                press_and_release('ctrl + w')

            elif "problem" in query:
                Speak("Tell me the problem")
                Date = self.TakeCommand()
                Date = Date.replace("service", "")
                Date = Date.replace("multiply", "*")
                Date = Date.replace("plus", "+")
                Date = Date.replace("minus", "-")
                Date = Date.replace("into", "*")
                Date = Date.replace("root", "√")
                Date = Date.replace("so", ",")
                Date = Date.replace("power", "^")
                Date = Date.replace("equel", "=")
                from features import calculater
                print(Date)
                calculater(Date)
            elif "enable"in query:
                os.system("python Security.py")
            else:

                from Chatbot import ChatterBot

                ChatterBot(self.query)

                

                if 'bye' in self.query:

                    break

                elif 'exit' in self.query:

                    break

                elif 'go' in self.query:

                    break
            
            
StartExe = MainThread()

class StartExecution(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_Face()

        self.ui.setupUi(self)

        self.ui.label = QMovie("E:\\Service Sales Robot\\Dataset\\face3.gif")

        self.ui.gif.setMovie(self.ui.label)

        self.ui.label.start()

        StartExe.start()
App = QApplication(sys.argv)
speedtest = StartExecution()
speedtest.show()


sys.exit(App.exec_())

