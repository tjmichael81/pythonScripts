# -------------------------------------------------------------------------------
# DESCRIPTION #
# Add commonly used settings to all feature classes in a geodatabase:
# - Editor Tracking
# - GlobalID
# - Feature Attachments
# -------------------------------------------------------------------------------

# Import Modules
import arcpy
import sys
import traceback

try:
    arcpy.CreateSpatialReference_management()

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