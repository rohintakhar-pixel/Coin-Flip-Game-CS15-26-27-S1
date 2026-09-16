import random

print(" Welcome to the Coin Flip Game!")
print("You start with 10 points.")
print("Try to earn as many points as you can!\n")

points = 10

while points > 0:

    guess = input("Guess Heads or Tails (H/T): ").strip().lower()
    while guess not in ["h", "t", "heads", "tails"]:
        print("Invalid input. Please enter H or T.")
        guess = input("Guess Heads or Tails (H/T): ").strip().lower()


    if guess in ["h", "heads"]:
        guess = "Heads"
    else:
        guess = "Tails"


    print(f"You currently have {points} points.")
    wager = input("How many points do you want to wager? ")


    while not wager.isdigit() or int(wager) < 1 or int(wager) > points:
        print("Invalid wager. You must enter a number between 1 and your current points.")
        wager = input("How many points do you want to wager? ")

    wager = int(wager)


    flip = random.choice(["Heads", "Tails"])
    print(f"The coin landed on: {flip}")


    if guess == flip:
        points += wager
        print(f" Correct! You win {wager} points.")
    else:
        points -= wager
        print(f" Incorrect. You lose {wager} points.")

    print(f"Current points: {points}\n")
    print("-" * 30)

print("Game over! You ran out of points.")
