import os
import sys
import re
from os.path import isfile, join
from os import listdir

clusterfolder = "../data/CLASS_ENCRYPTION_APK/Malgenome/"


malware_family_name = next(os.walk(clusterfolder))[1]

manifest_extracted = 0

for malware in malware_family_name:
	
	print("Family:"+malware)
	fileList = [f for f in listdir(clusterfolder+malware) if isfile(join(clusterfolder+malware, f))]
	
	for file in fileList:
		
		print("Filename:"+file)
		file_path = clusterfolder+malware+"/"+file
		manifest_extraction = "apktool -s d " + file_path
		folder_name = re.sub("\.apk","",file)	

		output_file_name = malware+"_"+folder_name+".xml"


		
		os.system(manifest_extraction)
		os.system("mv " + folder_name + "/AndroidManifest.xml dataset/ClusterManifestFiles/" + output_file_name)
		os.system("rm -rf " +folder_name)

		manifest_extracted= manifest_extracted + 1
		print("Number of Mainfest Downloaded till now : "+str(manifest_extracted)+"\n\n")

