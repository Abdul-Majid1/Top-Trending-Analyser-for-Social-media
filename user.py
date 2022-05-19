class User():
    def __init__(self, username, password, hobbies):
        self.username = username
        self.password = password
        self.hobbies = []
        for i in hobbies:
            self.hobbies.append(i)
