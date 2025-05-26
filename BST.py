class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = Node()
    def Insert(self, data):
        if self.root.data == None:
            self.root.data = data
        else:
            def InsertToVertex(data, vertex):
                if data < vertex.data:
                    if vertex.left == None:
                        vertex.left = Node(data)
                    else:
                        InsertToVertex(data, vertex.left)
                if data > vertex.data:
                    if vertex.right == None:
                        vertex.right = Node(data)
                    else:
                        InsertToVertex(data, vertex.right)
            InsertToVertex(data, self.root)
    def Display(self):
        result = ""
        def Vlr(result, vertex):
            if vertex:
                if vertex.data:
                    result += str(vertex.data) + "-"
                    result = Vlr(result, vertex.left)
                    result = Vlr(result, vertex.right)
            return result
        print(Vlr(result, self.root))

tree = BST()
tree.Insert(3)
tree.Insert(2)
tree.Insert(1)
tree.Insert(8)
tree.Insert(7)
tree.Insert(99)

tree.Display()