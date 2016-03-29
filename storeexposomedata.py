
'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
import pandas
import json
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.exposome
posts = db.alldata
#posts.remove()
data = pandas.read_csv('Sheet3.csv')
print(data.empty)
data0=pandas.ExcelFile('/Users/Vivekanand/Downloads/Exposome2.0dataset/housing data 2000 ready for use.xlsx')
data1=data0.sheet_names
for sheet in data1:
                 # target.write("\n")
                  data2 = data0.parse(sheet)
                  #print(data2)
if not (data.empty):
                    print(data.empty)
                    data_json = json.loads(data.to_json(orient='records'))
                    posts.insert(data_json,check_keys=False)
                 # data2.to_csv(sheet+'.csv', encoding='utf-8')
#print(data1)



#posts.insert(data)


#tweets_iterator = posts.find()
#for tweet in tweets_iterator:
  #print tweet