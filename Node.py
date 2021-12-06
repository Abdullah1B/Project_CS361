class Node(object):
    def __init__(self,Stick_a, Stick_b, Stick_c, parent, goal_node= False):
        self.Towers = ([e for e in Stick_a],
                       [e for e in Stick_b],
                       [e for e in Stick_c])
        self.parent = parent
        self.goal_node = goal_node
        self.Fvalue = None
    
    def f(self,cost,goal_node,target):# f(n) = g(n) + h(n)
        self.Fvalue = self.backward_cost_g(cost) + self.forward_cost_heuristic(goal_node,target)
        return self.Fvalue

    def backward_cost_g(self,cost): # g(n)
        return cost + 1
        
    def forward_cost_heuristic(self,goal_node,target):# h(n) heuristic is the number of misplaced of disks in the target stick.
        if target == 2:
            #return (len(goal_node.Towers[:]) + 2) % 2
            return len(goal_node.Towers[1]) - len(self.Towers[1]) # targt stick in the middle
        elif target == 3:
            #return (len(goal_node.Towers[:]) + 3)%2
            return len(goal_node.Towers[2]) - len(self.Towers[2]) # target stick the last one 
