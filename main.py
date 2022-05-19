from distutils.command import register
from doctest import master
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
import pickle
import datetime
from unicodedata import category
from Backend import Data
from Post import Post
import tkinter as tk
from tkinter import ttk
from post_encapsulator import Post_encapsulator





class User():
    def __init__(self, username, password, hobbies):
        self.username = username
        self.password = password
        self.hobbies = []
        for i in hobbies:
            self.hobbies.append(i)


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


authentication = Authentication()
authentication.click("oqba", "abdul", ["fishing", "farming"])


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(loginpage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class loginpage(Frame):  # login page

    def top_trending(self):  # Code when opening the new window when the top trensing button is clicked 
        window1 = Toplevel()   # tkinter object to show new window on top of the other
        window1.geometry("1280x720")

       
        login_frame1 = Frame(window1, borderwidth=2,
                             relief='sunken', bg="white", bd='2', width=1280, height=720) #this is just for teending frame
        BG_GRAY = "#ABB2B9"
        BG_COLOR = "#17202A"
        TEXT_COLOR = "#EAECEE"       # ALL these lines are tkinter specifications for design 
        FONT = "Helvetica 14"
        FONT_BOLD = "Helvetica 13 bold"

        canvas10 = Canvas(login_frame1, width=1280, height=720)# for the image in  the trending page
        self.b10 = PhotoImage(file="post.png")
        canvas10.create_image(0, 0, image=self.b10)
        Label(login_frame1, image=self.b10, width='1280', height='720').pack()

        label3 = Label(login_frame1, text="Top trending Now", font=(
            "Goudy old style", 20, "bold"), fg='white', bg='purple').place(x=720, y=150)

        txte = Text(login_frame1, bg='#D6C5F1',
                    fg="black", font=15, width=45, height=15)
        txte.place(x=580, y=200)
        txte.config(state=NORMAL)
        txte.insert(END, self.currentData.getTopTrending())
        login_frame1.place(x=0, y=0, height=720, width=1280)
        # These next two buttons call the relevant functions to toggle between the next most liked or previous less liked posts in the trending page( see binded functions)
        nextPost = Button(login_frame1, text="Next", font=15, bg="purple", fg="white", command=lambda: self.nextTrending(
            txte), width='10', height='5').place(x=200, y=270)  # 700by580
        prevPost = Button(login_frame1, text="Previous", font=15, bg="purple", fg="white",
                          command=lambda: self.prevTrending(txte), width='10', height='5').place(x=400, y=270)
       

        window1.mainloop()

        

    def nextTrending(self, text):
        text.delete('1.0', END)       #deletes item in the textbox
        text.insert(END, self.currentData.nextTrending()) # calls the pairing heap functionality for the next most liked post

    def prevTrending(self, text):
        text.delete("1.0", END)
        text.insert(END, self.currentData.prevTrending())   # calls the pairing heap functionality for the next most liked post

    def __init__(self, root):
        Frame.__init__(self, root)
        # this will create a window and between this and main loop we have to work for GUI
        self.root = root
        self.authentication = Authentication()
        self.authentication.click("oqba", "abdul", ["biking", "farming"])
        f1 = open('userfile.txt', 'r')    # This code basically just writes the usernames and password in a file to be retrieved next time the file opens so that username stay can be accessed 
        for line in f1:

            lineElem = line.strip('\n').split(" ")
            self.authentication.click(lineElem[0],lineElem[1],[lineElem[2]])
        self.root.title("Top Trending Blogs - Pairing Heap")
        self.root.geometry('1280x720')
        self.root.resizable(False, False)
        self.post_list = Post_encapsulator()   # post encapsulator object to keep all the posts 
        self.currentData = Data()    # data type object that maintains the pairing heap
        
        # some initial default posts for testing and other such purposes 
        self.post_list.append_post(
            Post("faraz ", ["biking"], 4444, 8, "Your patience means everything "))
        self.post_list.append_post(
            Post("abdul ", ["biking"], 248, 1, "The summer Heat is riveting "))
        self.post_list.append_post(
            Post("oqba ", ["biking"], 267, 3, "hot to worry though "))
        self.post_list.append_post(
            Post("faraz ", ["biking"], 4444, 8, "Your patience means everything "))
        self.post_list.append_post(
            Post("abdul ", ["biking"], 248, 1, "YEs the shift does indeed happen "))
        self.post_list.append_post(
            Post("oqba ", ["biking"], 267, 3, "not to worry though "))
        self.post_list.append_post(
            Post("faraz ", ["biking"], 4444, 8, "Your patience means everything "))
        self.post_list.append_post(
            Post("faraz ", ["podcasting"], 4444, 8, "test podcast "))
        self.post_list.append_post(
            Post("faraz ", ["podcasting"], 4444, 3, "test podcast 1"))
        self.post_list.append_post(
            Post("faraz ", ["podcasting"], 4444, 8, "test podcast 3"))
        # This 
        for i in self.post_list.list_of_posts:
            self.currentData.constructHeap(i)

        def Message(Text):
            messagebox.showinfo("Message", Text)

        login_frame = Frame(self.root, borderwidth=2,
                            relief='sunken', bg="white", bd='2') # login frame
        login_frame.place(x=0, y=0, height=720, width=1280)

        canvas1 = Canvas(login_frame, width=1280, height=720)# image for login frame
        self.b = PhotoImage(file="login3.png")
        canvas1.create_image(0, 0, image=self.b)
        Label(login_frame, image=self.b, width='1280', height='720').pack()

        self.E1 = Entry(login_frame, bd=0, bg="white") #entries for username and password
        self.E1.place(x=780, y=280, width=245, height=30)

        # --> create an Entry for user to write his name
        self.E2 = Entry(login_frame, bd=0, bg="white", show="*")
        self.E2.place(x=780, y=377, width=245, height=30)

        self.b1 = PhotoImage(file="registershape.png")
        signup_button = Button(login_frame, text='SignUp', command='c', image=self.b1, relief='sunken', padx=5, pady=5,
                               activebackground='white', activeforeground='red', bg='white', fg='black', font=('Bebas Neue', 15), bd=0, height='30', width='120')
        signup_button.place(x=837, y=507)

        def _login():
            user = self.E1.get()  # This gets the entry type object entries 
            password = self.E2.get()
            if self.authentication.check(user, password)[0] == "Password is correct..... Login Successful":
                # This is for the login functionality and user authentication
                # print(self.authentication.check(user, password)[1])
                self.current_user = self.authentication.check(user, password)[
                    1]    
                login_frame.destroy()
                self.post_list.i = 0 # since new frame was made post iterator is set to zero 

                self.post_main_frame = Frame(
                    self.root, borderwidth=2, relief='sunken', bg="white", bd='1')
                self.post_main_frame.place(x=0, y=0, height=720, width=1280)

                canvas5 = Canvas(self.post_main_frame, width=1280, height=720) #post image and frame
                self.b5 = PhotoImage(file="post.png")
                canvas5.create_image(0, 0, image=self.b5)
                Label(self.post_main_frame, image=self.b5,
                      width='1280', height='720').pack()
               
                BG_GRAY = "#ABB2B9"
                BG_COLOR = "#17202A"
                TEXT_COLOR = "#EAECEE"
               
                FONT = "Helvetica 14"
                FONT_BOLD = "Helvetica 13 bold"

                def send(username, category):
                    send = maintxt.get(1.0, "end-1c") # This gets textbox entries so that posts can be made when the send button is pressed
                    HOBBY1 = [e2.get().lower()]
                    currentPost = Post(username, HOBBY1, 0,
                                       self.post_list.increment_post(), send)  # actually appending the new post after getting the textbox entries 
                    self.post_list.append_post(currentPost) 
                    a = self.post_list.return_top_three(category) # returning nrew three posts after the current insertion
                    txt.delete('1.0', END)
                    tx1.delete('1.0', END)
                    tx2.delete('1.0', END)
                    txt.insert(END, a[0].text)   # showing the new three elements in the textboxes after the updation
                    tx1.insert(END, a[1].text)
                    tx2.insert(END, a[2].text)
                    print("Inserting in heap")
                    self.currentData.constructHeap(currentPost)  # adding the post in the heap with the 0 likes initially for the maintainance 
                    self.currentData.printPairingHeap()

                txt = Text(self.post_main_frame, bg='#D6C5F1',
                           fg="black", font=FONT, width=30, height=6) #texts box to display posts input by the user
                txt.place(x=640, y=80)
                tx1 = Text(self.post_main_frame, bg='#D6C5F1',
                           fg="black", font=FONT, width=30, height=6)
                tx1.place(x=640, y=260)
                tx2 = Text(self.post_main_frame, bg='#D6C5F1',
                           fg="black", font=FONT, width=30, height=6)
                tx2.place(x=640, y=440)

                label_main = Label(self.post_main_frame, text="P O S T  H E R E", font=(
                    "Product Sans", 25, "bold"), bg="#8955E3", fg="white").place(x=205, y=73)
                maintxt = Text(self.post_main_frame, bg="#D6C5F1", fg="black", font=("Times New Roman", 15, "bold"),
                               width=30, height=7, bd=10, insertborderwidth=10, spacing2=2, spacing1=2, spacing3=2, wrap=CHAR)
                maintxt.place(x=200, y=170)
                label_main1 = Label(self.post_main_frame, text="I N T E R E S T S", font=(
                    "comic Sans", 25, "bold"), bg="#8955E3", fg="white").place(x=205, y=420)
                e2 = Entry(self.post_main_frame, bg="#D6C5F1",
                           fg="white", font=FONT, width=30) #entries for the interest and the text box above is for entering post
                e2.place(x=200, y=490)
#                 e3 = Entry(self.post_main_frame, bg="#D6C5F1",
#                            fg="white", font=FONT, width=30)
#                 e3.place(x=200, y=550)

                def checking(text):
                    print(text)

                def extract_next(category):
                    # functionality  for the next button 
                    function = self.post_list.return_next_three(category) # brings the next three posts in line 
                    txt.delete('1.0', END)
                    tx1.delete('1.0', END)
                    tx2.delete('1.0', END)

                    if (len(function) == 3):
                          # if three more posts exist then show those three posts 
                        txt.insert(END, function[0].text)
                        tx1.insert(END, function[1].text)
                        tx2.insert(END, function[2].text)
                    elif (len(function) == 2):
                        # if only two more exist then just show the next two
                        txt.insert(END, function[0].text)
                        tx1.insert(END, function[1].text)

                    elif len(function) == 1:
                        # if there is only one more post then justupdate that and leave the other two empty
                        txt.insert(END, function[0].text)
                    else:
                        next_3.destroy()

                def increase_like1():

                    if len(self.post_list.current_indexes) >= 1:
                        self.post_list.list_of_posts[self.post_list.current_indexes[0]].increase_likes(
                            1)  # Increwase the like attribute of the post index that is in textbox 0 i,.e first post
                        # Formula -> Priority
                        # y = a(1-b)^x
                        # https://stackoverflow.com/questions/32211596/subtract-two-datetime-objects-python
                        # currentData.assignPriority(post, priority)
                        currentPost = self.post_list.list_of_posts[self.post_list.current_indexes[0]]
                        print(
                            f'Text of current post = {currentPost.getText()}')
                        
                        # like has increased so call the decrease key function in the pairing heap
                        self.currentData.decreasePriority(
                            currentPost, currentPost.currentPriority)
                        self.currentData.printPairingHeap()
                    
                def increase_like2():
                    
                    
                    #same sunctionality as the like 1 but this time for teh second post
                    
                    if len(self.post_list.current_indexes) >= 2:
                        if  self.current_user.username not in self.post_list.list_of_posts[self.post_list.current_indexes[1]].liked_by:
                                
                            self.post_list.list_of_posts[self.post_list.current_indexes[1]].increase_likes(
                                1)
                            currentPost = self.post_list.list_of_posts[self.post_list.current_indexes[1]]
                            # print(type(currentPost))
                            print(f' Current Text = {currentPost.getText()}')
                            print(currentPost.getLikes())
                            self.currentData.decreasePriority(
                                currentPost, currentPost.currentPriority)
                            self.currentData.printPairingHeap()
                            # print('Test')
                        
                def increase_like3():
                    # same functionality as that for like 1 but this time for the third post that is showing 
                    if len(self.post_list.current_indexes) >= 3:
                        self.post_list.list_of_posts[self.post_list.current_indexes[2]].increase_likes(
                            1)
                        currentPost = self.post_list.list_of_posts[self.post_list.current_indexes[2]]
                        self.currentData.decreasePriority(
                            currentPost, currentPost.currentPriority)
                        self.currentData.printPairingHeap()

                send1 = Button(self.post_main_frame, text="Post", font=FONT_BOLD, bg="#13A4FC", fg="white",
                               command=lambda: send(self.current_user.username, self.current_user.hobbies)).place(x=465, y=135)

                print(self.current_user.hobbies)
                
                
                #These are the buttons showing in the comment pages 
                next_3 = Button(self.post_main_frame, text="Next 3", font=FONT_BOLD, bg="#13A4FC", fg="white", command=lambda: extract_next(self.current_user.hobbies)
                                ).place(x=700, y=580) #button for next 3 posts
                next_4 = Button(self.post_main_frame, text="Like", font=FONT_BOLD, bg="#13A4FC", fg="white", command=lambda: increase_like1()
                                ).place(x=640, y=218)

                next_6 = Button(self.post_main_frame, text="Like", font=FONT_BOLD, bg="#13A4FC", fg="white", command=lambda: increase_like2()
                                ).place(x=640, y=400) #button for like
                next_7 = Button(self.post_main_frame, text="Like", font=FONT_BOLD, bg="#13A4FC", fg="white", command=lambda: increase_like3()
                                ).place(x=640, y=580)
                next_8 = Button(self.post_main_frame, text="View Trending Post", font=FONT_BOLD, bg="#13A4FC", fg="white", command=lambda: self.top_trending()
                                ).place(x=785, y=580)
                logout = Button(self.post_main_frame, text="Logout", font=FONT_BOLD, bg="#13A4FC", fg="white", command=lambda: goback()
                                ).place(x=10, y=10)
                 # this is to show the first three comments
                less = self.post_list.return_next_three(
                    self.current_user.hobbies)
                print(self.current_user.hobbies)
                print(less)
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

            else:
                Message(self.authentication.check(user, password)[0])

            # print(self.authentication.check(user, password))
        self.b2 = PhotoImage(file="loginshape.png")

        login_button = Button(login_frame, text='LogIn', command=_login, image=self.b2, relief='sunken', padx=5, pady=5,  activebackground='light blue',
                              activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15), bd=0, height='30', width='120')
        login_button.place(x=840, y=450)
        self.b3 = PhotoImage(file="gobackshape.png")
        # self.b4 = PhotoImage(file = "registershape.png")

        def login_to_registeration(root): #you will see alot of destroy function we use this to change the wndow deame and for displaying other opage of our application
            login_frame.destroy()
            
            self.information_frame = Frame(
                self.root, borderwidth=0.5, relief='sunken', bg="white", bd='0')
            self.information_frame.place(x=0, y=0, height=720, width=1280)

            canvas2 = Canvas(self.information_frame, width=1280, height=720)
            self.b = PhotoImage(file="registerscreen.png")
            canvas2.create_image(0, 0, image=self.b)
            Label(self.information_frame, image=self.b,
                  width='1280', height='720').pack()

            back_button = Button(self.information_frame, text='Back', command=back, image=self.b3, padx=5, pady=2,
                                 activebackground='purple', bg='purple', fg='white', font=('Bebas Neue', 15, 'bold'), bd=0, height='30', width='120')
            back_button.place(x=854, y=530)

            self.E3 = Entry(self.information_frame, bd=0, bg="white") #username and password for registration or signup
            self.E3.place(x=793, y=243, width=245, height=30)

            self.E4 = Entry(self.information_frame, bd=0, bg="white")
            self.E4.place(x=793, y=340, width=245, height=30)

            self.E5 = Entry(self.information_frame, bd=0, bg="white")
            self.E5.place(x=793, y=449, width=245, height=30)
            selected_month = tk.StringVar()
            self.interest = ttk.Combobox(
                self.information_frame, textvariable=selected_month, width=37)
            lst = ["Data structures", "Podcasting", "Blogging",
                   "Marketing", "Sports", "Politics", "studies"]
            self.interest.place(x=795, y=457)

            self.interest['values'] = [lst[i] for i in range(0, len(lst))]
            self.interest['state'] = 'readonly'
            self.interest.bind('<<ComboboxSelected>>', registeration)
            register_button = Button(self.information_frame, command=registeration, image=self.b1, padx=0, pady=0,
                                     activeforeground='red', bg='#7F38EC', fg='white', font=('Bebas Neue', 15, 'bold'), bd=0, height='30', width='120')
            register_button.place(x=850, y=584)

        signup_button.bind('<Button-1>', login_to_registeration)
        
        # This is to save the user names and passwords for the users so they are saved next time the application opens 
        def addToFile(user, password, hobbies):
            f = open('userfile.txt', "a")
            f.write(user + " " + password + " " + str(hobbies) + "\n")
        def registeration():
            user = self.E3.get()
            password = self.E4.get()
            # hobbies = self.E5.get()
            hobbies = self.interest.get()
            # This pices of code just obtains the username and hobbies that the user wants to register with and adds it into out backend 
            self.authentication.click(user, password, [hobbies.lower()])
            addToFile(user,password,hobbies)

        def goback():
            self.post_main_frame.destroy()
            login_frame = Frame(self.root, borderwidth=2,
                                relief='sunken', bg="white", bd='2')
            login_frame.place(x=0, y=0, height=720, width=1280)

            canvas1 = Canvas(login_frame, width=1280, height=720)
            self.b = PhotoImage(file="login3.png")
            canvas1.create_image(0, 0, image=self.b)
            Label(login_frame, image=self.b, width='1280', height='720').pack()

            self.E1 = Entry(login_frame, bd=0, bg="white")
            self.E1.place(x=780, y=280, width=245, height=30)

            self.E2 = Entry(login_frame, bd=0, bg="white", show="*")
            self.E2.place(x=780, y=377, width=245, height=30)

            self.b1 = PhotoImage(file="registershape.png")
            signup_button = Button(login_frame, text='SignUp', command='c', image=self.b1, relief='sunken', padx=5, pady=5,
                                   activebackground='white', activeforeground='red', bg='white', fg='black', font=('Bebas Neue', 15), bd=0, height='30', width='120')
            signup_button.place(x=837, y=507)
            signup_button.bind('<Button-1>', login_to_registeration) #signup button

            self.b2 = PhotoImage(file="loginshape.png")
            login_button = Button(login_frame, text='LogIn', command=_login, image=self.b2, relief='sunken', padx=5, pady=5,  activebackground='light blue',
                                  activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15), bd=0, height='30', width='120')
            login_button.place(x=840, y=450)

        def back():
            self.information_frame.destroy()
            login_frame = Frame(self.root, borderwidth=2,
                                relief='sunken', bg="white", bd='2')
            login_frame.place(x=0, y=0, height=720, width=1280)

           
            canvas1 = Canvas(login_frame, width=1280, height=720)
            self.b = PhotoImage(file="login3.png")
            canvas1.create_image(0, 0, image=self.b)
            Label(login_frame, image=self.b, width='1280', height='720').pack()

           
            self.E1 = Entry(login_frame, bd=0, bg="white")
            self.E1.place(x=780, y=280, width=245, height=30)

            
            self.E2 = Entry(login_frame, bd=0, bg="white", show="*")
            self.E2.place(x=780, y=377, width=245, height=30)

            self.b1 = PhotoImage(file="registershape.png")
            signup_button = Button(login_frame, text='SignUp', command='c', image=self.b1, relief='sunken', padx=5, pady=5,
                                   activebackground='white', activeforeground='red', bg='white', fg='black', font=('Bebas Neue', 15), bd=0, height='30', width='120')
            signup_button.place(x=837, y=507)
            signup_button.bind('<Button-1>', login_to_registeration)

            self.b2 = PhotoImage(file="loginshape.png")
            login_button = Button(login_frame, text='LogIn', command=_login, image=self.b2, relief='sunken', padx=5, pady=5,  activebackground='light blue',
                                  activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15), bd=0, height='30', width='120')
            login_button.place(x=840, y=450)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
