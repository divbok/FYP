import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline

malwaredata = pd.read_csv("dataset/malware.csv")
malwaredata['Class'] = 1
benigndata = pd.read_csv("dataset/benign.csv")
benigndata['Class'] = 0
mixeddata = [malwaredata,benigndata]
result = pd.concat(mixeddata)
X = result.drop([0,1,-1], axis=1)
Y = result['Class']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)
print (X)
