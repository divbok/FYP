import os

skip_file ="dataset/skip.txt"
list_file = "dataset/list.csv"
api_key = "f8c0594ac124026fbb71973a5ee54b6e5d65ca098c92ec030cd5f760ed350aa0"
sha_key = ""
url = "https://androzoo.uni.lu/api/download?apikey="

skipped_list = open(skip_file,"w+")
fh = open(list_file,"r")
size_limit = 2500000

fh.readline()
for apk in fh:
    elements = apk.split(",")
    if( int(elements[4]) > size_limit ) :
        skipped_list.write(elements[0]+"blah" + "\n")
        print("SKipping")
        continue

    download_link = "curl -O --remote-header-name -G -d apikey="+api_key+" -d sha256="+elements[0] + " https://androzoo.uni.lu/api/download"
    os.system(download_link)
    manifest_extraction = "apktool d " + elements[0] +".apk"
    os.system(manifest_extraction)
    os.system("rm -f " +elements[0] +".apk")
    os.system("mv " + elements[0] + "/AndroidManifest.xml dataset/Manifestfiles/" + elements[0] + ".xml" )
    os.system("rm -rf " +elements[0])
