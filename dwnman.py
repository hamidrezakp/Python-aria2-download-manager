# Aria2 DownLoad Manager for Raspberry pi
# hamidrezakp.ir
# Hamid Reza Kaveh Pishghadam <hamidreza@hamidrezakp.ir>
import os
df = '/home/pi/Download/'
# get list of files in Download folder
filesList = os.listdir(df)
filesList.remove('List')
filesList.remove('Completed')

# check download files to completed or not
def isCompleted(f):
    if f + '.aria2' in filesList :
        return False
    else :
        return True

# remove compeleted links
def removelink(name):
    Listfile = open(df + 'List', 'r')
    lines = Listfile.readlines()
    Listfile.close()
    Listfile = open(df + 'List', 'w')
    for line in lines:
        if not name.replace(' ', '%20') in line:
            Listfile.write(line)
    Listfile.close()

# Main
for i, f in enumerate(filesList) :
    if 'aria2' in f.split('.')[-1]:    
        continue
    if isCompleted(f) :
        removelink(f)
        os.rename(df + f, df + 'Completed/' + f)
    i = i+1




