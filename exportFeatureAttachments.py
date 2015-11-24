def main():
    pass
import arcpy
import os

#Script Variables
sourceFeatureTable = r'C:\TEMP\Database.gdb\AttachmentTable__ATTACH'
sourceAttachmentTable = r'C:\TEMP\Database.gdb\AttachmentTable__ATTACH'
targetOutputFolder = r'C:\TEMP\AttachmentExport'
filePathAttribute = 'FILE_PATH'
localPathExpression = '!AttachmentTable__ATTACH.FILE_PATH!'

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

#Create a new column to contain the path to each exported file
if not filePathAttribute in arcpy.ListFields(sourceFeatureTable):
    arcpy.AddField_management(sourceAttachmentTable, filePathAttribute, 'TEXT', '', '', 200)

#Make feature layer & table view to prepare for join
arcpy.MakeFeatureLayer_management(sourceFeatureTable, 'featureTable')
arcpy.MakeTableView_management(sourceAttachmentTable, 'tableView')

# Add a join between the feature table and table view
arcpy.AddJoin_management('featureTable', 'OBJECTID', 'tableView', 'REL_OBJECTID')

# Calculate the value for the file path URL to the feature table
arcpy.CalculateField_management('featureTable', 'AttachmentTable.FILE_PATH', localPathExpression, 'PYTHON')

if __name__ == '__main__':
    main()
