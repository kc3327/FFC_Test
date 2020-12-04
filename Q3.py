# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 01:10:03 2020

@author: Aaron
"""
import numpy as np
def lastndigit(a,b,n): 
    if b<=0 or a<=0 or n<=0:#check if the inputs are positive
        raise TypeError("Inputs should be positive")
    if not isinstance(b,int) or not isinstance(a,int) or not isinstance(n,int):
        raise TypeError("Inputs should be integers")
    result=a
    while b>1:
        b-=1
        result=np.mod(result*a,10**n)# only take last n digits of intermediate result
    return str(result) if len(str(result))==n else (n-len(str(result)))*"0"+str(result)#if the length of reminder is less than n, add leading zeros
      
def lastndigit_brutal(a,b,n):
    result=np.mod(a**b,10**n)#brutal force
    return str(result) if len(str(result))==n else (n-len(str(result)))*"0"+str(result)#if the length of reminder is less than n, add leading zeros    
def lastndigit_log(a,b,n):
    res=1
    p=10**n
    a=a%p
    while b>0:
        if b%2!=0:
            res=res*a%p
        b=int(b/2)
        a=a**2%p
    return res    
a=23472
b=2347
n=4
print(lastndigit(a,b,n))
print("-----")
print(lastndigit_brutal(a,b,n))
print("-----")
print(lastndigit_log(a,b,n))
