from tkinter import Tk, Text,Button,END, re

class Interfaz:
    def __init__(self, ventana):
        """
        It creates a calculator.
        
        :param ventana: The window that the calculator will be in
        """
        self.ventana=ventana
        self.ventana.title("Calculadora")
        self.pantalla=Text(ventana,state="disabled",width=38,height=3,background="black",foreground="white",font=("Helvetica",15))
        self.pantalla.grid(row=0,column=0,columnspan=6,padx=10,pady=5)
        self.operacion=""
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton(u"\u232B",escribir=False)
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("-")
        boton16=self.crearBoton("+")
        boton17=self.crearBoton("=",escribir=False,ancho=40,alto=2)
        botones=[boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador += 1
        botones[16].grid(row=5,column=0,columnspan=4)
        return
    def crearBoton(self,valor,escribir=True,ancho=9,alto=1):
        """
        It creates a button with the text "valor" and the width and height of "ancho" and "alto"
        respectively, and when it's clicked, it calls the function "click" with the parameters "valor"
        and "escribir"
        
        :param valor: The text that will be displayed on the button
        :param escribir: If True, the value of the button will be written to the screen, defaults to
        True (optional)
        :param ancho: width, defaults to 9 (optional)
        :param alto: height, defaults to 1 (optional)
        :return: A Button object.
        """
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda: self.click(valor,escribir))
    def click(self,texto,escribir):
        """
        It takes the text from the button and if it's not an operator, it will show it on the screen. If
        it is an operator, it will do the operation and show the result on the screen
        
        :param texto: The text that is displayed on the button
        :param escribir: Boolean value that indicates whether the text should be written to the screen
        or not
        :return: The return value is the value of the last expression evaluated, or None if no
        expression was evaluated.
        """
        if not escribir:
            if texto=="=" and self.operacion!="":
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                resultado=str(eval(self.operacion))
                self.operacion=""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
        return
    def limpiarPantalla(self):
        """
        It clears the text in the textbox.
        :return: The return statement is used to exit a function and go back to the place from where it
        was called.
        """
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0",END)
        self.pantalla.configure(state="disabled")
        return
    def mostrarEnPantalla(self,valor):
        """
        It takes a value, inserts it into the text box, and then disables the text box.
        
        :param valor: The value to be displayed on the screen
        :return: Nothing.
        """
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return
ventana_principal=Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()