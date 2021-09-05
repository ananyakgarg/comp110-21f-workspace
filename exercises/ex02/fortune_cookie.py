"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730475029" 
from random import randint
print("Your fortune cookie says...")
x: int = (randint(1, 4))
if x == 1:
    print("You will be very successful.")
else:
    if x == 2:
        print("Your business endeavors will prosper.")
    else:
        if x == 3:
            print("You will live a happy life.")
        else:

            if x == 4:
                print("You will make a lot of money.")
print("Now, go spread positive vibes!")