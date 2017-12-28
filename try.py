

######-5-ud120:lesson8:17-######
"""
dict1={'d':{'a1':2,'b1':'NaN'},'e':{'a2':6,'b2':7}}
dict1(keys=='d').pop('a1',0)
del dict1['d']
del dict1['d']['a1']
print dict1   
"""

######-4-ud120:lesson8:12-######
"""import numpy as np
a=[1,2,3,4,5]
a=np.array(a)
x=a.reshape(-1,1)
y_pred=2*x+2 # [4,6,8,10,12]

z=zip(x,y_pred)
print len(z)
print z

y=[5,6,7,16,12]
y=np.array(y)
y=y.reshape(-1,1)

y_len=30/5*len(y)/10  # remove:3

error=abs(y-y_pred)

maxerror=max(error) # 1,0,1,5,0

for num in range(1,y_len):
	where_max=np.where(error==np.max(error))
	error=np.delete(error,where_max[0])	
print where_max,error
"""

######-3-ud120:lesson7-######
"""
import numpy as np
a=[1,2,3,4,5]
a=np.array(a)
d=a.reshape(-1,1)
c=a.reshape(1,-1)
print c
print d


import numpy as np
pred = reg.predict(feature_train)
target_train = np.array(target_train)
pred = np.array(pred)
pred.reshape(1, -1)
target_train.reshape(1,-1)

### type: target_train :numpy.ndarray, pred :list
pred = reg.predict(feature_train)
print  target_train - pred

np.array(target_train)
np.array(pred)
print np.shape(pred), np.shape(target_train)
target_train = target_train.reshape(1,len(target_train))
pred = pred.reshape(1,len(pred))
"""
######-2-ud120:lesson6-######
"""
filename = "try1.txt"
myfile = open(filename) 
lines = len(myfile.readlines()) 
print "There are %d lines in %s" % (lines, filename) 

"""

######-1-ud120:lesson6-######
"""
dict={'a':{'a':2,'b':'NaN'},'b':{'a':6,'b':7}}
dict1=dict.keys()
print (dict1[0])
# dict['a']['a']    # right
# dict{'a','b'}['a']    # error
person_poi = 0 
for num in range(len(dict1)):
	if dict[dict1[num]]['b'] != 'NaN :
		person_poi = person_poi+1
print(person_poi)

print ("123",type(dict['a']['a']))
"""


