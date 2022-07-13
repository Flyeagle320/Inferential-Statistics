# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 22:01:20 2022

@author: Rakesh
"""
##importing packages
import pandas as pd

#loading dataset#
df= pd.read_excel('C:/Users/Rakesh/Downloads/inferential-statistics-main/inferential-statistics-main/Qtn 7/inferentialStatsQ7.xlsx')

#using Boxplot #

import matplotlib.pyplot as plt
plt.boxplot(df.iloc[:,1])
plt.show()

## there are few outlier#
#data is right skewed#

#finding mean variance and standard deviation
print("\n_____________Mean___________\n")
df.iloc[:,1].mean()

print("\n_____________Variance___________\n")
df.iloc[:,1].var()

print("\n_____________Standard Deviation___________\n")
df.iloc[:,1].std()

print("\n_____________Measures of centarlity___________\n")
df.describe()
df.iloc[:,1].median()

print("\n_____________Measures of spread___________\n")
df.iloc[:,1].var()