import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty("rate",176)


def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

Hello = ('hello','hey','hii','hi')

reply_Hello = ('Hello Sir , I Am amigo .',
            "Hey , What's Up sir ?",
            "Hey How Are You ?",
            "Hello Sir , Nice To Meet You Again .",
            "hola sir , i am amigo.")

Bye = ('bye','exit','sleep','go')

reply_bye = ('Bye Sir.',
            "It's Okay .",
            "It Will Be Nice To Meet You .",
            "Bye.",
            "Thanks.",
            "Okay.")

How_Are_You = ('how are you','are you fine')

reply_how = ('I Am Fine.',
            "Excellent .",
            
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

nice = ('nice','good','thanks')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.")

Functions = ['functions','abilities','what can you do','features']

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            
            'I Can Message Your Mom That You Are Not Studing..',
            'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta , Facebbook etc!',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')

sorry_reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.")

def ChatterBot(Text):



    if  Text=="hello" or Text=="hola":
        rep=random.choice(reply_Hello)
        print(rep)
        Speak(rep)
    
        
    elif  'function' in Text or 'do' in Text or "abilities"in Text:
        repl=random.choice(reply_Functions)
        print(repl)
        Speak(repl)
    else:
        return " "





        
        
    


 

    
   
  




        




           
   




      


