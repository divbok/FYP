import numpy as np  
import pandas as pd 
from apyori import apriori

#Import dataset and add class labels
dataset = pd.read_csv("dataset/drebin-215-dataset-5560malware-9476-benign.csv")

#Import ranks
permRanks = pd.read_csv("results_new/permissionrank.txt",names =['permName','malware_sum','benign_sum','support','rank'])
n_perm = permRanks.shape[0]

#Prepare dataset for training
X = dataset.drop(dataset.columns[[-1]],axis = 1)
Y = dataset['class']

pruned_dataset_size = 52 
minimum_support = 100

permName =  [x for x in permRanks['permName'][0:pruned_dataset_size]]
permName =  permName + [x for x in permRanks['permName'][-pruned_dataset_size:]]

for i in range(n_perm):
	for j in range(len(permName)):
		if permRanks['support'].iloc[i] > minimum_support and permName[j] == permRanks['permName'].iloc[i]:
			print(permName[j], permRanks['support'].iloc[i])



apriori_list = []

for i in range(X.shape[0]):
	apriori_list.append([j for j in permName if X[j].iloc[i] == 1])
	print(i)

support = 0.1
confidence = 0.965 
length = 2

association_rules = apriori(apriori_list, min_support=support, min_confidence=confidence,min_length=length)  
association_results = list(association_rules) 

for i in range(len(association_results)):
	print(association_results[i])
