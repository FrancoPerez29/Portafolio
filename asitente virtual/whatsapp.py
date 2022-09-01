import webbrowser
import pyautogui as at
import time

def mandar_msj(contacto, mensaje):
    webbrowser.open(f'https://web.whatsapp.com/send?phone={contacto}&text={mensaje}')
    time.sleep(5)
    at.press('enter')