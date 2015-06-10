#-------------------------------------------------------------------------------
# Name:        getFolderServiceCount.py
# Author:      Timothy Michael
# Created:     19/10/2013
# Copyright:   (c) Timothy Michael 2013
# Licence:     N/A
#-------------------------------------------------------------------------------

def main():
    pass

    import json
    import requests
    import urlparse

    #URL and parameters for the request
    #Set values for now...
    catalogURL = 'http://sampleserver1.arcgisonline.com/arcgis/rest/services'
    params = {'f': 'json'}

    request = requests.get(catalogURL, params=params)
    data = json.loads(request.text)

    #Server Folder and Service Counts
    serverFolderCount = 0
    serverServiceCount = 0

    #Print service names T/F
    printInfo = False

    #Count, list services in 'root' of ArcGIS Server Catalog
    if 'services' in data:
        serviceNames = data['services']
        serverServiceCount = serverServiceCount + len(serviceNames)
        for service in serviceNames:
            if printInfo:
                print 'Catalog Root ' + '\n\t' + service['name']

    #Check for folders in the ArcGIS Server Catalog
    if 'folders' in data:
        folderNames = data['folders']
        serverFolderCount = serverFolderCount + len(folderNames)
        for folder in folderNames:
            if printInfo:
                print folder
            """
            For each folder, construct a new URL to query
            Tried using urlparse.urljoin to build the URL below
            with unexpected behavior
            """
            folderURL = catalogURL + '/' + folder
            folderRequest = requests.get(folderURL, params=params)
            folderData = json.loads(folderRequest.text)
            #Check for services and print info
            if 'services' in folderData:
                serviceNames = folderData['services']
                serviceCount = len(serviceNames)
                #print str(serviceCount) + ' services in Folder'
                serverServiceCount = serverServiceCount + serviceCount
                for service in serviceNames:
                    if printInfo:
                        print '\t' + service['name']

    #Print Server Results
    print '\n\n'
    print 'ArcGIS Version: ' + str(data['currentVersion'])
    print 'Server Contains ' + str(serverFolderCount) + ' Folders'
    print 'Server Running ' + str(serverServiceCount) + ' Services'




if __name__ == '__main__':
    main()


