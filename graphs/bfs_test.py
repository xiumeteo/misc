
from graphs.BFS import BFS
from graphs.Node import Node


def test_print_tree():
    r2 = Node(3)
    l2 = Node(3, [Node(4)])
    left = Node(2, [r2])
    right = Node(2, [l2])
    r = Node(1, [left, right])
    b = BFS(r)

    b.print()
