# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:59:09 2017

@author: Niket
"""
# Data Preprocessing 
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:, -1].values

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:,-1] = labelEncoder_X.fit_transform(X[:,-1])
oneHotEncoder = OneHotEncoder(categorical_features = [-1]) 
X = oneHotEncoder.fit_transform(X).toarray()

# Avoiding Dummy Variable Trap
X = X[:, 1:]

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1/3, random_state=42)

# Fitting Mutiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Results
y_pred = regressor.predict(X_test)

