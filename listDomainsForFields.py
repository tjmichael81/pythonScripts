#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothy Michael
#
# Created:     25/06/2014
# Copyright:   (c) Timothy Michael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
#-------------------------------------------------------------------------------
#import modules
#-------------------------------------------------------------------------------

import arcpy
import sys
import traceback

try:
    #---------------------------------------------------------------------------
    #script variables
    #---------------------------------------------------------------------------
    dataSource = r'Database Servers\TMICHAEL-PC_SQLEXPRESS.gds\LGIM_102 (VERSION:DBO.DEFAULT)'
    arcpy.env.workspace = dataSource
    datasetName = 'WaterDistribution'
    datasetType = 'Feature'
    domainDict = {}
    reportText = ''

    #---------------------------------------------------------------------------
    #script functions
    #---------------------------------------------------------------------------

    def listFeatureClasses(wildcard=None, featureType=None, featureDataset=None):
        '''List feature classes in dataset'''
        featureClasses = arcpy.ListFeatureClasses(wildcard, featureType, featureDataset)
        return featureClasses

    def listFeatureDatasets(wildcard, featureType):
        '''List datasets in workspace'''
        datasets = arcpy.ListDatasets(wildcard, featureType)
        return datasets

    #---------------------------------------------------------------------------
    #script processes
    #---------------------------------------------------------------------------

    #Get list of domains in the workspace
    domainList = arcpy.da.ListDomains(dataSource)

    #Convert list of domains to dictionary, where
    #key:value = <domain name> : <list index>
    #This will allow us to discover the index position of a domain name
    #to use to query the domainList for additional information
    for index, element in enumerate(domainList):
        domainName = str(element.name)
        domainDict[domainName] = str(index)

    #Get a list of datasets in the workspace
    #Check to see if the datasetName variable has a value
    #If no value, function will return all datasets
    if not datasetName:
        dsList = listFeatureDatasets('*', datasetType)
    else:
        wildCard = '*' + datasetName + '*'
        dsList = listFeatureDatasets(wildCard, datasetType)

    #Loop through datasets returned in dsList
    #List feature classes contained in the dataset
    for ds in dsList:
        #Add dataset name to report
        #Create list of feature classes within dataset
        reportText += 'Dataset Name: {0} \n'.format(ds.split('.')[-1])
        fcList = listFeatureClasses('*', 'All', ds)

        #Feature class / field loop
        for fc in fcList:
            #Add feature class name to report
            #Create list of fields within each feature class
            reportText += '\t{0}\n'.format(fc.split('.')[-1])

            #Create field list for each feature class
            #Determine if the field has an associated domain
            ###TODO move this into a function###
            fieldList = arcpy.ListFields(fc)
            for field in fieldList:
                #If the field does not have a domain
                #Print field name only
                if field.domain == '' or field.domain == None:
                    print 'Field Name: {}'.format(field.name)

                #If the field has a domain
                #Print field name, domain, and info
                else:
                    print 'Field Name: {0} \n Field Domain: {1}'.format(field.name, field.domain)

                    #BEGIN DOMAIN DETAILS DISCOVERY
                    #Determine index position of domain from domainDict
                    domainIndex = domainDict[field.domain]
                    domainType = domainList[int(domainIndex)].domainType

                    print 'Domain Type: {}'.format(domainType)
                    if domainType == 'CodedValue':
                        coded_values = domainList[int(domainIndex)].codedValues
                        for val, desc in coded_values.iteritems():
                            print('{0} : {1}'.format(val, desc))
                    elif domainType == 'Range':
                        print('Min: {0}'.format(domainList[int(domainIndex)].range[0]))
                        print('Max: {0}'.format(domainList[int(domainIndex)].range[1]))




    #Print report
    #This will be written to a file when complete
    #print reportText
#---------------------------------------------------------------------------
#Error Handling
#---------------------------------------------------------------------------
except arcpy.ExecuteError:
    # Get the tool error messages
    #
    msgs = arcpy.GetMessages(2)

    # Return tool error messages for use with a script tool
    #
    arcpy.AddError(msgs)

    # Print tool error messages for use in Python/PythonWin
    #
    print msgs

except:
    # Get the traceback object
    #
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    #
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    # Return python error messages for use in script tool or Python Window
    #
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

    # Print Python error messages for use in Python / Python Window
    #
    print pymsg + "\n"
    print msgs




if __name__ == '__main__':
    main()
