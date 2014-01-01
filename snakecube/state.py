class State(object):

    def __init__(self, blocks):
        self.blocks = blocks
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
       return State([])

    @classmethod
    def getGoalState(self):
       ...

class Block(object):
    pass

class GameSpace(object):
    def __init__(self):
        space = \
            [[
                [ 
                        [None, None, None],
                        [None, None, None],
                        [None, None, None]
                        ]
