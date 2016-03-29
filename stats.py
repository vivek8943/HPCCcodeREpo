

for i in array:
  print(i)

  iterator1 = pandas.DataFrame(list(posts.find({ i: { '$exists': True } },{i:1,'_id':0})))
  print iterator1


iterator2 = posts.find({ 'b_infant_mort_9911': { '$exists': True } },{'b_infant_mort_9911':1,'FIPS':1,'_id':0})
for tweet in iterator2:

  listofrecords2.append(tweet)

df1 = pandas.DataFrame(listofrecords1)
df2 = pandas.DataFrame(listofrecords2)

print df1.append(df2)

#resul=posts.aggregate([{
#	'$group' : {'_id' : "FIPS", 'total' : { '$sum' : 1 }}
 #   }])
#for t in resul:
#    print(t)











concat=pandas.concat([df1, df2], axis=1)
print(concat)
print("\n quantile 0.5")
print concat.quantile(0.5)

print concat.describe()
print("\n median \n")
print concat.median()
print("\n sum \n ")
print concat.sum()
print("\n varience \n ")
print concat.var()
print("\n Covarience \n ")
print concat.cov()
print("\n skewness \n ")
print(concat.skew())
print("\n Corr coeff \n ")
print(concat.corr())
print("\n R2 value \n ")
print(concat.corr()**2)

slope, intercept, r_value, p_value, std_err = stats.linregress(concat['RATE_MDS_TOT_FM_OFFBASED'], concat['b_infant_mort_9911'])
print "\n r-squared:", r_value**2
#regr.fit(concat['RATE_MDS_TOT_FM_OFFBASED'], concat('b_infant_mort_9911'))
#print('Coefficients: \n', regr.coef_)


