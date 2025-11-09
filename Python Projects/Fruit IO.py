import time 

import random 

import math

import winsound

for z in range(2): 

    winsound.Beep(1000, 500)

    time.sleep(0.1)

welcome = input("Welcome to Fruit IO!  Press 1 + 'Enter' to start . . . ")

time.sleep(0.5)

print("Loading . . . ")

time.sleep(2)


print("Fruit IO is a game made for guessing fruit order. The fruits are: 🍎🍊🍋 | Let's start! ")

time.sleep(0.5)

fruits = ["🍎", "🍊", "🍋"]



apple = 1 

orange = 2

lemon = 3

first_frut = random.randint(0, 4)

second_frut = random.randint(0, 4)

third_frut = random.randint(0, 4)


all_together = [first_frut, second_frut, third_frut]



tries = 3 

guess = int(input("Guess the order of the fruits (1 for apple, 2 for orange, 3 for lemon) | (Notice: write all numbers together): "))

if guess == all_together: 

    print("You guessed it right! Well done! ")

else: 
   

   print("Wrong guess! Try again! The order was:  ", all_together )

   


if tries == 0:
   
   print("You have ran out of tries! The correct order was: ", all_together)





