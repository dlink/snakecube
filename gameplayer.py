#!/usr/bin/env python

import sys

DEBUG = 1

class GamePlayer(object):
    '''Preside over the game'''

    def __init__(self, Action, State):
        self.Action = Action
        self.State  = State
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
        #if DEBUG:
        #    self.displayFrontier(frontier)

        # init explored
        explored = [state]

        # iterate
        # For each state in frontier
        #   check if it is the Goal State
        #   if not add all new possible states to frontier
        done = 0
        while not done:
            if not frontier:
                return "Failed"

            # get next state
            #self.displayFrontier(frontier)
            state = self.State.next_state(frontier)
            print 'state:', state
            #print 'hit any key',
            #yn = sys.stdin.readline()
            print
            explored.append(state)
            self.iterations += 1
            if self.State.isGoalState(state):
                return state.paths

            # update frontier
            for action in self.Action.getPossibleActions(state):
                newState = action.doAction(state)
                if self.stateIn(newState, frontier):
                    continue
                if self.stateIn(newState, explored):
                    continue
                frontier.append(newState)
            #if DEBUG:
            #    self.displayFrontier(frontier)

    def displayFrontier(self, frontier):
        print 'frontier:\n  ',
        print '\n   '.join(map(str, frontier))
        print
        #print 'hit any key',
        #yn = sys.stdin.readline()
        #print

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
