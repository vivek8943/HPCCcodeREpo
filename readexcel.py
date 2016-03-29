'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
import pandas
from pymongo import MongoClient
import json
str1="data.csv";

client = MongoClient('localhost', 27017)
db = client.exposome
posts = db.alldata
posts.remove()
path = "/Volumes/FLASHDRIVE/Exposome2.0dataset";
for root, dirs, files in os.walk(path,topdown=True):
    for name in files:
        if name.endswith((".xlsx")):
            if not name.startswith('.'):

              filepath = os.path.join(root, name)
              print(filepath)

              data = pandas.read_excel(filepath,header=0,sheetname=None)
              print(data)
              #data_json = json.loads(data)
              pandas.DataFrame.from_dict(data)
            #  posts.insert(data_json,check_keys=False)





tweets_iterator = posts.find()
for tweet in tweets_iterator:
  print tweet
