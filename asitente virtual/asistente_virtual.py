
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import camara
import os
from pygame import mixer
import subprocess as sub
from tkinter import *
from PIL import Image, ImageTk
import threading as tr
import navegador as nv
import base_datos
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import preprocessors



main_window = Tk()
main_window.title("Asistente virtual")

main_window.geometry("1600x900")
main_window.resizable(0,0)
main_window.configure(bg='#0F2027')

comandos = """
        Comandos que puedes usar:
        - Reproduce...(Video Youtube)
        - Busca.......(wikipedia)
        - Abre........(pagina web o app)
        - Alarma......(formato 24hs)
        - Colores.....(rojo, azul, amarillo)
        - Conversar...(conversar con el bot)
        - Termina.....(deja de escuchar)
"""


label_title = Label(main_window, bg='#304352',fg="#1F1C18",
                    font=('Arial', 30, 'bold'))
label_title.pack(pady=10)

canvas_comandos = Canvas(bg="#0F2027", height=400, width=255,)
canvas_comandos.place(x=0,y=0)
canvas_comandos.create_text(110,80, text=comandos, fill="white", font="Arial 12")

negra_photo = ImageTk.PhotoImage(Image.open("negra.jpg"))
window_photo = Label(main_window, image=negra_photo)
window_photo.pack(pady=5)


name = "ayudante"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 145)



sites = {

                'google': 'google.com',
                'facebook': 'facebook.com',
                'whatsapp': 'web.whatsapp.com',
                'portafolio': 'github.com/FrancoPerez29/Portafolio',
                'star': 'starplus.com/es-419/home',
                'hbo': 'play.hbomax.com/page/urn:hbo:page:home',
                'disney': 'disneyplus.com/es-419/home',
                'pelis': 'pelismkvhd.com',
                'amazon': 'primevideo.com/storefront/home/ref=atv_dp_tv_c_9zZ8D2_1_0',
                'futbol': 'futbollibre.net/inicio/',
                'twitch': 'twitch.tv'

}

programs = {
}

files = {
}



def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen(phrase=None):
    listener=sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        talk(phrase)
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()    
    except sr.UnknownValueError:
        print("No entendi, intenta de nuevo")
    except sr.RequestError as e:
        print("Could not request result from google speech recognition service; " + e)
    return rec

def clock(rec):
    num = rec.replace('alarma', '')
    num = num.strip()
    talk("Alarma activada a las " + num + "horas")
    if num[0] != '0' and len(num) < 5:
        num ='0' + num
    print(num) 
    while True:
        if datetime.datetime.now().strftime('%H:%M') == num:
            print("DESPIERTAAAAAAAAAA!!!...")
            mixer.init()
            mixer.music.load("asi_fue.mp3")
            mixer.music.play()
        else:
            continue
        if keyboard.read_key() == "s":
            mixer.music.stop()
            break        

def reproduce(rec):
    musica = rec.replace('reproduce', '')
    print("REPRODUCIENDO " + musica)
    talk("REPRODUCIENDO " + musica)
    pywhatkit.playonyt(musica)

def busca(rec):
    buscar = rec.replace('busca', '')
    wikipedia.set_lang("es")
    # summary funciona para resumir los textos
    wiki = wikipedia.summary(buscar, 1)
    print(buscar + " : " + wiki)
    talk(wiki)
    
def alarma(rec):
    t = tr.Thread(target=clock, args=(rec,))
    t.start()
                       
def colores(rec):
    talk("Enseguida:")
    camara.capture()          

def abre(rec):
    task = rec.replace('abre', '').strip()
    if task in sites:
        for task in sites:
            if task in rec:
                sub.call(f'start opera.exe {sites[task]}', shell=True)
                talk(f'Abriendo {task}')
    elif task in programs:
        for task in programs:
            if task in rec:
                talk(f'Abriendo {task}')
                os.Popen(programs[task])
    else:
        talk("Lo siento, no encontre lo que estas buscando, posiblemente no esta agregado\
                    usa los botones de agregar!")          


def archivo(rec):
    file=rec.replace('archivo', '').strip()
    if file in files:
        for file in files:
            if file in rec:
                sub.Popen([files[file]], shell=True)
                talk(f'Abriendo {file}')

def escribe():
    try:
        with open("nota.txt", 'a') as f:
            write(f)
    except FileNotFoundError as e:
        file = open("nota.txt", 'w')
        write(file)
        
