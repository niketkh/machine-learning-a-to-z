# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:35:23 2017

@author: Niket
"""
import pandas as pd
import numpy as np

# Importing the Dataset
dataset = pd.read_csv('50_Startups.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder = LabelEncoder()
X[:,-1] = labelEncoder.fit_transform(X[:,-1])
oneHotEncoder = OneHotEncoder(categorical_features=[-1])
X = oneHotEncoder.fit_transform(X).toarray()

# Avoid Dummy Variable Trap
X = X[:, 1:]

# Splitting Dataset into Training Set and Test Set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Results
y_pred = regressor.predict(X_test)

# Building the Optimal Model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr=np.ones((50,1)).astype(int), values = X, axis=1) 

X_opt = X[:,[0, 1, 2, 3, 4, 5]]
# regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
# regressor_OLS.summary()

SL = 0.05
X_labels = ['constant', 'en_state', 'en_state', 'RnD', 'Admin', 'Marketing Spend']
while True:
    regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
    # regressor_OLS.summary()
    pvalues = regressor_OLS.pvalues
    max_index = np.argmax(pvalues)
    print(max_index)
    if(pvalues[max_index] < SL):
        break
    else:
        X_opt =  np.delete(X_opt, max_index, 1)
        X_labels.remove(X_labels[max_index])
        
