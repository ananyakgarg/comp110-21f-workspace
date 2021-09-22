"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
treeRow: str = " "
while depth > 0:
    treeRow += TREE
    print(treeRow)
    depth = depth - 1
