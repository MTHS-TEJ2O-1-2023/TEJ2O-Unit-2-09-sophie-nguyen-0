"""
Created by: sophie
Created on: Oct 2023
This module is a Micro:bit MicroPython program does rock paper scissors
"""

from microbit import *
from random import *

display.clear
display.show(Image.Heart)

random_number = 0
score = 0
scissor = Image("77007:77070:00700:77070:77007")
rock = Image("00000:07770:07770:07770:00000")
paper = Image("77777:70007:70007:70007:77777")

while True:
    if button_a.is_pressed():
        score = score + 1
        display.show(Image.YES)
        sleep(2000)
        display.show(Image.HEART)


    if button_b.is_pressed():
        display.scroll(str(score))

    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.clear()
        random_number = randint(1, 3)

        # random_number == 1
        if random_number == 1:
            display.show(scissor)
            sleep(5000)

            # random_number == 2
        if random_number == 2:
            display.show(rock)
            sleep(5000)

            # random_number == 3
        if random_number == 3:
            display.show(paper)
            sleep(5000)

            display.show(Image.HEART)
