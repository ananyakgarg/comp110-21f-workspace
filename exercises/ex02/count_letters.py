"""Counting letters in a string."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

searchLetter: str = input("What letter do you want to search for: ")
word: str = input("Enter a word: ")
i: int = 0
occurrenceCount: int = 0
lengthWord: int = len(word)
while i < lengthWord:
    if searchLetter in word:
        occurrenceCount += 1
    i += 1
    word = word[i:lengthWord]
if occurrenceCount > 0:
    print("Count: " + str(occurrenceCount))
else:
    print("Count: 0")
