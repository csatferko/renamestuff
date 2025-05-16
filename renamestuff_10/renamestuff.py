#!/usr/bin/env python3
# renamestuff 1.0

import os, sys, time, datetime, shutil
from pathlib import Path

cwDir = os.path.dirname(os.path.abspath(sys.argv[0]))
timeStamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
logName = 'renamestuff_log_' + str(timeStamp) + '.txt'

print('\nrenamestuff 1.0\n')
print('The renamestuff tool renames all of the files in a given folder.')
print('The source must be one level below the script (current working directory).')
print('The new name scheme is amended by an ordinal number for each file. \n') 

time.sleep(1)

print('Current working directory:')

print(cwDir)
print()

while True:
    time.sleep(0.5)
    print('Provide the name of the source folder.')
    srcFold = input('> ')
    srcPath = cwDir / Path(str(srcFold))
    if os.path.exists(srcPath) is True:
        break
    else:
        print('\nPath does not exist. Please name an existing folder.\n')
        continue     

time.sleep(0.5)

print('\nGive a scheme for the new filenames. (E.g.: "Zabhegyezes_Kukutyinban_").')
nameScheme = input('> ')

srcPath = cwDir / Path(str(srcFold))
srcPath2 = os.path.join(srcPath, "")
# print(srcPath2)

sourceFolder = str(srcPath)
sourceFolder2 = str(srcPath2)

count = 1
# iterate all files from a directory:
listDir = os.listdir(sourceFolder)
listDir.sort()
n = len(listDir)
#print(n)
if int(n) < 100:
    l = 2
elif int(n) < 1000:
    l = 3
elif int(n) < 10000:
    l = 4
elif int(n) < 100000:
    l = 5
else:
    l = 10        

print()

time.sleep(0.5)

print('Do you want a change log file? (yes/no):')
logFile = input('> ')

if logFile.lower() in ["y", "yes"] or logFile.upper() in ["Y", "YES"]:
    renameLog = open(cwDir / Path(str(logName)), 'w')
    renameLog.write('Files renamed \n')
    renameLog.close()
    renameLog = open(cwDir / Path(str(logName)), 'a')
    renameLog.write((str(timeStamp)) + '\n')
    renameLog.close()
    print()
else:
    print()

time.sleep(0.5)

print('Do you want to save the renamed files in a separate folder? (yes/no):')
newFold = input('> ')
if newFold.lower() in ["y", "yes"] or newFold.upper() in ["Y", "YES"]:
    newfoldName = str(srcFold) + '_new_' + (str(timeStamp))
    destFolder = cwDir / Path(str(newfoldName))
    os.mkdir(destFolder)
    destinationFolder1 = str(destFolder)
#    print(sourceFolder)
#    print(destinationFolder)
    print('\nCopying...')
    for fileName1 in listDir:
        shutil.copy2(os.path.join(sourceFolder,fileName1), destinationFolder1)
    listDir2 = os.listdir(destinationFolder1)
    listDir2.sort()
    destFolder2 = os.path.join(destFolder, "")
    destinationFolder = str(destFolder2)
    print()
else:
    listDir2 = listDir
    destinationFolder = sourceFolder2
    print()

for fileName in listDir2:
    # Construct old file name
    src = destinationFolder + fileName
    
    split = os.path.splitext(fileName)
    splitExt = split[1]
    
    dest = destinationFolder + str(nameScheme) + str(count).rjust(int(l), '0') + str(splitExt)
    
    newfileName = str(nameScheme) + str(count).rjust(int(l), '0') + str(splitExt)
    # Renaming the file:
    os.rename(src, dest)
    print(fileName, " -----> ", newfileName)
    
    if logFile.lower() in ["y", "yes"] or logFile.upper() in ["Y", "YES"]:
        renameLog = open(cwDir / Path(str(logName)), 'a')
        renameLog.write(str(fileName) + '\t' + '----->' + '\t' + '\t' + str(newfileName) + '\n')
    
    count += 1
print('\nAll the files have been renamed.')
print()

time.sleep(5)