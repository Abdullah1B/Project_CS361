from Node import Node
from Tower import Tower as tower
import sys

class Tower_Hanoi(object):
    def __init__(self,Initial,Goal,target , num_of_tower = 3):
        self.Initial = Initial
        self.Goal = Goal
        self.target = target
        self.Open_list  = [] 
        self.Closed_list = []
        if num_of_tower != 3:
            self.num_of_tower = 3

    def next_node(self,cost:int) -> Node:
        child_cost = sys.maxsize
        child_Index = sys.maxsize

        for i , node in enumerate(self.Open_list):
            node_cost = node.f(cost,self.Goal,self.target) # f(n) = g(n) + h(n)
            if node_cost < child_cost:
                child_cost = node_cost
                child_Index = i
        return self.Open_list[child_Index]
    
    def Copy(self,s3):
            copy = (tower(s3[0].disks[:]),tower(s3[1].disks[:]),tower(s3[2].disks[:]))
            return copy

    def moves(self, node:Node) -> Node: 
        x = 0
        towers = []
        while x < self.num_of_tower:
            towers.append(tower(node.Towers[x]))
            x += 1



        copy_towers = []
        list_moves = []
        
        Tower = 0
        stop = self.num_of_tower * 2
        divisor = self.num_of_tower - 1 # in our case the number of tower is 3


        copy_towers = self.Copy(towers)
        while Tower < stop:
           
            
            if Tower in [0 , 1]: # A --> 0 // 2 = 0 or 1 // 0 = 0 which we at 'A' first tower by taking the floor
                if Tower == 0:# A to B
                    copy_towers[ Tower // divisor ].travel(copy_towers[1])
                    list_moves.append(Node(copy_towers[Tower // 2] ,copy_towers[1], towers[2], parent= node))
                    
                
                else: # A to C
                    copy_towers[Tower // divisor].travel(copy_towers[2])
                    list_moves.append(Node(copy_towers[Tower // 2] ,towers[1], copy_towers[2], parent= node))
                    
            if Tower in [2 , 3]:# B --> 2 // 2 = 1 or 3 // 2 = 1 which we at 'B' second tower 
                if Tower == 2: # B to A
                    copy_towers[Tower // divisor].travel(copy_towers[0])
                    list_moves.append(Node(copy_towers[0] ,copy_towers[Tower // divisor], towers[2], parent= node))
                
                else:# B to C
                    copy_towers[Tower // divisor].travel(copy_towers[2])
                    list_moves.append(Node(towers[0] ,copy_towers[Tower // divisor], copy_towers[2], parent= node))

            if Tower in [4 , 5]:# C --> 4 // 2 = 2 , 5 // 2 = 2 which we at 'C' third tower 
                if Tower == 4:# C to A
                    copy_towers[Tower // divisor].travel(copy_towers[0])
                    list_moves.append(Node(copy_towers[0] , towers[1], copy_towers[Tower // divisor],parent=node ))
                else: # C to B
                    copy_towers[Tower // divisor].travel(copy_towers[1])
                    list_moves.append(Node(towers[0] , copy_towers[1], copy_towers[Tower // divisor] , parent= node ))
            
            
            Tower += 1
            copy_towers = self.Copy(towers)
            


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
            if currentNode.Towers == self.Goal.Towers:
                print(f"We reach to the goal\nExpanded nodes:{len(self.Closed_list)}")
                return currentNode
            else:
                list_moves : Node = self.moves(currentNode)
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

    