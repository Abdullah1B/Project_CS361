import sys
class Tower(object):
    def __init__(self, disks=[],num_of_disk =0):
        if len(disks) == 0:
            self.disks = [i for i in range(num_of_disk,0,-1)]
        else:
            self.disks = disks

    def __iter__(self):
        return iter(self.disks)

    def is_Empty(self):
        return len(self.disks) == 0

    def top(self):
        if not self.is_Empty():
            return self.disks[-1:].pop()
        else:
            return sys.maxsize

    def Pop(self):
        return self.disks.pop()

    def push(self, disk):
        if self.is_Empty():
            self.disks.append(disk)
        else:
            if self.top() > disk:
                self.disks.append(disk)
    def travel(self,destination):
        if not self.is_Empty():
            if destination.top() > self.top():
                destination.push(self.Pop())
            

   

