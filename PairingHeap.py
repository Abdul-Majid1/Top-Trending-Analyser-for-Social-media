from Post import Post


class HeapNode:

    # creates a new node
    def __init__(self, post_=None, key_=None, leftChild_=None, nextSibling_=None):
        self.post = post_
        self.key = post_.currentPriority
        self.leftChild = leftChild_
        self.nextSibling = nextSibling_

    # Adds a child and sibling to the node
    def addChild(self, node):
        if(self.leftChild == None):
            self.leftChild = node
        else:
            node.nextSibling = self.leftChild
            self.leftChild = node

    def __iter__(self):
        stack = []
        currentNode = self
        stack.append(currentNode)
        while len(stack) > 0:
            if currentNode.leftChild:
                currentNode = currentNode.leftChild
                stack.append(currentNode)
                yield currentNode
                while currentNode.nextSibling:
                    currentNode = currentNode.nextSibling
                    stack.append(currentNode)
                    yield currentNode
                currentNode = stack.pop()
            elif len(stack) != 0:
                currentNode = stack.pop()


# Returns true if root of the tree
# is None otherwise returns false


def Empty(node):
    return (node == None)

# Function to merge two heaps


def Merge(A, B):

    # If any of the two-nodes is None
    # the return the not None node
    if(A == None):
        return B
    if(B == None):
        return A

    # To maintain the min heap condition compare
    # the nodes and node with minimum value become
    # parent of the other node
    print(A.key)
    print(B.key)
    if(A.key < B.key):
        A.addChild(B)
        return A
    B.addChild(A)
    return B

# Returns the root value of the heap


def Top(node):
    return node


# Function to insert the new node in the heap
def Insert(node, post, priority):
    return Merge(node, HeapNode(post, priority))


# This method is used when we want to delete root node
def TwoPassMerge(node):
    if(node == None or node.nextSibling == None):
        return node
    A = node
    B = node.nextSibling
    newNode = node.nextSibling.nextSibling

    A.nextSibling = None
    B.nextSibling = None

    return Merge(Merge(A, B), TwoPassMerge(newNode))


# Function to delete the root node in heap
def Delete(node):
    return TwoPassMerge(node.leftChild)


class PairingHeap:
    def __init__(self):
        self.root = None
        self.TraversalNodes = []
        self.stackOfNodes = []

    def Empty(self):
        return Empty(self.root)

    def Top(self):
        return Top(self.root)

    def Insert(self, post, priority):
        self.root = Insert(self.root, post, priority)

    def Delete(self):
        self.root = Delete(self.root)

    def Join(self, other):
        self.root = Merge(self.root, other.root)

    def __iter__(self):
        stack = []
        currentNode = self.root
        stack.append(currentNode)
        yield currentNode
        while len(stack) > 0:
            if currentNode.leftChild:
                currentNode = currentNode.leftChild
                stack.append(currentNode)
                yield currentNode
                # print(currentNode.key)
                while currentNode.nextSibling:
                    currentNode = currentNode.nextSibling
                    stack.append(currentNode)
                    yield currentNode
                    # print(currentNode.key)
                currentNode = stack.pop()
            elif len(stack) != 0:
                currentNode = stack.pop()

    def find(self, p):
        for i in self:
            if i.leftChild:
                if i.leftChild.post == p:
                    indicator = 'L'
                    return (i, i.leftChild, indicator)
            if i.nextSibling:
                if i.nextSibling.post == p:
                    indicator = 'N'
                    return (i, i.nextSibling, indicator)
        indicator = 'R'
        return (0, i, indicator)

    def decreaseKey(self, post, priority):
        prevNode, currentNode, indicator = self.find(post)
        # if currentNode.key < priority:
        #     return
        if prevNode == 0:
            self.root.key = priority
            return
        if indicator == 'N':
            if currentNode.nextSibling:
                prevNode.nextSibling = currentNode.nextSibling
            else:
                prevNode.nextSibling = None
        elif indicator == 'L':
            if currentNode.nextSibling:
                prevNode.leftChild = currentNode.nextSibling
            else:
                prevNode.leftChild = None

        newHeap = PairingHeap()
        newHeap.Insert(currentNode.post, priority)
        for i in currentNode:
            newHeap.Insert(i.post, i.key)

        self.Join(newHeap)
        for i in self:
            print(f'Printing Posts: {i.post.getText()}')
        return self


