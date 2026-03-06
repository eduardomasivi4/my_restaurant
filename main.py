import pyautogui
import time
import pandas as pd

tabela = pd.read_csv('menu.csv')

pyautogui.hotkey('alt', 'tab')
time.sleep(2)

# colunas cuisine,price
for linha in tabela.index:
    pyautogui.click(x=465,y=323)
    time.sleep(0.5)

    cuisine = str(tabela.loc[linha, 'cuisine'])
    pyautogui.write(cuisine)
    
    time.sleep(0.5)
    pyautogui.click(x=373, y=569)

    time.sleep(0.5)
    price = str(tabela.loc[linha, 'price'])
    pyautogui.write(price)
    
    pyautogui.click(x=287, y=652)

    if linha == 14:
        break