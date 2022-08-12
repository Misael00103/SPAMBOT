import pyautogui
import webbrowser as web
from time import sleep

web.open('https://web.whatsapp.com/send?phone=8298744467')
sleep(10)

with open('spam.txt', 'r') as file:
      for line in file:
        pyautogui.typewrite(line)
        pyautogui.press('enter')