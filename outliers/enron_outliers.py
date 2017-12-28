#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL",0)    # or:  del data_dict["TOTAL"]
data = featureFormat(data_dict, features)

### your code below
import numpy as np

for n in range(1,3):
	salarys =  featureFormat(data_dict, ["salary"])
	data_keys = data_dict.keys()
	data_length = len(data_keys)
	maxs = np.max(salarys)
	for num in range(1,data_length):
		if data_dict[data_keys[num]]["salary"] == maxs :
			print data_keys[num]
			del data_dict[data_keys[num]]
"""
print(len(data_dict),len(data))    # (146, 95)
import numpy as np
salarys =  featureFormat(data_dict, ["salary"]) 
print len(salarys)    # 95
where_max = np.where(salarys == np.max(salarys))
# maxs = np.max(salarys)
# print salarys[where_max],maxs
# print where_max[0]
# print int( where_max[0] )
data_keys = data_dict.keys()
print data_keys[int(where_max[0])]    # OLSON CINDY K
"""
### plot the data
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


