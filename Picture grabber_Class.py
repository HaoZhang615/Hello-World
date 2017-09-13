from tkinter import Tk, Button, Frame, Entry, StringVar, W, E
import tkinter.filedialog
import tkinter.messagebox
from urllib.request import urlretrieve
import os


class PictureGrabber:


    def __init__(self, master):

        # first, set up 3 frames to order the widgets nicely

        frame1 = Frame(master)
        frame1.pack()

        frame2 = Frame(master)
        frame2.pack()

        frame3 = Frame(master)
        frame3.pack()

        # set the initial variable to empty string
        self.outputDirname=""
        self.inputDirname=""

        # initiate the string variable
        self.Entry_Text1=StringVar()
        self.Entry_Text1.set(self.outputDirname)
        self.Entry_Text2=StringVar()
        self.Entry_Text2.set(self.inputDirname)

        # set the lay out of the entry and button widgets in their frame and bind the function calls, respectively
        self.dirEntry = Entry(frame1,textvariable=self.Entry_Text1)
        self.dirEntry.grid(row=0,column=0,sticky=W+E)

        self.dirBut = Button(frame1, text='select a folder to save the files...')
        self.dirBut.bind("<Button-1>", self.askdirectory)
        self.dirBut.grid(row=0,column=1,sticky=W+E)

        self.txtFileEntry = Entry(frame2,textvariable=self.Entry_Text2)
        self.txtFileEntry.grid(row=1,column=0,sticky=W+E)

        self.txtFileBut = Button(frame2, text='select the TXT-file with URLs...')
        self.txtFileBut.bind("<Button-1>", self.findtxtFile)
        self.txtFileBut.grid(row=1,column=1,sticky=W+E)

        self.loadBut = Button(frame3, text='download the files and save')
        self.loadBut.bind("<Button-1>", self.load_file)
        self.loadBut.grid(columnspan=2)

    # a function to browse into a directory on local PC to save the pictures
    def askdirectory(self, event):

        self.outputDirname = tkinter.filedialog.askdirectory()

        # the selected folder is set to variable Entry_Text1
        self.Entry_Text1.set(self.outputDirname)

    # a function to browse into a directory on local PC to find the txt file with URLs
    def findtxtFile(self, event):

        self.inputDirname = tkinter.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        # the selected folder is set to variable Entry_Text2
        self.Entry_Text2.set(self.inputDirname)

    # a function to execute the download and save the pictures in the selected directory
    def load_file(self, event):
        try:
            with open(self.inputDirname) as f:
                for line in f:
                    # split the URL with the right most '/' in to 2 parts
                    fname = line.rsplit('/', 1)

                    # use the second part as the original file name, remove any spaces and newlines with str.strip()
                    # and give every picture a new full file adress
                    fullfilename = os.path.join(self.Entry_Text1.get(), str.strip(fname[1]))

                    # download!
                    urlretrieve(line, fullfilename)
                f.close()
        except Exception as ex:

            # format the error message as a string.
            tkinter.messagebox.showerror('Error!', "Can't save to the folder\n %s" % ex)


app = Tk()
app.title('Picture Grabber')

newFile= PictureGrabber(app)

app.mainloop()