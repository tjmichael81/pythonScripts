def main():
    pass
import arcpy
import os

#Script Variables
sourceAttachmentTable = r'C:\TEMP\Database.gdb\AttachmentTable__ATTACH'
targetOutputFolder = r'C:\TEMP\AttachmentExport'
filePathAttribute = 'FILE_PATH'

#Create a new column to contain the path to each exported file
if not filePathAttribute in arcpy.ListFields(sourceAttachmentTable):
    arcpy.AddField_management(sourceAttachmentTable, filePathAttribute, 'TEXT', '', '', 200)

#Update the new column with the export path for each attachment
with arcpy.da.UpdateCursor(sourceAttachmentTable, [filePathAttribute, 'REL_OBJECTID', 'ATT_NAME']) as cursor:
    for row in cursor:
        row[0] = targetOutputFolder + os.sep + str(row[1]) + row[2]
        cursor.updateRow(row)
        del row
del cursor

#Export attachments from attachment table
with arcpy.da.SearchCursor(sourceAttachmentTable, [filePathAttribute, 'DATA']) as cursor:
    for row in cursor:
        outPath = row[0]
        blobData = row[1]
        open(outPath, 'wb').write(blobData.tobytes())
        del row
del cursor


if __name__ == '__main__':
    main()
