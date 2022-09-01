from tkinter import Button
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, camara ,os
from pygame import mixer
import subprocess as sub

name = "negra"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 145)

sites = {
                'google': 'google.com'
                #'facebook': 'facebook.com',
                #'whatsapp': 'web.whatsapp.com',
                #'portafolio': 'github.com/FrancoPerez29/Portafolio',
                #'star': 'starplus.com/es-419/home',
                #'hbo': 'play.hbomax.com/page/urn:hbo:page:home',
                #'disney': 'disneyplus.com/es-419/home',
                #'pelis': 'pelismkvhd.com',
                #'amazon': 'primevideo.com/storefront/home/ref=atv_dp_tv_c_9zZ8D2_1_0',
                #'futbol': 'futbollibre.net/inicio/',
                #'twitch': 'twitch.tv'
}

programas = {
    
    'discord':r"C:\Users\Emperador\AppData\Local\Discord\Update.exe",
    
    
}



def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando . . .")
            print(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                
    except:
        pass
    return rec

def run_negra():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            musica = rec.replace('reproduce', '')
            print("REPRODUCIENDO " + musica)
            talk("REPRODUCIENDO " + musica)
            pywhatkit.playonyt(musica)
        
        elif 'busca' in rec:
            buscar = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(buscar, 1)#summary funciona para resumir los textos
            print(buscar + ": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            alarma = rec.replace('alarma', '')
            alarma = alarma.strip()
            talk("Alarma activada a las "+ alarma + "horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == alarma:
                    print("DESPIERTAAAAAAAAAA!!!...")
                    mixer.init()#
                    mixer.music.load("asi_fue.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif 'colores' in rec:
            talk("Enseguida:")
            camara.capture()
            
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call('start chrome.exe' + {sites[site]}, shell=True)
                    talk(f'Abriendo {site}')
            for app in programas:
                if app in rec:
                    talk(f'Abriendo {app}')
                    os.popen(programas[app])
                    
        elif 'escribe' in rec:
            try:
                with open("nota.txt", 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", 'w')
                write(file)
                    
        elif 'termina' in rec:
            talk('llamame si me necesitas, Adios!')
            break

def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)
    
    

        
        
        
if __name__ == '__main__':
    run_negra()