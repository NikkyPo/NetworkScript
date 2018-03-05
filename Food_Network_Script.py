# ---------------------------------------------------------------------------
# Food Network Script
# Author: Nicole Helgeson
# GIS 5572
# Description: 
# This script creates a new Food Network and associated attributes by copying an original Food Network and appending it
# to the master "AllNetworks" shapefile. This script is for helping maintain the Minnesota Food Networks web map.
# ---------------------------------------------------------------------------

# Import arcpy Module and ask user for workspace path.
import arcpy

print("This script creates a new Food Network from the geometry of an input Food Network and adds the information to " +
      "the AllNetworks shapefile, a master list of all known Food Networks.")
print("\n")
arcpy.env.workspace = raw_input("Please enter your workspace path: ")
arcpy.env.workspace = True


def FieldManagement(New_Input):
    ''' The following function defines the variables that ask for user input for the new fields.
        Then, the previously defined variables are used as input to calculate the fields of the
        new Food Network. This information is returned.'''
    
    print('Please provide the new information for the New Food Network. Be sure to put the answers in "double quotes". ')
    print("\n")
    Network_Name = raw_input("New Network Name: ")
    Contact = raw_input("Contact: ")
    Email = raw_input("Email: ")
    Status = raw_input("Status: ")
    Region = raw_input("Region: ")
    Geography = raw_input("Geography: ")

    # The previously defined variables are used as input to calculate the fields of the new Food Network
    arcpy.CalculateField_management(New_Input_Food_Network_Name, "Network_Na", Network_Name, "VB", "")
    arcpy.CalculateField_management(New_Input_Food_Network_Name, "Contact", Contact, "VB", "")
    arcpy.CalculateField_management(New_Input_Food_Network_Name, "Email", Email, "VB", "")
    arcpy.CalculateField_management(New_Input_Food_Network_Name, "Status", Status, "VB", "")
    arcpy.CalculateField_management(New_Input_Food_Network_Name, "Region", Region, "VB", "")
    arcpy.CalculateField_management(New_Input_Food_Network_Name, "Geography", Geography, "VB", "")

    return New_Input


# First, the script variables are defined. These include defining the paths to the original Food Network, where the new
# Food Network will be stored, and identifying where the All Networks shapefile is located.
      
Input_Food_Network = raw_input("Original Food Network path that you want to copy: ") 
New_Input_Food_Network_Name = raw_input("New Food Network path. Be sure to include a new name. ") 
NEW_All_Networks_shp = raw_input("AllNetworks shapefile path: ")
New_Food_Network = New_Input_Food_Network_Name
New_All_Networks_file = NEW_All_Networks_shp

print("\n")
print("Thank you. Creating....")

# This process copies the original Food Network to the New Network.
arcpy.Copy_management(Input_Food_Network, New_Input_Food_Network_Name, "ShapeFile")

# The function is called that will complete the process of editing the new Food Network.
FieldManagement(New_Input_Food_Network_Name)

# This process appends the newly created Food Network (with the defined fields) into the All Networks
# shapefile.
arcpy.Append_management(New_Input_Food_Network_Name, New_All_Networks_file, "NO_TEST", "", "")

# Final message that confirms everything worked properly.
print("\n")
print("Your new Food Network has been created.")

