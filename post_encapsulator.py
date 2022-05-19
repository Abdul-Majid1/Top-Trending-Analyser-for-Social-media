
class Post_encapsulator():
    def __init__(self):
        self.list_of_posts = []
        self.i = 0
        self.current_indexes = []
        self.post_number = 0

    def increment_post(self):
        self.post_number = self.post_number+1
        return self.post_number

    def append_post(self, Post):
        self.list_of_posts.insert(0, Post)

    def return_next_three(self, category):

        return_intention = []
        self.current_indexes = []

        def check_similar(a, b):
            for i in a:
                for j in b:
                    if i == j:
                        return True

        for i in range(self.i, len(self.list_of_posts)):
            if check_similar(self.list_of_posts[i].categories, category):

                return_intention.append(self.list_of_posts[i])
                self.current_indexes.append(i)
            self.i = self.i+1
            if len(return_intention) == 3:
                break
        return return_intention

    def return_top_three(self, category):
        def check_similar(a, b):
            for i in a:
                for j in b:
                    if i == j:
                        return True
            return False
        return_intention = []
        self.current_indexes = []
        self.i = 0

        for i in range(self.i, len(self.list_of_posts)):

            if check_similar(self.list_of_posts[i].categories, category):

                return_intention.append(self.list_of_posts[i])
                self.current_indexes.append(i)
            self.i = self.i+1
            if len(return_intention) == 3:
                break

        return return_intention
