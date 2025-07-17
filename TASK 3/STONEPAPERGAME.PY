import random

print("Stone, Paper, Scissors Game!")
print("Type stone, paper, or scissors. Type quit to stop.\n")

while True:
    user = input("Your choice: ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in ["stone", "paper", "scissors"]:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(["stone", "paper", "scissors"])
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!\n")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You win!\n")
    else:
        print("Computer wins!\n")
