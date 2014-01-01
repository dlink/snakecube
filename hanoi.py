#!/usr/bin/env python

import sys

'''Tower of Hanoi Puzzle Solver

   Using GamePlayer
'''

from gameplayer import GamePlayer
from action import Action
from state import State, initState, goalState

# Main:

gamePlayer = GamePlayer(Action, goalState)
result = gamePlayer.treeSearch(initState)

# Somme comments:
#print "Search type:", SEARCH_TYPE
print "Iterations Checked:", gamePlayer.iterations
print "Solution Path:", result
print "Num of moves needed:", len(result)
print "Hit Enter to see it played out."
yn = sys.stdin.readline()

# Play solution
gamePlayer.play(initState, result)
