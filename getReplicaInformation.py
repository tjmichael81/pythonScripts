#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tmichael
#
# Created:     17/01/2014
# Copyright:   (c) tmichael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
import smtplib
import sys
import traceback


#Script Variables
connFileDirectory = r'C:\TEMP\ConnectionFiles'
arcpy.env.workspace = connFileDirectory

#Email Settings
emailBody = ''
emailSubject = 'Replica Information'
emailRecipient = ''
smtpuser = ''
smtppass = ''


#Script Functions
def getGDBName(gdb):
    fileName = os.path.basename(gdb)
    dbName = os.path.splitext(fileName)[0]
    return dbName

try:
    #Get a list of SDE files in the specified directory
    workspaces = arcpy.ListWorkspaces('*', 'SDE')

    #Get the replicas in each dataabse
    for gdb in workspaces:
        #Get the geodatabase name from the file name
        #Add geodatabase name to email body
        gdbName = getGDBName(gdb)
        emailBody += gdbName + '\n'


        for replica in arcpy.da.ListReplicas(gdb):
            #Add replica name to email body
            emailBody += '\t' + replica.name + '\n'

            #Determine the replica role (Parent / Child)
            #Print when last changes sent or received based on role type
            replicaRole = replica.isParent
            if replicaRole == True:
                emailBody += '\t\t Last Changes Sent' + ' ' + str(replica.lastSend) + '\n'
            else:
                emailBody += '\t\t Last Changes Received' + ' ' + str(replica.lastReceive) + '\n'




    #Finally
    print emailBody
    #Send email
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #erver.starttls()
    #server.ehlo()
    #server.login(smtpuser, smtppass)
    #server.sendmail(smtpuser, emailRecipient, emailBody)
    #server.quit()

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

