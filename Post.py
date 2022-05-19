import datetime


class Post():
    '''
    A Post interface.
    '''

    def __init__(self, user, categories, likes, post_id, texting) -> None:
        """ Creates a Post type object. Each Post has a user, number of likes, a unique
        post id, Category of the post, the main text body of the post and a list 
        which shows who have liked the post. Current priority is always the negative equivalent
        of current number of likes.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        none
        """
        self.date_time = datetime.datetime.now()
        self.post_id = post_id
        self.likes = 0
        self.user = user
        self.categories = categories
        self.text = texting
        self.liked_by = []
        self.currentPriority = 0

    def increase_likes(self, num) -> None:
        """ Increases the like of the post by one.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        none
        """
        self.likes = self.likes+1
        self.currentPriority -= 1

    def getLikes(self) -> int:
        """ A getter function to return the current number of likes of the post.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        Current Number of likes
        """
        return self.likes

    def getText(self) -> str:
        """ A getter function to return the main text of the post.

        Parameters:
        - self: mandatory reference to this object.

        Returns:
        Text of the post
        """
        return self.text

    def __eq__(self, other) -> bool:
        """ An overridden dunder method that checks if two posts are similar. Both posts
        are compared with their post ids.

        Parameters:
        - self: mandatory reference to this object.
        - other: Post with which the equality is compared.

        Returns:
        A Boolean value
        """
        if isinstance(other, Post):
            return self.post_id == other.post_id
        return False
