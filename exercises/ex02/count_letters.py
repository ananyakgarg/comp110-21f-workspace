"""Counting letters in a string."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

searchLetter: str = input("What letter do you want to search for: ")
word: str = input("Enter a word: ")
i: int = 0
occurrence: int = 0
while occurrence < len(word):
    if searchLetter == word[occurrence]:
        i += 1
        occurrence += 1
    else:
        occurrence += 1
print("Count: " + str(i))
