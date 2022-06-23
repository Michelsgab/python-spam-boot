from bs4 import BeautifulSoup
import requests
import pyautogui
import time


def bot_spam(url, tag):
    time.sleep(5)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    html = parse.find_all(tag)


    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press('enter')


bot_spam('https://pdfcoffee.com/shrek-roteiro-4-pdf-free.html', 'p')