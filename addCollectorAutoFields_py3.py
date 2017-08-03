#-------------------------------------------------------------------------------
# DESCRIPTION
#-------------------------------------------------------------------------------

def main():
    pass

##############################################################################
# Import Modules
##############################################################################
import arcpy
import datetime

##############################################################################
# Script Variables
##############################################################################
# Connection / path to root geodatabase
# Will be used to check for / add required domains
inWorkspace = r'C:\TEMP\collectorgpstest\WaterUtilities.gdb'

# Input dataset - could be geodatabase, feature dataset, stand-alone feature
inData = r'C:\TEMP\collectorgpstest\WaterUtilities.gdb'

##############################################################################
# Script Functions
##############################################################################
def addPointFields(inFeature, fieldList):
    '''Adds GPS metadata to point features'''

    print('Adding GPS metadata fields to {0}'.format(inFeature))
    print('\n')

    # This list of fields will be used to compare against the list of fields
    # for the input feature, and then to call the function to add new fields
    pointFields = ['ESRIGNSS_RECEIVER', 'ESRIGNSS_H_RMS', 'ESRIGNSS_V_RMS',
    'ESRIGNSS_LATITUDE', 'ESRIGNSS_LONGITUDE', 'ESRIGNSS_ALTITUDE', 'ESRIGNSS_PDOP',
    'ESRIGNSS_VDOP', 'ESRIGNSS_HDOP', 'ESRIGNSS_FIXTYPE', 'ESRIGNSS_CORRECTIONAGE',
    'ESRIGNSS_STATIONID', 'ESRIGNSS_NUMSATS', 'ESRIGNSS_FIXDATETIME', 'ESRIGNSS_AVG_H_RMS',
    'ESRIGNSS_AVG_V_RMS', 'ESRIGNSS_AVG_POSITIONS', 'ESRIGNSS_H_STDDEV']

    #######################################
    # Field Configurations
    #######################################

    def ESRIGNSS_RECEIVER(inFeature):
        startMessage('ESRIGNSS_RECEIVER')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_RECEIVER', 'TEXT', None, None, 50, 'Receiver Name', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_RECEIVER')

    def ESRIGNSS_H_RMS(inFeature):
        startMessage('ESRIGNSS_H_RMS')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_H_RMS', 'DOUBLE', None, None, None, 'Horizontal Accuracy (m)', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_H_RMS')

    def ESRIGNSS_V_RMS(inFeature):
        startMessage('ESRIGNSS_V_RMS')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_V_RMS', 'DOUBLE', None, None, None, 'Vertical Accuracy (m)', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_V_RMS')

    def ESRIGNSS_LATITUDE(inFeature):
        startMessage('ESRIGNSS_LATITUDE')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_LATITUDE', 'DOUBLE', None, None, None, 'Latitude', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_LATITUDE')

    def ESRIGNSS_LONGITUDE(inFeature):
        startMessage('ESRIGNSS_LONGITUDE')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_LONGITUDE', 'DOUBLE', None, None, None, 'Longitude', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_LONGITUDE')

    def ESRIGNSS_ALTITUDE(inFeature):
        startMessage('ESRIGNSS_ALTITUDE')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_ALTITUDE', 'DOUBLE', None, None, None, 'Altitude', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_ALTITUDE')

    def ESRIGNSS_PDOP(inFeature):
        startMessage('ESRIGNSS_PDOP')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_PDOP', 'DOUBLE', None, None, None, 'PDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_PDOP')

    def ESRIGNSS_HDOP(inFeature):
        startMessage('ESRIGNSS_HDOP')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_HDOP', 'DOUBLE', None, None, None, 'HDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_HDOP')

    def ESRIGNSS_VDOP(inFeature):
        startMessage('ESRIGNSS_VDOP')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_VDOP', 'DOUBLE', None, None, None, 'VDOP', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_VDOP')

    def ESRIGNSS_FIXTYPE(inFeature):
        startMessage('ESRIGNSS_FIXTYPE')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_FIXTYPE', 'SHORT', None, None, None, 'Fix Type', 'NULLABLE', 'NON_REQUIRED', 'GNSSFixType')
        successMessage('ESRIGNSS_FIXTYPE')

    def ESRIGNSS_CORRECTIONAGE(inFeature):
        startMessage('ESRIGNSS_CORRECTIONAGE')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_CORRECTIONAGE', 'DOUBLE', None, None, None, 'Correction Age', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_CORRECTIONAGE')

    def ESRIGNSS_STATIONID(inFeature):
        startMessage('ESRIGNSS_STATIONID')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_STATIONID', 'SHORT', None, None, None, 'Station ID', 'NULLABLE', 'NON_REQUIRED', 'NumStationID')
        successMessage('ESRIGNSS_STATIONID')

    def ESRIGNSS_NUMSATS(inFeature):
        startMessage('ESRIGNSS_NUMSATS')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_NUMSATS', 'SHORT', None, None, None, 'Number of Satellites', 'NULLABLE', 'NON_REQUIRED', 'NumSatellites')
        successMessage('ESRIGNSS_NUMSATS')

    def ESRIGNSS_FIXDATETIME(inFeature):
        startMessage('ESRIGNSS_FIXDATETIME')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_FIXDATETIME', 'DATE', None, None, None, 'Fix Time', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_FIXDATETIME')

    def ESRIGNSS_AVG_H_RMS(inFeature):
        startMessage('ESRIGNSS_AVG_H_RMS')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_AVG_H_RMS', 'DOUBLE', None, None, None, 'Average Horizontal Accuracy', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_AVG_H_RMS')

    def ESRIGNSS_AVG_V_RMS(inFeature):
        startMessage('ESRIGNSS_AVG_V_RMS')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_AVG_V_RMS', 'DOUBLE', None, None, None, 'Average Vertical Accuracy', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_AVG_V_RMS')

    def ESRIGNSS_AVG_POSITIONS(inFeature):
        startMessage('ESRIGNSS_AVG_POSITIONS')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_AVG_POSITIONS', 'LONG', None, None, None, 'Number of Positions Averaged', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_AVG_POSITIONS')

    def ESRIGNSS_H_STDDEV(inFeature):
        startMessage('ESRIGNSS_H_STDDEV')
        arcpy.AddField_management(inFeature, 'ESRIGNSS_H_STDDEV', 'DOUBLE', None, None, None, 'Standard Deviation', 'NULLABLE', 'NON_REQUIRED', None)
        successMessage('ESRIGNSS_H_STDDEV')

    # This locals() thing is awesome
    # https://docs.python.org/2/library/functions.html#locals
    # http://stackoverflow.com/questions/3061/calling-a-function-of-a-module-from-a-string-with-the-functions-name-in-python
    localFunctions = locals()

    # Compare the fields in the pointFields list in this function to the
    # list of fields for the input feature.  For each field that does not
    # match a field from the input, call the corresponding function to
    # add the field
    for field in pointFields:
        if field.lower() not in fieldList:
            localFunctions[field](inFeature)
        else:
            print('{0} already exists in {1}'.format(field, inFeature))

