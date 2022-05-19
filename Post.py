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
    def __init__(self, user, categories, likes, post_id, texting):
        self.date_time = datetime.datetime.now()
        self.post_id = post_id
        self.likes = 0
        self.user = user
        self.categories = categories
        self.text = texting
        self.liked_by = []
        self.currentPriority = 0

    def increase_likes(self, num):
        self.likes = self.likes+1
        self.currentPriority -= 1

    def getLikes(self):
        return self.likes

    def getText(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.post_id == other.post_id
        return False
