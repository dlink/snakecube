SEARCH_TYPE = 'breath-first'
#SEARCH_TYPE = 'depth-first'
#SEARCH_TYPE = 'A*' # with a poor heuristic

ROWS = 3
COLS = 3
X = 'X'
O = 'O'

class State(object):

    def __init__(self, board):
        self.board = board
        
        # record paths thru solution
        self.paths = []

    def equals(self, state2):
        '''Return true if this state is equal to that state'''
        
        cell_matches = 0
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if self.board[r][c] != state2.board[r][c]:
                    cell_matches += 1
        if cell_matches == ROWS * COLS:
            return True
        return False

    def __repr__(self):
        return self.board.display()

    def display(self):
        print self.board.display()

    @classmethod
    def next_state(cls, frontier):
        '''Return the a state from a LIST of states
           Using algorithm Based on SEARCH_TYPE
        '''
        if SEARCH_TYPE == 'breath-first':
            state = frontier.pop(0)
        elif SEARCH_TYPE == 'depth-first':
            state = frontier.pop()
        #elif SEARCH_TYPE == 'A*':
        #    pass
        else:
            print 'unrecognized SEARCH_TYPE: %s' % SEARCH_TYPE
        return state

    @classmethod
    def getInitState(self):
        return State(Board())
    
    @classmethod
    def isGoalState(cls, state):
        
        # check verticals:
        for row in state.board.board:
            if State.threeInARow(row):
                return True
            
        # check horizontal
        for c in range(0, COLS):
            if State.threeInARow([r[c] for r in state.board.board]):
                return True
            
        b = state.board.board
        # diag top-right to bot-left
        if State.threeInARow([ b[0][0], b[1][1], b[2][2] ]):
            return True
        
        # diag bot-right to top-left
        if State.threeInARow([ b[0][2], b[1][1], b[2][0] ]):
            return True

        return False

    @classmethod
    def threeInARow(cls, run):
        '''Given a list of three cells
           return X if the are all X
           return O if the ar all O
           else return None
        '''
        x = list(set([c.value for c in run]))
        if x in [[X], [O]]:
            return x[0]
        return False

class Board(object):

    def __init__(self):
        self.board = []
        self._initBoardT1()
        
    def _initBoard(self):
        for r in range(0, ROWS):
            row = []
            for c in range(0, COLS):
                row.append(Cell())
            self.board.append(row)
            
    def _initBoardT1(self):
        '''Test init state as goal state'''
        for r in range(0, ROWS):
            row = []
            for c in range(0, COLS):
                cell = Cell()
                if (r==2 and c==0) or (r==1 and c==1) or (r==0 and c==2):
                    cell.value = X
                row.append(cell)
            self.board.append(row)
            
    def display(self):
        o = ''
        for row in self.board:
            for cell in row:
                o += " %s " % cell.value
            o += '\n'
        return o
    
class Cell(object):

    def __init__(self):
        self.value = '_'
        
if __name__ == '__main__':
    state = State.getInitState()
    state.display()
    print state.isGoalState(state)
    
