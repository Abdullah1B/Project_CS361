from Node import Node
from Stick import Stick as stick
import sys

class Tower_Hanoi(object):
    def __init__(self,Initial,Goal,target):
        self.Initial = Initial
        self.Goal = Goal
        self.target = target
        self.Open_list = []
        self.Closed_list = []

    def next_node(self,cost:int) -> Node:
        child_cost = sys.maxsize
        index = 0
        child_Index = sys.maxsize
        for node in self.Open_list:
            node_cost = node.f(cost,self.Goal,self.target)
            if child_cost > node_cost:
                child_cost = node_cost
                child_Index = index
            index += 1
        next_node = self.Open_list[child_Index]
        return next_node

    def moves(self,node:Node) -> Node: # design for 3 sticks
        """

        from A to B and C 
        from B to A and C
        from C to A and B
        return a list of childer for the given node 

        """
        S_A = stick(node.Sticks[0])
        S_B = stick(node.Sticks[1])
        S_C = stick(node.Sticks[2])

        list_moves = []

        A = stick(S_A.disks[:])
        B = stick(S_B.disks[:])
        
        A.travel(B) # move disk from A to B
        list_moves.append(Node(A, B, S_C, parent= node))
        
        A = stick(S_A.disks[:])
        C = stick(S_C.disks[:])
        
        A.travel(C) # move disk from A to C
        list_moves.append(Node(A, S_B, C, parent= node))
        
        A = stick(S_A.disks[:])
        B = stick(S_B.disks[:])
        
        B.travel(A) # move disk from B to A
        list_moves.append(Node(A, B, S_C, parent= node))
        
        
        B = stick(S_B.disks[:])
        C = stick(S_C.disks[:])
        
        B.travel(C) # move disk from B to C
        list_moves.append(Node(S_A, B, C, parent= node))

        
        C = stick(S_C.disks[:])
        A = stick(S_A.disks[:])
        
        C.travel(A) # move disk from C to A
        list_moves.append(Node(A, S_B, C, parent= node))

        
        C = stick(S_C.disks[:])
        B = stick(S_B.disks[:])
        
        C.travel(B) # move disk from C to B
        list_moves.append(Node(S_A, B, C, parent= node))
        
        return list_moves

    def path_to_goal(self,node:Node) -> Node: # return the path form goal node to start node 
        Path = []
        while node.parent != None:
            Path.append(node)
            node = node.parent
        Path.append(self.Initial)
        return Path


        
    def A_star_search(self):
        cost = 0
        self.Open_list.append(self.Initial)
        while len(self.Open_list) > 0:
            currentNode = self.next_node(cost)
            self.Open_list.remove(currentNode)
            cost += 1
            self.Closed_list.append(currentNode)
            if currentNode.Sticks == self.Goal.Sticks:
                print(f"We reach to the goal\nExpanded nodes:{len(self.Closed_list)}")
                return currentNode
            else:
                list_moves = self.moves(currentNode)
                for next_move in list_moves:
                    new_move = True
                    for expanded in self.Closed_list:
                        if expanded.Sticks == next_move.Sticks:
                            new_move = False
                    if new_move:
                        for unexpanded in self.Open_list:
                            if unexpanded.Sticks == next_move.Sticks:
                                new_move = False
                                if next_move.Fvalue != None:
                                    if unexpanded.Fvalue > next_move.Fvalue:
                                        self.Open_list.remove(unexpanded)
                                        self.Open_list.append(next_move)
                                        break
                        if new_move:
                            self.Open_list.append(next_move)

    