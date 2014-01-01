from copy import deepcopy

class Action(object):
    def __init__(self, disk, src, dst):
        """Disk number, source post number and dest. post number"""
        self.disk = disk
        self.src = src
        self.dst = dst
        
    def getNumbers(self):
        return (self.disk, self.src, self.dst)
        
    def __repr__(self):
        return "P%s:D%s -> P%s" % (self.src, self.disk, self.dst)

    @classmethod
    def getPossibleActions(self, state):
        '''Given a state
           Return a LIST of possible actions from that state
        '''
        actions = []
        for i, post in enumerate(state.posts):
            if i == 0:
                opost1 = state.posts[1]
                opost2 = state.posts[2]
            elif i == 1:
                opost1 = state.posts[0]
                opost2 = state.posts[2]
            else:
                opost1 = state.posts[0]
                opost2 = state.posts[1]
            if post.hasDisks:
                if not opost1.hasDisks or post.topDisk < opost1.topDisk:
                    actions.append(Action(post.topDisk, post.num, opost1.num))
                if not opost2.hasDisks or post.topDisk < opost2.topDisk:
                    actions.append(Action(post.topDisk, post.num, opost2.num))
        return actions

    def doAction(self, state):
        '''Given a state perform action on that state
           Return the new state
        '''
        newState = deepcopy(state)
        newState.paths.append(self)
        disk, src_num, dst_num = self.getNumbers()
        src = newState.getPost(src_num)
        dst = newState.getPost(dst_num)
        if src.topDisk != disk:
            raise Exception("Move: D%s not on post%s." % (disk, src.num))
        if dst.hasDisks and disk > dst.topDisk:
            raise Exception("Move: Can not put disk %s on post%s, too big." 
                            % (d, dst.num))
        dst.disks.append(src.disks.pop())
        return newState

