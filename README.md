pythonScripts
=============

A collection of Python projects and utilities that I use / am working on

File Descriptions:

### addCollectorAutoFields _py2 and _py3
- Add fields to feature class(es) to support GPS metadata capture in Collector for ArcGIS
- Versions for Python 2 and Python 3 (Python 3 version can be imported into ArcGIS Pro)
- [Record GPS Metadata in Collector for ArcGIS](http://doc.arcgis.com/en/collector/ios/create-maps/gps-map-prep.htm)

### addCommonFeatureSettings.py
- Add feature attachments, editor tracking, and GlobalID fields to features and tables in a geodatabase

### batchReconcileandPost.py
- Script used to schedule reconcile/post of all database versions and generate log file

### createMapsByFeatureExtent.py
- Given an input polygon feature class and template map, create a new .mxd for each polygon in the input feature class

### exportFeatureAttachments.py
- Export feature attachments from an Esri geodatabase feature attachment table to a specified folder
- Write the path to each expoted file to a new column in the feature attachment table
- [Thanks to Andrew and his blog post here for the post on working with blob data](http://anothergisblog.blogspot.com/2012/06/working-with-blob-data-at-101-arcpyda.html)

### getFolderServiceCount.py
- For provided ArcGIS Server, return server version, folder count, service count

### getReplicaInformation.py
- Get .sde files from given directory
- Get basic replica information (name, last sync) from each replica
- Print or email output

### listDomainsForFields.py
- For provided workspace, get feature datasets, feature classes, fields
- Check if fields have domains.  If so, get domain name and values (range and coded domains)

### renameAGSCacheFiles.py
- Input _alllayers folder from an ArcGIS Server-created cache (exploded format)
- Convert directory and file names from hexadecimal to integer
- Once converted the cache is in the correct format to be used as a hosted tile service

### updatePointCoordinates.py
- Update point coordinates (X, Y) based on new coordinates stored in the attribute table of the feature class