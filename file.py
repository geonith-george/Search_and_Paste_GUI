from tkinter import filedialog
from tkinter import *
import os
import shutil,sys
from shutil import copyfile
from os import path
from pathlib import Path, PureWindowsPath


def browse_button():
    # Allow user to select a directory and store it in global var
    # called directory
    global directory
    global stat_val
    global flc_cnt
    flc_cnt.configure(text="    0    ")
    stat_val = Label(master=root,text='    Stable    ')
    stat_val.grid(row=3, column=4)
    filename = filedialog.askdirectory()
    directory.set(filename)
    print(filename)
    global dir1
    dir1 = filename

def browse_button_destination():
    # Allow user to select a directory and store it in global var
    # called directory
    global directory_destination
    global stat_val
    stat_val = Label(master=root,text='    Stable    ')
    stat_val.grid(row=3, column=4)
    filename = filedialog.askdirectory()
    directory_destination.set(filename)
    print(filename)
    global dir2
    dir2 = filename 

root = Tk()
root.title("Copy your files")
root.geometry('450x150')

directory = StringVar()
directory_destination = StringVar()

dir1 = ''
dir2 = ''
val = 0

src = Label(master=root,text='Choose source folder: ')
src.grid(row=0, column=1)
browse = Button(text="    Browse    ", command=browse_button)
browse.grid(row=0, column=3)
src_path = Label(master=root,textvariable=directory)
src_path.grid(row=0, column=2)

dst = Label(master=root,text='Choose destination folder: ')
dst.grid(row=1, column=1)
browse2 = Button(text="    Browse    ", command=browse_button_destination)
browse2.grid(row=1, column=3)
dst_path = Label(master=root,textvariable=directory_destination)
dst_path.grid(row=1, column=2)

ext = Label(master=root,text='Extension: ')
ext.grid(row=2, column=1)
txt = Entry(root,width=10)
txt.grid(column=3, row=2)

flc = Label(master=root,text='Total files copied: ')
flc.grid(row=3, column=1)
flc_cnt = Label(master=root,text=val)
flc_cnt.grid(row=3, column=2)

stat = Label(master=root,text='Status: ')
stat.grid(row=3, column=3)
stat_val = Label(master=root,text='    Stable    ')
stat_val.grid(row=3, column=4)

def run(path2,dst_dir,extension):
    try:
        global flc_cnt
        filescopied = 0
        for root, dirs, files in os.walk(path2):
            for file in files: 

                if file.endswith(extension):
                    filename = Path(str(file))
                    src = path.realpath(str(file))   
                    # print("filename : ", end='') 
                    # print(filename)
                    # print("directory : ", end='')
                    copyy=root+"\\"+str(file)
                    # print(copyy)
                    # print("destination : ", end='')
                    # print(dst_dir)
                    shutil.copy(copyy, dst_dir)
                    filescopied = filescopied + 1
                    flc_cnt.configure(text=filescopied)
                    print(filescopied)
    except Exception as Emove:
        print("Error: ", end='')
        print(Emove) 

    print("\nNo of files copied",filescopied)
    return filescopied

def run2():
    global val
    global stat_val
    global flc_cnt
    global root

    root.title("Please wait, do not exit.")
    stat_val.configure(text="Copying..")
    # stat_val.grid(row=3, column=4)

    val = run(dir1,dir2,txt.get())
    flc_cnt.configure(text=val)
    stat_val.configure(text="Completed")
    root.title("Copy your files")

ok = Button(text="    OK    ", command=run2)
ok.grid(row=4, column=3)

mainloop()