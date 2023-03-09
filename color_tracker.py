#!/usr/bin/python3.11

import pyautogui
while True:
  x, y = pyautogui.position()
  px = pyautogui.pixel(x, y)
  print(px)

