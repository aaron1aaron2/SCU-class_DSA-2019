class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BSTree:
    def __init__(self):
        self.Root=None
        
    def setRoot(self, val):
        self.Root = Node(val)
        
    def insert(self, val):
        if (self.Root != None):
            self.insertNode(self.Root, val)
        else:
            self.setRoot(val)
        
    def insertNode(self, currentNode, val):

    def find(self, val):

    def findNode(self, currentNode, val):
