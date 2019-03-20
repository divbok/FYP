import numpy as np
import pandas as pd
import math

def get_rank(x):
    return float(x.split(",")[-1])

#Get the datasets
dataset = pd.read_csv("dataset/drebin-215-dataset-5560malware-9476-benign.csv")

#Prepare dataset for training
# mixeddata = [malwaredata,benigndata]
# result = pd.concat(mixeddata)
#X = dataset.drop(dataset.columns[[0,1]],axis = 1)
#Y = dataset['']
#print(dataset)
chi_square_file = "dataset/permissions1.csv"
perm_list = [line.strip() for line in open(chi_square_file)]
print(perm_list)

malwaredata = dataset.loc[dataset['class'] == 'S']
benigndata = dataset.loc[dataset['class'] == 'B']

#dataset.loc[dataset['c']]
#Extract permissions name
#mdata = open("dataset/malware.csv")
#columns = mdata.readline().strip()
#permission = columns.split(",")[2:]
#mdata.close()

#Count of apps per permission
#msum_col= np.sum(malwaredata[perm_list],axis=0)
#bsum_col= np.sum(benigndata,axis=0)

msum_col = [malwaredata[perm].sum() for perm in perm_list]
print(msum_col)
bsum_col = [benigndata[perm].sum() for perm in perm_list]
#Size of datasets
mal_size= malwaredata.shape[0] - 1
ben_size= benigndata.shape[0] - 1

#Calculate support and rank for each permission
support_perm = [x*mal_size/ben_size for x in bsum_col]
rank = [(x-y)/(x+y) for x,y in zip(msum_col,support_perm)]
#rank = [mal_size*math.pow(x/mal_size - (x+y)/(mal_size+ben_size),2) + ben_size*math.pow(y/ben_size - (x+y)/(mal_size+ben_size),2)   for x,y in zip(msum_col,bsum_col)]


results = [a+","+str(b)+","+str(c)+","+str(d)+","+str(e) for a,b,c,d,e in zip(perm_list,msum_col,bsum_col,support_perm,rank) if math.isnan(e) is False]
sorted_results = sorted(results,key = get_rank)
for r in sorted_results:
	print(r)
