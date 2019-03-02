import os
import re

skip_file ="dataset/skipped.txt"
list_file = "dataset/lists.csv"
api_key = "f8c0594ac124026fbb71973a5ee54b6e5d65ca098c92ec030cd5f760ed350aa0"
url = " https://androzoo.uni.lu/api/download"

size_limit = 10000000
manifest_downloaded = 0



skipped_list = open(skip_file,"a")
fh = open(list_file,"r")
# fh.readline() #Skip the header

for apk in fh:
    
    sha256,sha1,md5,dex_date,apk_size,pkg_name,vercode,vt_detection,vt_scan_date,dex_size,markets = apk.split(",")
    
    if( int(apk_size) > size_limit ) :
        #skipped_list.write(apk)
        print("Size Limit Exceeded..Skipping apk\n")
        continue

    download_link = "curl  -O --remote-header-name -G -d apikey=" + api_key + " -d sha256=" + sha256 + url
    manifest_extraction = "apktool d " + sha256 +".apk"
    output_file_name = sha256+"_"+re.sub('\"','',pkg_name)+"_"+vt_detection+".xml"


    print("Downloading the apk file\n") 
    os.system(download_link)

    print("Extracting files from apk")
    os.system(manifest_extraction)
   
    print("Copying the manifest file alone")
    os.system("mv " + sha256 + "/AndroidManifest.xml dataset/Manifestfiles/" + output_file_name)
    
    print("Removing all other files that are not required")
    os.system("rm -f " + sha256 +".apk")
    os.system("rm -rf " +sha256)
    

    manifest_downloaded = manifest_downloaded + 1
    print("Number of Mainfest Downloaded till now : "+str(manifest_downloaded)+"\n\n")