#!/usr/bin/env python

import sys

SEARCH_TYPE = 'breath-first'
#SEARCH_TYPE = 'depth-first'
#SEARCH_TYPE = 'A*' # with a poor heuristic

class GamePlayer(object):
    '''Preside over the game'''

    def __init__(self, Action, goalState):
        self.Action = Action
        self.goalState = goalState
        self.iterations = 0

    def isGoal(self, state):
        '''Return true if the game is solved'''
        if state.equals(self.goalState):
            return True
        return False

    def getPossibleActions(self, state):
        '''Given a state
           Return a LIST of possible actions from that state
        '''
        actions = []
        for i, post in enumerate(state.posts):
            if i == 0:
                opost1 = state.posts[1]
                opost2 = state.posts[2]
            elif i == 1:
                opost1 = state.posts[0]
                opost2 = state.posts[2]
            else:
                opost1 = state.posts[0]
                opost2 = state.posts[1]
            if post.hasDisks:
                if not opost1.hasDisks or post.topDisk < opost1.topDisk:
                    actions.append(self.Action(post.topDisk, post.num, 
                                               opost1.num))
                if not opost2.hasDisks or post.topDisk < opost2.topDisk:
                    actions.append(self.Action(post.topDisk, post.num, 
                                               opost2.num))
        return actions

    def getFrontier(self, state):
        '''Given a state, perform all possible actions
           Return a LIST of all resulting stages
        '''
        frontier = []
        for action in self.getPossibleActions(state):
            newState = action.doAction(state)
            frontier.append(newState)
        return frontier
            
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
        frontier = self.getFrontier(state)
        explored = [state]
        goal_states = []
        done = 0

        while not done:
            if not frontier:
                return "Failed"
            state = self.remove_choice(frontier)
            explored.append(state)
            self.iterations += 1
            if self.isGoal(state):
                return state.paths
            for action in self.getPossibleActions(state):
                newState = action.doAction(state)
                if self.stateIn(newState, frontier):
                    continue
                if self.stateIn(newState, explored):
                    continue
                frontier.append(newState)
                
    def remove_choice(self, frontier):
        '''Return the a state from frontier
           Using algorithm Based on SEARCH_TYPE
        '''
        if SEARCH_TYPE == 'breath-first':
            state = frontier.pop(0)
        elif SEARCH_TYPE == 'depth-first':
            state = frontier.pop()
        elif SEARCH_TYPE == 'A*':
            # get lowest total cost:
            states_by_cost = defaultdict(lambda:[])
            for s in frontier:
                total_cost = len(s.paths)
                states_by_cost[total_cost].append(s)
            min_total_cost = min(states_by_cost.keys())
            
            # Heuristic: lest amount of disks on post 1
            states_by_heuristic = defaultdict(lambda:[])
            for s in states_by_cost[min_total_cost]:
                h = len(s.posts[0].disks)
                states_by_heuristic[h].append(s)
            min_h = min(states_by_heuristic.keys())
            
            # choose a state with least cost and least h and remove from f
            state = states_by_heuristic[min_h].pop(0)
            for i, s in enumerate(frontier):
                if state.equals(s):
                    del frontier[i]
                    break
        else:
            print 'unrecognized SEARCH_TYPE: %s' % SEARCH_TYPE
        return state

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
