#!/usr/bin/env python
"""Snake Game"""
#Written by Sam Scott on 22-02-2016
#Ported from C++
__author__ = "Sam Scott"
__version__ = "1.0"
__email__ = "samueltscott@gmail.com"

#More information is in the readme.txt file

import time, os, random, msvcrt
game_over = False
width = 20
height = 20
score = 0
n_tail = 0
tail_y = []
tail_x = []
fruit_y = random.randrange(height)
fruit_x = random.randrange(width)
dir_ = "STOP" # direction of snake
for x in range(1000): # fill the arrays with placeholder values because c++
    tail_y.append(0)
    tail_x.append(0)


def setup():
    global x, y, game_over, key
    key = ""
    game_over = False
    x = width / 2
    y = height / 2

def draw():
    os.system("cls") # clear screen
    for i in range(width+2):
        print("#", end = "") # print the top border
    print()
    for i in range(height): # i = y
        for j in range(width): # j = x
            if j == 0: 
                print("#", end = "") # print the left wall
            if i == y and j == x:
                print("O", end = "") # print the head
            elif i == fruit_y and j == fruit_x:
                print("@", end = "") # print the fruit
            else:
                print_bool = False 
                for k in range(n_tail):
                    if tail_x[k] == j and tail_y[k] == i:
                        print("o", end = "") # print the tail
                        print_bool = True
                if not print_bool:
                    print(" ", end = "") # print the empty space
            if j == width-1:
                print("#", end = "") # print the right wall
        print()
    for i in range(width + 2):
        print("#", end = "") # print the bottom border
    print()
    print("X: " + str(x) + "\nY: " + str(y)) # print the current values of x and y for debugging purposes
    print("Score: " + str(score)) # print the score
    
def get_input():
    global game_over, dir_, c
    global x, y, n_tail, fruit_x, fruit_y, key
    if msvcrt.kbhit(): # if a key is pressed
        c = msvcrt.getch() # get the key as bytes data
        key = c.decode("utf-8").lower() # decode it and format lowercase
    print("[" + key + "]")
    if key == "w": # do stuff
        dir_ = "UP"
    elif key == "a":
        dir_ = "LEFT"
    elif key == "s":
        dir_ = "DOWN"
    elif key == "d":
        dir_ = "RIGHT"
    elif key == "x":
        game_over = True

def logic():
    global x, y, n_tail, fruit_x, fruit_y, score, game_over
    prev_x = tail_x[0]
    prev_y = tail_y[0]
    tail_x[0] = x
    tail_y[0] = y # hissssssssss
    for i in range(1, n_tail):
        prev2_x = tail_x[i]
        prev2_y = tail_y[i]
        tail_x[i] = prev_x
        tail_y[i] = prev_y
        prev_x = prev2_x
        prev_y = prev2_y

    if dir_ == "UP":
        y -= 1 # up is down because computers
    elif dir_ == "LEFT":
        x -= 1
    elif dir_ == "DOWN":
        y += 1
    elif dir_ == "RIGHT":
        x += 1
    else:
        pass
        
    if x >= width: # controls movement of snake from one side of the screen to the opposite side
        x = 0
    elif x < 0:
        x = width - 1
    if y >= height:
        y = 0
    elif y < 0:
        y = height - 1

    for i in range(n_tail):
        if tail_x[i] == x and tail_y[i] == y: # if head touches tail
            game_over = True

    if x == fruit_x and y == fruit_y: # if head touches fruit
        score += 10 # increment score
        fruit_x = random.randrange(width) # place the fruit somewhere else
        fruit_y = random.randrange(height)
        n_tail += 1 # add a new tail segment

def main():
    global dir_, c # c is the raw bytes data from msvcrt.getch()
    setup() # initialises important variables
    while not game_over: # this is the main game loop
        try:
            draw() # draws the map
            get_input() # checks to see if a key is pressed
            logic() # controls game systems
            time.sleep(0.1) # controls game speed
        except Exception as e:
            print("\n\n[ERROR]", e)
            if "utf-8" in str(e):
                print("[INFO] This basically means that you pressed a key that Python doesn't like. So don't do it again.")
                print("[INFO] If you're trying to move, use WASD.")
                print("[RUNTIME INFO] msvcrt.getch() call returned: " + str(c)) # c is bytes data
            print("\nPress enter to continue . . . ")
            input()
    print("Game Over!")
    os.system("pause")

if __name__ == "__main__": # allows the program to be imported as a module without it causing problems
    main()
    
