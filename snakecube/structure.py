from state import Blocks

class Structure(object):
    '''Define initial State of structure

       xxx
         x
         xxx

    '''

    CONNECTORS = [2,2,1,3,2]
    def __init__(self):
        self.structure = [Block(x) for x in CONNECTORS]
                                             


