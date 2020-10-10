from copy import deepcopy

class Action(object):
    def __init__(self)
        pass
        
    def __repr__(self):
        return self
    
    @classmethod
    def getPossibleActions(self, state):
        '''Given a state
           Return a LIST of possible actions from that state
        '''
        return None

    def doAction(self, state):
        '''Given a state perform action on that state
           Return the new state
        '''
        pass
