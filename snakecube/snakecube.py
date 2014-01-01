#!/usr/bin/env python

'''Snake Cube Puzzle Solver

   Using GamePlayer
'''

import sys
import os

# Add parent directory to PYTHONPATH
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir) 

from gameplayer import GamePlayer
from action import Action
from state import State

# Main:

initState = State.getInitState()
"""
gamePlayer = GamePlayer(Action, State)
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
"""
