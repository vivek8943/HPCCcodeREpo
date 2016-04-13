
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
errortarget=open("errorvars1.txt",'w')
target=open("stats1.txt",'w')
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


target.write("Infant Mortality Mean :"+str(numpy.nanmean(dfList))+"\n")
target.write("Infant Mortality STD "+str(numpy.nanstd(dfList))+"\n")
target.write("Infant Mortality Median "+str(numpy.nanmedian(dfList))+"\n")
for i in array:
       # print(i)
        target.write("\n"+"Variable : "+i+"\n")
        vector=list(posts.find({ i: { '$exists': True } },{i:1,'_id':0}))
        df2=pandas.DataFrame(vector)

        mean=df2.mean()
        print(mean)
        std=df2.std()
        min=df2.min()
        max=df2.max()
        diffmeanandmin=mean-min
        diffmeanandmax=mean-max
        #print(df2)
        if not df2.empty:
            varlist = df2[i].tolist()
            sampledarray=(numpy.random.choice(varlist,infantlen))
        else:
           print i
        try:
            target.write(i)
            target.write(" Mean ")
            print(numpy.nanmean(sampledarray))
            target.write(str(numpy.nanmean(sampledarray)))
            target.write("\n")
            target.write(" STD ")
            target.write('{}'.format(stats.nanstd(sampledarray)))
            target.write("\n")
            target.write(" min ")
            target.write('{}'.format(numpy.nanmin(sampledarray)))
            target.write("\n")
            target.write( " max ")
            target.write('{}'.format(numpy.nanmax(sampledarray)))
            target.write("\n")
            target.write( " diffmeanandmin :")
            target.write('{}'.format(diffmeanandmin))
            target.write("\n")
            target.write(" diffmeanandmax :")
            target.write('{}'.format(diffmeanandmax))
            target.write("\n")
            target.write(" r2 value :")
            corr=scipy.stats.stats.spearmanr(sampledarray, dfList)
            target.write('{}'.format(corr.correlation**2))
            target.write("\n")
            target.write(" p value :")
            target.write('{}'.format(corr.pvalue))
        except ValueError:
            print(i+"corr error"+"\n")
            errortarget.write(i)
            continue
        except TypeError,AttributeError:
            print(i+"TypeError")
            errortarget.write(i)
            continue
        #print("Corr",corr)





