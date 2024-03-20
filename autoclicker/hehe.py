import pyautogui as gui
import keyboard
import winsound
import time
import os
            
def timer():
    for i in range(1,6):
        os.system("cls")
        print(f'{i}/5')
        time.sleep(1)

def startm(speed):
    timer()
    for i in range(500 ** 999):
        gui.click()
        time.sleep(speed/10)
        check()

def startk(speed, key):
    timer()
    for i in range(500 ** 999):
        gui.keyDown(key)
        time.sleep(speed/10)
        check()
        

def select():
    global m
    global s
    m = int(input("Mouse | Keyboard (1,2) --> "))
    s = int(input("At What Speed (Ms) --> "))

def check():
    global m
    global s
    if keyboard.is_pressed('ctrl+l'):
            m = 0
            s = 0
            os.system('cls')
            select()
            return

def start():
    while m == 1 or 2:
      if m == 1:
          os.system("cls")
          startm(s)
      elif m == 2:
          os.system("cls")
          k = str(input("What Key Do You Want To Press --> "))
          startk(s, k)
      else:
          print
          os.system("cls")
          print("invalid Choices!\n\n")
          winsound.MessageBeep()
          check()
          