import pyautogui as gui
import time
import os
import sys

os.system('title Made By Hesam ;)')
os.system('cls')

def timer():
    left = 5
    for i in range(5):
        os.system("cls")
        print(f"{left}...")
        left -= 1
        time.sleep(1)


def startm(speed):
    timer()
    for i in range(500 ** 999):
        gui.click()
        time.sleep(speed)


def startk(speed, key):
    timer()
    for i in range(500 ** 999):
        gui.keyDown(key)
        time.sleep(speed)


m = int(input("Mouse | Keyboard (1,2) --> "))
s = int(input("At What Speed --> "))

if m == 1:
    os.system("cls")
    startm(s)

elif m == 2:
    os.system("cls")
    k = str(input("What Key Do You Want To Press --> "))
    startk(s, k)
else:

    os.system("cls")
    print("invalid Choices!\n\n")
    time.sleep(1)
    sys.exit()