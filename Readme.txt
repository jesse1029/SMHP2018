=======================================================
Environmental setting
OS: Microsoft Windows 10 Pro 64bit
Software: Anaconda3 64 bit, Sklern toolbox
Contact: Chih-Chung Hsu, cchsu@mail.npust.edu.tw
Introduction:
We DO NOT use any external data and the train/test images.
We directly predict the popularity score on the metadata.
Since the random state in RandomForestClassifier will be
different each run time, the predicted results of multiple
executions will be slightly different as well.
=======================================================

Dir Suructure:
source/
       Original test and train files downloaded from 
       SHMP official website.
./
RFC_v3_final_released.py
preproc.py
test_prec.py
train_prec.py
t2_metadata[0-9].txt
train_data2.txt
train_label2.txt
=======================================================
How to use
=======================================================
**If there is no any preprocessed files in the directory,
Please follow the instructions below to construct the 
processed trainin/test files. 
Note, the original train/test files should be preprocessed 
before executing RFC_v3_final_released.py 


1. In Anaconda promot, type "python test_prec.py"
   ==>Preprocessing the test data (metadata0-9) in source directory
   ==>Generated 10 processed metadata in current directory

2. In Anaconda promot, type "python train_prec.py"
   ==>Preprocessing the train data in source directory
   ==>Generated 2 processed data/label in current directory

3. In Anaconda promot, type "python RFC_v3_final_released.py"
   ==>Train the predictive model based on iterative refinement
   ==>It will generate the final result "SMHP18.json"

=============================================================