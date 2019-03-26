import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix



#Import dataset and add class labels

dataset = pd.read_csv("dataset/drebin-215-dataset-5560malware-9476-benign.csv")
#Import ranks
permRanks = pd.read_csv("results_new/perm_rank.txt",names =['permName','malware_sum','benign_sum','support','rank','support_SPR'])


apriori =[]
#Prepare dataset for training
# #INTERNET
# apriori.append(["ACCESS_NETWORK_STATE","ACCESS_COARSE_LOCATION","ACCESS_FINE_LOCATION"])
# #WRITE_SMS
# apriori.append(['READ_SMS'])
# #SEND_SMS
# apriori.append(['RECEIVE_SMS'])
# #ACCESS_WIFI_STATE
# apriori.append(['CHANGE_WIFI_STATE','CHANGE_WIFI_MULTICAST_STATE'])
# #READ_EXTERNAL_STORAGE
# apriori.append(['WRITE_EXTERNAL_STORAGE'])
# #RECORD_AUDIO
# apriori.append(['MODIFY_AUDIO_SETTINGS'])
# #READ_CALL_LOG
# apriori.append(['WRITE_CALL_LOG','CALL_PHONE','CALL_PRIVILEGED','PROCESS_OUTGOING_CALLS'])
# #READ_USER_DICTIONARY
# apriori.append(['WRITE_USER_DICTIONARY'])
# #READ_SYNC_SETTINGS
# apriori.append(['WRITE_SYNC_SETTINGS','READ_SYNC_STATS'])




dataset.loc[dataset['class'] == 'S', 'class'] = 1
dataset.loc[dataset['class'] == 'B', 'class'] = 0

# for perm_list in apriori:
# 	print (perm_list)
# 	for perm in perm_list:
# 		permRanks = permRanks[permRanks['permName'] != perm]

n_perm = permRanks.shape[0]

# print(n_perm)

X = dataset.drop(dataset.columns[[-1]],axis = 1)
Y = dataset['class']



#Split data into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)

#Train the svm model
classifier = DecisionTreeClassifier()

for subset_size in range(3,int(n_perm/2)+1):
	perm_subset = [x for x in permRanks['permName'][0:subset_size]]
	perm_subset = perm_subset + [x for x in permRanks['permName'][-subset_size:]]

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


	print(subset_size,accuracy,precision,recall,falseposrate,fscore)
