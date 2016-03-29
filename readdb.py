
'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
import pandas
import json
from pymongo import MongoClient
from bson.code import Code
data = pandas.read_csv('data.csv')



client = MongoClient('localhost', 27017)
db = client.exposome
posts = db.alldata
#posts.remove()
#posts.insert(data)
#data_json = json.loads(data.to_json(orient='records'))
#posts.insert(data_json,check_keys=False)

tweets_iterator = posts.find()
#for tweet in tweets_iterator:
#  print tweet
#

mapper = Code("""
    function() {
                  for (var key in this) { emit(key, null); }
               }
""")
reducer = Code("""
    function(key, stuff) { return null; }
""")

distinctFields = posts.map_reduce(mapper, reducer
    , out = {'inline' : 1}
    , full_response = True)

print((distinctFields))