def buscame(rec):
    something=rec.replace('buscame ', '').strip()
    talk("Buscando..."+ something)
    nv.search(something)
    

        
        
palabras_claves = {
    'reproduce': reproduce,
    'busca': busca,
    'alarma': alarma,
    'colores': colores,
    'abre': abre,
    'archivo': archivo,
    'escribe': escribe,
    'buscame': buscame,
}                  
            
def run_negra():
    chat = ChatBot("negra", base_datos_uri=None)
    trainer = ListTrainer(chat)
    trainer.train(base_datos.get_preguntas_y_respuestas())
    talk("te escucho")
    while True:
        try:
            rec = listen("")
        except UnboundLocalError:
            talk("No te entendi, intenta de nuevo")
            continue
        if "busca" in rec:
            palabras_claves['busca'](rec)
            break
        elif rec.split()[0] in palabras_claves:
            palabras_claves[rec.split()[0]](rec)
        else:
            print("Tu :"+ rec)    
            respuesta = chat.get_response(rec)
            print("negra : ", respuesta)
            talk(respuesta)
            if 'adios' in rec:
                break
        
    main_window.update()

def di_mi_nombre():
    talk("¿Como te llamas?")
    nombre= listen()
    nombre = nombre.strip()
    talk("Bienvenido "+ nombre)
    try:
        with open("name.txt",'w') as f:
            f.write(nombre)
    except FileNotFoundError:
        file = open("name.txt",'w')
        file.write(nombre)
    run_negra()
    
def di_hola():
    hour=datetime.datetime.now().hour
    if os.path.exists("name.txt"):
        with open("name.txt") as f:
            for nombre in f:
                if hour >0 and hour<12:
                    talk("Hola,"+ nombre + " Buenos Dias " )
                elif hour >12 and hour<20:
                    talk("Hola,"+ nombre + " Buenas Tardes " )
                else:
                    talk("Hola,"+ nombre + " Buenas Noches " )
    else:
        di_mi_nombre()   
    
def thread_hola():
    t = tr.Thread(target=di_hola)
    t.start()
thread_hola()


def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen("Dime ")
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)
    
