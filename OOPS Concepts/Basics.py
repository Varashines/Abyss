# Data based modules
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import datasets
# Regression based plugins
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
# Linear and Logistic Regression
################ Data from sklearn datasets ###############
house = datasets.fetch_california_housing()
X = house.data
y = house.target
columns = house.feature_names
out = house.target_names
data = pd.DataFrame()
data[columns] = house.data
data['y'] = house.target
print(data.shape)
################## ANOVA #################
corr = data.iloc[:,:-1].corr().round(2)
plt.close()
sns.set_theme(rc={'figure.figsize':(12,9)})
sns.heatmap(corr,cmap = "Blues",annot=True,linewidths=0.4)
plt.show()
print(data.isnull().sum())
print(columns)
for i in range(8):
    plt.boxplot(data.iloc[:,i])
    plt.ylabel(data.columns[i])
    # plt.show()
print(data.describe())
###############################################
X_train, X_test,y_train, y_test = train_test_split(X,y ,
                                   random_state=104,
                                   test_size=0.25,
                                   shuffle=True)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
model = LinearRegression()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
#################################################
iris = datasets.load_iris()
X = iris.data
y = iris.target
columns = iris.feature_names
data = pd.DataFrame()
data[columns] = X
data['y'] = y
#########################################
corr = data.iloc[:,:-1].corr().round(2)
plt.close()
sns.set_theme(rc={'figure.figsize':(12,9)})
sns.heatmap(corr,cmap = "Blues",annot=True,linewidths=0.4)
#plt.show()
print(data.isnull().sum())
print(columns)
for i in range(4):
    plt.boxplot(data.iloc[:,i])
    plt.ylabel(data.columns[i])
    # plt.show()
print(data.describe())
###############################################
X_train, X_test,y_train, y_test = train_test_split(X,y ,
                                   random_state=104,
                                   test_size=0.25,
                                   shuffle=True)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



model = LogisticRegression()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
y_pred = model.predict(X_test)
#################################################
plt.close()
result = confusion_matrix(y_test,y_pred)
sns.heatmap(result,annot=True,fmt='g',
xticklabels=['Setosa','Versicolor', 'Virginica'],
yticklabels=['Setosa','Versicolor', 'Virginica'])
plt.ylabel('Prediction',fontsize=13)
plt.xlabel('Actual',fontsize=13)
plt.title('Confusion Matrix',fontsize=17)
# plt.show()
result = classification_report(y_test,y_pred)
print(result)
y_pred = model.predict(X_train)
results = classification_report(y_train,y_pred)
print(results)
#####################################################
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
