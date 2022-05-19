from PairingHeap import PairingHeap
from Post import Post


class Data:
    def __init__(self) -> None:
        self.PairingHeap = PairingHeap()
        self.TrendingList = []

    def decreasePriority(self, post: Post, priority: int) -> None:
        print('Backend Priority:')
        print(priority)
        self.PairingHeap.decreaseKey(post, priority)

    def constructHeap(self, post: Post) -> None:
        self.PairingHeap.Insert(post, post.currentPriority)

    def getTopTrending(self) -> Post:
        if self.PairingHeap.Top():
            return self.PairingHeap.Top().post.getText()
        return "No more Trending Posts"

    def printPairingHeap(self):
        for i in self.PairingHeap:
            print(i.post.getText())

    def nextTrending(self) -> Post:
        if self.PairingHeap.Top():
            self.TrendingList.append(self.PairingHeap.Top().post)
            self.PairingHeap.Delete()
            return self.getTopTrending()

    def prevTrending(self) -> Post:
        if len(self.TrendingList) > 0:
            prevPost = self.TrendingList.pop()
            self.PairingHeap.Insert(prevPost, prevPost.currentPriority)
            return self.getTopTrending()
        return "No new stories!"
