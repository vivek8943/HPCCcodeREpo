
'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import scipy
import pandas
import numpy
from sklearn import  linear_model
from bson.son import SON
target=open("stats.txt",'w')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.exposomedataset
posts = db.cleaneddata
listofrecords1=[]
listofrecords2=[]
array=[]
with open("decodedvarsdummy.txt", "r") as f:
  for line in f:
    line=line.strip('\n')
    #print(line)
    array.append(line)
datafromquery=[]
df2=pandas.DataFrame

infantvector=pandas.DataFrame(list(posts.find({ 'b_infant_mort_9911': { '$exists': True } },{'b_infant_mort_9911':1,'_id':0})))

target.write("Infant Mortality Mean "+str(infantvector.mean())+"\n")
target.write("Infant Mortality STD "+str(infantvector.std())+"\n")
target.write("Infant Mortality Median "+str(infantvector.median())+"\n")
for i in array:
    print(i)
    target.write("Variable : "+i+"\n")
    df2=pandas.DataFrame(list(posts.find({ i: { '$exists': True } },{i:1,'_id':0})))
    mean=df2.mean()
    std=df2.std()
    min=df2.min()
    max=df2.max()
    diffmeanandmin=mean-min
    diffmeanandmax=mean-max
    #print(df2)
    if not df2.empty:
        print df2[i]
    else:
        print(i)


   # corr=scipy.stats.pearsonr(df2[i], infantvector['b_infant_mort_9911'])
   # print("Corr",corr)
        target.write(i)
        target.write(" Mean "+str(mean)+"\n")
        target.write(" STD "+str(std)+"\n")

        target.write(" min "+str(min)+"\n")
        target.write(" max "+str(max)+"\n")
        target.write(" diffmeanandmin"+str(diffmeanandmin)+"\n")
        target.write(" diffmeanandmax"+str(diffmeanandmax)+"\n")
        target.write(" r2 value"+str(diffmeanandmin**2)+"\n")



