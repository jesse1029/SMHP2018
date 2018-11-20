The implementation of paper titled: C.C. Hsu, C.Y. Lee, T.X. Liao, et.al., "An Iterative Refinement Approach for Social Media Headline Prediction," ACM Multimedia (ACMMM), Seoul, Korea, 22 - 26 Oct. 2018.

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

@article{hsu2018iterative,
  title={An Iterative Refinement Approach for Social Media Headline Prediction},
  author={Hsu, Chih-Chung and Lee, Chia-Yen and Liao, Ting-Xuan and Lee, Jun-Yi and Hou, Tsai-Yne and Kuo, Ying-Chu and Lin, Jing-Wen and Hsueh, Ching-Yi and Zhan, Zhong-Xuan and Chien, Hsiang-Chin},
  journal={arXiv preprint arXiv:1809.08753},
  year={2018}
}
