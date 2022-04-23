# -*- coding: utf-8 -*-
"""week6_lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GNpZ0-3C5QswxC3VWS0Vctv-eIjgKQ6Q
"""

#resources
#https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python

import pandas as pd
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("sample_data/diabetes.csv", header=None, names=col_names)
pima.head()

#split dataset
feature_cols = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = pima[feature_cols] # Features
y = pima.label # Target variable
X.head()
y.head()

# split X and y into training and testing sets
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
#the Dataset is broken into two parts in a ratio of 75:25. It means 75% data will be used for model training and 25% for model testing.

from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit model with data
logreg.fit(X_train,y_train)

y_pred=logreg.predict(X_test)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class_names=[0,2] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("bottom")
plt.tight_layout()
plt.title('Confusion matrix', y=1.4)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')