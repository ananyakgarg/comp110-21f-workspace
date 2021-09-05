"""Counting letters in a string."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

searchLetter: str = input("What letter do you want to search for: ")
word: str = input("Enter a word: ")
i: int = 0
if searchLetter in word:
    i += 1
    print("Count: " + str(i))
else:
    if searchLetter not in word:
        print("Count: 0")
