import random


def main():
    roll_dice()
    play_again()


def roll_dice():
    '''Generates a random number between 1 and 6
    and prints it to the screen'''
    dice_roll = (random.randint(1, 6))
    print(dice_roll)


def play_again():
    '''Asks the user if you want to play again
    if the user responds with Yes or Y (case insensitive), 
    it replays the game. For all other responses, game ends'''
    your_input = input("Do you want to play again? ").upper()
    if your_input == "YES" or your_input == "Y":
        main()

    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
