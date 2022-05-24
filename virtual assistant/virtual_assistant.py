import speech_recognition as sr
import pyttsx3, pywhatkit


name = "viernes"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    """
    It takes a string as an argument and speaks it out loud.
    
    :param text: The text that you want to convert to speech
    """
    engine.say(text)
    engine.runAndWait()
    

# Listening to the microphone and then it is recognizing the words that you say.
def listen():
    try:
        with sr.Microphone() as source:
            print("ESCUCHANDO...")
            pc=listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                
            
    except:
        pass
    return rec
def corre_viernes():
    """
    It takes the input from the user, and if the user says "reproduce" followed by the name of a song,
    it will play that song on YouTube.
    """
    
    rec = listen()
    if 'reproduce' in rec:
        musica = rec.replace('reproduce','')
        print("REPRODUCIENDO..." + musica)
        talk("REPRODUCIENDO..." + musica)
        pywhatkit.playonyt(musica)
        
if __name__ == '__main__':
    corre_viernes()