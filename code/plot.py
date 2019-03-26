
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt



results = pd.read_csv("results_new/dt_chi_PRNR_SPR.txt",names =['noofperm','accuracy','precision','recall','falsposrate','fscore'],sep='\s+')
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

plt.axis([0, 50, 0.7, 1])
plt.title("DecisionTree PRNR+PCA")
plt.ylabel('Metrics')
plt.xlabel('Number of Principal Components')
plt.show()
