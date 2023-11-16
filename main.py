# This program for playing the dice game
# import random module
# import numpy module
import random
import numpy as np

# Constants for the minimum and maximum random numbers
MAX = 6
MIN = 2
k = 1
again_dice = 0  # create a variable to control the loop


# create def function
def main():
    dice_welcome()
    dice_rules()

    # calculate play again and Exit
    play_dice = True
    while play_dice:
        get_score()

        again_dice = input('Do you want to play again? (y/n): ')
        # if the user wants to do another one
        if again_dice == 'n':
            print('goodbye')
            play_dice = False
        else:
            k += 5  # Increase the round counter for the next game


# create dice processing function
def get_score():
    players = int(input('how many players are there(1..4): '))
    array = np.zeros(players, dtype=int)  # initialize numpy array with zeros

    for r in range(5):  # create for loop each player playing five rounds
        print('round ', str(k + r))
        # create while loop generate players
        i = 1
        while i <= players:
            dice_val = random.randint(MIN, MAX)  # generate random values assigned to 'dice_val' variable
            array[i - 1] = array[i - 1] + dice_val  # 'dice_val' variable values add array elements
            print('Rolling dice for player', i, ':', (dice_val))  # print player roll dice values
            i = i + 1

        print('Round Scores:', array)

    # find winner
    winner = np.argmax(array) + 1  # find the index of the maximum score
    print('Final Scores:', array)
    print("The winner is player", winner)


# print dice game login
def dice_welcome():
    print('################WELCOME################ \n\t'
          '        NASTY DICE GAME!              ')


# print dice game rules
def dice_rules():
    print('* Each player rolls five dice ')
    print('* Each player gets the sum  ')
    print('  the highest score wins')
    print('* player wants to play again or ')
    print('  Exit game put it (y/n)')


main()
