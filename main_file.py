# Libraries used and needed to be installed first
from tkinter import *
import os
from PIL import ImageTk, Image
from prettytable import PrettyTable
# importing other files used
import AreaGraph
import BinaryLinear
import MergesortArea
main_root = Tk()

# Function to get the absolute path of directory where the files or pictures used are stored.


def AbsolutePath(dir):
    AbsoluteDirectory = os.path.dirname(os.path.abspath(__file__))
    returnDir = os.path.join(AbsoluteDirectory, dir)
    return returnDir

# Function to display the shortest path from the area user gave to Habib University


def display_shortest_path(starting_area):
    temp_root = Toplevel()
    temp_root.geometry("1366x720")
    temp_root.config(bg='#1C1C1C')
    temp_root.geometry('1366x720')
    main_image = ImageTk.PhotoImage(Image.open(
        AbsolutePath('pictures_used/fourth_window_image.png')))
    temp_label = Label(temp_root, bg='#1C1C1C', image=main_image)
    temp_label.place(x=0, y=0, relwidth=1, relheight=1)
    picture_frame = Frame(temp_root, bg='#1C1C1C')
    picture_frame.grid(padx=225, pady=200)
    # Made dictionary to store the paths of pictures so that they can easily be used later on.
    dictionary_for_areas_nodes = {
        'Gulshan e Iqbal': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/IqbalLoc.png'))),
        'Shahrah e Faisal': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/SeFLoc.png'))),
        'Gulistan e Johar': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/JoharLoc.png'))),
        'Defence(Ph4,Ph5,Gizri)': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/D45GLoc.png'))),
        'Clifton Block (1,2,3)': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/C123Loc.png'))),
        'Saddar': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/SaddarLoc.png'))),
        'Defence(Ph1,Ph2)': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/D12Loc.png'))),
        'North Nazimabad': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/NNLoc.png'))),
        'Garden': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/GardenLoc.png'))),
        'Malir Cantt': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/MalirLoc.png'))),
        'Defence(Ph6,Ph7,Ph8)': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/D678Loc.png'))),
        'Shaheed e Millat': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/SeMLoc.png'))),
        'Federal B Area': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/FBLoc.png'))),
        'Clifton Block (7,8,9)': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/C789Loc.png'))),
        'Bahadurabad': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/BahadurabadLoc.png'))),
        'Clifton Cantt': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/CCLoc.png'))),
        'PECHS': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/PECHSLoc.png'))),
        'Habib University': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Areas Nodes/HULoc.png')))
    }

    # using the file named as AreaGraph from which using function get shortest path using Dijsktra Algorithm
    # there will be tupple stored inside the temp_lst
    # the first index shows the path while second index shows the total distance of the journey.
    temp_lst = AreaGraph.getShortesetPath(starting_area, 'Habib University')
    shortest_path = temp_lst[0]
    counter_for_row = 0
    counter_for_column = 0

    # Running loop to display the pictures according to the paths detected by the dijsktra algorithm.
    for i in range(len(shortest_path)):
        for j in dictionary_for_areas_nodes:
            if shortest_path[i] == j:
                Label(picture_frame, bg='#1C1C1C', image=dictionary_for_areas_nodes[j], height=100, width=225).grid(
                    row=counter_for_row, column=counter_for_column)
                counter_for_column += 1
                if counter_for_column >= 4:
                    counter_for_column = 0
                    counter_for_row += 1
    Label(temp_root, text='Total distance from your Area to HU is Approximately ' +
          str(temp_lst[1]) + " Km", bg='#1C1C1C', font=("Courier", 25, 'bold'), fg='#ffbd59').grid(padx=10, pady=40)

    temp_root.mainloop()


