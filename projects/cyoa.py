"""Fun, interactive python experience."""

__author__ = "730475029"  
import random
points: int = 0
player: str
WINKING_FACE: str = "\U0001F601"


def main() -> None:
    """Initializes program."""
    global points
    greet()
    while True:
        decision: int = int(input("Press 1 to tell us your age and earn points. Press 2 to play a number guessing game. Press 3 to end."))
        if decision == 1:
            name_game()
        if decision == 2:
            points = number_game(points) 
        if decision == 3:
            print("Thanks for playing, see you next time!")


def greet() -> None:
    """Greets the player."""
    global player
    print("Welcome to the game!")
    player = input("What is your name? ")
    return None


def name_game() -> None:
    """Gives points for entering your age. Your age becomes the points you receive."""
    global points
    while points < 100: 
        age: int = int(input("What is your age? "))
        print(f"Wow!, you don't look {age} at all! Just for that, you get {age} points! Plus check out this cool emoji: {WINKING_FACE}")
        points += age
        print(f"Wow!, you now have {points} points.")
    if points > 100:
        print("You have more than 100 points, congrats! Choose a new game play or play this game again!")
    

def number_game(sum_points: int) -> int:
    """A simple number guessing game."""
    global player
    print(f"Hey, {player}, welcome to the number guessing game. You have 10 tries to guess as many numbers as you can between 1-10. Every time you guess correctly, you get a point!")
    num: int = random.randint(1, 10)
    tries: int = 0
    while tries < 10:
        guess: int = int(input("Guess the number. ")) 
        tries += 1
        if guess > num:
            print("No that guess is too high, try again.") 
        if guess < num:
            print("No that guess is too low, try again. ")
        if guess == num:
            print(f"Correct! Good job. The number was {num} and you got it in {tries} tries.")
            sum_points += 1
    print(f"You finished the game with {sum_points} points. Good job!")
    return sum_points


if __name__ == "__main__":
    main()