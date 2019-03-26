import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix


#Import dataset and add class labels

dataset = pd.read_csv("dataset/drebin-215-dataset-5560malware-9476-benign.csv")
#Import ranks
permRanks = pd.read_csv("results_new/apriori_27.txt",names =['permName','malware_sum','benign_sum','support','rank','support_SPR'])
n_perm = permRanks.shape[0]

#Prepare dataset for training
apriori =[]
#ACCESS_NETWORK_STATE
apriori.append(["INTERNET"])
#"ACCESS_COARSE_LOCATION",
apriori.append(["ACCESS_FINE_LOCATION"])
#SEND_SMS
apriori.append(['RECEIVE_SMS'])
#WAKE_LOCK
apriori.append(['VIBRATE'])

#27 0.9414893617021277 0.9658484525080042 0.9417273673257024 0.9536354056902001

dataset.loc[dataset['class'] == 'S', 'class'] = 1
dataset.loc[dataset['class'] == 'B', 'class'] = 0
X = dataset.drop(dataset.columns[[-1]],axis = 1)
Y = dataset['class']

for perm_list in apriori:
	print (perm_list)
	for perm in perm_list:
		permRanks = permRanks[permRanks['permName'] != perm]

n_perm = permRanks.shape[0]


#Split data into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)

#Train the svm model
classifier = DecisionTreeClassifier()



for select_perm in range(n_perm,n_perm+1):
	perm_subset =  [x for x in permRanks['permName'][0:select_perm]]

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
	falseposrate = FP/(FP+TN)
	fscore = (2*precision*recall)/(precision+recall)


	print(select_perm,accuracy,precision,recall,fscore)
