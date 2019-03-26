import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA,FastICA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

dataset = pd.read_csv("dataset/drebin-215-dataset-5560malware-9476-benign.csv")
cluster_dataset = pd.read_csv("dataset/cluster_dataset.csv")
permRanks = pd.read_csv("results_new/perm_final_list.csv",names =['permName','malware_sum','benign_sum','support','rank','support_SPR'])

dataset.loc[dataset['class'] == 'S', 'class'] = 1
dataset.loc[dataset['class'] == 'B', 'class'] = 0

n_perm = permRanks.shape[0]

X = dataset.drop(dataset.columns[[-1]],axis = 1)
Y = dataset['class']

pruning_size = 24
perm_subset = [x for x in permRanks['permName']]
perm_subset1 = ["android.permission."+x for x in permRanks['permName']]

n=10

pca = PCA(n_components=n)
pca.fit(dataset[perm_subset])
principalComponents = pca.transform(cluster_dataset[perm_subset1])
col_name = ["col"+str(i) for i in range(n)]
X_reduced = pd.DataFrame(data = principalComponents, columns =col_name)
X_reduced.to_csv("dataset/cluster_10.csv", sep=',')
