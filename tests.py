import scipy
import pandas
import numpy
from sklearn import  linear_model
from bson.son import SON
from scipy.stats.stats import pearsonr
from scipy import signal
from scipy import stats
errortarget=open("finalerrors1.txt",'w')
#target=open("stats1.txt",'w')
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
infant=list(posts.find({ 'b_infant_mort_9911': { '$exists': True } },{'b_infant_mort_9911':1,'_id':0}))
infantlen=len(infant)
#print(infant)
infantvector=pandas.DataFrame(infant)
mean=numpy.nanmean(infant)
sampledarray=(numpy.random.choice(varlist,infantlen))
std=mean-mean
print(mean)