def abrir_pagina():
    global name_pagina_entry,patha_pagina_entry
    window_pagina =Toplevel()
    window_pagina.title("Agregar pagina")
    window_pagina.configure(bg='#0F2027')
    window_pagina.geometry("400x200")
    window_pagina.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_pagina)} center')   
    
    title_label = Label(window_pagina, text="Agregar Pagina", bg="white", font=('Arial',20,'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_pagina, text="nombre de la pagina",bg="#304352", font=('Arial',15,'bold'))
    name_label.pack(pady=2)
    
    name_pagina_entry = Entry(window_pagina)
    name_pagina_entry.pack(pady=1)
    
    path_label = Label(window_pagina, text="link de la pagina",bg="#304352", font=('Arial',15,'bold'))
    path_label.pack(pady=2)
    
    patha_pagina_entry = Entry(window_pagina, width=50)
    patha_pagina_entry.pack(pady=1)
    
    save_button = Button(window_pagina, text="Guardar",bg="#000000",  fg="white", width=8,height=1,command=add_pagina)
    save_button.pack(pady=4)

            
def abrir_programa():
    global name_programa_entry,paths_programa_entry
    window_programa =Toplevel()
    window_programa.title("Agregar programa")
    window_programa.configure(bg='#0F2027')
    window_programa.geometry("400x200")
    window_programa.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_programa)} center')   
    
    title_label = Label(window_programa, text="Agregar programa", bg="white", font=('Arial',20,'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_programa, text="nombre del programa",bg="#304352", font=('Arial',15,'bold'))
    name_label.pack(pady=2)
    
    name_programa_entry = Entry(window_programa)
    name_programa_entry.pack(pady=1)
    
    path_label = Label(window_programa, text="Ruta del programa",bg="#304352", font=('Arial',15,'bold'))
    path_label.pack(pady=2)
    
    paths_programa_entry = Entry(window_programa, width=50)
    paths_programa_entry.pack(pady=1)
    
    save_button = Button(window_programa, text="Guardar",bg="#000000",  fg="white", width=8,height=1,command=add_programa)
    save_button.pack(pady=4)
              
def abrir_archivo():
    global name_archivo_entry,pathf_archivo_entry
    window_archivo =Toplevel()
    window_archivo.title("Agregar Archivo")
    window_archivo.configure(bg='#0F2027')
    window_archivo.geometry("400x200")
    window_archivo.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_archivo)} center')   
    
    title_label = Label(window_archivo, text="Agregar Archivo", bg="white", font=('Arial',20,'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_archivo, text="Nombre del Archivo",bg="#304352", font=('Arial',15,'bold'))
    name_label.pack(pady=2)
    
    name_archivo_entry = Entry(window_archivo)
    name_archivo_entry.pack(pady=1)
    
    path_label = Label(window_archivo, text="Ruta del Archivo",bg="#304352", font=('Arial',15,'bold'))
    path_label.pack(pady=2)
    
    pathf_archivo_entry = Entry(window_archivo, width=50)
    pathf_archivo_entry.pack(pady=1)
    
    save_button = Button(window_archivo, text="Guardar",bg="#000000",  fg="white", width=8,height=1,command=add_archivo)
    save_button.pack(pady=4)  

def add_pagina():
    name_pagina = name_pagina_entry.get().strip()
    path_pagina = patha_pagina_entry.get().strip()
    sites[name_pagina] = path_pagina
    guardar_datos(name_pagina, path_pagina, "paginas.txt")
    name_pagina_entry.delete(0,"end")
    patha_pagina_entry.delete(0,"end")

def add_programa():
    name_programa = name_programa_entry.get().strip()
    path_programa = paths_programa_entry.get().strip()
    sites[name_programa] = path_programa
    guardar_datos(name_programa, path_programa, "programas.txt")
    name_programa_entry.delete(0,"end")
    paths_programa_entry.delete(0,"end")

def add_archivo():
    name_archivo = name_archivo_entry.get().strip()
    path_archivo = pathf_archivo_entry.get().strip()
    sites[name_archivo] = path_archivo
    guardar_datos(name_archivo, path_archivo, "archivo.txt")
    name_archivo_entry.delete(0,"end")
    pathf_archivo_entry.delete(0,"end")


def guardar_datos(key, value, file_name):
    try:
        with open(file_name,'a') as f:
            f.write(key+","+value + "\n")
    except FileNotFoundError as f:
        file = open(file_name,'a')
        file.write(key+","+value+"\n")
    
def vos_mexicana():
    cambiar_vos(0)
    
def vos_española():
    cambiar_vos(1)
    
def vos_EEUU():
    cambiar_vos(2)

def cambiar_vos(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    talk("")

button_listen = Button(main_window, text="Escuchar",fg="white",bg="#000000",
                      font=("Arial",15, "bold"),width=20, height=5, command=run_negra) 
button_listen.pack(pady=10)

button_add_pagina = Button(main_window, text="Agregar Pagina",fg="white",bg="#000000",
                       font=("Arial",15, "bold"),width=20, height=5, command=abrir_pagina) 
button_add_pagina.place(x = 1200, y=65, width=250, height=50)

button_add_programa = Button(main_window, text="Agregar Programa",fg="white",bg="#000000",
                       font=("Arial",15, "bold"),width=20, height=5, command=abrir_programa) 
button_add_programa.place(x = 1200, y=100, width=250, height=50)

button_add_archivo = Button(main_window, text="Agregar Archivo",fg="white",bg="#000000",
                       font=("Arial",15, "bold"),width=20, height=5, command=abrir_archivo) 
button_add_archivo.place(x = 1200, y= 140,width=250, height=50)

button_voices_mx = Button(main_window, text="Voz Mexico",fg="white",bg="#000000",
                       font=("Arial",15, "bold"),width=20, height=5, command=vos_mexicana) 
button_voices_mx.place(x = 1200, y= 640,width=250, height=50)

button_voices_es = Button(main_window, text="Voz España",fg="white",bg="#000000",
                       font=("Arial",15, "bold"),width=20, height=5, command=vos_española) 
button_voices_es.place(x = 1200, y= 680,width=250, height=50)

button_voices_us = Button(main_window, text="Voz EEUU",fg="white",bg="#000000",
                       font=("Arial",15, "bold"),width=20, height=5, command=vos_EEUU) 
button_voices_us.place(x = 1200, y= 720,width=250, height=50)


main_window.mainloop()