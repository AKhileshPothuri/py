# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:21:26 2018

@author: surbhi.jain
"""

def gcd(a,b):
   
   
    if(b==0):
        print("GCD is ".format(a));
    else:
        c=int(a)%int(b);
        print(c);
        gcd(b,c);
a=input('enter 1st number');
b=input('enter second number');        
gcd(a,b);