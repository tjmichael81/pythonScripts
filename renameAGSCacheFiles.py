#-------------------------------------------------------------------------------
# Name:        renameAGSCacheFiles
# Purpose:     Creating a cache for an image in ArcGIS for Server creates
#              folders and files named with Level, Row, or Column identifiers
#              and hexadecimal numbering.  To be used as a tile service in
#              ArcGIS Online (or other places, I assume) the identifers need
#              to be removed and the hexadecimal numbers need to be converted
#              to integers
#
# Author:      Timothy Michael
#
# Created:     31/10/2014
# Copyright:   (c) Timothy Michael 2014
#-------------------------------------------------------------------------------

def main():
    pass

import datetime
import os

rootFolder = r'C:\TEMP\CacheTestService\Layers\_alllayers'
validImageExtensions = ['.jpeg', '.jpg', '.png']

renamedFileCount = 0
renamedFolderCount = 0
startTime = datetime.datetime.now()

def convertToHex(inStr):
    convertedNum = int(inStr, 16)
    return str(convertedNum)

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
for dirpath, dirnames, files in os.walk(rootFolder, topdown=True):
    for dirname in dirnames:
        #Filter for directories that start with 'R' (Row directories)
        if dirname[0] == 'R':
            fullPath = os.path.join(dirpath, dirname)
            convertedHex = convertToHex(str(dirname[1:]))
            os.rename(fullPath, os.path.join(dirpath, convertedHex))
            renamedFolderCount = renamedFolderCount + 1

#Rename 'Level' folders
for dirpath, dirnames, files in os.walk(rootFolder, topdown=True):
    for dirname in dirnames:
        #Filter for directories that start with 'L' (Level directories)
        if dirname[0] == 'L':
            fullPath = os.path.join(dirpath, dirname)
            os.rename(fullPath, os.path.join(dirpath, dirname[1:]))
            renamedFolderCount = renamedFolderCount + 1

endTime = datetime.datetime.now()
elapsedTime = str(endTime - startTime)

print 'Renamed {0} directories and {1} files in {2}'.format(renamedFolderCount, renamedFileCount, elapsedTime)

if __name__ == '__main__':
    main()
