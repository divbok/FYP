import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier  
from sklearn.metrics import confusion_matrix 
from sklearn.decomposition import PCA,FastICA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA


#Import dataset and add class labels
malwaredata = pd.read_csv("dataset/malware.csv")
malwaredata['Class'] = 1
benigndata = pd.read_csv("dataset/benign.csv")
benigndata['Class'] = 0

#Import ranks
permRanks = pd.read_csv("results/perm_rank_chi.csv",names =['permName','malware_sum','benign_sum','support','rank'])
n_perm = permRanks.shape[0]

#Prepare dataset for training
mixeddata = [malwaredata,benigndata]
result = pd.concat(mixeddata)
X = result.drop(result.columns[[0,1,-1]],axis = 1)
Y = result['Class']

pruning_size = 40
perm_subset = [x for x in permRanks['permName'][0:pruning_size]]
perm_subset = perm_subset + [x for x in permRanks['permName'][-pruning_size:]]

#Train the svm model
classifier = DecisionTreeClassifier()

for n in range(3,pruning_size*2+1):
	
	#LDA 
	# lda = LDA(n_components=n)
	# X_reduced = lda.fit(X, Y).transform(X)
	

	#PCA
	# pca = PCA(n_components=n)
	# principalComponents = pca.fit_transform(X[perm_subset])
	# col_name = ["col"+str(i) for i in range(n)]
	# X_reduced = pd.DataFrame(data = principalComponents, columns =col_name)

	# #ICA
	# ica  = FastICA(n_components=n)
	# principalComponents = ica.fit_transform(X[perm_subset])
	# col_name = ["col"+str(i) for i in range(n)]
	# X_reduced = pd.DataFrame(data = principalComponents, columns =col_name)


	X_train, X_test, Y_train, Y_test = train_test_split(X_reduced, Y, test_size = 0.2)
	classifier.fit(X_train, Y_train)

	#Predict the class on testing data
	Y_pred = classifier.predict(X_test)

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
    

	print(n,accuracy,precision,recall,falseposrate,fscore)
