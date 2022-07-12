import tkinter as tk
import tkinter.messagebox as mb
import shutil
import os
import time
from pathlib import Path


#create a dictionary for all source directory paths
sourcedirectorypaths = {'SkyStudio':r'E:\SkyStudio Captures',
                        'PythonScripts':r'E:\Python Scripts',
                        'Tester':r'E:\TestingFolder'}

#create a dictionary for all destination directory paths
destdirectorypaths = {'TimeLapses':r'D:\Captures\Time Lapse Dumps',
                        'PythonBackups':r'D:\My Files\PythonBackups',
                        'TestDest': r'D:\My Files\TestDest' }

#initialize a variable for the source path
sourceloc = Path()

#initialize a variable for the dest path
destloc = Path()

#initialize the interface environment
root = tk.Tk()

#define the size of the interface window
root.geometry('960x540')

#define a name for the window that opens
root.title("Ed's Sick Rocking Utilities")

sourceselectcount = 0
destselectcount = 0

#create a function that selects a folder path and places it into a variable as the source
def selectsource(btnname):
    global sourceloc
    global sourceselectcount
    sourceselectcount +=1
    sourceloc = sourcedirectorypaths[btnname]
    sourcetext = '{}{}'.format("Source to Copy = ", sourceloc)
    tk.Label (root, text = sourcetext, bd=10, wraplength=165).place(x=60,y=175)
    mb.showinfo("Files in source",os.listdir(sourceloc))
    if sourceselectcount != 0 and sourceselectcount is destselectcount :

        ExecBtn.place(x = 420,y = 100)

#create a function that selects a folder path and places it into a variable as the destination
def selectdest(btnname):
    global destloc
    global destselectcount
    destselectcount +=1
    destloc = destdirectorypaths[btnname]
    desttext = '{}{}'.format("Destination to Receive Files = ", destloc)
    tk.Label (root, text = str(desttext), bd=10, wraplength=165).place(x=680,y=175)
    mb.showinfo("Files in destination",os.listdir(destloc))
    if sourceselectcount != 0 and sourceselectcount is destselectcount :

        ExecBtn.place(x = 420,y = 100)

#create label for source directory section
sourcelabel = tk.Label(root, text = "Source Directories",font=("Courier",15,"bold",'underline')).place(x=43,y=10)

#create button for Testing source folder
TestBtn = tk.Button  (root, 
                    text = "Tester",
                    width = 13,
                    bg = 'blue', 
                    fg = "white",
                    command=lambda : selectsource("Tester"))

TestBtn.place(x=40,y=85)

#create button for SkyStudio source folder
SkyBtn = tk.Button  (root, 
                    text = "SkyStudio",
                    width = 13,
                    bg = 'blue',
                    fg = 'white',
                    command =lambda: selectsource("SkyStudio"))

SkyBtn.place(x=40,y=55)

#create button for PythonScripts source folder
PythBtn = tk.Button  (root, 
                    text = "PythonScripts",
                    width = 13,
                    bg = 'blue',
                    fg = 'white',
                    command =lambda: selectsource("PythonScripts"))

PythBtn.place(x=145,y=55)

#create label for desination directory section
destlabel = tk.Label(root, text = "Destination Directories", font = ("Courier",15,"bold",'underline')).place(x=645,y=10)

#create button for TimeLapse destination folder
TestDestBtn = tk.Button  (root, 
                    text = "TestDest",
                    width = 13,
                    bg = 'green',
                    command =lambda: selectdest("TestDest"))

TestDestBtn.place(x=663,y=85)


#create button for TimeLapse destination folder
TLBtn = tk.Button  (root, 
                    text = "TimeLapses",
                    width = 13,
                    bg = 'green',
                    command =lambda: selectdest("TimeLapses"))

TLBtn.place(x=663,y=55)

#create button for PythonBackups destination folder
PythBckBtn = tk.Button  (root, 
                    text = "PythonBackups",
                    width = 13,
                    bg = 'green',
                    command =lambda: selectdest("PythonBackups"))

PythBckBtn.place(x=768,y=55)

#initialize list for all files in source directory
sourcelist = []

#initialize list for all file paths in destination
destlist = []

#initialize list for all file names in destination
namelist = []

def digsource(x):
    global sourcelist
    
    for root, dirs, fns, in os.walk(Path(x)):
        for y in fns:
           sourcelist.append(Path(os.path.join(root,y)))

def digdest(x):
    global destlist
    
    for root, dirs, fns, in os.walk(Path(x)):
        for y in fns:
            fullpath = Path(os.path.join(root,y))
            destlist.append(fullpath)
            namelist.append(fullpath.name)

def copier():
    global sourcelist
    global destlist
    global namelist

    #loop to evaluate all items in the destination location
    digdest(destloc)

    #loop to evaluate all items in the source location
    digsource(sourceloc)
        
    start = ()
    end = ()
    counter = 0

    #look at each item in the sourcelist i.e. the source directory
    for unit in sourcelist:
        
        #check all items in destlist
        for item in destlist:
                
                start = time.time()
                counter += 1
                #compare file names
                if Path(item).name is Path(unit).name:
                    
                    #determine size of the item in the sourcelist and compare to item size in destlist
                    if os.path.getsize(Path(unit)) > os.path.getsize(Path(item)):
                        
                        print("Dest" , Path(item).name)
                        print("Source" , Path(unit).name)

                        #copy larger file into
                        shutil.copy(unit , destloc)
                        destlist.append(unit)
                end = time.time()
                looptime = end - start
                #print(counter, " - ", looptime)

        #determines if the file name is not in the destination folder
        if unit.name not in namelist:
                    
            #full file using the file path is copied from source to destination
            if '.git' and '.pyc' not in unit.name:
                shutil.copy(unit , destloc)
                destlist.append(unit)

                #filename is added to namelist
                #((for troubleshooting just in case))
                namelist.append(unit.name)  
    
    if destlist == sourcelist:
        fromto = '{}{}{}{}'.format("From ", sourceloc," to ",destloc)
        mb.showinfo("All files copied!", fromto )
    
    if destlist != sourcelist:
        fromto = '{}{}{}{}'.format("From ", sourceloc," to ",destloc)
        mb.showinfo("No copies made!", fromto )

ExecBtn = tk.Button(root, 
                    text = "Run that shit!?",
                    width = 13,
                    bg = 'orange',
                    font = ('Helvetica',12,'bold'),
                    command = copier)

#set a loop for the interface to continue showing
root.mainloop()