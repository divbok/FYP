from sklearn.datasets import load_iris
from sklearn.tree import tree
from sklearn_porter import Porter
import pandas as pd

# Load data and train the classifier:
#Import dataset and add class labels
dataset = pd.read_csv("dataset/drebin-215-dataset-5560malware-9476-benign.csv")
#Import ranks
permRanks = pd.read_csv("results_new/permissionsupport.txt",names =['permName','malware_sum','benign_sum','support','rank'])
n_perm = permRanks.shape[0]

#Prepare dataset for training
no_of_permissions = 27
perm_list = [x for x in permRanks['permName'][0:no_of_permissions]]

dataset.loc[dataset['class'] == 'S', 'class'] = 1
dataset.loc[dataset['class'] == 'B', 'class'] = 0
X = dataset.drop(dataset.columns[[-1]],axis = 1)[perm_list]
Y = dataset['class']


clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)

# Export:
porter = Porter(clf, language='java')
output = porter.export(embed_data=True)
print(output)
