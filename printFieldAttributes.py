import arcpy

##############################################################################
# Script Variables
##############################################################################

# Input dataset - could be geodatabase, feature dataset, stand-alone feature
in_data = r'C:\TEMP\bsb\_server\gdb.gdb\SewerStormwater'

##############################################################################
# Script Functions
##############################################################################


def get_datatype(feture):
    """Return the DataType from arcpy.Describe"""
    describe = arcpy.Describe(feture)
    return describe.DataType


def get_fields(feature):
    """Return list of fields from input feature"""
    return arcpy.ListFields(feature)

##############################################################################
# Script Processing
##############################################################################

# Get the data type of the input data (geodatabase, feature dataset, feature class)
dataType = get_datatype(in_data)

if dataType == "FeatureClass":
    # Only dealing with one feature class
    dsc = arcpy.Describe(in_data)
    print dsc.baseName
    fields = get_fields(in_data)
    for f in fields:
        print "\t", f.baseName, "\t\t", f.type

elif dataType == "FeatureDataset":
    # Feature Dataset - print fields for each feature class in the dataset
    arcpy.env.workspace = in_data
    fcList = arcpy.ListFeatureClasses()
    for fc in fcList:
        dsc = arcpy.Describe(fc)
        print dsc.baseName
        fields = get_fields(fc)
        for f in fields:
            print "\t", f.name, "\t\t", f.type

elif dataType == "Workspace":
    # Workspace - add fields to features within feature datasets
    # and any stand-alone feature classes
    arcpy.env.workspace = in_data

    """ This section needs updating"""

    """
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
    """