# Driver Code
if __name__ == '__main__':
    pass

    #     heap1, heap2 = PairingHeap(), PairingHeap()
    #     tempPost1 = Post("faraz ", ["biking"], 4444, 8,
    #                      "YOur patience means everything ")
    #     tempPost2 = Post("abdul ", ["Biking"], 248, 1,
    #                      "The summer Heat is riveting ")
    #     tempPost3 = Post("oqba ", ["Biking"], 267, 3, "hot to worry though ")
    #     tempPost4 = Post("faraz ", ["biking "], 4444, 8,
    #                      "YOur patience means everything ")
    #     tempPost5 = Post("abdul ", ["Biking"], 248, 1,
    #                      "YEs the shift does indeed happen ")
    #     tempPost6 = Post("oqba ", ["Biking"], 267, 3, "not to worry though ")
    #     tempPost7 = Post("faraz ", ["Biking"], 4444, 8,
    #                      "YOur patience means everything ")

    #     # print(f'Post 1 = {tempPost1.getText()}')
    #     # print(f'Post 2 = {tempPost2.getText()}')
    #     # print(f'Post 7 = {tempPost7.getText()}')
    #     # print(f'Post1 = Post2 = {tempPost2 == tempPost1}')
    #     # print(f'Post1 = Post7 = {tempPost7 == tempPost1}')
    #     heap1.Insert(tempPost1, 0)
    #     heap1.Insert(tempPost2, 0)
    #     heap1.Insert(tempPost3, 0)

    #     for i in heap1:
    #         print(i.post.getText())

    #     heap1.decreaseKey(tempPost2, -1)
    #     for i in heap1:
    #         print(i.post.getText())

    #     heap1.decreaseKey(tempPost1, -2)
    #     for i in heap1:
    #         print(i.post.getText())

    #     # heap2.Insert(tempPost5, 5)
    #     # heap2.Insert(tempPost2, 2)

    #     # heap2.Insert(tempPost6, 6)
    #     # heap1.Insert(tempPost1, 1)
    #     # heap1.Insert(tempPost3, 3)
    #     # heap1.Insert(tempPost4, 4)

    #     # heap1.Join(heap2)

    #     # print("Initial Heap")
    #     # for i in heap1:
    #     #     print(i.key)

    #     # print()

    #     # heap1.decreaseKey(2, 0)

    #     # print("Heap after decrease key")
    #     # for i in heap1:
    #     #     print(i.key)

    #     # print()

    #     # print('Deleting top element')
    #     # print(heap1.Top().key)
    #     # print(heap1.Top().post.getText())
    #     # heap1.Delete()

    #     # print('Deleting top element')
    #     # print(heap1.Top().key)
    #     # print(heap1.Top().post.getText())
    #     # heap1.Delete()

    #     # print('Deleting top element')
    #     # print(heap1.Top().key)
    #     # print(heap1.Top().post.getText())
    #     # heap1.Delete()

    #     # print('Deleting top element')
    #     # print(heap1.Top().key)
    #     # print(heap1.Top().post.getText())
    #     # heap1.Delete()

    #     # print('Deleting top element')
    #     # print(heap1.Top().key)
    #     # print(heap1.Top().post.getText())
    #     # heap1.Delete()

    #     # print('Deleting top element')
    #     # print(heap1.Top().key)
    #     # print(heap1.Top().post.getText())
    #     # heap1.Delete()

    # # This code is contributed by Amartya Ghosh and Faraz Ali
