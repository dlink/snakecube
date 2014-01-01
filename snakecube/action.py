class Action(object):

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

