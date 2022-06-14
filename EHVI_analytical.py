# -*- coding: utf-8 -*-
"""
@author: Tinkle Chugh
"""

import numpy as np
from scipy import stats

def EHVI_2D(PF,r,mu,sigma):
    n = PF.shape[0]
    S1 = np.array([r[0],-np.inf])
    S1 = S1.reshape(1,-1)
    Send = np.array([-np.inf,r[1]])
    Send = Send.reshape(1,-1)
    index = np.argsort(PF[:,1])
    
    S = PF[index,:]
    
    S = np.concatenate((S1,S,Send),axis = 0)
    
    y1 = S[:,0] 
    y2 = S[:,1]
    
    y1 = y1.reshape(-1,1)
    y2 = y2.reshape(-1,1)
    
    mu = mu.reshape(1,-1)
    sigma = sigma.reshape(1,-1)
        
    sum_total1 = 0;
    sum_total2 = 0;
    
    for i in range(1,n+2):
        t = (y1[i] - mu[0][0])/sigma[0][0]
        if i==n+1:
            sum_total1 = sum_total1
        else:
            sum_total1 = sum_total1 + (y1[i-1] - y1[i])*stats.norm.cdf(t)*psi_cal(y2[i],y2[i],mu[0][1],sigma[0][1])
        sum_total2 = sum_total2 + (psi_cal(y1[i-1],y1[i-1],mu[0][0],sigma[0][0]) \
                                   - psi_cal(y1[i-1],y1[i],mu[0][0],sigma[0][0]))*psi_cal(y2[i],y2[i],mu[0][1],sigma[0][1])
        
    EHVI = sum_total1 + sum_total2
    return EHVI


def psi_cal(a,b,m,s):
    t = (b - m)/s
    return s*stats.norm.pdf(t) + (a - m)*stats.norm.cdf(t)
