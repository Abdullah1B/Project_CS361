from Node import Node
from Tower import Tower as tower
import sys

class Tower_Hanoi(object):
    def __init__(self,Initial,Goal,target ,heuristic_n):
        self.Initial = Initial
        self.Goal = Goal
        self.target = target
        self.Open_list  = [] 
        self.Closed_list = []
        self.num_of_tower = 3
        self.heuristic_n = heuristic_n

    def next_node(self,cost:int) -> Node:
        child_cost = sys.maxsize
        child_Index = sys.maxsize

        for i , node in enumerate(self.Open_list):
            node_cost = node.f(cost,self.Goal,self.target ,self.heuristic_n) # f(n) = g(n) + h(n)
            if node_cost < child_cost:
                child_cost = node_cost
                child_Index = i
        return self.Open_list[child_Index]
    

    def moves(self,node:Node):

        def list_disk(list):
            disks = []
            for  l in list:
                disks.append(l.disks[:])
            return disks
        
        towers = (tower(node.Towers[0]) ,tower(node.Towers[1]), tower(node.Towers[2])) 

        
        copy_towers = ((tower(towers[0].disks[:]),tower(towers[1].disks[:]),tower(towers[2].disks[:])))
        MoveTo = [0 , 1 , 2]
        list_moves = []
        Tower = 0

        
        while (Tower < self.num_of_tower):

            if Tower in MoveTo:
                MoveTo.remove(Tower)
                for move in MoveTo:
                    copy_towers[Tower].travel(copy_towers[move])
                    
                    disks = list_disk(copy_towers)
                    list_moves.append(Node( disks ,parent= node))
                    copy_towers = ((tower(towers[0].disks[:]),tower(towers[1].disks[:]),tower(towers[2].disks[:])))
            MoveTo = [0 , 1, 2]
            Tower +=1
        return list_moves
        


    def path_to_goal(self,node:Node) -> list: # return the path form goal node to start node 
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
            if currentNode.Towers == self.Goal.Towers:
                print(f"We reach to the goal\nExpanded nodes:{len(self.Closed_list)}")
                return currentNode
            else:
                list_moves = self.moves(currentNode)
                for next_move in list_moves:
                    new_move = True
                    for expanded in self.Closed_list:
                        if expanded.Towers == next_move.Towers:
                            new_move = False
                    if new_move:
                        for unexpanded in self.Open_list:
                            if unexpanded.Towers == next_move.Towers:
                                new_move = False
                                if next_move.Fvalue != None:
                                    if unexpanded.Fvalue > next_move.Fvalue:
                                        self.Open_list.remove(unexpanded)
                                        self.Open_list.append(next_move)
                                        break
                        if new_move:
                            self.Open_list.append(next_move)

    