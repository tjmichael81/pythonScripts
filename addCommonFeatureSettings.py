# -------------------------------------------------------------------------------
# DESCRIPTION #
# Add commonly used settings to all feature classes in a geodatabase:
# - Editor Tracking
# - GlobalID
# - Feature Attachments
# -------------------------------------------------------------------------------

# Import Modules #
import arcpy
import datetime
import sys
import traceback

# Script Variables #

inWorkspace = r"C:\TEMP\pydev\WaterUtilities.gdb"
startTime = datetime.datetime.now()

# Script Functions #


def add_globalid(in_dataset):
    """
    :param in_dataset: Input feature class
    :return: None
    """
    arcpy.AddGlobalIDs_management(in_dataset)
    print("GlobalID field added to " + in_dataset)


def alter_editor_tracking_fields(in_data):
    """
    Modify the aliases for the editor tracking fields
    :param in_data: Input feature class
    :return: None
    """
    arcpy.AlterField_management(in_data, "CREATED_BY", "", "Created By")
    arcpy.AlterField_management(in_data, "CREATED_DATE", "", "Created Date")
    arcpy.AlterField_management(in_data, "LAST_EDIT_BY", "", "Last Edit By")
    arcpy.AlterField_management(in_data, "LAST_EDIT_DATE", "", "Last Edit Date")
    print("Editor Tracking field aliases modified for " + in_data)


def enable_attachments(in_data):
    """
    :param in_data: Input feature class
    :return: None
    """
    arcpy.EnableAttachments_management(in_data)
    print("Feature Attachments enabled for " + in_data)


def enable_editor_tracking(in_data):
    """
    :param in_data: Input feature class
    :return: None
    """
    arcpy.EnableEditorTracking_management(in_data, "CREATED_BY", "CREATED_DATE", "LAST_EDIT_BY",
                                          "LAST_EDIT_DATE", "ADD_FIELDS", "UTC")
    print("Editor Tracking enabled for " + in_data)

# Main Script #

try:
    # Set arcpy workspace to inWorkspace
    arcpy.env.workspace = inWorkspace

    # Create lists to store dataset and feature items
    featuredatasetList = []
    featureList = []

    # Find feature datasets in the workspace
    featuredatasetList += [fd for fd in arcpy.ListDatasets(None, "Feature")]

    # Add feature classes from each feature dataset to featureList
    # Add GlobalID field to features in each dataset
    for dataset in featuredatasetList:
        featureList += [fc for fc in arcpy.ListFeatureClasses(None, "All", dataset)]
        add_globalid(dataset)

    # Search for standalone features in the workspace
    # Add GlobalID field each feature and add to featureList
    standalone_features = [fc for fc in arcpy.ListFeatureClasses()]
    for feature in standalone_features:
        add_globalid(feature)
        featureList.append(feature)

    # Describe the shape type for each feature in featureList
    # Enable attachments and editor tracking for point, line, and polygon features
    # Alter aliases for editor tracking fields
    for feature in featureList:
        desc = arcpy.Describe(feature)
        if desc.shapeType == "Polygon" or "Polyline" or "Point":
            enable_attachments(feature)
            enable_editor_tracking(feature)
            alter_editor_tracking_fields(feature)
            print("\n")

    # Find standalone tables in the workspace
    # Enable editor tracking
    tableList = arcpy.ListTables()
    for table in tableList:
        enable_editor_tracking(table)
        alter_editor_tracking_fields(table)

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

# Calculate script duration
endTime = datetime.datetime.now()
timeDelta = str(endTime - startTime)
print('Script completed in {0}'.format(timeDelta))
