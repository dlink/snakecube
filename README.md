GamePlayer implements a TreeSearch to solve Games.

#### Example:

    from gameplayer import GamePlayer
    
    class State():
        ...
    class Action():
        ...
    
    initState = State.getInitState()
    gamePlayer = GamePlayer(Action, State)
    result = gamePlayer.treeSearch(initState)
    
    # Some comments:
    print "Iterations Checked:", gamePlayer.iterations
    print "Solution Path:", result
    print "Num of moves needed:", len(result)
    
    # Play solution
    gamePlayer.play(initState, result)

#### The State Abstract Class:

This class implements the state and the problem domain.

    class State(object):
  
        def __init__(self):
            # record paths thru solution
            self.paths = []
            ...
    
        def equals(self, state2):
            '''Return true if this state is equal to that state'''
           ...
    
        def display(self):
            '''Output display of state'''
            ...
    
        @classmethod
        def next_state(self, frontier):
            '''Return the a state from a LIST of states
               Using algorithm Based on SEARCH_TYPE
          '''
    
        @classmethod
        def getInitState(self):
           ...
    
        @classmethod
        def getGoalState(self):
           ...

#### The Action Abstract Class:

    class Action(object)
  
        def doAction(self, state):
            '''Given a state perform action on that state
               Return the new state
            '''
            ...
    
        @classmethod
        def getPossibleActions(self, state):
            '''Given a state
               Return a LIST of possible actions from that state
            '''
            ...
  
