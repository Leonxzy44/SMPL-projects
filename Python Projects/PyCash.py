# Config

import time 

import random 

import winsound

import math

for x in range(2): 

    winsound.Beep(1000, 500)

    time.sleep(0.1)

# Program starts here

print("Welcome to PyCash! This is a simple program to simulate a cash register. ")

start = int(input("Press any key to start . . . "))

product = int(input("Enter amount of products: "))

for x in range(product) :

    price = float(input("Enter price of product " + str(x + 1) + ": "))

    quantity = int(input("Enter quantity of product " + str(x + 1) + ": "))

    total = price * quantity


    print("Total for product " + str(x + 1) + ": $" + str(total))

    if total > 1000:
        print("Warning: Total for product " + str(x + 1) + " exceeds $1000!")
    if total < 0:
        print("Warning: Total for product " + str(x + 1) + " is negative!")
    if total == 0:
        print("Warning: Total for product " + str(x + 1) + " is zero!")
    if total < 10:
        print("Warning: Total for product " + str(x + 1) + " is less than $10!")
    if total > 10000:
        print("Warning: Total for product " + str(x + 1) + " exceeds $10000!")






 
