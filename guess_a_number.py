import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number between 1 and 100: ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        print("You guess it!")
        break
    elif player_number > 100:
        print("Invalid input. Try again...")
    elif player_number > computer_number:
        print("Your number is too high! Guess again..")
    elif player_number < computer_number:
        print("Your number is too low. Guess again...")
