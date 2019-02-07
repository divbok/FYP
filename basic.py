import numpy as np
import math

def get_rank(x):
    return float(x.split("\t")[-1])

malwaredata= np.genfromtxt("dataset/malware.csv",delimiter=',')
benigndata= np.genfromtxt("dataset/benign.csv",delimiter=',')

mdata = open("dataset/malware.csv")
columns = mdata.readline().strip()
permission = columns.split(",")[2:]
print(len(permission))
mdata.close()
#print data.shape
#print len(col_totals)
msum_col= np.sum(malwaredata[1:,2:],axis=0)
bsum_col= np.sum(benigndata[1:,2:],axis=0)
mal_size= malwaredata.shape[0] - 1
ben_size= benigndata.shape[0] - 1
#print msum_col
#print ben_size
support_perm = [x*mal_size/ben_size for x in bsum_col]
rank = [(x-y)/(x+y) for x,y in zip(msum_col,support_perm)]

results = [a+"\t"+str(b)+"\t"+str(c)+"\t"+str(d)+"\t"+str(e) for a,b,c,d,e in zip(permission,msum_col,bsum_col,support_perm,rank) if math.isnan(e) is False]
sorted_results = sorted(results,key = get_rank)



for r in sorted_results:
    print r

#print rank
#print support_perm
#print len(msum_col)
#print bsum_col
