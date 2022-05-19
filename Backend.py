from PairingHeap import PairingHeap
from Post import Post


class Data:
    '''
    A Backend Data Interface.
    '''

    def __init__(self) -> None:
        """ Creates a Backend with an attribute of type Pairing heap
        and a Trending List that will store the top trending posts

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        none
        """
        self.PairingHeap = PairingHeap()
        self.TrendingList = []

    def decreasePriority(self, post: Post, priority: int) -> None:
        """ A function that takes a Post type object and applies DecreaseKey operation.

        Parameters:
        - self: mandatory reference to this object.
        - Post: The Post whose priority needs to be changed 
        - Priority: The updated priority

        Returns:
        None
        """
        self.PairingHeap.decreaseKey(post, priority)

    def constructHeap(self, post: Post) -> None:
        """ A function that takes a Post type object and inserts it into 
        the Pairing Heap

        Parameters:
        - self: mandatory reference to this object.
        - Post: The Post whose priority needs to be changed 

        Returns:
        None
        """
        self.PairingHeap.Insert(post, post.currentPriority)

    def getTopTrending(self) -> Post:
        """ A function that returns the top most trending post.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        The text of the Post type object
        """
        if self.PairingHeap.Top():
            return self.PairingHeap.Top().post.getText()
        return "No more Trending Posts"

    def printPairingHeap(self):
        """ A helper function to iterate over the Paiting Heap and print each Post's text.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        None
        """
        for i in self.PairingHeap:
            print(i.post.getText())

    def nextTrending(self) -> Post:
        """ A function that removes the current Trending Post
        adds the Post into self.TrendingList and then returns the next most
        Trending Post in the Pairing Heap.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        Post Type Object
        """
        if self.PairingHeap.Top():
            self.TrendingList.append(self.PairingHeap.Top().post)
            self.PairingHeap.Delete()
            return self.getTopTrending()

    def prevTrending(self) -> Post:
        """ A function that pops the last most element of self.TrendingList
        and adds it back into the Pairing Heap which automatically 
        brings it to the top again. Making it the most trending post or the
        root of Pairing Heap. Function then returns Trending Post.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        Post Type Object
        """
        if len(self.TrendingList) > 0:
            prevPost = self.TrendingList.pop()
            self.PairingHeap.Insert(prevPost, prevPost.currentPriority)
            return self.getTopTrending()
        return "No new stories!"
