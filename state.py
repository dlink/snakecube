SEARCH_TYPE = 'breath-first'
#SEARCH_TYPE = 'depth-first'
#SEARCH_TYPE = 'A*' # with a poor heuristic

MAX_DISKS = 4
NUM_POSTS = 3
DISPLAY_NUM_ROWS = 7

D1 = 1
D2 = 2 
D3 = 3
D4 = 4

class State(object):

    def __init__(self, posts):
        self.posts = posts

        # set post numbers:
        for i, post in enumerate(posts):
            post.num = i+1

        self.paths = []

    def getPost(self, num):
        if num not in range(1, NUM_POSTS+1):
            raise Exception("State.get: bad num: %s" % num)
        return self.posts[num-1]

    def equals(self, state2):
        for i in range(0, 3):
            if self.posts[i].disks != state2.posts[i].disks:
                return False
        return True

    def __repr__(self):
        t = []
        for p in self.posts:
            t.append(str(p))
        return "posts: %s; paths: %s" % ("-".join(t), self.paths)

    def display(self):
        '''Output state displayed like this:
                |               |               |       
               xxx              |               |       
              xxxxx             |               |       
             xxxxxxx            |               |       
            xxxxxxxxx           |               |       
          -------------   -------------   ------------- 
          '''
        rep = []
        for post in self.posts:
            rep.append(post.representation())
        print
        for y in range(0, DISPLAY_NUM_ROWS):
            for x in range(0, NUM_POSTS):
                print rep[x][y],
            print

    @classmethod
    def next_state(self, frontier):
        '''Return the a state from frontier
           Using algorithm Based on SEARCH_TYPE
        '''
        if SEARCH_TYPE == 'breath-first':
            state = frontier.pop(0)
        elif SEARCH_TYPE == 'depth-first':
            state = frontier.pop()
        elif SEARCH_TYPE == 'A*':
            # get lowest total cost:
            states_by_cost = defaultdict(lambda:[])
            for s in frontier:
                total_cost = len(s.paths)
                states_by_cost[total_cost].append(s)
            min_total_cost = min(states_by_cost.keys())
            
            # Heuristic: lest amount of disks on post 1
            states_by_heuristic = defaultdict(lambda:[])
            for s in states_by_cost[min_total_cost]:
                h = len(s.posts[0].disks)
                states_by_heuristic[h].append(s)
            min_h = min(states_by_heuristic.keys())
            
            # choose a state with least cost and least h and remove from f
            state = states_by_heuristic[min_h].pop(0)
            for i, s in enumerate(frontier):
                if state.equals(s):
                    del frontier[i]
                    break
        else:
            print 'unrecognized SEARCH_TYPE: %s' % SEARCH_TYPE
        return state

    @classmethod
    def getInitState(self):
        return State([ Post([D4, D3, D2, D1]), 
                       Post(), 
                       Post()])
    @classmethod
    def getGoalState(self):
        return State([ Post(),
                       Post(), 
                       Post([D4, D3, D2, D1]) ])

class Post(object):

    def __init__(self, disks=None):
        self.disks = []
        if disks:
            self.disks = disks
        self.num = 0  # unset 

    @property
    def hasDisks(self):
        return len(self.disks)

    @property
    def topDisk(self):
        if self.hasDisks:
            return self.disks[-1]
        else:
            return None

    def representation(self):
        '''Render post state like this:
                |
               xxx 
              xxxxx
             xxxxxxx
            xxxxxxxxx
          -------------
                1
        '''
        o = []
        o.append("       |       ")
        for r in range(0, MAX_DISKS-len(self.disks)):
            o.append("       |       ")
        for d in reversed(self.disks):
            o.append('%s%sx%s%s%s' % (' '*(7-d), 'x'*d, 'x'*d, d, ' '*(6-d)))
        o.append(" ------------- ")
        o.append("       %s       " % self.num)
        return o

    def __repr__(self):
        return "(%s)" % "-".join(["D%s" % x for x in self.disks]) 


