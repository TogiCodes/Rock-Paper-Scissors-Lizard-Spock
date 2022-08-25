import os
import sys
import time
from ai import AI
from game import Game

os.system("cls")

moves = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

ai = AI()
game = Game()

print("Welcome to Rock Paper Scissors Lizard and Spock created by Sheldon Cooper")
time.sleep(.3)

with open('rules.txt', 'r') as file:
    rules = file.read() 
    print(f'Rules: \n{rules}')
    print('\n')



time.sleep(1)


def make_move():
    selected_move = input("What is your move (rock, paper, scissors, lizard, spock): ").title()
    if selected_move not in moves:
        print("Invalid Move")
        time.sleep(.3)
        return make_move()
    else:
        return selected_move


def gameloop():


    player_move = make_move()
    print("You:", player_move)

    ai_move = ai.make_move(moves)
    print("AI:", ai_move)
    winner = game.selected_winner(player_move, ai_move)

    wins = [line.rstrip() for line in open('rules.txt')]

    if winner != 0:
        explanation = [sentence for sentence in wins if player_move in sentence and ai_move in sentence][0]
        print(explanation)
    else:
        should_play = print("Tie, would you like to play again (yes or no): ")
        if should_play != 'yes':
            sys.exit()
        gameloop()
    if winner == 1:
        print('You Won!') 
    elif winner == -1:
        print("You lost!")

gameloop()
        



