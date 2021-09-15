"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
treeRow: str = " "
"""i: int = 0
while i <= depth:
    j: int = i + 1
    while j <= depth:
        treeRow += TREE
        print(treeRow)
        j += 1
    i += 1"""

while depth > 0:
    treeRow += TREE
    print(treeRow)
    depth -= 1
