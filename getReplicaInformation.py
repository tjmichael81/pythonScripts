#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tmichael
#
# Created:     17/01/2014
# Copyright:   (c) tmichael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import arcpy
import sys
import traceback





arcpy.env.workspace = "C:/Data/myData.gdb"
try:
    ''' Code Here '''



    ''' Handle Errors '''
except arcpy.ExecuteError:
    # Get the tool error messages
    msgs = arcpy.GetMessages(2)

    # Return tool error messages for use with a script tool
    arcpy.AddError(msgs)

    # Print tool error messages for use in Python/PythonWin
    print msgs

except:
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

