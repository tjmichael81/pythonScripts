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

# Script Variables #

inWorkspace = r"C:\TEMP\pydev\WaterUtilities.gdb"

# Script Functions #

def add_globalid(in_dataset):
    """
    :param in_dataset: Input feature class
    :return: None
    """
    arcpy.AddGlobalIDs_management(in_dataset)
    print("GlobalID field added to " + in_dataset)

def enable_attachments(in_data):
    """
    :param in_data: Input feature class
    :return: None
    """
    arcpy.EnableAttachments_management(in_data)
    print("Feature Attachments enabled for " + in_data)

try:
    # Set arcpy workspace to inWorkspace
    arcpy.env.workspace = inWorkspace

    # Create lists to store dataaset, feature, nd table items
    featuredatasetList = []
    featureList = []
    tableList = []

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
    # Enable attachments for point, line, and polygon features
    for feature in featureList:
        desc = arcpy.Describe(feature)
        if desc.shapeType == "Polygon" or "Polyline" or "Point":
            enable_attachments(feature)

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