
class Node():
    def __init__(self, data=None, children=None):
        if children is None:
            children = []
        self.data = data
        self.children = children