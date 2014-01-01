#!/usr/bin/env python

import sys

class GamePlayer(object):
    '''Preside over the game'''

    def __init__(self, Action, State):
        self.Action = Action
        self.State  = State
        self.goalState = State.getGoalState()
        self.iterations = 0

    def isGoal(self, state):
        '''Return true if the game is solved'''
        if state.equals(self.goalState):
            return True
        return False

    def stateIn(self, state, state_list):
        '''Given a state, and a LIST of states
           Return True if state is in that list
        '''
        for s in state_list:
            if state.equals(s):
                return True
        return False

    def treeSearch(self, state):
        '''Implements a Tree Search Algorithm to solve the Game

           Starts with a Initial State.
           Maintain two LISTs:  frontier, and explored

           Iterates thru all possible states taken from frontier and
           added to explored.  Then determine new frontier.  Until
           solved or fails.
        '''
        
        # init frontier:
        frontier = []
        for action in self.Action.getPossibleActions(state):
            newState = action.doAction(state)
            frontier.append(newState)

        # init explored
        explored = [state]
            
        # iterate
        done = 0
        while not done:
            if not frontier:
                return "Failed"

            # get next state
            state = self.State.next_state(frontier)
            explored.append(state)
            self.iterations += 1
            if self.isGoal(state):
                return state.paths

            # update frontier
            for action in self.Action.getPossibleActions(state):
                newState = action.doAction(state)
                if self.stateIn(newState, frontier):
                    continue
                if self.stateIn(newState, explored):
                    continue
                frontier.append(newState)
                
    def play(self,state, paths):
        '''Play the game, and solve the Puzzle'''

        print "Initial State:"
        state.display()
        i = 0
        for p in paths:
            yn = sys.stdin.readline()
            state = p.doAction(state)
            i += 1
            print "Move", i
            state.display()

'''
# Main:

initState = State([Post([D4, D3, D2, D1]), Post(), Post()])
game = Game()
result = game.treeSearch(initState)

# Somme comments:
print "Search type:", SEARCH_TYPE
print "Iterations Checked:", game.iterations
print "Solution Path:", result
print "Num of moves needed:", len(result)
print "Hit Enter to see it played out."
yn = sys.stdin.readline()

# Play solution
game.play(initState, result)
'''