def creating_third_window(starting_area):
    top = Toplevel()
    top.geometry("1366x720")
    top.config(bg='#1C1C1C')
    top.geometry('1366x720')
    student_data_frame = Frame(top, bg='#1C1C1C')
    student_data_frame.grid()
    # Using the .py file BinaryLinear to search the students living in the selected area
    lst_of_data = BinaryLinear.main(starting_area)
    # As we are using the randomized order and the excel file was sorted on the basis of area so that
    # searching complexity get reduced.
    lst_of_data = MergesortArea.mergeSort(lst_of_data, 1)
    # used the created Merge sort program and sorted the data according to column 1 which is name
    headline_image = ImageTk.PhotoImage(
        Image.open(AbsolutePath('pictures_used/HeadingPage3.png')))
    Label(student_data_frame, image=headline_image,
          bg='#1C1C1C', height=70).grid(row=0, column=0)
    # Creating table to display the data
    table = PrettyTable()
    label = Text(student_data_frame, bg='#1C1C1C', fg='white',
                 height=22, width=75, borderwidth=0)
    label.config(font=("Courier", 15))
    table.field_names = ["S.N", "First Name", "Last name", "Id", "Email"]
    for i in range(len(lst_of_data)):
        lst_of_data[i] = list(lst_of_data[i])
        lst_of_data[i][0] = i+1
        lst_of_data[i] = tuple(lst_of_data[i])
        # taking the data from the list as individual row and storing it in table row
        table.add_rows([lst_of_data[i]])
    label.insert(INSERT, table)
    label.config(state=DISABLED)
    label.grid(padx=300, pady=10, sticky=E+W)
    get_shortest_path_image = ImageTk.PhotoImage(
        Image.open(AbsolutePath('pictures_used/ShortestPath.png')))
    Button(student_data_frame, image=get_shortest_path_image, height=80, bg='#1C1C1C',
           command=lambda: display_shortest_path(starting_area), borderwidth=0).grid()

    top.mainloop()


# Function if about us option button is selected then a new window will popup
def select_about_us_option():
    about_us = Toplevel()
    about_us.geometry("1366x720")
    bg_image = ImageTk.PhotoImage(
        Image.open(AbsolutePath('pictures_used/about_us_image.png')))
    label = Label(about_us, image=bg_image)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    about_us.mainloop()

# If select your area option is selected this window will pop up


