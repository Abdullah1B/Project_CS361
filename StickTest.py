import sys
class Stick(object):
    def __init__(self, disks=[],num_of_disk =0):
        if len(disks) == 0:
            self.disks = [i for i in range(num_of_disk,0,-1)]
        else:
            self.disks = disks

    def __iter__(self):
        return iter(self.disks)
    def print2(self):
        return self.disks
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
            else:
                print ('not allowed to put %s over %s'%(self.top(),destination.top()))

    def current_state(self):
        return tuple(self.disks)


st1 = Stick(num_of_disk=3)
st2 = Stick()
st3 = Stick()

print(st1.print2())
print(st2.print2())
print(st3.print2())

print("move 1 to stick 3")
st1.travel(st3)
print(st1.print2())
print(st2.print2())
print(st3.print2())

print("attempt to move 2 over 1")
st1.travel(st3)
print(st1.print2())
print(st2.print2())
print(st3.print2())


print("move 2 to stick 2")
st1.travel(st2)
print(st1.print2())
print(st2.print2())
print(st3.print2())

print("move 1 to stick 2")
st3.travel(st2)
print(st1.print2())
print(st2.print2())
print(st3.print2())

print("move 3 to stick 3")
st1.travel(st3)
print(st1.print2())
print(st2.print2())
print(st3.print2())

print("move 1 to stick 1")
st2.travel(st1)
print(st1.print2())
print(st2.print2())
print(st3.print2())

print("move 2 to stick 3")
st2.travel(st3)
print(st1.print2())
print(st2.print2())
print(st3.print2())

print("move 1 to stick 3")
st1.travel(st3)
print(st1.print2())
print(st2.print2())
print(st3.print2())