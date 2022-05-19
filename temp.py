from distutils.command import register
from doctest import master
from tkinter import *   
from tkinter import messagebox
from tkinter import ttk
import pickle
# from PIL import ImageTk

class LinearDict():

    '''Overrides and implementes the methods defined in MyDict. Uses a linear
    probing hash table to implement the dictionary.
    '''
    def __init__(self) -> None:
        """Initializes this dictionary.
        Arg+s:
        - self: manadatory reference to this object.
        Returns:
        none
        """
        self.HashTable = [None for _ in range(2*2)]
        self.size=2*2
        self.filled=0
        self.filled_with_marker=0
       
        
    def Hashing(self,keyvalue):
        
        return hash(keyvalue) % self.size
  
    def __setitem__(self, key, newvalue ) -> None:
        """Adds (key, newvalue) to the dictionary, overwriting any prior value.
        dunder method allows assignment using indexing syntax, e.g.
        d[key] = newvalue
        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key to add to the dictionary
        - newvalue: the value to store for the key, overwriting any prior value 
        Returns:
        None
        """
        
        #self.length += 1
        item=(key,newvalue)
        found=False
        hashed_key = self.Hashing(key)
        while self.HashTable[hashed_key]!= None :
            
            if self.HashTable[hashed_key][0] == key :
                 #self.length -= 1
                
                break
            hashed_key=hashed_key+1
            if (hashed_key>self.size-1):
                hashed_key=hashed_key% self.size     
    
        self.HashTable[hashed_key]=item
        self.filled=self.filled+1
        self.filled_with_marker=self.filled_with_marker+1
        if self.filled_with_marker>=0.8*self.size:
               
            self.resize_up()



    def resize_up(self):
         self.size *= 2
         self.filled_with_marker=0
         self.filled=0
         old_table =(self.HashTable)
         
         self.HashTable= [None for i in range(0,self.size)]
         
         for tuple in old_table:
            
            if tuple is not  None and  tuple!="$$":
                 self.__setitem__(tuple[0],tuple[1])
    def get(self, key, default) :

        """Returns the value stored for key, default if no value exists.
        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key whose value is sought.
        - default: the value to return if key does not exist in this dictionary
        Returns:
        the stored value for key, default if no such value exists.
        """
        
        hashed_key = self.Hashing(key)
        found=False
        while self.HashTable[hashed_key]!= None :
            if self.HashTable[hashed_key][0] == key:
                 #self.length -= 1
                found=True 
                break
            hashed_key=hashed_key+1
            if (hashed_key>self.size-1):
                hashed_key=hashed_key% self.size     
        if found==True:
            return self.HashTable[hashed_key][1] # if it is found we just return the value of that key 
        else:
            return  default 
        
            


    def items(self) :
        """Returns the key-value pairs of the dictionary as tuples in a list.
        
        Args:
        - self: manadatory reference to this object.
        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        lst=[]
        # since our data was already in the key value pair we just traverse the whole list and skipp where None and append into a list
        for i in range (0 ,self.size):
            if self.HashTable[i]!=None:
                lst.append(self.HashTable[i])
        return lst               

    def clear(self) -> None:
        """Clears the dictionary.
        Args:
        - self: manadatory reference to this object.
        Returns:
        None.
        """
        # Just the __init__ called in clear to empty the hashtable 
        self.HashTable = [None for _ in range(2*2)]
        self.size=2*2
        self.filled=0
        self.filled_with_marker=0
# dictionary= LinearDict()


class User():
    def __init__(self, username, password):
        self.username=username 
        self.password=password
        # self.hobbies=[]
        # for i in hobbies:
        #     self.hobbies.append(i)

    

class Authentication():

    def __init__(self):
        self.list_of_record=dict()

    def click(self, username, password):
        user1=User(username,password)
        self.list_of_record[user1.username]=user1
        print(self.list_of_record[user1.username])
    
    def check(self,username,password):
        found=self.list_of_record.get(username,False)
        
        if found:
            # print(found.password)
            if password == found.password:
                return  "Password is correct..... Login Successful"
            else:
                return "Incorrect password"

        else:
            return "No username of this ID was foud"
            
authentication=Authentication()
authentication.click("oqba", "abdul")

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

class loginpage(Frame):#login page
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root        # this will create a window and between this and main loop we have to work for GUI
        self.authentication = Authentication()
        self.authentication.click("oqba", "abdul")
        self.root.title("Login Page")
        self.root.geometry('1280x720')   
        self.root.resizable(False, False)
        # register_frame=Frame(self.root, borderwidth=2, relief='sunken', bg="white", bd='10')
        # register_frame.place(x=0, y=0,height = 720, width =1280 ) 
        # self.b = PhotoImage(file = "login.png")
        # Label(register_frame, image=self.b).place(x=0, y=0, relwidth = 1, relheight = 1)
        
        def Message(Text):
            messagebox.showinfo("Message", Text)

        canvas1 = Canvas(self.root, width = 1280, height = 720)    
        self.b = PhotoImage(file = "login.png")                   
        canvas1.create_image( 0, 0, image = self.b)
        Label(self.root, image=self.b, width='2000', height='4000').pack()

        login_frame = Frame(self.root,borderwidth=2, relief='sunken', bg="white", bd='10')
        login_frame.place(x=250, y=110,height = 500, width = 800)  
        
        label = Label(login_frame,text="Login Here", font=("Bebas Neue", 35, "bold"), fg='#405898', bg="white").place(x=125, y=0) 
        
        label1 = Label(login_frame,text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=120) 
        self.E1= Entry(login_frame,bd=2.5, bg = "lightgray")                    #--> create an Entry for user to write his name 
        self.E1.place(x=170,y=120, width=200, height = 30)
        
        label2 = Label(login_frame,text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=170) 
        self.E2= Entry(login_frame,bd=2.5, bg = "lightgray")                    #--> create an Entry for user to write his name 
        self.E2.place(x=170,y=170, width=200, height = 30)

        signup_button=Button(login_frame, text='SignUp',command='c', padx=5, pady=5,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15), bd=5)
        signup_button.place(x=160, y=230)    
        
        def _login():
            user = self.E1.get()
            password= self.E2.get()
            if self.authentication.check(user, password) == "Password is correct..... Login Successful":
                login_frame.destroy() 
                self.post_frame = Frame(self.root,borderwidth=2, relief='sunken', bg="white", bd='10')
                self.post_frame.place(x=0, y=0,height = 720, width = 1280) 
            else: 
                Message(self.authentication.check(user, password))


            # print(self.authentication.check(user, password))
        login_button=Button(login_frame, text='LogIn',command=_login, padx=5, pady=5,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15), bd=5)
        login_button.place(x=300, y=230)    
        
        def login_to_registeration(root):
            login_frame.destroy() 
            self.curr_register_frame=Frame(self.root, borderwidth=2, relief='sunken', bg="#405898", bd='10')
            self.curr_register_frame.place(x=0, y=0,height = 720, width =1380) 
            
            information_frame = Frame(self.curr_register_frame, borderwidth=0.5, relief='sunken', bg="white", bd='10')
            information_frame.place(x=200, y=50,height = 600, width =900)
            
            back_button=Button(information_frame, text='Back',command=back, padx=5, pady=5,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15, 'bold'), bd=5)
            back_button.place(x=170, y=300)

            label3 = Label(information_frame,text="Username", font=("Goudy old style", 15, "bold"), fg='gray', bg="white").place(x=50, y=120) 
            self.E3= Entry(information_frame,bd=2.5, bg = "lightgray")                    #--> create an Entry for user to write his name 
            self.E3.place(x=170,y=110, width=200, height = 40)
            
            label4 = Label(information_frame,text="Password", font=("Goudy old style", 15, "bold"), fg='gray', bg="white").place(x=50, y=170) 
            self.E4 = Entry(information_frame,bd=2.5, bg = "lightgray")                    #--> create an Entry for user to write his name 
            self.E4.place(x=170,y=170, width=200, height = 40)

            label5 = Label(information_frame,text="Hobbies", font=("Goudy old style", 15, "bold"), fg='gray', bg="white").place(x=50, y=235) 
            self.E5 = Entry(information_frame,bd=2.5, bg = "lightgray")                    #--> create an Entry for user to write his name 
            self.E5.place(x=170,y=235, width=200, height = 40)
        

            register_button=Button(information_frame, text='NEXT',command=Post, padx=5, pady=5,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15,'bold'), bd=5)
            register_button.place(x=300, y=300)

        signup_button.bind('<Button-1>', login_to_registeration)

        def Post():
            user = self.E3.get()
            password = self.E4.get()
            # hobbies = self.E5.get()
            self.authentication.click(user, password)
            print(self.authentication.click(user, password))
            # self.curr_register_frame.destroy()
            # post_frame = Frame(self.root,borderwidth=2, relief='sunken', bg="white", bd='10')
            # post_frame.place(x=0, y=0,height = 720, width = 1280) 

        
        def back():
            self.curr_register_frame.destroy()
            login_frame = Frame(self.root,borderwidth=2, relief='sunken', bg="white", bd='10')
            login_frame.place(x=250, y=110,height = 500, width = 800)  
            
            label = Label(login_frame,text="Login Here", font=("Bebas Neue", 35, "bold"), fg='#405898', bg="white").place(x=125, y=0) 
            
            label1 = Label(login_frame,text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=120) 
            self.E1= Entry(login_frame,bd=2.5, bg = "lightgray")                    #--> create an Entry for user to write his name 
            self.E1.place(x=170,y=120, width=200, height = 30)
            
            label2 = Label(login_frame,text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=170) 
            self.E2= Entry(login_frame,bd=2.5, bg = "lightgray")                    #--> create an Entry for user to write his name 
            self.E2.place(x=170,y=170, width=200, height = 30)

            signup_button=Button(login_frame, text='SignUp',command='c', padx=5, pady=5,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15), bd=5)
            signup_button.place(x=160, y=230)    
            signup_button.bind('<Button-1>', login_to_registeration)
            
            login_button=Button(login_frame, text='LogIn',command='c', padx=5, pady=5,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15), bd=5)
            login_button.place(x=300, y=230) 
           
            

        



















# class registerpage(Frame):#register page
#     print("here")
#     def __init__(self, root):
#         print("here")
#         Frame.__init__(self, root)
#         Button(self, text="Return to start page", command=lambda: root.switch_frame(loginpage)).pack()

# class PageTwo(Frame):#after login
#     def __init__(self, root):
#         Frame.__init__(self, root)
#         Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
#         Button(self, text="Return to start page",
#                   command=lambda: root.switch_frame(loginpage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()