#----------------Importing Modules---------------------#
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile
import os
from turtle import undo
import win32api
from tkinter import filedialog
#-------------------Functions--------------------------#
#------File Menu------#
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("Text Documents (*.txt)", "*.txt "),("All Files", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = '*.txt', defaultextension=".txt",
                           filetypes=[
                                     ("Text Documents (*.txt)", "*.txt"),("All Files", "*.*")])
        if file =="":
            file = None
        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def saveasFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = '*.txt', defaultextension=".txt",
                           filetypes=[
                                     ("Text Documents (*.txt)", "*.txt"),("All Files", "*.*")])
        if file =="":
            file = None
        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def pagesetup():
    pass

def printfile():
    # Ask for file (Which you want to print)
    file_to_print = filedialog.askopenfilename(
      initialdir="/", title="Select file", 
      filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    if file_to_print:
        # Print Hard Copy of File
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
 
def quitApp():
    root.destroy()
#------Edit Menu------#
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def delete():
    TextArea.event_generate(("<<Delete>>"))

def find():
    pass

def findnext():
    pass

def replace():
    pass

def goto():
    pass

def selectall():
    pass

def timedate():
    pass
#------About Menu------#
def about():
    showinfo("About Notepad", '''Microsoft Windows
Version 6. 1 (Build 7601: Service Pack 1)
Copyright @ 2009 Arsh Corporation. All rights reserved.
The Windows 7 Ultimate operating system and its user interface are
protected by trademark and other pending or existing intellectual property rights in the United States and other countries.

This product is licensed under the Microsoft Software License
Terms to:
    Arsh Goel
''')

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap(r"D:\Python\Python Files\Notepad\Icon.ico")
    root.geometry("945x510")

    #Add TextArea
    TextArea = Text(root, font="lucida 13",undo="True")
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    
    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    # Separator object
    FileMenu.add_command(label="New                    Ctrl+N", command=newFile)  
    FileMenu.add_command(label="Open...                Ctrl+O", command = openFile)
    FileMenu.add_command(label = "Save                     Ctrl+S", command = saveFile)
    FileMenu.add_command(label = "Save As...", command = saveasFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Page Setup...", command = pagesetup)
    FileMenu.add_command(label = "Print...", command = printfile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Undo               Ctrl+Z", command=TextArea.edit_undo)
    EditMenu.add_command(label = "Redu               Ctrl+Z", command=TextArea.edit_redo)
    EditMenu.add_separator()
    EditMenu.add_command(label = "Cut                  Ctrl+X", command=cut)
    EditMenu.add_command(label = "Copy               Ctrl+C", command=copy)
    EditMenu.add_command(label = "Paste               Ctrl+V", command=paste)
    EditMenu.add_command(label = "Delete                  Del", command=delete)
    EditMenu.add_separator()
    EditMenu.add_command(label = "Find                 Ctrl+F", command=find)
    EditMenu.add_command(label = "Find Next               F3", command=findnext)
    EditMenu.add_command(label = "Replace           Ctrl+H", command=replace)
    EditMenu.add_command(label = "Go To              Ctrl+G", command=goto)
    EditMenu.add_separator()
    EditMenu.add_command(label = "Select All         Ctrl+A", command=selectall)
    EditMenu.add_command(label = "Time/Date             F5", command=timedate)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends
    FormatMenu=Menu(MenuBar, tearoff=0)
    FormatMenu.add_command(label = "Font...", command=about)
    MenuBar.add_cascade(label="Format", menu=FormatMenu)

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()