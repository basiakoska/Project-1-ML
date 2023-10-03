# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:44:48 2023

@author: mediaworld
"""

import pandas as pd


def outlier_hunter (column1,dataset, maxValue=None ,minValue=None ):
    
    
    if column1.name == 'Pregnancies' :
        
        dataset= dataset[dataset['Pregnancies']/dataset['Age'] < 0.5]
        return dataset
      
    else:
        dataset=dataset[dataset[column1.name] > minValue]
        dataset=dataset[dataset[column1.name] < maxValue]
     
        return dataset

         
dataset = pd.read_excel('diabetes_dataset.xlsx')


dataset = dataset[dataset['Insulin'] != 0]
dataset = dataset[dataset['SkinThickness'] !=0]


pregnanciesColumn = dataset['Pregnancies'] 
glucoseColumn = dataset['Glucose']
bloodPressureColumn = dataset['BloodPressure']
skinThicknessColumn =dataset['SkinThickness']
insulinColumn = dataset['Insulin']
bmiColumn= dataset['BMI']
ageColumn = dataset['Age']
outcomeColumn= dataset['Outcome']



dataset = outlier_hunter(column1= pregnanciesColumn,dataset= dataset)
dataset= outlier_hunter(column1=glucoseColumn,dataset=dataset,maxValue=160,minValue=0)
dataset =outlier_hunter(column1=bloodPressureColumn,dataset=dataset,maxValue=180, minValue=20)
dataset = outlier_hunter(column1=bmiColumn,dataset=dataset,maxValue=50, minValue=15)
dataset =  outlier_hunter(column1=ageColumn,dataset=dataset,maxValue=120, minValue=0)

print(len(dataset))
