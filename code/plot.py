
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt



results = pd.read_csv("results/decisiontreePRNR_SPR",names =['noofperm','accuracy','precision','recall','fscore'],sep='\s+')
#n_perm = permRanks.shape[0]

noofperms = [x for x in results['noofperm']]
accuracy  = [x for x in results['accuracy']]

# noofperms = [1,2,3,4]
# accuracy = [4,3,2,1]

print(noofperms)
print(accuracy)


#sample_data_table = FF.create_table(results)
#py.iplot(sample_data_table, filename='sample-data-table')
plt.plot(results['noofperm'].tolist(),results['accuracy'].tolist())
plt.plot(results['noofperm'].tolist(),results['precision'].tolist())
plt.plot(results['noofperm'].tolist(),results['recall'].tolist())
plt.plot(results['noofperm'].tolist(),results['fscore'].tolist())

plt.legend(['Accuracy','Precision','Recall','F-Score'],loc="upper left")

plt.axis([0, 110, 0.6, 1])
plt.title("DecisionTree PRNR+SPR")
plt.ylabel('Metrics')
plt.xlabel('Number of Permissions')
plt.show()
fig = plt.figure()
fig.savefig("plots/decisiontreePRNR_SPR.png",bbox_inches="tight")

