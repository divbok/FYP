from os import listdir
from os.path import isfile, join
from xml.dom import minidom
import re

 # <uses-permission android:name="android.permission.INTERNET"/>

ManifestFolder = "dataset/Manifestfiles/"
permissionListFile = "dataset/android_perm_list.txt"

perm_file = open(permissionListFile,"r")
perm_dict = { }

number_of_permissions = 0 # initialize value

for permission in perm_file:
	perm_dict[permission.strip()] = number_of_permissions
	number_of_permissions = number_of_permissions + 1



fileList = [f for f in listdir(ManifestFolder) if isfile(join(ManifestFolder, f))]


for file in fileList:
	
	permission_vector = [0 for _ in range(number_of_permissions)]
	xmldoc = minidom.parse(ManifestFolder+file)
	perm_tags = xmldoc.getElementsByTagName('uses-permission')
	permission_list = [p.attributes['android:name'].value for p in perm_tags]
	
	for permission in permission_list:
		if permission in perm_dict:
			permission_vector[perm_dict[permission]] = 1

	sha256,remaining = file.split("_pkgname")
	package_name,vt_score = remaining.split("_vtscore")
	print(package_name+","+sha256+",".join([str(val) for val in permission_vector])+","+re.sub("\.xml","",vt_score))

	
	


