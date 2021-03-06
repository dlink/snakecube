# Number of blocks and whether ea. is Straight (0) or Turn (1)

NUM_BLOCKS = 27
STRAIGHT = 0
TURN = 1
BLOCK_TYPES = [0,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,0]

class Structure(object):
    '''Structure is a collection of Blocks
    '''
    structure_names = []

    def __init__(self):
        self._name = 0
        Structure.structure_names.append(self._name)

        self.blocks = []
        for i, t in enumerate(BLOCK_TYPES):
            self.blocks.append(Block(self, i+1, t))

    # name
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name
        Structure.structure_names.append(name)
    name = property(getName, setName)

    def incrementName(self):
        '''Set Structure Name to a number one larger than
           the maximum Structure Name'''
        self.setName(max(Structure.structure_names)+1)

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
        return ('Block%s (%s,%s,%s)' % (self.num, self.x, self.y, self.z))
