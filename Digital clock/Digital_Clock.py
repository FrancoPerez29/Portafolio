from tkinter import *
import time

ventana = Tk()
ventana.title("Reloj Digital")
ventana.geometry("1900x450+10+10")
ventana.minsize(width=250, height=200)

def Reloj_Digital():
    hora = time.strftime("%H:%M:%S")
    Reloj.config(text=hora,font=("Courier", 295, "italic"), fg="white", bg="black",)    
    Reloj.after(200, Reloj_Digital)

Reloj = Label(ventana, font=("times",200,"bold")) 
 
Reloj.grid(row=2,column=2,pady=0,padx=0)
Reloj_Digital()


ventana.mainloop()