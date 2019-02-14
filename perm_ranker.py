import numpy as np
import math

def get_rank(x):
    return float(x.split(",")[-1])

#Get the datasets
malwaredata = np.genfromtxt("dataset/malware.csv",delimiter=',')
benigndata = np.genfromtxt("dataset/benign.csv",delimiter=',')

#Extract permissions name
mdata = open("dataset/malware.csv")
columns = mdata.readline().strip()
permission = columns.split(",")[2:]
mdata.close()

#Count of apps per permission
msum_col= np.sum(malwaredata[1:,2:],axis=0)
bsum_col= np.sum(benigndata[1:,2:],axis=0)

#Size of datasets
mal_size= malwaredata.shape[0] - 1
ben_size= benigndata.shape[0] - 1

#Calculate support and rank for each permission
support_perm = [x*mal_size/ben_size for x in bsum_col]
rank = [(x-y)/(x+y) for x,y in zip(msum_col,support_perm)]

results = [a+","+str(b)+","+str(c)+","+str(d)+","+str(e) for a,b,c,d,e in zip(permission,msum_col,bsum_col,support_perm,rank) if math.isnan(e) is False]
sorted_results = sorted(results,key = get_rank)
for r in sorted_results:
	print(r)
