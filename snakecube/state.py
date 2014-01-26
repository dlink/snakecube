#from vlib.utils import echoized

from structure import Structure, NUM_BLOCKS

class State(object):

    structure = Structure()

    def __init__(self):
        self.paths = []  # set of actions

    @classmethod
    def next_state(cls, frontier):
        '''Return the a state from a LIST of states
           Using algorithm Based on SEARCH_TYPE
        '''
        return frontier.pop(0)

    @classmethod
    def getInitState(cls):
       return State()

    @classmethod
    def isGoalState(cls, state):
        if len(state.paths) == NUM_BLOCKS:
            return True
        return False

    def __repr__(self):
        return 'paths: %s' % self.paths

    def display(self):
        '''Output display of state'''
        return str(self.paths)

    def equals(self, state2):
        '''Return true if this state is equal to that state'''

        paths  = self.paths
        paths2 = state2.paths

        if len(paths) != len(paths2):
            return False

        for i, path in enumerate(paths):
            if path != paths2[i]:
                return False
        return True

