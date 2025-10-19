#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
renamebydict.py beta

Created on Fri Oct 17 08:20:03 2025

@author: csatferko
"""

import os, sys, time, datetime, openpyxl
from pathlib import Path

def nameDict(tup1, tup2):
    if len(tup1) == len(tup2):
        l1 = []
        for i in tup1:
            l1.append(i.value)
        l2 = []
        for j in tup2:
            l2.append(j.value)
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

print('Current working directory:')

print(cwDir)
print()

wb = openpyxl.load_workbook(cwDir / Path('dict.xlsx'))

ws = wb['Sheet1']

cmn_0 = ws['A']    
cmn_1 = ws['B']
#cmn_2 = ws['C']
#cmn_3 = ws['D']    
#cmn_4 = ws['E']
#cmn_5 = ws['F']

renameDict = nameDict(cmn_0, cmn_1)       

#print(renameDict)    

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
