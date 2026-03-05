import pyautogui
import time
import pandas as pd

pd.read_csv('menu.csv')


pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.click(624,47)
time.sleep(1)
pyautogui.write('youtube.com')
time.sleep(1)
pyautogui.press('enter')
