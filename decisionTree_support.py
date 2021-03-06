import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier  
from sklearn.metrics import confusion_matrix 




#Import dataset and add class labels
malwaredata = pd.read_csv("dataset/malware.csv")
malwaredata['Class'] = 1
benigndata = pd.read_csv("dataset/benign.csv")
benigndata['Class'] = 0

#Import ranks
permRanks = pd.read_csv("results/perm_rank.csv",names =['permName','malware_sum','benign_sum','support','rank'])
n_perm = permRanks.shape[0]

#Prepare dataset for training
mixeddata = [malwaredata,benigndata]
result = pd.concat(mixeddata)
X = result.drop(result.columns[[0,1,-1]],axis = 1)
Y = result['Class']


#Split data into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)

#Train the svm model
classifier = DecisionTreeClassifier()

max_support = 8400
min_support = 10
dec_step = -10

for minimum_support in range(max_support,min_support,dec_step):
	perm_subset = []
	for i in range(n_perm):
		if permRanks['support'].iloc[i] >= minimum_support:
			perm_subset.append(permRanks['permName'].iloc[i])
	
	
	classifier.fit(X_train[perm_subset], Y_train)

	#Predict the class on testing data
	Y_pred = classifier.predict(X_test[perm_subset])

	#Get the model metrics
	conf_matrix = confusion_matrix(Y_test,Y_pred)

	TP = conf_matrix[0][0]
	FP = conf_matrix[0][1]
	FN = conf_matrix[1][0]
	TN = conf_matrix[1][1]

	precision = TP/(TP+FP)
	recall = TP/(TP+FN)
	accuracy = (TP+TN)/(TP+FP+TN+FN)
	# falseposrate = FP/(FP+TN) 
	fscore = (2*precision*recall)/(precision+recall)
    

	print(minimum_support,accuracy,precision,recall,fscore)

