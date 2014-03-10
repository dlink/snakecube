from datetime import datetime
from copy import deepcopy

from structure import STRAIGHT, TURN

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
        #new_state.structure.num_structures +=1 
        #print 'ns:', new_state.structure.num_structures
        new_state.structure.name = uniqueId()
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
        #print 'last_vector:', last_vector
        num_blocks = len(state.paths)
        print 'num_blocks:', num_blocks;
        block = state.structure.blocks[num_blocks]
        #print 'xxblock:', block
        if num_blocks == 0:
            block.x, block.y, block.z = 0,0,0
        else:
            prev_block = state.structure.blocks[num_blocks-1]
            block.x, block.y, block.z = \
                prev_block.x + last_vector.x, \
                prev_block.y + last_vector.y, \
                prev_block.z + last_vector.z
            #print 'prev_block:', prev_block
            #print 'block:', block
        if self.XOkay(state, block):
            if block.type == STRAIGHT:
                vector = last_vector
                actions.append(Action(block, vector))
            else:
                for vector in ROTATION_VECTORS[last_vector]:
                    actions.append(Action(block, vector))
        #print 'getPossibleActions: actions: %s' % actions
        return actions

    @classmethod
    def XOkay(cls, state, block):
        '''Check to see if this action takes the structure
           outside of the 3x3x3 matrix'''
        #print 'XOkay(%s, %s, %s)' % (cls, state, block)
        minx = miny = minz = 999
        maxx = maxy = maxz = -999

        #i = 0
        for i in range(len(state.paths)+1):
            #print 'i:', i
            minx = min(minx, state.structure.blocks[i].x)
            #print '   minx:', minx, state.structure.blocks[i]
            maxx = max(maxx, state.structure.blocks[i].x)

            miny = min(miny, state.structure.blocks[i].y)
            maxy = max(maxy, state.structure.blocks[i].y)

            minz = min(minz, state.structure.blocks[i].z)
            maxz = max(maxz, state.structure.blocks[i].z)
            #i += 1
        #print 'min max:', minx, maxx, miny, maxy, minz,maxz
        if \
                maxx - minx > 2 or \
                maxy - miny > 2 or \
                maxz - minz > 2:
            print 'Went out side of structure'
            return False
        return True

def uniqueId():
    """Return system time to the millisec as set of numbers"""
    d = str(datetime.now())
    #return d[0:4]+d[5:7]+d[8:10]+'-'+d[11:13]+d[14:16]+d[17:19]+'-'+d[20:]
    #return d[11:13]+d[14:16]+d[17:19]+'.'+d[20:]
    return d[11:13]+d[14:16]+d[17:19]+'.'+d[20:]
