
'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
import pandas
from pymongo import MongoClient



target = open('decodedvarsdummy.txt', 'r');


       #for row in reader:
       # print(row)

data = pandas.read_csv('Copy.csv')
data1 = pandas.read_csv('list2.csv')
requiredvariables = [];
print('--------------------')
#for i in range(0,35):

 #  for row in data.itertuples():
  #     requiredvariables.append(row[i]);
for i in range(0,53):

   for row in data1.itertuples():
       requiredvariables.append(row[i]);
#print(colfromdataset)

requiredvariables=(filter(lambda v: v==v, requiredvariables))


#c = list(set(requiredvariables).difference(availablevars))
#print(len(c))




requiredvariables=set(requiredvariables)
for item in requiredvariables:
  print(item)
#target.write(str(requiredvariables))
#c = [i for i in requiredvariables if i not in availablevars]
#print(len(c))

print("Total variables in input data set")

print("Variables needed for  infant...")
print(len(requiredvariables))




