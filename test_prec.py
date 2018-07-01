# encoding=utf8  

import numpy as np
import random as rn
import sys  


for k in range(10):
	f=open('source/t2_metadata%d.txt'%(k),'r', encoding='utf-8', errors="replace")

	data=f.readlines()
	len1=len(data)

	idx = np.asarray(np.zeros((len1)), np.int32)
	for i in range(len1):
		idx[i]=i


	f=open('t2_metadata%d.txt'%(k),'w', encoding='utf-8')
	for i in range(len1):
		f.write(data[idx[i]])
	f.close()
