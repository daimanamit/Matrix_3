##Amit Daiman, Locker Number - 375
# -*- coding: utf-8 -*-
"""
@author: ada003
"""
import numpy as np
import os
os.chdir(r"Amit Daiman(1042956), LN-375")#directory of input and output text file
os.getcwd()
A = np.loadtxt('M1.txt') #Put the txt file which containing matrix A
B = np.loadtxt('M2.txt') #Put the txt file which containing matrix B

C = []
for i in range (len(A)):
    Cii=[]
    for j in range (len(B[0])):
        Ci=[]
        for k in range (len(B)):
            Ci.append(A[i][k] * B [k][j])     
        Cii.append(sum(Ci))
    C.append(Cii)
    
print(C, 'resultant multiplication matirx C')
mult_matrix=np.array(C)
print(C)
# Saving the resultant matrix in output file
fname = 'M3.txt'
np.savetxt(fname, C)

   