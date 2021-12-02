from Node import Node
from Stick import Stick as stick
from Tower_Hanoi import Tower_Hanoi

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

Stick_a = stick(num_of_disk=n)
Stick_b = stick()
Stick_c = stick()

if t == 2:
    G_Stick_a = stick()
    G_Stick_b = stick(num_of_disk=n)
    G_Stick_c = stick()
elif t == 3:
    G_Stick_a = stick()
    G_Stick_b = stick()
    G_Stick_c = stick(num_of_disk=n)

Initial = Node(Stick_a, Stick_b, Stick_c, parent=None)
Goal = Node(G_Stick_a, G_Stick_b, G_Stick_c, parent=None, goal_node=True)
print(f"Initial: {Initial.Sticks}\nGoal: {Goal.Sticks}\n")

Tower = Tower_Hanoi(Initial, Goal, t)
node = Tower.A_star_search()
Path = Tower.path_to_goal(node)

print(f"number of moves: {len(Path) - 1}\nFirst one is the Initial move\n ")
for i in reversed(Path):
    print(i.Sticks)
