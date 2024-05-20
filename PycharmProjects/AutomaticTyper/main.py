import pyautogui
import time

while True:
    time.sleep(5)
    pyautogui.typewrite('Enter Text.')
    time.sleep(2)
    pyautogui.press('enter')