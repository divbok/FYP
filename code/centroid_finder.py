from os import listdir
from os.path import isfile, join
from xml.dom import minidom
import re

ManifestFolder = "dataset/ClusterManifestFiles/"
permissionListFile = "results_new/perm_final.txt"
missingPermissionFile = "dataset/missed_perm.csv"

cutoff = 3
min_permission_count = 2

perm_file = open(permissionListFile,"r")
miss_perm_file = open(missingPermissionFile,"a")
perm_dict = { }

number_of_permissions = 0 # initialize value

for permission in perm_file:
	perm_dict[permission.strip()] = number_of_permissions
	number_of_permissions = number_of_permissions + 1



fileList = [f for f in listdir(ManifestFolder) if isfile(join(ManifestFolder, f))]
fileList.sort()

fname = "ADRD"
count_of_apps = 0
permission_count_vector = [0 for _ in range(number_of_permissions)]

for file in fileList:
	
	permission_vector = [0 for _ in range(number_of_permissions)]
	xmldoc = minidom.parse(ManifestFolder+file)
	perm_tags = xmldoc.getElementsByTagName('uses-permission')
	permission_list = [p.attributes['android:name'].value for p in perm_tags if p.hasAttribute('android:name')]


	family_name = file.split("_")[0]
	app_name = re.sub("\.xml","",file.split("_")[-1])

	if family_name != fname:
			cluster_value = []
			for count in permission_count_vector:
				if count >= int(count_of_apps/2)+1:
					cluster_value.append(1)
				else:
					cluster_value.append(0)

			print(fname+",["+" ".join([str(val) for val in cluster_value])+"]")
			# print(fname+","+str(count_of_apps))
			fname = family_name
			permission_count_vector = [0 for _ in range(number_of_permissions)]
			count_of_apps = 0

	count_of_apps += 1
	for permission in permission_list:
		if permission in perm_dict:
			permission_vector[perm_dict[permission]] = 1
			permission_count_vector[perm_dict[permission]] += 1

cluster_value = []
for count in permission_count_vector:
	if count >= int(count_of_apps/2)+1:
		cluster_value.append(1)
	else:
		cluster_value.append(0)
print(fname+",["+" ".join([str(val) for val in cluster_value])+"]")


	
	

	
	


