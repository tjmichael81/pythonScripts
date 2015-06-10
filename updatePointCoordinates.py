import arcpy
import sys
import time
import traceback

# Capture start time
tStart = time.time()

# Workspace, target feature class, and fields variables
# Coordinate fields in attribute table should be of type 'Double'
arcpy.env.workspace = r'C:\TEMP\PointMoveTest.gdb'
fc = r'C:\TEMP\PointMoveTest.gdb\AddressPointsModified'
fields = ['SHAPE@X', 'SHAPE@Y', 'gps_x', 'gps_y']

try:
    # Create update cursor for feature class
    with arcpy.da.UpdateCursor(fc, fields) as cursor:
        for row in cursor:

            # Set X, Y values to fields in 'fields' variable
            row[0] = row[2]
            row[1] = row[3]

            # Update the row
            cursor.updateRow(row)

except arcpy.ExecuteError:
    msgs = arcpy.GetMessages(2)
    arcpy.AddError(msgs)
    print(msgs)

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)
    print(pymsg)
    print(msgs)

# Capture end time and calculate elapsed time
tEnd = time.time()
elapsedTime = round(tEnd - tStart, 2)

print 'Script completed in {0} seconds'.format(elapsedTime)
