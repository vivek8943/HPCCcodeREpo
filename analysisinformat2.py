
'''
Created on Dec 10, 2015

@author: Vivekanand
'''
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
dfList = infantvector['b_infant_mort_9911'].tolist()
#print(dfList)


dataframeofvalues=pandas.DataFrame(columns=['Variable','Mean','std','Min','Max','diffofmeanandmin','diffmeanandmax','r2value','pvalue'])
#print(dataframeofvalues)
#target.write("Infant Mortality Mean :"+str(numpy.nanmean(dfList))+"\n")
#target.write("Infant Mortality STD "+str(numpy.nanstd(dfList))+"\n")
#target.write("Infant Mortality Median "+str(numpy.nanmedian(dfList))+"\n")
for i in array:
       # print(i)
      #  target.write("\n"+"Variable : "+i+"\n")
    try:
        vector=list(posts.find({ i: { '$exists': True } },{i:1,'_id':0}))
        vectorlen=len(vector)
        vectornumpy=(numpy.random.choice(vector,vectorlen))
        df2=pandas.DataFrame(vector)
        vector = df2[i].tolist()
        mean=numpy.nanmean(vector)
        std=numpy.nanstd(vector)
        min=numpy.nanmin(vector)
        max=numpy.nanmax(vector)
        diffmeanandmin=mean-min
        diffmeanandmax=mean-max

        #print(df2)
        if not df2.empty:
            varlist = df2[i].tolist()
            sampledarray=(numpy.random.choice(varlist,infantlen))
            corr=scipy.stats.stats.spearmanr(sampledarray, dfList)
            print(corr)
            r2value=corr.correlation**2
            pvalue=((corr.pvalue))
            #print(dataframeofvalues)
            dataframeofvalues.loc[len(dataframeofvalues)]=[i,mean,std,min,max,diffmeanandmin,diffmeanandmax,r2value,pvalue]
           # print(dataframeofvalues)
        else:
            errortarget.write(i)
            print i



    except TypeError:
            print(i+"TypeError")
            errortarget.write(i+"\n")
            continue
    except ValueError:
            print(i+"corr error"+"\n")
            errortarget.write(i+"\n")
            continue
    except AttributeError:
            print(i+"TypeError")
            errortarget.write(i+"\n")
            continue
        #print("Corr",corr)


print(dataframeofvalues)
dataframeofvalues.to_csv("results.csv")


