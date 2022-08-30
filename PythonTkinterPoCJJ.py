####PoC to show a window with non-functional tabs/menu bars####
    #Features include:
        #Tabs that will show submenu options when you hover
        #A help pop up window
        #An image 
        #A button
        #Text

from tkinter import * 
from tkinter import ttk 

rootWindow = Tk(screenName='Welcome to My Website')

inactiveButton = ttk.Button(rootWindow, text = 'Enter Website')
inactiveButton.pack()

labelImage = PhotoImage(file = 'C:\\Users\joyasha.johnson\Downloads\RepairIcon.gif').subsample(20, 20)
label = Label(rootWindow, text = 'Coming Soon...', font= 'Roman')
label.config(image = labelImage, compound = 'left')
label.pack()

rootWindow.option_add('*tearOff', False)

menubar = Menu(rootWindow) 
rootWindow.config(menu = menubar)

file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu = file, label = "File")
menubar.add_cascade(menu = edit, label = "Edit")
menubar.add_cascade(menu = help_, label = "Help")

#Haven't learned event triggers, only printing for now
file.add_command(label = 'New', command = lambda: print('New File'))
file.add_separator()
file.entryconfig('New', accelerator = 'Ctrl + N')

file.add_command(label = 'Open...',command = lambda: print('Opening file'))
file.entryconfig('Open...', accelerator = 'Ctrl + O')

file.add_command(label = 'Save', command = lambda: print('Saved'))
file.entryconfig('Save', accelerator = 'Ctrl + S')
file.add_command(label = 'Save as...', command = lambda: print('Saved as user input'))
file.entryconfig('Save as...', accelerator = 'Ctrl + Shift + S')

choice = IntVar()
edit.add_radiobutton(label = 'Undo', variable = choice, value = 1)
edit.add_radiobutton(label = 'Redo', variable = choice, value = 2)
edit.add_separator()
edit.add_radiobutton(label = 'Cut', variable = choice, value = 3)
edit.add_radiobutton(label = 'Copy', variable = choice, value = 4)
edit.add_radiobutton(label = 'Paste', variable = choice, value = 5)
edit.add_separator()
edit.add_radiobutton(label = 'Find', variable = choice, value = 6)
edit.add_radiobutton(label = 'Replace', variable = choice, value = 7)

help_.add_command(label = 'Get Started')
help_.add_command(label = 'Tips and Tricks')


help_.post(400, 300)

rootWindow.mainloop()






