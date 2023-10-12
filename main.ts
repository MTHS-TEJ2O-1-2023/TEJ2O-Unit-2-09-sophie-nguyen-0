/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: sophie
 * Created on: Oct 2023
 * This program does rock paper scissors
*/

// variables
let randomNumber: number = 0
let score: number = 0

basic.clearScreen()
basic.showIcon(IconNames.Heart)

input.onGesture(Gesture.Shake, function () {
  randomNumber = randint(1, 3)
  basic.clearScreen()

  // randomNumber is 1
  if (randomNumber === 1) {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
    `)
  }
  // randomNumber is 2
  if (randomNumber === 2) {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
    `)
  }
  // randomNumber is 3
  if (randomNumber === 3) {
    basic.showIcon(IconNames.Scissors)
  }
  basic.pause(3000)
  basic.showIcon(IconNames.Heart)
})

input.onButtonPressed(Button.A, function () {
  score = score + 1
  basic.showIcon(IconNames.Yes)
  basic.pause(3000)
  basic.showIcon(IconNames.Heart)
})

input.onButtonPressed(Button.B, function () {
  basic.clearScreen()
  basic.showString('Score: ' + score.toString())
})
