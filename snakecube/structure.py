NUM_BLOCKS = 8
BLOCK_TYPES = [0, 0, 1, 0, 1, 0, 1, 0]

STRAIGHT = 0
TURN = 1

class Structure(object):

    def __init__(self):

        self.structure_cnt = 1

        self.blocks = []
        for i, t in enumerate(BLOCK_TYPES):
            self.blocks.append(Block(i+1, t, self.structure_cnt))

        #self.blocks = [Block(x) for x in BLOCK_TYPES]

class Block(object):

    def __init__(self, num, type, snum):
        self.snum = snum
        self.num  = num
        self.type = type
        self.type_name = '' if type == STRAIGHT else '-TR'

        self.x = None
        self.y = None
        self.z = None

    def __repr__(self):
        return ('%sBlock%s%s (%s,%s,%s)' % (self.snum, self.num, self.type_name,
                                         self.x, self.y, self.z))
