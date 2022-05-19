from user import User
class Authentication():

    def __init__(self):
        self.list_of_record = dict()

    def click(self, username, password, hobbies):
        for i in range(len(hobbies)):
            hobbies[i] = hobbies[i].lower()
        user1 = User(username, password, hobbies)
        self.list_of_record[user1.username] = user1

    def check(self, username, password):
        found = self.list_of_record.get(username, False)

        if found:
            # print(found.password)
            if password == found.password:
                return ("Password is correct..... Login Successful", found)
            else:
                return ("Incorrect password", found)

        else:
            return ("No username of this ID was found", found)
