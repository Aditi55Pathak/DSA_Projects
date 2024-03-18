# Project Decision Making Tree based on binary tree


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def make_decision(node):
    if node.left is None and node.right is None:
        # Leaf node, end of decision-making process
        print("Your decision is:", node.value)
        return

    answer = input(f"{node.value} Answer yes or no: ")
    if answer.lower() == "yes":
        if node.right is not None:
            make_decision(node.right)
        else:
            print("Invalid path. Please start again.")
            return
    elif answer.lower() == "no":
        if node.left is not None:
            make_decision(node.left)
        else:
            print("Invalid path. Please start again.")
            return
    else:
        print("Invalid input. Please answer yes or no.")
        make_decision(node)

# Creating the binary tree
root = BinaryTreeNode("Do you like chocolate?")
root.left = BinaryTreeNode("Do you like vanilla?")
root.right = BinaryTreeNode("Do you like strawberry?")

make_decision(root)
