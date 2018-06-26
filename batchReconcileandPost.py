import arcpy    
import datetime
import os

# Reconvile Versions help page
# http://desktop.arcgis.com/en/arcmap/latest/tools/data-management-toolbox/reconcile-versions.htm

# Get todays date to use in log file name
date_today = datetime.datetime.today()
date_str = date_today.strftime('%Y%m%d')

# Database connection path - .sde file
# This script uses relative paths, where .sde files are stored in a 'dbconnectionfiles' subdirectory
db_connection = os.path.join(os.getcwd(), r"\dbconnectionfiles\< file name >.sde") #UPDATE

# Get list of database versions
version_list = arcpy.ListVersions(db_connection)

# Variables and configuration for output log path
output_log_path = r"C:\< path to log folder >" #UPDATE
output_project_name = "< Project Name >" #UPDATE
output_log_name = output_project_name + date_str + ".txt"
output_log = os.path.join(output_log_path, output_log_name)

arcpy.ReconcileVersions_management(db_connection, "ALL_VERSIONS", "dbo.DEFAULT", version_list, "LOCK_ACQUIRED", 
                                    "ABORT_CONFLICTS", "BY_ATTRIBUTE", "FAVOR_TARGET_VERSION", "POST", "KEEP_VERSION", output_log)

print("Reconcile and Post Complete")
