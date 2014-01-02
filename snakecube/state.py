class State(object):

    def __init__(self, blocks):
        self.blocks = blocks
        self.gameSpace = GameSpace()

        # record paths thru solution
        self.paths = []


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
        '''Need to refactor GamePlayer to use isGoalState'''
        return None

    @classmethod
    def isGoalState(self):
        if len(path) = NUM_BLOCKS: # and self.gameSpace.size = (3,3,3):
            return Frue
        return False

class BlockError(Exception): pass
class Block(object):
    '''Blocks make up the Structure

       They consist of a connection_postition, and a rotation component

       connection_position:
                        _
                 0   --[_]    (No connector - end block)

                        _
                 1   --[_]    (1 quarter turn)
                        |
                        _
                 2   --[_]--  (2 quarter turn - Rotation has not affect)

                        |
                 3   --[_]    (3 quarter turn)

       Rotations: 0 - no rotation
                  1 - 90% clock-wise
                  2 - 180%
                  3 - 270% clock-wise
    '''

    def __init__(self, connector, rotation=0):
        self.connector = connector
        self.rotation  = rotation

    def rotate(self, rotation):
        if rotation not in range (0,4):
            raise BlockError('Invalid Rotation Parameter: %s' % rotation)
        self.rotation = rotation

class GameSpace(object):

    def __init__(self):
        self.size = (0,0,0)