def getDataType(inData):
    '''Return the DataType from arcpy.Describe'''
    dsc =  arcpy.Describe(inData)
    return dsc.DataType

def featureHandler(inFeature):
    '''
    Describe the input feature class to determine the ShapeType
    Based on the ShapeType, send the feature to the correct function(s)
    to add new fields
    '''

    dsc = arcpy.Describe(inFeature)

    if dsc.shapeType == 'Point':
        print('{0} is a {1} feature'.format(dsc.name, dsc.shapeType))

        # Create a list of fields to compare against
        fieldList = createFieldList(inFeature)
        addPointFields(inFeature, fieldList)

    elif dsc.shapeType == 'Polyline':
        print('{0} is a {1} feature \n'.format(dsc.name, dsc.shapeType))
        print('GPS metadata not supported for {0} features'.format(dsc.shapeType))

    elif dsc.shapeType == 'Polygon':
        print('{0} is a {1} feature'.format(dsc.name, dsc.shapeType))
        print('GPS metadata not supported for {0} features'.format(dsc.shapeType))

    else:
        print('{0} is not a valid feature type.'.format(dsc.name))

def createFieldList(inputFeature):
    '''Return a list of fields from the input feature'''
    fieldList = [f.name.lower() for f in arcpy.ListFields(inputFeature,"*","All")]
    return fieldList

