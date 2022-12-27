import pywhatkit
import wikipedia
from pywikihow import search_wikihow
import os
import pyttsx3
import webbrowser as web
import requests
import bs4

#from time import sleep

# geopy==2.0.0
# geocoder==1.38.1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def GoogleSearch(term):
    query = term.replace("service", "")
    query = query.replace("what is", "")
    query = query.replace("how to", "")
    query = query.replace("what is", "")
    query=query.replace(" ","")
    query=query.replace("search","")

    query = query.replace("what do you mean by", "")


   # writeab = str(query)

   # oooooo = open('C:\\Users\\Tonni\\PycharmProjects\\Advance Service\\data.txt','a')
   # oooooo.write(writeab)
   # oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)

    #os.system('python Start,py.py')

    #if 'how to' in Query:


       # max_result = 1

       # how_to_func = search_wikihow(query=Query,max_results=max_result)

       # assert len(how_to_func) == 1

       # how_to_func[0].print()

        #Speak(how_to_func[0].summary)



    search = wikipedia.summary(Query,2)

    Speak(f": According To Your Search : {search}")
def YoutubeSearch(term):
    result="https://www.youtube.com/results?search_query="+term

    web.open(result)
    Speak("okey sir")
    pywhatkit.playonyt(term)
    Speak("enjoy the play")
def YouTubeDownload():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from pyperclip import paste
    from time import sleep
    sleep(2)
    click(x=765,y=58)
    hotkey('ctrl','c')
    value=pyperclip.paste()
    Link=str(value)
    def Download(link):
        url=YouTube(link)
        video=url.streams.first()
        video.download("E:\Service Sales Robot\Dataset\DataBase")
    Download(Link)
    Speak("Done,sir")

    os.startfile('E:\Service Sales Robot\Dataset\DataBase')
def Wolfrem(query):
    import wolframalpha
    api_key="2H9RH2-R534VRVPLY"
    requester=wolframalpha.Client(api_key)
    requested=requester.query(query)

    try:
        Answer = next(requested.results).text
        return  Answer
    except:
        Speak("A string value is not found")

def calculater(query):
    Term=str(query)
    Term =Term.replace("service","")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("into", "*")
    Term = Term.replace("root", "√")
    Term = Term.replace("so", ",")
    Term = Term.replace("power", "^")



    Final=str(Term)
    try:
        result = Wolfrem(Final)
        Speak(f"{result}")
    except:
        Speak('i cant find any answer,plz try again')


def Temp(query):
    Term=str(query)
    Term=Term.replace("service","")
    Term=Term.replace("in","")
    Term=Term.replace("what is the","")
    Term=Term.replace("temperature","")

    temp_query=str(Term)
    if 'outside' in temp_query:
        var1="Temperature in Dhaka"
        answer=Wolfrem(var1)
        Speak(F"Temperature in Dhaka Is {answer}")
    else:
        var2="Temperature in"+temp_query
        answ=Wolfrem(var2)
        Speak(f"{var2} Is{answ}")
def DateConverter(Query):
    Date = Query.replace(" and ", "-")
    Date = Date.replace(" and ", "-")
    Date = Date.replace("and", "-")
    Date = Date.replace("and", "-")
    Date = Date.replace(" ", "")



    return str(Date)
def My_Location():



    Speak("Checking....")



    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")




















