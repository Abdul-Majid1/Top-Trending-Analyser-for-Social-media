from Post import Post

'''
The basic Pairing Heap implementation is taken from
https://www.geeksforgeeks.org/pairing-heap/
Contributed by Amratya Ghosh.
We used this implementation and modified it to match our requirments 
'''


class HeapNode:
    '''
    A Heap Node Interface.
    '''

    def __init__(self, post_=None, key_=None, leftChild_=None, nextSibling_=None) -> None:
        """ Creates a Heap Node with properties Post of Post Type object
        key which is the priority of integer, leftchild and nextSibling pointers

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        none
        """
        self.post = post_
        self.key = post_.currentPriority
        self.leftChild = leftChild_
        self.nextSibling = nextSibling_

    def addChild(self, node: 'HeapNode') -> None:
        """ Creates a Backend with an attribute of type Pairing heap
        and a Trending List that will store the top trending posts

        Parameters:
        - self: mandatory reference to this object.
        - node: HeapNode that is to be added

        Returns:
        none
        """
        if(self.leftChild == None):
            self.leftChild = node
        else:
            node.nextSibling = self.leftChild
            self.leftChild = node

    def __iter__(self) -> 'HeapNode':
        """ Makes it possible to iterate over Nodes. Starting from the
        Root node and traverses level wise

        Parameters:
        - self: mandatory reference to this object.

        Yields:
        HeapNode type object
        """
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


def Empty(node: 'HeapNode') -> bool:
    return (node == None)


def Merge(A: 'HeapNode', B: 'HeapNode') -> 'HeapNode':
    if(A == None):
        return B
    if(B == None):
        return A
    if(A.key < B.key):
        A.addChild(B)
        return A
    B.addChild(A)
    return B


def Top(node: 'HeapNode') -> 'HeapNode':
    return node


def Insert(node: 'HeapNode', post: Post, priority: int) -> 'HeapNode':
    return Merge(node, HeapNode(post, priority))


def TwoPassMerge(node: 'HeapNode') -> 'HeapNode':
    if(node == None or node.nextSibling == None):
        return node
    A = node
    B = node.nextSibling
    newNode = node.nextSibling.nextSibling
    A.nextSibling = None
    B.nextSibling = None
    return Merge(Merge(A, B), TwoPassMerge(newNode))


def Delete(node: 'HeapNode') -> 'HeapNode':
    return TwoPassMerge(node.leftChild)


class PairingHeap:
    '''
    A Pairing Heap Interface
    '''

    def __init__(self) -> None:
        """ Creates a Pairing Heap Type Object

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        none
        """
        self.root = None
        self.TraversalNodes = []
        self.stackOfNodes = []

    def Empty(self) -> bool:
        """ Checks if Pairing Heap has any nodes inserted or is empty

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        Whether The Pairing Heap has any nodes or not
        """
        return Empty(self.root)

    def Top(self) -> 'HeapNode':
        """ Returns the root node of Pairing Heap. 

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        The Top most HeapNode type object
        """
        return Top(self.root)

    def Insert(self, post: Post, priority: int) -> None:
        """ Inserts a post into the Pairing Heap

        Parameters:
        - self: mandatory reference to this object.
        - post: Post that is to be inserted.
        - priority: initial priority of the post.

        Returns:
        none
        """
        self.root = Insert(self.root, post, priority)

    def Delete(self) -> None:
        """ Deletes the top most node of the pairing heap and then performs the two
        pass merge operation to restructure the pairing heap

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        none
        """
        self.root = Delete(self.root)

    def Join(self, other: 'PairingHeap') -> None:
        """ Joins the two pairing heaps into one.

        Parameters:
        - self: mandatory reference to this object.
        - other: The other Pairing Heap object that is to be merged.

        Returns:
        none
        """
        self.root = Merge(self.root, other.root)

    def __iter__(self) -> None:
        """ a dunder function that allows iterating over the pairing heap.

        Parameters:
        - self: mandatory reference to this object.

        Yields:
        HeapNode type object. Each node of the pairing heap.
        """
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

    def find(self, p: Post) -> "tuple(HeapNode, HeapNode, str)":
        """ Traverses the pairing heap and returns the Post p with its previous node.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        A Tuple of Previous Node, CurrentNode and an indicator whether the current
        post is nextSibling or leftChild of prevNode.
        Returns (0, i, indicator) if post is the root node
        Returns (-1, -1, -1) if Post doesn't exist
        """
        for i in self:
            if i.leftChild:
                if i.leftChild.post == p:
                    indicator = 'L'
                    return (i, i.leftChild, indicator)
            if i.nextSibling:
                if i.nextSibling.post == p:
                    indicator = 'N'
                    return (i, i.nextSibling, indicator)
        if i == p:
            indicator = 'R'
            return (0, i, indicator)
        return(-1, -1, -1)

    def decreaseKey(self, post: Post, priority: int) -> 'PairingHeap':
        """ Takes a Post type object, finds it in the Pairing heap and reduces its priority

        Parameters:
        - self: mandatory reference to this object.
        - post: The Post whose priority is to be updated.
        - priority: The updated priority

        Returns:
        self
        """
        prevNode, currentNode, indicator = self.find(post)
        if currentNode.key < priority:
            return
        if prevNode == currentNode == indicator == -1:
            return
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
        return self
