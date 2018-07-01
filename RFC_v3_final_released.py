import numpy as np
from sklearn.preprocessing import LabelEncoder  
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import pdb
from scipy import stats
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from collections import OrderedDict
from sklearn.ensemble import GradientBoostingClassifier

import matplotlib.pyplot as plt
from preproc import *
import json
import pickle
from sklearn.externals import joblib

"""
Processing the data!
"""
def loadXY(f1, f2, vf1):
	Y=[]
	X,k2,k3,k4,k5,k6,k7,k9 = preprocessing(f1)
	with open(f2, 'r') as fp:
		label = fp.readlines();
	
	for i in range(len(label)):
		Y.append(float(label[i]))
	Y = np.asarray(Y, np.float32)
	
	vY=[]
	vX,k2,k3,k4,k5,k6,k7,k9 = preprocessing(vf1, key2=k2, key3=k3, key4=k4, key5=k5, key6=k6, key7=k7, key9=k9)

	
	return X, Y, vX

fn = 'train_data2.txt'
fn2 = 'train_label2.txt'
val_fn = 't2_metadata0.txt'
X, Y, vX = loadXY(fn, fn2, val_fn)

clf = RandomForestRegressor(n_estimators=800, max_features="log2", n_jobs =-1)
clf.fit(X, Y)
y2 = clf.predict(X)
py2 = clf.predict(vX)

importances = clf.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf.estimators_],
			 axis=0)
indices = np.argsort(importances)[::-1]

#~ joblib.dump(clf, 'clf.pkl')

# Print the feature ranking
print("Feature ranking:")
for f in range(X.shape[1]):
	print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))


"""
Calculating the residual of the predicted value and the ground truth
Mapping the residual and the data into random forest classifier(s)
"""

num2s=[900] # set the number of iterative refinement.
clf2=[]
for i in range(len(num2s)):
	diff1 = Y - y2
	clf2.append(RandomForestRegressor(n_estimators=num2s[i], max_features="log2", n_jobs =-1))
	clf2[i].fit(X, diff1)

	resi = clf2[i].predict(X)
	y2 = y2 + resi
	
	resi = clf2[i].predict(vX)
	py2 = py2 + resi
	
	#~ joblib.dump(clf2[i], 'clf2%d.pkl'%(i))                                                                                                                                                                                                       

#~ clf = joblib.load('clf.pkl')
#~ clf2=[]
#~ for i in range(len(num2s)):
	#~ clf2.append(joblib.load('clf2%d.pkl'%(i)))
    

#~ [X,Y,vX]=np.load("processedData%d.npy"%(0))
#~ py, py2 = np.load("result%d.npy"%(0))

pred=py2
test_x=vX
total_len = len(pred)
for kk in range(1,10,1):
	val_fn = 't2_metadata%d.txt'%(kk)

	X, Y, vX = loadXY(fn, fn2, val_fn)
	#~ np.save("processedData%d.npy"%(kk), [X,Y,vX])
	#~ [X,Y,vX]=np.load("processedData%d.npy"%(kk))
	print("Loading data from metadata %d"%(kk))
	#~ print("Load training data completed...total %d data"%(len(Y)))
	py = clf.predict(vX)
	py2 = py
	for i in range(len(num2s)):
		resi = clf2[i].predict(vX)
		py2 = py2 + resi

	
	#~ np.save("result%d.npy"%(kk), [py, py2])
	#~ py, py2 = np.load("result%d.npy"%(kk))
	test_x=np.concatenate((test_x, vX), axis=0)
	pred = np.concatenate((pred, py2), axis=0)
	total_len += len(py2)
	print("Collecting %d data"%(total_len))
	# Output the result in JSON file format
	# Sorting

#~ test_x = np.reshape(test_x, [total_len, 15])
pred = np.reshape(pred, [total_len, 1])	
test_x = np.concatenate((test_x, pred), axis=1)
print("Now we have data shaped [%d, %d]"%(test_x.shape[0], test_x.shape[1]))

sorted_idx = sorted(range(len(test_x[:,1])), key=lambda k: test_x[k,1])
score_idx = sorted(range(len(pred)), key=lambda k: pred[k], reverse=True)
for k in range(len(pred)):
	test_x[score_idx[k], 15] = k+1
data={}
strs = '{\n"version": "VERSION 1.2",\n'
strs += '"result": [\n'
for k in range(len(pred)):

	str1= '\t{\n\t"post_id": "post%d",\n'%(test_x[sorted_idx[k], 1])
	str1=str1+'\t"ranking_position": %d,\n' % (test_x[sorted_idx[k], 15])
	if (k == len(pred)-1):
		str1=str1+'\t"popularity_score": %f\n\t}\n],\n' %(pred[sorted_idx[k]])
	else:
		str1=str1+'\t"popularity_score": %f\n\t},\n' %(pred[sorted_idx[k]])
	strs +=str1

strs+='"external_data": {\n"used": "False", \n"details": "VGG-19 pre-trained on ImageNet training set"\n}\n}'
with open("SMHP18.json","w") as f:
	f.write(strs)

