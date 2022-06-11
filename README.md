# slide

A slide-based audio game in python.

## What is this?

Slide is a slide puzzle. Your goal is to move numbers around on a grid to get them in correct order. This version might work a little different than other games, but the idea remains the same.
When starting the game, you start at the bottom left corner of the grid. When ending the game, the empty space should be at the top right of the grid with all rows in order.

### How do I win the game?

You need to move the numbers around. But the trick is that you can only move a number to the right, left, up or down. You can only move the number if there is an empty space to the left, right, above or below the current number. I hope it makes sence.

## Controlls

- Up, Down, Left and right arrows: move on the grid.
- Q: quit the game.
  \*W, A, S and D: moves the number up, left, down or right if possible and replaces current square with a blank tile.

## How do I run the game?

In order to run the game, you need python installed, I use version 3.9.7. Then you can just do pip install cytolk and pip install pygame and do python main.py
