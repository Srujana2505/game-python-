#!/usr/bin/env python3
import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

#computer moves
comp_move = random.choice(moves)

#user moves
user_move = input("Enter your move: ")

win_moves = {
	'rock' : ['scissors', 'lizard'],
	'scissors' : ['paper', 'lizard'],
	'paper' : ['rock', 'spock'],
	'lizard' : ['spock', 'paper'],
	'spock' : ['scissors', 'rock']
}

def logic(user_move):
	defeat_moves = win_moves[user_move]
	return defeat_moves

if user_move == comp_move:
	print("It is a tie!")
elif comp_move in logic(user_move):
	print("You won!")
else:
	print("computer won!")
