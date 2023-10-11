"""
Created by: sophie
Created on: Oct 2023
This module is a Micro:bit MicroPython program does rock paper scissors
"""

from microbit import *

display.clear
display.show(Image.Heart)

random_number = 0
score = 0

while True:
    if button_a.is_pressed():
        score = score + 1

    if button_b.is_pressed() :
        display.scroll(str(score))
