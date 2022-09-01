from http.server import executable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search(something):
    navegador = webdriver.Opera(executable_path="C:\\Users\\Emperador\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
    navegador.maximize_window()
    navegador.get('https://www.google.com/')
    findElem = navegador.find_element_by_name('q')
    findElem.send_keys(something)
    findElem.send_keys(Keys.RETURN)