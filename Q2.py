# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:00:11 2020

@author: Aaron
"""
import numpy as np
import pandas as pd
def DFManipulation_groupby(data):
        data.loc[:,"Max"]=(data.loc[:,"B"]-data.loc[:,"A"]).apply(lambda t:max(t,0))#take the maximum of B-A and 0
        data.loc[:,"Min"]=(data.loc[:,"B"]-data.loc[:,"A"]).apply(lambda t:min(t,0))#take the minimum of B-A and 0
        data.loc[:,"K"]=data.loc[:,"R"].diff()#K is the difference between R
        data.iloc[0,8]=data.iloc[0,3]# K1=R1
        data.loc[:,"K_Max"]=data.loc[:,"K"]*data.loc[:,"Max"]#multiply K and Max(B-A,0)
        data.loc[:,"K_Min"]=data.loc[:,"K"]*data.loc[:,"Min"]#multiply K and Min(B-A,0)
        if data.iloc[-1,3]==0: #the sum of K is actually the last term of R; it may be zero; 8th column is K
            raise ZeroDivisionError("Sum of K equals to zero")
        data.loc[:,"Result1"]=data.loc[:,"K_Max"].cumsum()/data.iloc[-1,3]#every x is cumsum from previous index
        data.loc[:,"Result2"]=data.loc[:,"K_Min"].iloc[::-1].cumsum().iloc[::-1]/data.iloc[-1,3]#we do cumsum on reversed series and then reverse the series again; 8th column is K
        data=data.drop(columns=["Max","Min","K_Max","K_Min","K"])#drop columns not needed
        return data
# print(df.groupby(["ID1","ID2","ID3"]).apply(lambda t: DFManipulation(t))








def DFManipulation(df):
    final_table=pd.DataFrame(columns=["ID1","ID2","ID3","R","A","B"])
    for i in range(int(df.shape[0]/10)):
        data=df.iloc[i*10:(i+1)*10]#iterate every 10 row
        data.loc[:,"Max"]=(data.loc[:,"B"]-data.loc[:,"A"]).apply(lambda t:max(t,0))#take the maximum of B-A and 0
        data.loc[:,"Min"]=(data.loc[:,"B"]-data.loc[:,"A"]).apply(lambda t:min(t,0))#take the minimum of B-A and 0
        data.loc[:,"K"]=data.loc[:,"R"].diff()#K is the difference between R
        data.iloc[0,8]=data.iloc[0,3]# K1=R1
        data.loc[:,"K_Max"]=data.loc[:,"K"]*data.loc[:,"Max"]#multiply K and Max(B-A,0)
        data.loc[:,"K_Min"]=data.loc[:,"K"]*data.loc[:,"Min"]#multiply K and Min(B-A,0)
        if data.iloc[-1,3]==0: #the sum of K is actually the last term of R; it may be zero; 8th column is K
            raise ZeroDivisionError("Sum of K equals to zero")
        data.loc[:,"Result1"]=data.loc[:,"K_Max"].cumsum()/data.iloc[-1,3]#every x is cumsum from previous index
        data.loc[:,"Result2"]=data.loc[:,"K_Min"].iloc[::-1].cumsum().iloc[::-1]/data.iloc[-1,3]#we do cumsum on reversed series and then reverse the series again; 8th column is K
        data=data.drop(columns=["Max","Min","K_Max","K_Min","K"])#drop columns not needed
        final_table=pd.concat([final_table,data],ignore_index=True)#concatinate dataframes
    return final_table
np.random.seed(seed=10)##set random seed
N=100#1000 dataset
raw_data=np.random.rand(10*N,6)#random generate the data
df=pd.DataFrame(raw_data,columns=["ID1","ID2","ID3","R","A","B"]).sort_values(by=["R"]).reset_index().drop(columns=["index"])
df.loc[:,["ID1","ID2","ID3"]]="A","AA","AAA"#create a pandas dataframe
result=DFManipulation(df)
print(result)

