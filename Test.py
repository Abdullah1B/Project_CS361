from Node import Node
from Tower import Tower as tower
from Tower_Hanoi import Tower_Hanoi
import time

class Test:

        
    Continue = True
    while Continue:
        try:
            t = int(input("Enter the target 2 Or 3: "))
            if t == 2 or t == 3:
                Continue = False
        except ValueError:
            print("Enter either 2 Or 3\n")
            continue

    Continue = True
    while Continue:
        try:
            n = int(input("Enter the number of disk: "))
            Continue = False
        except ValueError:
            print("Enter Intger value (1,2,3,....)\n")
            continue
    Continue = True
    while Continue:
        try:
            heuristic_n = int(input("choice the heuristic\n1-misplace heuristic\n2-admissible heuristic\nEnter: "))
            if heuristic_n in [1,2]:
                Continue = False
        except ValueError:
            print("Enter either 2 Or 3\n")
            continue
    Stick_a = tower(num_of_disk=n)
    Stick_b = tower()
    Stick_c = tower()

    if t == 2:
        G_Stick_a = tower()
        G_Stick_b = tower(num_of_disk=n)
        G_Stick_c = tower()
    elif t == 3:
        G_Stick_a = tower()
        G_Stick_b = tower()
        G_Stick_c = tower(num_of_disk=n)

    Initial = Node([Stick_a.disks[:], Stick_b.disks[:], Stick_c.disks[:]], parent=None)
    Goal = Node([G_Stick_a.disks[:], G_Stick_b.disks[:], G_Stick_c.disks[:]], parent=None, goal_node=True)
    print(f"Initial: {Initial.Towers}\nGoal: {Goal.Towers}\n")

    Tower = Tower_Hanoi(Initial, Goal, t , heuristic_n) 
    start_time = time.time()

    
    node = Tower.A_star_search()
    Path = Tower.path_to_goal(node)
    print(f"number of moves: {len(Path) - 1}\nFirst one is the Initial move\n ")
    for i , move in enumerate( reversed(Path)):
        print(f'No: {i}: {move.Towers}')
    print("--- %s seconds ---" % (time.time() - start_time))
