
'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
import pandas

target=open("lowvars.txt",'w')
data = pandas.read_csv('Copy.csv')
data1 = pandas.read_csv('list2.csv')
requiredvariables = [];
print('--------------------')
for i in range(0,35):

   for row in data.itertuples():
       requiredvariables.append(row[i]);
#for i in range(0,53):

#   for row in data1.itertuples():
#       requiredvariables.append(row[i]);
#print(colfromdataset)

requiredvariables=(filter(lambda v: v==v, requiredvariables))

requiredvariables=set(requiredvariables)
print(requiredvariables)
for item in requiredvariables:
  target.write(str(item)+"\n")

print(len(requiredvariables))




