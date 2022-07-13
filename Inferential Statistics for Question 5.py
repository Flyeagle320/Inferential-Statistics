# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 21:33:04 2022

@author: Rakesh
"""
import pandas as pd

##importing dataset ##
df=pd.read_excel('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/Assignment_module02 (1).xlsx')


##defining range function##
def minmax(val):
    min_val=min(val)
    max_val=max(val)
    range_val=max_val-min_val
    print('min:',min_val)
    print('max:',max_val)
    print('range:',range_val)
    return' '
    
print("\n----------- Calculate Mean -----------\n")
print(df.mean())    
 
print("\n----------- Calculate Median -----------\n")
print(df.median())

print("\n----------- Calculate Mode -----------\n")
print(df.mode())

print("\n----------- Calculate Variance -----------\n")
print(df.var())

print("\n----------- Calculate Std Var -----------\n")
print(df.std())
   
print("\n----------- Calculate Range -----------\n")
print(minmax(df.Points))
print(minmax(df.Score))
print(minmax(df.Weigh))

