import pandas as pd
import numpy as np

data = pd.read_csv("train.csv")
#print(data.head())

#cleaning the data 
column_target=['Survived']

#factor sex,age,P-class,Fare of the ticket
column_train=['Age','Pclass','Sex','Fare']

#sepearting train and target

x=data[column_train]
y=data[column_target]
print(x['Sex'].isnull().sum())
print(x['Pclass'].isnull().sum())
print(x['Fare'].isnull().sum())
print(x['Age'].isnull().sum())

#fill the NA values 
x['Age']=x['Age'].fillna(x['Age'].mean())
print(x['Age'].isnull().sum())
