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

#######################################
# Import Modules
#######################################
import arcpy
import datetime

#######################################
# Script Functions
#######################################

# Common fields
def addCommonFields(inFeature, fieldList):
    '''Adds fields common to all feature types'''

    print 'Adding common fields to {0}'.format(inFeature)
    print '\n'

    # This list of fields will be used to compare against the list of fields
    # for the input feature, and then to call the function to add new fields
    commonFields = ['CollectedBy', 'DeviceType', 'DeviceID', 'CorrectionStatus',
    'CorrectionSource', 'CreateDate', 'UpdateDate', 'EstimatedAccuracy',
    'GeometryCaptureType', 'PDOP', 'HDOP']

    #######################################
    # Field Configurations
    #######################################

    # 'Collected By' field
    def CollectedBy(inFeature):
        startMessage('Collected By')
        arcpy.AddField_management(inFeature, 'CollectedBy', 'TEXT', None, None, textFieldLength, 'Collected By', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Collected By')

    # 'Device Type' field
    def DeviceType(inFeature):
        startMessage('Device Type')
        arcpy.AddField_management(inFeature, 'DeviceType', 'TEXT', None, None, textFieldLength, 'Device Type', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Device Type')

    # 'Device ID' field
    def DeviceID(inFeature):
        startMessage('Device ID')
        arcpy.AddField_management(inFeature, 'DeviceID', 'TEXT', None, None, textFieldLength, 'Device ID', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Device ID')

    # 'Correction Status' field
    def CorrectionStatus(inFeature):
        startMessage('Correction Status')
        arcpy.AddField_management(inFeature, 'CorrectionStatus', 'TEXT', None, None, textFieldLength, 'Correction Status', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Correction Status')

    # 'Correction Source' field
    def CorrectionSource(inFeature):
        startMessage('Correction Source')
        arcpy.AddField_management(inFeature, 'CorrectionSource', 'TEXT', None, None, textFieldLength, 'Correction Source', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Correction Source')

    # 'Create Date' field
    def CreateDate(inFeature):
        startMessage('Create Date')
        arcpy.AddField_management(inFeature, 'CreateDate', 'TEXT', None, None, textFieldLength, 'Create Date', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Create Date')

    # 'Update Date' field
    def UpdateDate(inFeature):
        startMessage('Update Date')
        arcpy.AddField_management(inFeature, 'UpdateDate', 'TEXT', None, None, textFieldLength, 'Update Date', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Update Date')

    # 'Estimated Accuracy' field
    def EstimatedAccuracy(inFeature):
        startMessage('Estimated Accuracy')
        arcpy.AddField_management(inFeature, 'EstimatedAccuracy', 'DOUBLE', None, None, None, 'Estimated Accuracy', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Estimated Accuracy')

    # 'Geometry Capture Type' field
    def GeometryCaptureType(inFeature):
        startMessage('Geometry Capture Type')
        arcpy.AddField_management(inFeature, 'GeometryCaptureType', 'TEXT', None, None, textFieldLength, 'Geometry Capture Type', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Geometry Capture Type')

    # 'PDOP' field
    def PDOP(inFeature):
        startMessage('PDOP')
        arcpy.AddField_management(inFeature, 'PDOP', 'DOUBLE', None, None, None, 'PDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('PDOP')

    # 'HDOP' field
    def HDOP(inFeature):
        startMessage('HDOP')
        arcpy.AddField_management(inFeature, 'HDOP', 'DOUBLE', None, None, None, 'HDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('HDOP')

    # This locals() thing is awesome
    # https://docs.python.org/2/library/functions.html#locals
    # http://stackoverflow.com/questions/3061/calling-a-function-of-a-module-from-a-string-with-the-functions-name-in-python
    localFunctions = locals()

    # Compare the fields in the commonFields list in this function to the
    # list of fields for the input feature.  For each field that does not
    # match a field from the input, call the corresponding function to
    # add the field
    for field in commonFields:
        if field not in fieldList:
            localFunctions[field](inFeature)
        else:
            print '{0} already exists in {1}'.format(field, inFeature)

# Line fields
def addLineFields(inFeature, fieldList):
    '''Adds fields specific to line features'''

    print 'Adding line fields to {0}'.format(inFeature)

    # This list of fields will be used to compare against the list of fields
    # for the input feature, and then to call the function to add new fields
    lineFields = ['GeometryLength']

    # 'Geometry Length' field
    def GeometryLength(inFeature):
        startMessage('Geometry Length')
        arcpy.AddField_management(inFeature, 'GeometryLength', 'DOUBLE', None, None, None, 'Geometry Length', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Geometry Length')

    localFunctions = locals()

    # Compare the fields in the lineFields list in this function to the
    # list of fields for the input feature.  For each field that does not
    # match a field from the input, call the corresponding function to
    # add the field
    for field in lineFields:
        if field not in fieldList:
            localFunctions[field](inFeature)
        else:
            print '{0} already exists in {1}'.format(field, inFeature)

# Polygon fields
def addPolygonFields(inFeature, fieldList):
    '''Adds fields specific to polygon features'''

    print 'Adding polygon fields'

    # This list of fields will be used to compare against the list of fields
    # for the input feature, and then to call the function to add new fields
    polygonFields = ['GeometryArea']

    # 'Geometry Area' field
    def GeometryArea(inFeature):
        startMessage('Geometry Area')
        arcpy.AddField_management(inFeature, 'GeometryArea', 'DOUBLE', None, None, None, 'Geometry Area', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Geometry Area')

    localFunctions = locals()

    # Compare the fields in the polygonFields list in this function to the
    # list of fields for the input feature.  For each field that does not
    # match a field from the input, call the corresponding function to
    # add the field
    for field in polygonFields:
        if field not in fieldList:
            localFunctions[field](inFeature)
        else:
            print '{0} already exists in {1}'.format(field, inFeature)

def createFieldList(inputFeature):
    '''Return a list of fields from the input feature'''
    fieldList = [f.name for f in arcpy.ListFields(inputFeature,"*","All")]
    return fieldList

def startMessage(fName):
    print 'Adding {0} field'.format(fName)

def successMessage(fName):
    print '{0} field added successfully'.format(fName)
    print '\n'

def getDataType(inData):
    '''Return the DataType from arcpy.Describe'''
    dsc =  arcpy.Describe(inData)
    return dsc.DataType

def getShapeType(inFeature):
    '''Return the FeatureType from arcpy.Describe'''
    dsc = arcpy.Describe(inFeature)
    return dsc.FeatureType

def featureHandler(inFeature):
    '''
    Describe the input feature class to determine the ShapeType
    Based on the ShapeType, send the feature to the correct function(s)
    to add new fields
    '''

    dsc = arcpy.Describe(inFeature)

    if dsc.shapeType == 'Point':
        print '{0} is a {1} feature'.format(dsc.name, dsc.shapeType)

        # Create a list of fields to compare against
        fieldList = createFieldList(inFeature)
        addCommonFields(inFeature, fieldList)

    elif dsc.shapeType == 'Polyline':
        print '{0} is a {1} feature'.format(dsc.name, dsc.shapeType)

        # Create a list of fields to compare against
        fieldList = createFieldList(inFeature)

        addCommonFields(inFeature, fieldList)
        addLineFields(inFeature, fieldList)

    elif dsc.shapeType == 'Polygon':
        print '{0} is a {1} feature'.format(dsc.name, dsc.shapeType)

        # Create a list of fields to compare against
        fieldList = createFieldList(inFeature)

        addCommonFields(inFeature, fieldList)
        addPolygonFields(inFeature, fieldList)

    else:
        print '{0} is not a valid feature type.'.format(dsc.name)

###############################################################################

#######################################
# Script Variables
inData = r'C:\TEMP\CincinnatiBell\CincinnatiBell_TerraFlex.gdb\Poles_2'
textFieldLength = 100
startTime = datetime.datetime.now()
#######################################

#######################################
# Get the data type of the input data
dataType = getDataType(inData)
# Workspace, FeatureDataset, FeatureClass

if dataType == 'FeatureClass':
    # Only dealing with one feature class
    featureHandler(inData)

elif dataType == 'FeatureDataset':
    # Feature Dataset - add new fields to all features in the dataset
    # Create a list of the features in the dataset and send to handler
    arcpy.env.workspace = inData
    fcList = arcpy.ListFeatureClasses()
    for fc in fcList:
        featureHandler(fc)

elif dataType == 'Workspace':
    # Workspace - add fields to features within feature datasets
    # and any stand-alone feature classes

    arcpy.env.workspace = inData

    # Handle feature datasets within the workspace
    fdList = [fd for fd in arcpy.ListDatasets(None, 'Feature')]
    for featureDataset in fdList:
        fcList = [fc for fc in arcpy.ListFeatureClasses(None, None, featureDataset)]
        for featureClass in fcList:
            featureHandler(featureClass)

    # Handle standalone feature classes within the workspace
    fcList =[fc for fc in arcpy.ListFeatureClasses()]
    for featureClass in fcList:
        featureHandler(featureClass)
#######################################

#######################################
# Script finish
endTime = datetime.datetime.now()
timeDelta = str(endTime - startTime)
print 'Script completed in {0}'.format(timeDelta)
#######################################
if __name__ == '__main__':
    main()