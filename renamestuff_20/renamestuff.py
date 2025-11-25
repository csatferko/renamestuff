#!/usr/bin/env python3
# renamestuff 2.0
"""
renamestuff.py 2.0

Created on Fri Oct 17 08:20:03 2025

@author: csatferko
"""

# integrate dict version
# granting extension handling
# granting log for dict (maybe it is not needed?)
# refactoring

import os, sys, time, datetime, shutil, openpyxl
from pathlib import Path

def nameDict(tup1, tup2):
    l1 = []
    for i in tup1:
        if i.value != None:
            l1.append(i.value)
    l2 = []
    for j in tup2:
        if j.value != None:
            l2.append(j.value)
    if len(l1) == len(l2):
        tupDict = dict(zip(l1, l2))
        return tupDict
    else:
        print('Dictionary cannot be created. The script ends.\n')
        time.sleep(5)
        exit()

def renameFilesDict(src, lis, dic):
    for fileName in lis:
        if str(fileName) in dic:
            newName = dic.get(str(fileName))
            old = src + str(fileName)
            new = src + str(newName)
            os.rename(old, new)
            print(fileName, " -----> ", newName)

cwDir = os.path.dirname(os.path.abspath(sys.argv[0]))
timeStamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
logName = 'renamestuff_log_' + str(timeStamp) + '.txt'

print('\nrenamestuff 2.0\n')
print('The renamestuff tool renames all of the files in a given folder.')
print('The source must be one level below the script (current working directory).')
print('The new name scheme is amended by an ordinal number for each file. \n') 
# Add pritout on dict function!

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

print('\nDo you want a to rename by a dictionary (yes)? Otherwise remaming is based on a name scheme (no).')
dictYes = input('> ')

if dictYes.lower() in ["y", "yes"] or dictYes.upper() in ["Y", "YES"]:
    wb = openpyxl.load_workbook(cwDir / Path('dict.xlsx'))

    ws = wb['Sheet1']

    cmn_0 = ws['A']    
    cmn_1 = ws['B']
    #cmn_2 = ws['C']
    #cmn_3 = ws['D']    
    #cmn_4 = ws['E']
    #cmn_5 = ws['F']

    renameDict = nameDict(cmn_0, cmn_1)  
    
    srcPath = cwDir / Path(str(srcFold))
    srcPath2 = os.path.join(srcPath, "")

    sourceFolder = str(srcPath)
    sourceFolder2 = str(srcPath2)

    # iterate all files from a directory:
    listDir = os.listdir(sourceFolder)
    listDir.sort()

    print()

    renameFilesDict(sourceFolder2, listDir, renameDict)

    print()

    time.sleep(5)   
    exit()

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