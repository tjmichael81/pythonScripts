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
    commonFields = ['ESRIGNSS_RECEIVER', 'ESRIGNSS_H_RMS', 'ESRIGNSS_V_RMS', 'ESRIGNSS_LATITUDE', 'ESRIGNSS_LONGITUDE',
                    'ESRIGNSS_ALTITUDE', 'ESRIGNSS_PDOP', 'ESRIGNSS_HDOP', 'ESRIGNSS_VDOP', 'ESRIGNSS_FIXTYPE',
                    'ESRIGNSS_NUMSATS', 'ESRIGNSS_FIXDATETIME']

    #######################################
    # Field Configurations
    #######################################

    # 'GNSS Receiver' field
    def ESRIGNSS_RECEIVER(inFeature):
        startMessage('Receiver Name')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_RECEIVER', 'TEXT', None, None, 50, 'Receiver Name', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Receiver Name')

    # 'H RMS' field
    def ESRIGNSS_H_RMS(inFeature):
        startMessage('Horizontal Accuracy')
        arcpy.AddField_management(inFeature, 'ESRIGNSS _H_RMS', 'DOUBLE', None, None, None, 'Horizontal Accuracy (m)', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Horizontal Accuracy')

    # 'V RMS' field
    def ESRIGNSS_V_RMS(inFeature):
        startMessage('Vertical Accuracy')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_V_RMS', 'DOUBLE', None, None, None, 'Vertical Accuracy (m)', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Vertical Accuracy')

    # 'Latitude' field
    def ESRIGNSS_LATITUDE(inFeature):
        startMessage('Latitude')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_LATITUDE', 'DOUBLE', None, None, None, 'Latitude', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Latitude')

    # 'Longitude' field
    def ESRIGNSS_LONGITUDE(inFeature):
        startMessage('Longitude')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_LONGITUDE', 'DOUBLE', None, None, None, 'Longitude', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Longitude')

    # 'Altitude' field
    def ESRIGNSS_ALTITUDE(inFeature):
        startMessage('Altitude')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_ALTITUDE', 'DOUBLE', None, None, None, 'Altitude', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Altitude')

    # 'PDOP' field
    def ESRIGNSS_PDOP(inFeature):
        startMessage('PDOP')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_PDOP', 'DOUBLE', None, None, None, 'PDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('PDOP')

    # 'HDOP' field
    def ESRIGNSS_HDOP(inFeature):
        startMessage('HDOP')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_HDOP', 'DOUBLE', None, None, None, 'HDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('HDOP')

    # 'VDOP' field
    def ESRIGNSS_VDOP(inFeature):
        startMessage('VDOP')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_VDOP', 'DOUBLE', None, None, None, 'VDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('VDOP')

    # 'Fix Type' field
    def ESRIGNSS_FIXTYPE(inFeature):
        startMessage('Fix Type')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_FIXTYPE', 'SHORT', None, None, None, 'Fix Type', 'NULLABLE', 'NON_REQUIRED', 'GNSSFixType')
        successMessage('Fix Type')

    # 'Number of Satellites' field
    def ESRIGNSS_NUMSATS(inFeature):
        startMessage('Number of Satellites')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_NUMSATS', 'SHORT', None, None, None, 'Number of Satellites', 'NULLABLE', 'NON_REQUIRED', 'NumSatellites')
        successMessage('Number of Satellites')

    # 'Fix Time' field
    def ESRIGNSS_FIXDATETIME(inFeature):
        startMessage('Fix Time')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_FIXDATETIME', 'DATE', None, None, None, 'Fix Time', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('Fix Time')

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
