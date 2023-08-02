# https://api.whatsapp.com/send?phone={telefone}

import webbrowser
import pyautogui
from time import sleep

telefones = []

with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(15)

    pyautogui.click(2994,200, duration=2)
    sleep(10)

    pyautogui.click(3004,955, duration=2)
    sleep(2)
    pyautogui.typewrite('ola')

    sleep(5)
    pyautogui.press('enter')
    sleep(300)