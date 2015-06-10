pythonScripts
=============

A collection of Python projects and utilities that I use / am working on

File Descriptions:
###createMapsByFeatureExtent.py
- Given an input polygon feature class and template map, create a new .mxd for each polygon in the input feature class

###exportFeatureAttachments.py
- Export feature attachments from an Esri geodatabase feature attachment table to a specified folder
- Write the path to each expoted file to a new column in the feature attachment table
- [Thanks to Andrew and his blog post here for the post on working with blob data](http://anothergisblog.blogspot.com/2012/06/working-with-blob-data-at-101-arcpyda.html)

###getReplicaInformation.py
- Get .sde files from given directory
- Get basic replica information (name, last sync) from each replica
- Print or email output

###listDomainsForFields.py
- For provided workspace, get feature datasets, feature classes, fields
- Check if fields have domains.  If so, get domain name and values (range and coded domains)

###renameAGSCacheFiles.py
- Input _alllayers folder from an ArcGIS Server-created cache (exploded format)
- Convert directory and file names from hexadecimal to integer
- Once converted the cache is in the correct format to be used as a hosted tile service

###updatePointCoordinates.py
- Update point coordinates (X, Y) based on new coordinates stored in the attribute table of the feature class
