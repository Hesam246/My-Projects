import keyboard
import winsound
import mouse
import time
import sys
import os

mode = input('Right | Left (1,2) -> ')
os.system('cls')
print('Press Ctrl + L to exit')
# Ammount of boost:
boost = 2
delay = 0.1

def Right(boost, delay):
  while mouse.is_pressed('right'):
      for i in range(boost):
        mouse.click('right')
        time.sleep(delay)

def Left(boost, delay):
  while mouse.is_pressed('left'):
      for i in range(boost):
        mouse.click('left')
        time.sleep(delay)

while True:
  if mode == '1':
    Right(boost, delay)
  elif mode == '2':
    Left(boost, delay)
  if keyboard.is_pressed('ctrl+l'):
    os.system('cls')
    winsound.MessageBeep()
    sys.exit()
    os.kill()