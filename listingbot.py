from threading import main_thread
import time
from tkinter import mainloop
import keyboard
from pyautogui import click, displayMousePosition, typewrite



bedrag = input("Sell value (0.25) example)").lower()

start = input("Wil je de bot starten? y/n:").lower()
if start == "y":
    main_thread()
else:
    exit()
    

def main():
   
##begin click en remove en add waarde

        time.sleep(10)
        click(750, 892)
        time.sleep(1)
        keyboard.press_and_release('backspace')
        time.sleep(1)
        keyboard.press_and_release('5')

        ##begin akkoord
        time.sleep(1)
        click(1600, 825)

        ##begin metamask click
        time.sleep(6)
        click(1875, 814)
        time.sleep(1)
        click(1767, 917)

        time.sleep(6)
        click(1875, 814)
        time.sleep(1)
        click(1767, 917)

        time.sleep(6)
        click(1875, 814)
        time.sleep(1)
        click(1767, 917)

        time.sleep(6)
        click(1875, 814)
        time.sleep(1)
        click(1767, 917)

        time.sleep(6)
        click(1875, 814)
        time.sleep(1)
        click(1767, 917)

        time.sleep(50)

        
for i in range(999):
    main()
