import datetime


# class Post:
#     def __init__(self, textEntry: str, DateTime: datetime) -> None:
#         self.Text = textEntry
#         self.numLikes = 0
#         self.postedOn = DateTime

#     def postLiked(self) -> None:
#         self.numLikes += 1

#     def getText(self):
#         return self.Text

class Post():
    def __init__(self, user, categories, likes, post_id, texting):  #each post posted has these attributes
        self.date_time = datetime.datetime.now()
        self.post_id = post_id   # identifier of the post
        self.likes = 0   # no of likes that the post has 
        self.user = user    # user type object that stores information about who makes the posts 
        self.categories = categories  # list of max two items of the categories the post covers (to show to only those users
        self.text = texting  # the actual text of the post 
        self.liked_by = []
        self.currentPriority = 0     # a priority keeper , since our heap is a min heap , this priority sdecreases on each like so that post reaches top when likes are max 

    def increase_likes(self, num):
        self.likes = self.likes+1  # setter function for likes
        self.currentPriority -= 1   # note that the likes increase the priority decrease as implementation is as a min heapp

    def getLikes(self):
        return self.likes

    def getText(self):
        return self.text

    def __eq__(self, other):   # magic method to compare post_ids (mainly for some internal functionality of pairing heap 
        if isinstance(other, Post):  
            return self.post_id == other.post_id
        return False
