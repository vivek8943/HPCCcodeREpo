'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
import pandas as pd
import openpyxl
str1="data.csv";
availablevars=[];
dummy = [];
target = open('listofvars1', 'w');
df = pd.DataFrame()
path = "/Users/Vivekanand/Downloads/Exposome2.0dataset";
for root, dirs, files in os.walk(path,topdown=True):
    for name in files:
        if name.endswith((".xlsx")):
            if not name.startswith('.'):
              filepath = os.path.join(root, name)
              print(filepath)
              data=pd.ExcelFile(filepath)
              data1=data.sheet_names
              for sheet in data1:
                  data2 = data.parse(sheet)
                  availablevars=list(data2.columns.values)
                  target.write(name)
                  target.write("\n")
                  for item in availablevars:
                     print(type((item).encode('utf-8')))
                     target.write((item).encode('utf-8'))
                  target.write("\n")
                  #target.write(filepath)
                #  availablevars.append(availablevars)
               #df = df.append(pd.read_excel(filepath, sheet))

             # print(data2.columns.values)

        if name.endswith((".csv")):
            if not name.startswith('.'):
              filepath = os.path.join(root, name)
              print(filepath)
              data = pd.read_csv(filepath)
              availablevars=list(data.columns.values)
              dummy.append(availablevars)
              target.write(name)
              target.write("\n")
              target.write(str(availablevars))
              target.write("\n")
              #target.write(filepath)
            #  availablevars.append(availablevars)

        if name.endswith((".xls")):
            if not name.startswith('.'):
              filepath = os.path.join(root, name)
              print(filepath)
              data=pd.ExcelFile(filepath)
              data1=data.sheet_names
              for sheet in data1:
                  data2 = data.parse(sheet)
                  availablevars=list(data2.columns.values)
                  target.write(name)
                  target.write("\n")
                  for item in availablevars:
                     print(type((item).encode('utf-8')))
                     target.write((item).encode('utf-8'))
                  target.write("\n")

target.close()

print( dummy)
       #for row in reader:
       # print(row)

data2 = pd.read_csv('Copy.csv')
data1 = pd.read_csv('list2.csv')
requiredvariables = [];
print('--------------------')
for i in range(0,35):

   for row in data2.itertuples():
       requiredvariables.append(row[i]);
for i in range(0,53):

   for row in data1.itertuples():
       requiredvariables.append(row[i]);
#print(colfromdataset)

requiredvariables=(filter(lambda v: v==v, requiredvariables))

c = [i for i in requiredvariables if i not in availablevars]
#c = list(set(requiredvariables).difference(availablevars))
#print(len(c))


availablevars=set(dummy)
requiredvariables=set(requiredvariables)

#c = [i for i in requiredvariables if i not in availablevars]
#print(len(c))

print("Total variables in input data set")
print(len(availablevars))
print("Variables needed for  infant...")
print(len(requiredvariables))


varsrequired=[];

for str1 in requiredvariables :
    if str1 not in availablevars:
        varsrequired.append(str1);




varsnotpresent=[];
print("---------")

for str1 in requiredvariables :
    if str1 not in availablevars:
         varsnotpresent.append(str1)




varsnotpresent=set(varsnotpresent);
print("Total Variables not present ")
print(varsnotpresent)
print(len(varsnotpresent))

for str1 in varsnotpresent:
    if str1 in availablevars:
        print( "is present")
