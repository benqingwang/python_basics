#===========================================================================
# Batch import DF
#===========================================================================
import os
filename_list=[filename for filename in os.listdir(os.getcwd()) if 
               filename.startswith('A')]
for filename in filename_list:
    print(filename) # replace print with your DF operation

#===========================================================================
# Batch combine txt files
#===========================================================================
from shutil import copyfileobj

sourcePath=r'C:\Users\Danish\Desktop\python sample'
targetPath=r'C:\Users\Danish\Desktop\python books'
savedFile=r'combined_file.txt'
filename_list=[filename for filename in os.listdir(os.chdir(sourcePath)) if 
               filename[0] in {'A','B','C','D','L','Q','X'}]

with open(targetPath+'\\'+savedFile,'wb') as wfd:
    for filename in filename_list:
        with open(sourcePath+'\\'+filename,'rb') as fd:
            copyfileobj(fd, wfd, 1024*1024*10)
#===========================================================================
# Batch rename files
#===========================================================================
filename_list=[filename for filename in os.listdir(os.getcwd()) if 
               filename.startswith('0')]
for filename in filename_list:
    os.rename(filename, "A"+filename)
