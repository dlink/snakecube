#NUM_BLOCKS = 8
#BLOCK_TYPES = [0, 0, 1, 0, 1, 0, 1, 0]

#NUM_BLOCKS = 12
#BLOCK_TYPES = [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]

#NUM_BLOCKS = 20
#BLOCK_TYPES = [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1,0,1,0,1,1,1,0,1]

NUM_BLOCKS = 27
BLOCK_TYPES = [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,0]

STRAIGHT = 0
TURN = 1

class Structure(object):
    '''Structure is a collection of Blocks
    '''
    #num_structures = 0

    def __init__(self):
        self.name = 0

        self.blocks = []
        for i, t in enumerate(BLOCK_TYPES):
            self.blocks.append(Block(self, i+1, t))

        #self.blocks = [Block(x) for x in BLOCK_TYPES]

    def __repr__(self):
        return str(self.name)

class Block(object):
    '''A block belongs to a Structure
       
       num: position in the structure
                                                 |
       type: 0, straight -[ ]-   1, L-shape    -[ ]

       x,y,z: coordinate in space

    '''
    def __init__(self, structure, num, type):
        self.structure = structure
        self.num  = num
        self.type = type
        self.type_name = '' if type == STRAIGHT else '-TR'

        self.x = None
        self.y = None
        self.z = None

    def __repr__(self):
        return ('%sBlock%s%s (%s,%s,%s)' % (self.structure, self.num, 
                                            self.type_name,
                                            self.x, self.y, self.z))
