# CODE FOR STONE PAPER SCISSOR GAME

import random

def game():
    compList = ['stone','paper','scissor']
    compTurn = random.choice(compList)
    yourTurn = input("Enter your turn, (Press for st for stone, p for paper, sc for scissors, q to quit game): ")

    if yourTurn == 'st' and compTurn == 'stone':
        print("Tie") 
    elif yourTurn == 'st' and compTurn == 'paper':
        print("You loose")
    elif yourTurn == 'st' and compTurn == 'scissor':
        print("You won")
    elif yourTurn == 'p' and compTurn == 'stone':
        print("You won")
    elif yourTurn == 'p' and compTurn == 'paper':
        print("Tie")
    elif yourTurn == 'p' and compTurn == 'scissor':
        print("You loose")
    elif yourTurn == 'sc' and compTurn == 'stone':
        print("You loose")
    elif yourTurn == 'sc' and compTurn == 'paper':
        print("You won")
    elif yourTurn == 'sc' and compTurn == 'scissor':
        print("Tie")
    elif yourTurn == 'q':
        quit()

    print(f"Computer choose {compTurn}")

if __name__=="__main__":
    while True:
        game()