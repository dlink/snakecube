from copy import deepcopy

from structure import Structure

class Action(object):
    '''Preside of Game Actions

       An action consists of Adding a block to an existing String of
       Blocks (as defined by the state), and rotating the block.

       Rotations: 0 - no rotation
                  1 - 90% clock-wise
                  2 - 180%
                  3 - 270% clock-wise
    '''

    def __init__(self, block, rotation=0):
        '''An action constists of a new block to add,
           And a rotation component
        '''
        self.block = block
        self.rotation = 0
        self.structure = Structure().structure

    def doAction(self, state):
        '''Given a state perform action on that state
           Return the new state
        '''
        new_state = deepcopy(state)
        new_state.paths.append(self)
        block.rotate(self.rotation)
        return new_state

    @classmethod
    def getPossibleActions(self, state):
        '''Given a state
           Return a LIST of possible actions from that state
        '''
        actions = []

        # Get next block from the structure
        block = self.structure[len(state.path)]

        # Try all rotations:
        rotations = if block.connector == 2 range(0,1) else range(0,4)
        for rotation in rotations:
            action = Action(block, rotation)
            if actionOk(action):
                actions.append(action)

        return actions

    def actionOk(self):
        '''Check to see if this action takes the structure
           outside of the 3x3x3 matrix'''

        pass

