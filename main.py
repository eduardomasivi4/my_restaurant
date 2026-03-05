import pyautogui
import time
import pandas as pd

toda_tabela = pd.read_csv('menu.csv')
tabela = toda_tabela[['cuisine', 'price']]

print(tabela)

time.sleep(3)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

pyautogui.hotkey('ctrl','t')
time.sleep(1)

pyautogui.click(539,57)
time.sleep(1)

pyautogui.write('127.0.0.1:8000/admin/')

time.sleep(1)

pyautogui.press('enter')