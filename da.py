from time import sleep
import pyautogui as pag


while True:
    pag.click(x=625, y=448)
    sleep(7)
    pag.hotkey('ctrl', 'w')
    sleep(0.5)
    pag.hotkey('ctrl', 'r')
    sleep(1)
