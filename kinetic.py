#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Created on Sun Jan 21 01:29:09 2018

Maria J. Molina
Ph.D. Student 
Central Michigan University


"""

###############################################################################
###############################################################################
###############################################################################  


import numpy as np


###############################################################################
###############################################################################
###############################################################################  


#k value ranges

ki_low = 0.00005
kii_low = 0.000009 
kiii_low = 0.0000005 
kiiii_low = 0.00000001 

ki_hi = 0.0005
kii_hi = 0.00005 
kiii_hi = 0.000009
kiiii_hi = 0.0000005

ki = np.linspace(ki_low,ki_hi,100000)
kii = np.linspace(kii_low,kii_hi,100000)
kiii = np.linspace(kiii_low,kiii_hi,100000)
kiiii = np.linspace(kiiii_low,kiiii_hi,100000)

#note: no kv for E needed
#note: ki>kii>kiii>kiiii


###############################################################################
###############################################################################
############################################################################### 


#time (seconds) intervals
time = np.array([0,7200,36000,86400,172800,259200,432000])

#total concentration
T_c = 0.000051279938744597

#A initial concentration
A_o = 0.000051279938744597  


###############################################################################
#####experiment measurements###################################################
############################################################################### 


A_exp = np.array([0.0000512799387446,0.0000024265947944,
                  0.0000004298964759,0.0000010637320588,
                  0.0000008250513479,0.0000009757276767,
                  0.0000007548700099])

B_exp = np.array([0.0000000000000000,0.0000339301493665,
                  0.0000269240752731,0.0000154374532268,
                  0.0000116978076108,0.0000097259007643,
                  0.0000095301247143])
        
C_exp = np.array([0.0000000000000000,0.0000064819400096,
                  0.0000221897300506,0.0000286759711338,
                  0.0000291772777796,0.0000298642478771,
                  0.0000271698225201])
        
D_exp = np.array([0.0000000000000000,0.0000011357846021,
                  0.0000024013590936,0.0000040001745345,
                  0.0000064622547114,0.0000068973370480,
                  0.0000107885408801])
        
E_exp = np.array([0.0000000000000000,0.0000006430691966,
                  0.0000008677730303,0.0000021595759473,
                  0.0000037395564770,0.0000042165468839,
                  0.0000070872873726])


###############################################################################
###############################################################################
############################################################################### 

# we will only have 4 equations since we are ignoring back reations, so the reactions proceede from A->D

for t in time:

    A = A_o * np.exp(-ki*t)

    B = np.divide((ki*A_o),(kii-ki)) * (np.exp(-ki*t)-np.exp(-kii*t))
    
    #Subject to change, Natalia and Dimtry will check my math for these equations
    
    C =  np.divide((ki*A_o),(kii-k_i)) * ((kiii-k_i) * np.exp(-ki*t) - (kiii-kii) * np.exp(-kii*t) +  (ki-kii) * np.exp(-kiii*t))
  
    D = np.divide((ki*A_o*kiii), (kii-k_i)) * ((np.divide((kiii-k_i),(-k_i)) * np.exp(-ki*t)
                  - np.divide((kiii-kii),(-kii)) * np.exp(-kii*t) + np.divide((ki-kii),(-kiii)) * np.exp(-kiii*t)
                  - (np.divide((ki*A_o*kiii),(kii-ki)) * (np.divide((kiii-ki),(-k_i) - np.divide((kiii-kii),(-kii) 
                  + np.divide((ki-kii),(-kiii)))



A_o = Tc = A + B + C + D



###############################################################################
###############################################################################
###############################################################################  

#Monte Carlo simulation

  
