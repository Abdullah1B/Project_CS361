from Node import Node
from Stick import Stick as stick

class Tower_Hanoi(object):
    def __init__(self,Initial,Goal,target):
        self.Initial = Initial
        self.Goal = Goal
        self.target = target
        self.Open_list = []
        self.Closed_list = []

    def next_node(self,cost:int):
       pass
    def moves(self,node:Node): # design for 3 sticks
        pass