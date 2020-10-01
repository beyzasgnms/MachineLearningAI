import random as rnd


# We have a node class that keeps its depth and value
# Plus it keeps which player's turn it is; user (1) or computer (-1)
class Node(object):
    def __init__(self, depth, player):
        self.depth = depth
        self.player = player
        # player = 1 --> player = user (maximizer)
        # player = -1 --> player = computer (minimizer)
        self.value = 0
        # Value is 0 now because it depends on player and value of children
        # And we have not created children yet
        self.children = []
        self.create_children()

    def create_children(self):
        if self.depth > 0:
            # Depth check
            for i in range(5):
                # A node will have 5 children nodes
                n = Node(self.depth - 1, -self.player)
                # Depth decreased
                self.children.append(n)

    def assign_values(self):
        if self.depth == 0:
            # Depth check, again
            # If 0, assign a random value between 0-1000
            value = rnd.randint(0, 1000)
            self.value = value
        else:
            # If > 0 then
            for n in self.children:
                n.assign_values()
                # Calls itself to go to where depth = 0
                values = self.get_children_values()
                # Then gets all value of children nodes
                if self.player == 1:
                    # If player is maximizer
                    self.value = max(values)
                    # Value is maximum of children nodes
                elif self.player == -1:
                    # If player is minimizer
                    self.value = min(values)
                    # Value is minimum of children nodes

    def get_children_values(self):
        # This method returns a list that includes all 5 children's values
        nodes = self.children
        values = []
        for n in nodes:
            values.append(n.value)
        return values

    def __str__(self):
        v = self.get_children_values()
        s = "Value of Nodes: "
        for i in v:
            s += str(i) + " "
        return s


def minimax(node, depth, player):
    val = node.value
    if depth == 0:
        # If the node is a leaf node then returns it's value
        return val

    child1 = node.children[0]
    child2 = node.children[1]
    child3 = node.children[2]
    child4 = node.children[3]
    child5 = node.children[4]
    # Else initializes all childrens as variables

    if player == 1:
        # If player is maximizer
        return max(minimax(child1, child1.depth, child1.player),
                   minimax(child2, child2.depth, child2.player),
                   minimax(child3, child3.depth, child3.player),
                   minimax(child4, child4.depth, child4.player),
                   minimax(child5, child5.depth, child5.player))
        # Returns maximum value of 5 recursive functions
    else:
        # If player is minimizer
        return min(minimax(child1, child1.depth, child1.player),
                   minimax(child2, child2.depth, child2.player),
                   minimax(child3, child3.depth, child3.player),
                   minimax(child4, child4.depth, child4.player),
                   minimax(child5, child5.depth, child5.player))
        # Returns minimum value of 5 recursive functions


def get_move(node):
    # Lets user to pick a node
    print()
    print(node)
    print("Which node would you like to pick?")
    choice = int(input("Input 1/2/3/4/5: "))
    while choice > 5 or choice < 1:
        # Checks validity to prevent an index exception
        choice = int(input("Input 1/2/3/4/5: "))
    return choice


def end_screen(node, choices):
    print()
    print("Game Over!")
    print("You reached " + str(node.value) + " points")
    seq = "A"
    for c in choices:
        seq += str(c)
    print("Sequence of moves: " + seq)


def play():
    depth = 4
    player = -1
    n = Node(depth, player)
    # We created a node with depth = 4 and player = computer
    # It creates its own children inside, and its children create their own...
    # Until depth becomes 0
    n.assign_values()
    # Now we assign value of every node

    print("GOAL: Reach to the maximum points")
    print("INSTRUCTIONS")
    print("There are 5 nodes which have their own value")
    print("Computer picks first and tries to minimize your point")
    print("You will try to maximize your point")

    choices = []
    while n.depth > 0:
        if n.player == 1:
            choice = get_move(n)
            choices.append(choice)
            n = n.children[choice - 1]
        elif n.player == -1:
            val = minimax(n, n.depth, player)
            choice = n.get_children_values().index(val)
            choices.append(choice + 1)
            print()
            print(n)
            print("Computer picked node #" + str(choice + 1))
            print("with value of " + str(n.value))
            n = n.children[choice]
    end_screen(n, choices)


play()
