# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 06:42:17 2021

@author: John
"""

#importing libraries
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

#matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso


df = pd.read_csv ('recs2015_public_v4.csv')
print (df.head())

print(df.size)

s = ""
for col_name in df.columns: 
    s += " " + col_name
print(s)

#target_col = "Avg_Elec_Un_kWh"
#
#X = df.drop(target_col,1)   #Feature Matrix
#y = df[target_col]          #Target Variable
#
##Using Pearson Correlation
#plt.figure(figsize=(12,10))
#cor = df.corr()
#sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
#plt.show()
#
##Correlation with output variable
#cor_target = abs(cor[target_col])
##Selecting highly correlated features
#relevant_features = cor_target[cor_target>0.3]
#
#print (relevant_features)



















##Loading the dataset
#x = load_boston()
#df = pd.DataFrame(x.data, columns = x.feature_names)
#df["MEDV"] = x.target
#X = df.drop("MEDV",1)   #Feature Matrix
#y = df["MEDV"]          #Target Variable
#
#print (df.head())
#
##Using Pearson Correlation
#plt.figure(figsize=(12,10))
#cor = df.corr()
#sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
#plt.show()
#
##Correlation with output variable
#cor_target = abs(cor["MEDV"])
##Selecting highly correlated features
#relevant_features = cor_target[cor_target>0.5]
#
#print (relevant_features)