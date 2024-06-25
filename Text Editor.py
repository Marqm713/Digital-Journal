from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

class DigitalJournal:
    def __init__(self):
        window = Tk()
        window.title("Studio Super: Text Editor V1")
       
        # menu bar
        menubar = Menu(window)
        window.config(menu=menubar)  # Display the menu bar
       
        # pulldown menu and add it to the menu bar
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=operationMenu)
        operationMenu.add_command(label="Open", command=self.openFile)
        operationMenu.add_command(label="Save", command=self.saveFile)
       
        # tool bar frame
        frame0 = Frame(window) 
        frame0.grid(row=1, column=1, sticky=W)
       
        # thumbnails
        openImage = Image.open(r"C:\Users\marqu\OneDrive\Desktop\Python projects\file editor\open-file-icon-6.jpg")
        openImage = ImageTk.PhotoImage(openImage)
        saveImage = Image.open(r"C:\Users\marqu\OneDrive\Desktop\Python projects\file editor\file-save-icon-2.jpg")
        saveImage = ImageTk.PhotoImage(saveImage)
       
        Button(window, image=openImage, command=self.openFile).grid(row=3, column=1, sticky=W)
        Button(window, image=saveImage, command=self.saveFile).grid(row=3, column=1, sticky=E)
       
        # Hold Journal pane
        frame1 = Frame(window)  
        frame1.grid(row=2, column=1)
       
        # scrollbar
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(frame1, width=40, height=20, wrap=WORD, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
       
        window.mainloop() 

    def openFile(self):
        filenameforReading = askopenfilename()
        if filenameforReading:  # Check if a file was selected
            with open(filenameforReading, "r") as inputFile:
                self.text.delete(1.0, END)  # Clear current text
                self.text.insert(END, inputFile.read())  # Read all from the file

    def saveFile(self):
        filenameforWriting = asksaveasfilename()
        if filenameforWriting:  # Check if a file name was provided
            with open(filenameforWriting, "w") as outputFile:
                outputFile.write(self.text.get(1.0, END))  # Write to the file

DigitalJournal()  # Create GUI
