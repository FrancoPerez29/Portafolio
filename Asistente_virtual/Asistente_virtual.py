import speech_recognition as sr
import pyttsx3, pywhatkit


name = "viernes"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
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
    rec = listen()
    if 'reproduce' in rec:
        musica = rec.replace('reproduce','')
        print("REPRODUCIENDO..." + musica)
        talk("REPRODUCIENDO..." + musica)
        pywhatkit.playonyt(musica)
        
if __name__ == '__main__':
    corre_viernes()