from copy import deepcopy

class Vector(object):

    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return self.name

# VECTORS
X  = Vector( 'X',  1, 0, 0)
MX = Vector('-X', -1, 0, 0)
Y =  Vector( 'Y',  0, 1, 0)
MY = Vector('-Y',  0,-1, 0)
Z  = Vector( 'Z',  0, 0, 1)
MZ = Vector('-Z',  0, 0,-1)

# For each vector, there are four possible 90% rotation vectors:
ROTATION_VECTORS = {X : [Y, MZ, MY, Z],
                    MX: [Y, MZ, MY, Z],
                    Y : [X, MZ, MX, Z],
                    MY: [X, MZ, MX, Z],
                    Z : [X, Y, MX, MY],
                    MZ: [X, Y, MX, MY]}

class Action(object):
    '''Preside of Game Actions

       An action consists of Adding a block to an existing String of
       Blocks (as defined by the state), and rotating the block.
    '''

    def __init__(self, block, vector):
        '''An action constists of a new block to add,
           And a rotation component
        '''
        self.block   = block
        self.vector  = vector

    def __repr__(self):
        return '{%s, %s}' % (self.block, self.vector)

    def doAction(self, state):
        new_state = deepcopy(state)
        new_state.paths.append(self)
        return new_state

    @classmethod
    def getPossibleActions(self, state):
        '''Given a state
           Return a LIST of possible actions from that state
        '''
        actions = []

        if not len(state.paths):
            last_vector = X
        else:
            last_vector = state.paths[-1].vector
        block = state.structure.blocks[len(state.paths)]
        print '  block:', block

        if block.type == 0:
            vector = last_vector
            actions.append(Action(block, vector))
        else:
            for vector in ROTATION_VECTORS[last_vector]:
                actions.append(Action(block, vector))
        return actions

    def actionOk(self):
        '''Check to see if this action takes the structure
           outside of the 3x3x3 matrix'''

        pass

