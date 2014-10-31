#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothy Michael
#
# Created:     31/10/2014
# Copyright:   (c) Timothy Michael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import os

rootFolder = r'C:\TEMP\CacheTestService\Layers\_alllayers'
validImageExtensions = ['.jpeg', '.jpg', '.png']

def convertToHex(inStr):
    convertedNum = int(inStr, 16)
    return str(convertedNum)

renamedFileCount = 0
renamedFolderCount = 0

#Rename image tiles
for dirpath, dirnames, files in os.walk(rootFolder, topdown=True):
    for name in files:
        fullPath = os.path.join(dirpath, name)
        #Assign variables to directory, file
        directory, fileName = os.path.split(fullPath)

        #Assign variables to file name and extension
        root, extension = os.path.splitext(fileName)

        #Only change the name of files that have valid image extensions
        #Extensions in list above
        if extension in validImageExtensions:

            #Ignore first character of file name ('C' for Column), convert to hex
            convertedHex = convertToHex(str(root[1:]))

            #Rename each file based on file name parts
            os.rename(fullPath, os.path.join(directory, convertedHex + extension))
            renamedFileCount = renamedFileCount + 1

#Rename 'Row' folders
#Walking the directory twice, which is probably unnecessary
for dirpath, dirnames, files in os.walk(rootFolder, topdown=True):
    for dirname in dirnames:
        #Filter for directories that start with 'R' (Row directories)
        if dirname[0] == 'R':
            fullPath = os.path.join(dirpath, dirname)
            convertedHex = convertToHex(str(dirname[1:]))
            os.rename(fullPath, os.path.join(dirpath, convertedHex))
            renamedFolderCount = renamedFolderCount + 1

#Rename 'Level' folders
#Walking the directory twice, which is probably unnecessary
for dirpath, dirnames, files in os.walk(rootFolder, topdown=True):
    for dirname in dirnames:
        #Filter for directories that start with 'L' (Level directories)
        if dirname[0] == 'L':
            fullPath = os.path.join(dirpath, dirname)
            #convertedHex = convertToHex(str(dirname[1:]))
            os.rename(fullPath, os.path.join(dirpath, dirname[1:]))
            renamedFolderCount = renamedFolderCount + 1

print 'Successfully converted {0} directory and {1} file names'.format(renamedFolderCount, renamedFileCount)

if __name__ == '__main__':
    main()
