"""Repeating a beat in a loop."""

__author__ = "730475029"


beat: str = input("What beat do you want to repeat?")
count: int = int(input("How many times do you want to repeat it?"))
repeat_beat: str = ""
if count <= 0:
    print("No beat...")
i = 0
while i < count:
    if i < count - 1:
        repeat_beat += beat + " "
    else:
        repeat_beat += beat
    i += 1
print(repeat_beat)