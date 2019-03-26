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
        result = ""
        if self.p<alpha:
            print(colX)


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



dataset = pd.read_csv("dataset/drebin-215-dataset-5560malware-9476-benign.csv")
dataset.loc[dataset['class'] == 'S', 'class'] = 1
dataset.loc[dataset['class'] == 'B', 'class'] = 0

cT = ChiSquare(dataset)
chi_square_file = "dataset/updatedpermission.txt"
permission = [line.strip() for line in open(chi_square_file)]
print(permission)


for var in permission:
    cT.TestIndependence(colX=var,colY="class") 