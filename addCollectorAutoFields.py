################################################################################
# addCollectorAutoFields
#
# Add field(s) to input features that correspond to each of the 'Auto Fields'
# that are supported by Esri's Collector for ArcGIS data collection software
#
# Documentation currently found on the
# "Create Data: Configuring GPS metadata storage"
# page in the documentation
################################################################################

def main():
    pass

################################################################################
# Import Modules
################################################################################
import arcpy
import datetime
import sys
import traceback

################################################################################
# Script Functions
################################################################################


try:
    print("In try block")

except arcpy.ExecuteError:
    # Get the tool error messages
    msgs = arcpy.GetMessages(2)

    # Return tool error messages for use with a script tool
    arcpy.AddError(msgs)

    # Print tool error messages for use in Python/PythonWin
    print(msgs)

except:
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    # Return python error messages for use in script tool or Python Window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

    # Print Python error messages for use in Python / Python Window
    print(pymsg)
    print(msgs)

if __name__ == '__main__':
    main()
