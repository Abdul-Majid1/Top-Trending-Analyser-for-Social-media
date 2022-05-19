# class LinearDict():

#     '''Overrides and implementes the methods defined in MyDict. Uses a linear
#     probing hash table to implement the dictionary.
#     '''
#     def __init__(self) -> None:
#         """Initializes this dictionary.
#         Arg+s:
#         - self: manadatory reference to this object.
#         Returns:
#         none
#         """
#         self.HashTable = [None for _ in range(2*2)]
#         self.size=2*2
#         self.filled=0
#         self.filled_with_marker=0
       
        
#     def Hashing(self,keyvalue):
        
#         return hash(keyvalue) % self.size
  
#     def __setitem__(self, key, newvalue ) -> None:
#         """Adds (key, newvalue) to the dictionary, overwriting any prior value.
#         dunder method allows assignment using indexing syntax, e.g.
#         d[key] = newvalue
#         key must be hashable by pytohn.
        
#         Args:
#         - self: manadatory reference to this object.
#         - key: the key to add to the dictionary
#         - newvalue: the value to store for the key, overwriting any prior value 
#         Returns:
#         None
#         """
        
#         #self.length += 1
#         item=(key,newvalue)
#         found=False
#         hashed_key = self.Hashing(key)
#         while self.HashTable[hashed_key]!= None :
            
#             if self.HashTable[hashed_key][0] == key :
#                  #self.length -= 1
                
#                 break
#             hashed_key=hashed_key+1
#             if (hashed_key>self.size-1):
#                 hashed_key=hashed_key% self.size     
    
#         self.HashTable[hashed_key]=item
#         self.filled=self.filled+1
#         self.filled_with_marker=self.filled_with_marker+1
#         if self.filled_with_marker>=0.8*self.size:
               
#             self.resize_up()



#     def resize_up(self):
#          self.size *= 2
#          self.filled_with_marker=0
#          self.filled=0
#          old_table =(self.HashTable)
         
#          self.HashTable= [None for i in range(0,self.size)]
         
#          for tuple in old_table:
            
#             if tuple is not  None and  tuple!="$$":
#                  self.__setitem__(tuple[0],tuple[1])
#     def get(self, key, default) :

#         """Returns the value stored for key, default if no value exists.
#         key must be hashable by pytohn.
        
#         Args:
#         - self: manadatory reference to this object.
#         - key: the key whose value is sought.
#         - default: the value to return if key does not exist in this dictionary
#         Returns:
#         the stored value for key, default if no such value exists.
#         """
        
#         hashed_key = self.Hashing(key)
#         found=False
#         while self.HashTable[hashed_key]!= None :
#             if self.HashTable[hashed_key][0] == key:
#                  #self.length -= 1
#                 found=True 
#                 break
#             hashed_key=hashed_key+1
#             if (hashed_key>self.size-1):
#                 hashed_key=hashed_key% self.size     
#         if found==True:
#             return self.HashTable[hashed_key][1] # if it is found we just return the value of that key 
#         else:
#             return  default 
        
            


#     def items(self) :
#         """Returns the key-value pairs of the dictionary as tuples in a list.
        
#         Args:
#         - self: manadatory reference to this object.
#         Returns:
#         the key-value pairs of the dictionary as tuples in a list.
#         """
#         lst=[]
#         # since our data was already in the key value pair we just traverse the whole list and skipp where None and append into a list
#         for i in range (0 ,self.size):
#             if self.HashTable[i]!=None:
#                 lst.append(self.HashTable[i])
#         return lst               

#     def clear(self) -> None:
#         """Clears the dictionary.
#         Args:
#         - self: manadatory reference to this object.
#         Returns:
#         None.
#         """
#         # Just the __init__ called in clear to empty the hashtable 
#         self.HashTable = [None for _ in range(2*2)]
#         self.size=2*2
#         self.filled=0
#         self.filled_with_marker=0
# dictionary= LinearDict()


# class Authentication():

#     def __init__(self):
#         self.list_of_record=LinearDict()