def startMessage(fName):
    print('Adding {0} field'.format(fName))

def successMessage(fName):
    print('{0} field added successfully'.format(fName))
    print('\n')

def getShapeType(inFeature):
    '''Return the FeatureType from arcpy.Describe'''
    dsc = arcpy.Describe(inFeature)
    return dsc.FeatureType

##############################################################################
# Do some actual stuff
##############################################################################
startTime = datetime.datetime.now()

# Check for / add required GPS metadata domains
# GNSSFixType, NumSatellites, NumStationID
domain_list = [domain.name.lower() for domain in arcpy.da.ListDomains(inWorkspace)]

# Check for / add GNSSFixType
if 'gnssfixtype' in domain_list:
    print('GNSSFixType domain found in workspace')

else:
    arcpy.CreateDomain_management(inWorkspace, 'GNSSFixType', 'GNSS Fix Type', 'SHORT', 'CODED', 'DUPLICATE', 'DEFAULT')
    arcpy.AddCodedValueToDomain_management(inWorkspace, 'GNSSFixType', '0', 'Fix not valid')
    arcpy.AddCodedValueToDomain_management(inWorkspace, 'GNSSFixType', '1', 'GPS')
    arcpy.AddCodedValueToDomain_management(inWorkspace, 'GNSSFixType', '2', 'Differential GPS')
    arcpy.AddCodedValueToDomain_management(inWorkspace, 'GNSSFixType', '4', 'RTK Fixed')
    arcpy.AddCodedValueToDomain_management(inWorkspace, 'GNSSFixType', '5', 'RTK Float')
    print('GNSSFixType domain added')

# Check for / add NumSatellites
if 'numsatellites' in domain_list:
    print('NumSatellites domain found in workspace')

else:
    arcpy.CreateDomain_management(inWorkspace, 'NumSatellites', 'Number of Satellites', 'SHORT', 'RANGE', 'DUPLICATE', 'DEFAULT')
    arcpy.SetValueForRangeDomain_management(inWorkspace, 'NumSatellites', '0', '99')
    print('NumSatellites domain added')

# Check for / add NumStationID
if 'numstationid' in domain_list:
    print('NumStationID domain found in workspace')

else:
    arcpy.CreateDomain_management(inWorkspace, 'NumStationID', 'Station ID', 'SHORT', 'RANGE', 'DUPLICATE', 'DEFAULT')
    arcpy.SetValueForRangeDomain_management(inWorkspace, 'NumSatellites', '0', '1023')
    print('NumStationID domain added')

# Get the data type of the input data
# (geodatabase, feature dataset, feature class)
dataType = getDataType(inData)

if dataType == 'FeatureClass':
    # Only dealing with one feature class
    featureHandler(inData)

elif dataType == 'FeatureDataset':
    # Feature Dataset - add new fields to all point features in the dataset
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
    fdList = [fd for fd in arcpy.ListDatasets('*', 'Feature')]
    fdList = [fd for fd in arcpy.ListDatasets(None, 'Feature')]
    for featureDataset in fdList:
        fcList = [fc for fc in arcpy.ListFeatureClasses(None, None, featureDataset)]
        for featureClass in fcList:
            featureHandler(featureClass)

    # Handle standalone feature classes within the workspace
    fcList =[fc for fc in arcpy.ListFeatureClasses()]
    for featureClass in fcList:
        featureHandler(featureClass)

##############################################################################
# Wrap up
##############################################################################
endTime = datetime.datetime.now()
timeDelta = str(endTime - startTime)
print('Script completed in {0}'.format(timeDelta))


if __name__ == '__main__':
    main()
