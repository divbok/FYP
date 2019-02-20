
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt



results = pd.read_csv("results/decisiontree_PRNR.txt",names =['noofperm','accuracy','precision','recall','falsposrate','fscore'],sep='\s+')
#n_perm = permRanks.shape[0]
print(results)

#sample_data_table = FF.create_table(results)
#py.iplot(sample_data_table, filename='sample-data-table')
plt.plot(results['noofperm'].tolist(),results['accuracy'].tolist())
print(results['recall'].tolist())

plt.plot(results['noofperm'].tolist(),results['precision'].tolist())
plt.plot(results['noofperm'].tolist(),results['recall'].tolist())
plt.plot(results['noofperm'].tolist(),results['fscore'].tolist())

plt.legend(['Accuracy','Precision','Recall','F-Score'],loc="upper left")

plt.axis([0, 81, 0.6, 1])
plt.title("DecisionTree PRNR")
plt.ylabel('Metrics')
plt.xlabel('Top N and Bottom N Permissions(Based on Rank)')
plt.show()