#     def click(self, word):
#         self.list_of_record[word]=word
    
#     def check(self,word,password):
#         found=self.list_of_record.get(word,False)
#         if found:
#             if password == found:
#                 return  "Password is correct..... Login Successful"
#             else:
#                 return "Incorrect password"

#         else:
#             "No username of this ID was foud"

# from tkinter import *   
# import tkinter.messagebox
# from tkinter import ttk
# import pickle
# from PIL import ImageTk

# # class loginPage():

# #     def __init__(self,root):
# #         self.root = root          # this will create a window and between this and main loop we have to work for GUI

# #         self.root.title("Login Page")
# #         self.root.geometry('1920x1080')
# #         self.bg = PhotoImage(file = r"C:\Users\omen\Desktop\python\login.png")

# #         self.bg_image = Label(self.root, image =self.bg).place(x=0, y=0, relwidth=1, relheight=1)    


# # root = Tk()
# # onject = loginPage(root)
# # root.mainloop()

# def create_widgets_in_first_frame():
#     # Create the label for the frame
#     first_window_label = tkinter.ttk.Label(first_frame, text='Window 1')
#     first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

#     # Create the button for the frame
#     first_window_quit_button = tkinter.Button(first_frame, text = "Quit", command = quit_program)
#     first_window_quit_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
#     first_window_next_button = tkinter.Button(first_frame, text = "Next", command = call_second_frame_on_top)
#     first_window_next_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

# def create_widgets_in_second_frame():
#     # Create the label for the frame
#     second_window_label = tkinter.ttk.Label(second_frame, text='Window 2')
#     second_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

#     # Create the button for the frame
#     second_window_back_button = tkinter.Button(second_frame, text = "Back", command = call_first_frame_on_top)
#     second_window_back_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
#     second_window_next_button = tkinter.Button(second_frame, text = "Next", command = call_third_frame_on_top)
#     second_window_next_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

# def create_widgets_in_third_frame():
#     # Create the label for the frame
#     third_window_label = tkinter.ttk.Label(third_frame, text='Window 3')
#     third_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

#     # Create the button for the frame
#     third_window_back_button = tkinter.Button(third_frame, text = "Back", command = call_second_frame_on_top)
#     third_window_back_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
#     third_window_quit_button = tkinter.Button(third_frame, text = "Quit", command = quit_program)
#     third_window_quit_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

# def call_first_frame_on_top():
#     # This function can be called only from the second window.
#     # Hide the second window and show the first window.
#     second_frame.grid_forget()
#     first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# def call_second_frame_on_top():
#     # This function can be called from the first and third windows.
#     # Hide the first and third windows and show the second window.
#     first_frame.grid_forget()
#     third_frame.grid_forget()
#     second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# def call_third_frame_on_top():
#     # This function can only be called from the second window.
#     # Hide the second window and show the third window.
#     second_frame.grid_forget()
#     third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# def quit_program():
#     root_window.destroy()

# ###############################
# # Main program starts here :) #
# ###############################

# # Create the root GUI window.
# root_window = tkinter.Tk()

# # Define window size
# window_width = 200
# window_heigth = 100

# # Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions. 
# first_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
# first_frame['borderwidth'] = 2
# first_frame['relief'] = 'sunken'
# first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# second_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
# second_frame['borderwidth'] = 2
# second_frame['relief'] = 'sunken'
# second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# third_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
# third_frame['borderwidth'] = 2
# third_frame['relief'] = 'sunken'
# third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# # Create all widgets to all frames
# create_widgets_in_third_frame()
# create_widgets_in_second_frame()
# create_widgets_in_first_frame()

# # Hide all frames in reverse order, but leave first frame visible (unhidden).
# third_frame.grid_forget()
# second_frame.grid_forget()

from tkinter import *  
  
root = Tk()  
  
root.geometry("200x200")  

def open():  
    top = Toplevel(root)  
    top.mainloop()  
btn = Button(root, text = "open", command = open)  
  
btn.place(x=75,y=50)  
  
  
root.mainloop()  