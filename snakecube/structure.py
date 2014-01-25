NUM_BLOCKS = 8
BLOCK_TYPES = [0, 0, 1, 0, 1, 0, 1, 0]

class Structure(object):
    def __init__(self):
        self.blocks = [Block(x) for x in BLOCK_TYPES]

class Block(object):

    block_cnt = 0

    def __init__(self, type):
        Block.block_cnt += 1

        self.num  = Block.block_cnt
        self.type = type
        self.type_name = 'Straight' if type == 0 else 'Turn'

    def __repr__(self):
        return ('Block%s-(%s)' % (self.num, self.type_name))