def select_your_area_option():
    root = Toplevel()
    root.geometry("1366x720")
    bg_image = ImageTk.PhotoImage(Image.open(
        AbsolutePath('pictures_used/second_window_image.png')))
    label = Label(root, image=bg_image)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    my_new_frame = Frame(root, bg='#1C1C1C')
    my_new_frame.grid(pady=200, padx=60)
    # All images of 16 area button are stored in dictionary
    dictionary_for_images = {
        'gulshan iqbal': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/GeI.png'))),
        'gulistane johar': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/GeJ.png'))),
        'Defence Phase4 5 and Gizri': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/D45G.png'))),
        'Clifton block 123': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/C123.png'))),
        'Saddar': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/saddar.png'))),
        'Defence Phase 1 and 2': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/D12.png'))),
        'north nazimabad': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/NN.png'))),
        'garden': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/Garden.png'))),
        'Malir cant': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/MC.png'))),
        'Defence Phase 6 7 8': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/D675.png'))),
        'Shaheed Milat': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/SeM.png'))),
        'Federal area': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/FBA.png'))),
        'Clifton block 7 8 9': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/C789.png'))),
        'Bahadurabad': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/Bahadurabad.png'))),
        'Clifton Cant': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/CC.png'))),
        'PECHS': ImageTk.PhotoImage(Image.open(AbsolutePath('pictures_used/Area pictures/PECHS.png')))
    }
    Button(my_new_frame, image=dictionary_for_images['gulshan iqbal'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Gulshan e Iqbal')).grid(row=1, pady=10, padx=5, column=0)
    Button(my_new_frame, image=dictionary_for_images['gulistane johar'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Gulistan e Johar')).grid(row=1, pady=10, padx=5, column=1)
    Button(my_new_frame, image=dictionary_for_images['Defence Phase4 5 and Gizri'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Defence(Ph4,Ph5,Gizri)')).grid(row=1, pady=10, padx=5, column=2)
    Button(my_new_frame, image=dictionary_for_images['Clifton block 123'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Clifton Block (1,2,3)')).grid(row=1, pady=10, padx=5, column=3)

    Button(my_new_frame, image=dictionary_for_images['Saddar'], borderwidth=0, bg='#1C1C1C', height=100,
           width=265, command=lambda: creating_third_window('Saddar')).grid(row=2, pady=10, padx=5, column=0)
    Button(my_new_frame, image=dictionary_for_images['Defence Phase 1 and 2'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Defence(Ph1,Ph2)')).grid(row=2, pady=10, padx=5, column=1)
    Button(my_new_frame, image=dictionary_for_images['north nazimabad'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('North Nazimabad')).grid(row=2, pady=10, padx=5, column=2)
    Button(my_new_frame, image=dictionary_for_images['garden'], borderwidth=0, bg='#1C1C1C', height=100,
           width=265, command=lambda: creating_third_window('Garden')).grid(row=2, pady=10, padx=5, column=3)

    Button(my_new_frame, image=dictionary_for_images['Malir cant'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Malir Cantt')).grid(row=3, pady=10, padx=5, column=0)
    Button(my_new_frame, image=dictionary_for_images['Defence Phase 6 7 8'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Defence(Ph6,Ph7,Ph8)')).grid(row=3, pady=10, padx=5, column=1)
    Button(my_new_frame, image=dictionary_for_images['Shaheed Milat'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Shaheed e Millat')).grid(row=3, pady=10, padx=5, column=2)
    Button(my_new_frame, image=dictionary_for_images['Federal area'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Federal B Area')).grid(row=3, pady=10, padx=5, column=3)

    Button(my_new_frame, image=dictionary_for_images['Clifton block 7 8 9'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Clifton Block (7,8,9)')).grid(row=4, pady=10, padx=5, column=0)
    Button(my_new_frame, image=dictionary_for_images['Bahadurabad'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Bahadurabad')).grid(row=4, pady=10, padx=5, column=1)
    Button(my_new_frame, image=dictionary_for_images['Clifton Cant'], bg='#1C1C1C', borderwidth=0, height=100,
           width=265, command=lambda: creating_third_window('Clifton Cantt')).grid(row=4, pady=10, padx=5, column=2)
    Button(my_new_frame, image=dictionary_for_images['PECHS'], borderwidth=0, bg='#1C1C1C', height=100,
           width=265, command=lambda: creating_third_window('PECHS')).grid(row=4, pady=10, padx=5, column=3)
    root.mainloop()


if __name__ == '__main__':
    # setting up the background image
    main_root.title('HU CARPOOLING SERVICE')
    main_root.geometry("1366x720")
    main_root.config(bg='White')
    main_image = ImageTk.PhotoImage(Image.open(
        AbsolutePath('pictures_used/first_window_image.png')))
    temp_label = Label(main_root, image=main_image)
    temp_label.place(x=0, y=0, relwidth=1, relheight=1)

    # creating the main window buttons of about us and select your area
    my_frame = Frame(main_root, bg='white', borderwidth=0)
    my_frame.grid(pady=380)
    about_us_image = ImageTk.PhotoImage(Image.open(
        AbsolutePath('pictures_used/About.png')))
    select_your_area_image = ImageTk.PhotoImage(
        Image.open(AbsolutePath('pictures_used/SelectArea.png')))
    select_your_area_button = Button(my_frame, image=select_your_area_image, bg='white', borderwidth=0, width=300,
                                     height=100, command=select_your_area_option)
    select_your_area_button.grid(pady=10, padx=100, row=1, column=2)

    about_us_button = Button(my_frame, image=about_us_image, bg='white',
                             width=300, height=100, borderwidth=0, command=select_about_us_option)
    about_us_button.grid(pady=10, padx=100, row=2, column=2)

mainloop()
