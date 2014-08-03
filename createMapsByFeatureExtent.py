#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tmichael
#
# Created:     8/1/2014
# Copyright:   (c) tmichael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
import smtplib
import sys
import traceback

#-------------------------------------------------------------------------------
# Script Variables
#-------------------------------------------------------------------------------
templateMap = r'C:\TEMP\Template.mxd'
gridFeature = r'C:\TEMP\gridFeature.shp'
fields = ['OID@', 'SHAPE@']
outputFolder = r'C:\TEMP\toDelete'

#-------------------------------------------------------------------------------
# Script Functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Main Script
#-------------------------------------------------------------------------------
try:

    print 'Script Started'

    #---------------------------------------------------------------------------
    # Verify the input feature class is a polygon
    # Return error and exit if not
    #---------------------------------------------------------------------------
    featureDescription = arcpy.Describe(gridFeature)
    print '{0} is {1} feature type'.format(os.path.basename(gridFeature), featureDescription.shapeType)
    if featureDescription.shapeType != 'Polygon':
        print 'Input feature is not a polygon.  Please try again'
        sys.exit()

    #---------------------------------------------------------------------------
    # Use Search Cursor to access rows in gridFeature
    # Use SHAPE@ field to get geometry and extent for row
    #---------------------------------------------------------------------------
    with arcpy.da.SearchCursor(gridFeature, fields) as cursor:
        for row in cursor:
            #Set variable for row (feature) extent
            featureExtentObject = row[1].extent

            #-------------------------------------------------------------------
            # Access the template map
            # Access the data frame of the template map
            # Set the data frame extent to row extent
            #-------------------------------------------------------------------

            mxd = arcpy.mapping.MapDocument(templateMap)
            mapDataFrame = arcpy.mapping.ListDataFrames(mxd)[0]
            newExtent = mapDataFrame.extent
            #Use polygon extent to set extent for data frame
            newExtent.XMin = featureExtentObject.XMin
            newExtent.XMax = featureExtentObject.XMax
            newExtent.YMin = featureExtentObject.YMin
            newExtent.YMax = featureExtentObject.YMax
            mapDataFrame.extent = newExtent

            #Save a new .mxd with the specified extent
            fileName = str(row[0])
            print fileName
            mxd.saveACopy(os.path.join(outputFolder, fileName + '.mxd'))

    #---------------------------------------------------------------------------
    print 'Script Completed Successfully'
    #---------------------------------------------------------------------------

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

