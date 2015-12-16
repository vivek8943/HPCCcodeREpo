'''
Created on Dec 10, 2015

@author: Vivekanand
'''
import csv
import os
str1="csv";
path = "/Users/Vivekanand/Documents/workspace/getHeaders/getHeader";
dirs = os.listdir( path )
for file in dirs:
   str2=file 
   if((str2.find(str1))>-1):
       print(file)
       csvfile = open( file, "r" )
       reader = csv.reader(csvfile)
       header = reader.next()
       print(header)
       csvfile.close()       
  
  
       

        
        
