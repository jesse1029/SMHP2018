# encoding=utf8  

import numpy as np
import random as rn
import sys  


f=open('source/t2_train_data.txt','r', encoding='utf-8', errors="replace")
f2=open('source/t2_train_label.txt','r', encoding='utf-8')

data=f.readlines()
lab=f2.readlines()
len1=len(data)

idx = np.asarray(np.zeros((len1)), np.int32)
for i in range(len1):
	idx[i]=i


f=open('train_data2.txt','w', encoding='utf-8')
f2=open('train_label2.txt','w', encoding='utf-8')
for i in range(len1):
	f.write(data[idx[i]])
	f2.write(lab[idx[i]])
f.close()
f2.close()
