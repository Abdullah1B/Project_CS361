class Node(object):
    def __init__(self,Towers, parent, goal_node= False):
        self.Towers = Towers 
        self.parent = parent
        self.goal_node = goal_node
        self.Fvalue = None
    
    def f(self,cost,goal_node,target, hur):# f(n) = g(n) + h(n)
        if hur == 1:
            self.Fvalue = self.backward_cost_g(cost) + self.misplaced(goal_node,target)
            return self.Fvalue
        elif hur == 2:
            self.Fvalue = self.backward_cost_g(cost) + self.heuristic_2(goal_node,target)
            return self.Fvalue

    def backward_cost_g(self,cost): # g(n)
        return cost + 1
        
    def misplaced(self,goal_node,target):# h(n) heuristic is the number of misplaced of disks in the target stick.
        if target == 2:
            return len(goal_node.Towers[1]) - len(self.Towers[1]) # targt stick in the middle
        elif target == 3:
            return len(goal_node.Towers[2]) - len(self.Towers[2]) # target stick the last one 
    
    def heuristic_2(self,goal_node,target):
        if target == 2:
            return (len(goal_node.Towers[:]) + 2) % 2
            
        elif target == 3:
            return (len(goal_node.Towers[:]) + 3)%2
