from distutils import text_file
from tkinter import *
import datetime
from unicodedata import category
from Backend import Data
from Post import Post


# class Post():
#     def __init__(self, user, categories, likes, post_id, texting):
#         self.date_time = datetime.datetime.now()
#         self.post_id = post_id
#         self.likes = 0
#         self.user = user
#         self.categories = categories
#         self.text = texting
#         self.liked_by = []

#     def increase_likes(self, num):
#         self.likes = self.likes+1

#     def getText(self):
#         return self.text

#     def __eq__(self, other):
#         if isinstance(other, Post):
#             return self.post_id == other.post_id
#         return False


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

        # if (self.i+2 < len(self.list_of_posts)):

        #     return_intention = (self.list_of_posts[self.i], self.list_of_posts[self.i+1], self.list_of_posts[self.i+2])
        #     self.i=self.i+3
        # elif (self.i+1 < len(self.list_of_posts)):
        #     return_intention = (self.list_of_posts[self.i], self.list_of_posts[self.i+1] )
        #     self.i=self.i+2
        # elif (self.i < len(self.list_of_posts)):
        #     return_intention = self.list_of_posts[self.i]
        #     self.i=self.i+1
        # else:
        #     return_intention=None

        # return return_intention


root = Tk()
root.title("Chatbot")
root.geometry("1270x720")
post_list = Post_encapsulator()
currentData = Data()
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
post_list.append_post(
    Post("faraz ", ["biking"], 4444, 8, "YOur patience means everything "))
post_list.append_post(
    Post("abdul ", ["Biking"], 248, 1, "The summer Heat is riveting "))
post_list.append_post(
    Post("oqba ", ["Biking"], 267, 3, "hot to worry though "))
post_list.append_post(
    Post("faraz ", ["biking "], 4444, 8, "YOur patience means everything "))
post_list.append_post(
    Post("abdul ", ["Biking"], 248, 1, "YEs the shift does indeed happen "))
post_list.append_post(
    Post("oqba ", ["Biking"], 267, 3, "not to worry though "))
post_list.append_post(
    Post("faraz ", ["Biking"], 4444, 8, "YOur patience means everything "))

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function


def send(username, category):
    send = e.get()
    HOBBY1 = [e2.get(), e3.get()]
    post_list.append_post(
        Post(username, HOBBY1, 0, post_list.increment_post(), send))
    a = post_list.return_top_three(category)
    txt.delete('1.0', END)
    tx1.delete('1.0', END)
    tx2.delete('1.0', END)
    txt.insert(END, a[0].text)
    tx1.insert(END, a[1].text)
    tx2.insert(END, a[2].text)
    currentData.constructHeap(
        Post(username, HOBBY1, 0, post_list.increment_post(), send))
    currentData.printPairingHeap()


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=100, height=10)
txt.grid(row=2, column=0, columnspan=1)
tx1 = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=100, height=10)
tx1.grid(row=5, column=0, columnspan=1)
tx2 = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=100, height=10)
tx2.grid(row=7, column=0, columnspan=1)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
scrollbar1 = Scrollbar(tx1)
scrollbar1.place(relheight=1, relx=0.974)
scrollbar2 = Scrollbar(tx2)
scrollbar2.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)

e.grid(row=2, column=0)


e2 = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e2.grid(row=3, column=0)
e3 = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e3.grid(row=4, column=0)


def checking(text):
    print(text)


def extract_next(category):

    function = post_list.return_next_three(category)
    txt.delete('1.0', END)
    tx1.delete('1.0', END)
    tx2.delete('1.0', END)

    if (len(function) == 3):

        txt.insert(END, function[0].text)
        tx1.insert(END, function[1].text)
        tx2.insert(END, function[2].text)
    elif (len(function) == 2):
        txt.insert(END, function[0].text)
        tx1.insert(END, function[1].text)

    elif len(function) == 1:
        txt.insert(END, function[0].text)
    else:
        next_3.destroy()


def increase_like1():

    if len(post_list.current_indexes) >= 1:
        post_list.list_of_posts[post_list.current_indexes[0]].increase_likes(1)
        # Formula -> Priority
        # y = a(1-b)^x
        # https://stackoverflow.com/questions/32211596/subtract-two-datetime-objects-python
        # currentData.assignPriority(post, priority)
        currentPost = post_list.list_of_posts[post_list.current_indexes[0]]
        currentData.decreasePriority(currentPost, currentPost.currentPriority)
        currentData.printPairingHeap()


def increase_like2():
    if len(post_list.current_indexes) >= 2:
        post_list.list_of_posts[post_list.current_indexes[1]].increase_likes(1)
        currentPost = post_list.list_of_posts[post_list.current_indexes[0]]
        # print(type(currentPost))
        print(f' Current Text = {currentPost.getText()}')
        print(currentPost.getLikes())
        currentData.decreasePriority(currentPost, currentPost.currentPriority)
        currentData.printPairingHeap()
        # print('Test')


def increase_like3():
    if len(post_list.current_indexes) >= 3:
        post_list.list_of_posts[post_list.current_indexes[2]].increase_likes(1)
        currentPost = post_list.list_of_posts[post_list.current_indexes[0]]
        currentData.decreasePriority(currentPost, currentPost.currentPriority)
        currentData.printPairingHeap()


send1 = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
               command=lambda: send("Abdul", ["Biking"])).grid(row=2, column=1)


next_3 = Button(root, text="Next 3", font=FONT_BOLD, bg=BG_GRAY, command=lambda: extract_next(["Biking"])
                ).grid(row=4, column=2)
next_4 = Button(root, text="Like1", font=FONT_BOLD, bg=BG_GRAY, command=lambda: increase_like1()
                ).grid(row=2, column=2)


next_6 = Button(root, text="Like2", font=FONT_BOLD, bg=BG_GRAY, command=lambda: increase_like2()
                ).grid(row=5, column=2)
next_7 = Button(root, text="Like3", font=FONT_BOLD, bg=BG_GRAY, command=lambda: increase_like3()
                ).grid(row=7, column=2)

less = post_list.return_next_three(["Biking"])

i = 0
if i == 0:
    print("dop thisw")
    txt.insert(END, less[0].text)
    tx1.insert(END, less[1].text)
    tx2.insert(END, less[2].text)
    i = i+1
txt.config(state=NORMAL)
tx1.config(state=NORMAL)
tx1.config(state=NORMAL)


# txt.delete('1.0', END)


root.mainloop()
