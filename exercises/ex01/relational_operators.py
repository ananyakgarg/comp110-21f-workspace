"""Prints the boolean value of the relationship operators between two inputs."""
__author__ = "730475029"
a: int = int(input("Left Hand Side: "))
b: int = int(input("Right Hand Side: "))
print(str(a) + " < " + str(b) + " is " + str(bool(a < b)))
print(str(a) + " >= " + str(b) + " is " + str(bool(a >= b)))
print(str(a) + " == " + str(b) + " is " + str(bool(a == b)))
print(str(a) + " != " + str(b) + " is " + str(bool(a != b)))
