'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
import json
import pandas as pd
import openpyxl
import unicodedata
import numpy
from pymongo import MongoClient
str1="data.csv";
client = MongoClient('mongodb://chsmongodb.ttu.edu', 27017)
db = client.exposomedataset
posts = db.cleaneddata
availablevars=[];
#target = open('Cleaneddatasetvars', 'w');
df = pd.DataFrame()
count=0;
myvar=1

path = "/Users/Vivekanand/Downloads/Exposome2.0dataset";
for root, dirs, files in os.walk(path,topdown=True):
    for name in files:
        if name.endswith((".xlsx")):
            myvar=myvar+1
            if not name.startswith('.'):
              print(count)
              count=count+1;
              filepath = os.path.join(root, name)
              #print(filepath)

              data=pd.ExcelFile(filepath)
              data1=data.sheet_names
              #print(data1)
              for sheet in data1:
                 # target.write(name+"sheet: "+sheet)
                  #target.write("\n")
                  data2 = data.parse(sheet)
                  #data2['dummy']=None
                  availablevars=list(data2.columns.values)
                  #target.write(str(availablevars))
                 # target.write("\n")
                  data_json = json.loads(data2.to_json(orient='records'))
                 # print(data_json)
                  if not (data2.empty):
                   try:

                   # print(data_json)
                    #print(availablevars)

                    posts.insert( data_json,check_keys=False)
                   except OverflowError:
                       print("error occured")
                       continue



        if name.endswith((".csv")):
            if not name.startswith('.'):
              myvar=myvar+1
              filepath = os.path.join(root, name)
              #print(filepath)
            #  target.write(name+"sheet: "+sheet)
             # target.write("\n")
              data = pd.read_csv(filepath)
              availablevars=list(data.columns.values)
            #  target.write(str(availablevars))
             # target.write("\n")
              data_json = json.loads(data.to_json(orient='records'))
              posts.insert(data_json,check_keys=False)



