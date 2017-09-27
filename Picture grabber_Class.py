from tkinter import Tk, Button, Frame, Entry, StringVar, W, E
import tkinter.filedialog
import tkinter.messagebox
from urllib.request import urlretrieve
import os


class PictureGrabber:


    def __init__(self, master):

        # first, set up 3 frames to order the widgets nicely

        _frame1 = Frame(master)
        _frame1.pack()

        _frame2 = Frame(master)
        _frame2.pack()

        _frame3 = Frame(master)
        _frame3.pack()

        # set the initial variable to empty string
        self.output_dirname=""
        self.input_dirname=""

        # initiate the string variable
        self.entry_text1=StringVar()
        self.entry_text1.set(self.output_dirname)
        self.entry_text2=StringVar()
        self.entry_text2.set(self.input_dirname)

        # set the layout of the entry and button widgets in their frame and bind the function calls, respectively
        self.dir_entry = Entry(_frame1,textvariable=self.entry_text1)
        self.dir_entry.grid(row=0,column=0,sticky=W+E)

        self.dir_but = Button(_frame1, text='select a folder to save the files...')
        self.dir_but.bind("<Button-1>", self.askdirectory)
        self.dir_but.grid(row=0,column=1,sticky=E)

        self.txt_file_entry = Entry(_frame2,textvariable=self.entry_text2)
        self.txt_file_entry.grid(row=0,column=0,sticky=W+E)

        self.txt_file_but = Button(_frame2, text='select the TXT-file with URLs...')
        self.txt_file_but.bind("<Button-1>", self.find_txt_File)
        self.txt_file_but.grid(row=0,column=1,sticky=E)

        self.loadBut = Button(_frame3, text='download the files and save')
        self.loadBut.bind("<Button-1>", self.load_file)
        self.loadBut.grid(columnspan=2)

    # a function to browse into a directory on local PC to save the pictures
    def askdirectory(self, event):

        self.output_dirname = tkinter.filedialog.askdirectory()

        # the selected folder is set to variable Entry_Text1
        self.entry_text1.set(self.output_dirname)

    # a function to browse into a directory on local PC to find the txt file with URLs
    def find_txt_File(self, event):

        self.input_dirname = tkinter.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        # the selected folder is set to variable Entry_Text2
        self.entry_text2.set(self.input_dirname)

    # a function to execute the download and save the pictures in the selected directory
    def load_file(self, event):
        try:
            with open(self.input_dirname) as f:
                for line in f:
                    # split the URL with the right most '/' in to 2 parts
                    fname = line.rsplit('/', 1)

                    # use the second part as the original file name, remove any spaces and newlines with str.strip()
                    # and give every picture a new full file adress
                    full_filename = os.path.join(self.entry_text1.get(), str.strip(fname[1]))

                    # download!
                    urlretrieve(line, full_filename)
                f.close()
        except Exception as ex:

            # format the error message as a string.
            tkinter.messagebox.showerror('Error!', "Can't save to the folder\n %s" % ex)


app = Tk()
app.title('Picture Grabber')

new_file= PictureGrabber(app)

app.mainloop()
