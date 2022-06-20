import shutil
from pathlib import Path
import os 
import time

s = Path('E:\SkyStudio Captures')
d = Path('D:\Captures\Time Lapse Dumps')

#initialize list for all files in source directory
sourcelist = []

#initialize list for all file paths in destination
destlist = []

#initialize list for all file names in destination
namelist = []

#walk function separates parts of path into 3 lists #TL = Time Lapse
#     1. A string of the current folder's name
#     2. A list of strings in the current folder
#     3. A list of strings of the files in the current folder
for TLDump, FolderNames, TLVideos in os.walk(d):
    
    #make list of all file paths in destination folder
    for tls in TLVideos:
        
        #create full file path string and puts into temppath variable
        temppath = Path(Path(TLDump) / Path(tls))

        #add full file path as a path object to the destination list
        destlist.append(Path(temppath))

        #create list of just file names without paths
        namelist.append(temppath.name)

#walk function separates parts of path into 3 lists
#     1. A string of the current folder's name
#     2. A list of strings in the current folder
#     3. A list of strings of the files in the current folder  
for SkyStudio, DateFolders, VideoFiles in os.walk(s):
    
    #loop to evaluate all items in the VideoFiles list
    for avi in VideoFiles:
        
        #create full file path string and puts into temppath variable
        temppath = (Path(SkyStudio) / Path(avi))
        
        #add full file path as a path object to the source list
        sourcelist.append(Path(temppath))
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
                if os.path.getsize(unit) > os.path.getsize(item):
                    
                    print("Dest" , Path(item).name)
                    print("Source" , Path(unit).name)

                    #copy larger file into
                    shutil.copy(unit , d)
            end = time.time()
            looptime = end - start
            print(counter, " - ", looptime)

    #determines if the file name is not in the destination folder
    if unit.name not in namelist:
                
        #full file using the file path is copied from source to destination
        shutil.copy(unit , d)

        #filename is added to destlist
        #((for troubleshooting just in case))
        namelist.append(unit.name)    