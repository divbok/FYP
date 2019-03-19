import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2_contingency

class ChiSquare:
    def __init__(self, dataframe):
        self.df = dataframe
        self.p = None #P-Value
        self.chi2 = None #Chi Test Statistic
        self.dof = None
        
        self.dfObserved = None
        self.dfExpected = None
        
    def _print_chisquare_result(self, colX, alpha):
        if self.p>=alpha:
            print(colX)
        else:
            result=""

 
        
    def TestIndependence(self,colX,colY, alpha=0.05):
        X = self.df[colX].astype(str)
        Y = self.df[colY].astype(str)
        
        self.dfObserved = pd.crosstab(Y,X) 
        chi2, p, dof, expected = stats.chi2_contingency(self.dfObserved.values)
        self.p = p
        self.chi2 = chi2
        self.dof = dof 
        
        self.dfExpected = pd.DataFrame(expected, columns=self.dfObserved.columns, index = self.dfObserved.index)
        
        self._print_chisquare_result(colX,alpha)

#Import dataset and add class labels
# malwaredata = pd.read_csv("dataset/malware.csv")
# malwaredata['Class'] = 1
# benigndata = pd.read_csv("dataset/benign.csv")
# benigndata['Class'] = 0

dataset = pd.read_csv("dataset/new_dataset.csv")
#Prepare dataset for training
# mixeddata = [malwaredata,benigndata]
# result = pd.concat(mixeddata)
X = dataset.drop(dataset.columns[[0,1]],axis = 1)
Y = dataset['score']


#Initialize ChiSquare Class
cT = ChiSquare(X)


#Feature Selection
testColumns = list(X.columns.values)
testColumns.pop(-1)
for var in testColumns:
    cT.TestIndependence(colX=var,colY="score") 