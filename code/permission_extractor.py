from os import listdir
from os.path import isfile, join
from xml.dom import minidom
import re

 # <uses-permission android:name="android.permission.INTERNET"/>

ManifestFolder = "dataset/ClusterManifestFiles/"
permissionListFile = "results_new/perm_final_list.csv"
missingPermissionFile = "dataset/missed_perm.csv"



perm_file = open(permissionListFile,"r")
miss_perm_file = open(missingPermissionFile,"a")
perm_dict = { }

number_of_permissions = 0 # initialize value

for permission in perm_file:

	perm_dict["android.permission."+permission.split(",")[0].strip()] = number_of_permissions
	number_of_permissions = number_of_permissions + 1



fileList = [f for f in listdir(ManifestFolder) if isfile(join(ManifestFolder, f))]


for file in fileList:

	permission_vector = [0 for _ in range(number_of_permissions)]
	xmldoc = minidom.parse(ManifestFolder+file)
	perm_tags = xmldoc.getElementsByTagName('uses-permission')
	permission_list = [p.attributes['android:name'].value for p in perm_tags if p.hasAttribute('android:name')]

	family_name = file.split("_")[0]
	app_name = file.split("_")[-1]
	for permission in permission_list:
		if permission in perm_dict:
			permission_vector[perm_dict[permission]] = 1
	print(family_name+","+app_name+","+",".join([str(val) for val in permission_vector]))
