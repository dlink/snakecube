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

