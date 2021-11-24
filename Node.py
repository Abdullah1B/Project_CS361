class Node(object):
    def __init__(self,Stick_a, Stick_b, Stick_c, parent, goal_node= False):
        self.Stick = ([e for e in Stick_a],[e for e in Stick_b],[e for e in Stick_c])
        self.parent = parent
        self.goal_node = goal_node
        self.Fvalue = None
   
    def f(self):# f(n) = g(n) + h(n)
        self.Fvalue = self.backward_cost_g() + self.forward_cost_h()
        return self.Fvalue
    def backward_cost_g(self): # g(n)
        pass
    def forward_cost_h(self):# h(n) 
        pass