from docx import *
import re
str1="docx";

path = "/Users/Vivekanand/PycharmProjects/untitled";
dirs = os.listdir( path )
for file in dirs:
    if( ((file.find(str1))>-1)  ):
        document = opendocx(file)
        text=getdocumenttext(document)
        geore=re.compile(".*(Geographic).*")
        geolist = filter(geore.match, text)
        i=0;
        lengthofcounty=geolist.__len__()
        target = open('parseddata.txt', 'a')
        print(text)
        for j in range(lengthofcounty):
            target.write((geolist[j]).encode('utf-8'))
            target.write("\n")

        for words in text:
             if (words=='Family households (families)................... With own children under 18 years .......... Married-couple family ....................... With own children under 18 years .......... Female householder, no husband present ..... With own children under 18 years .......... Nonfamily households ........................ '):
               target.write("\n"+text[i]+text[i+164]+" "+text[i+173])
               print(text[i]+text[i+164]+" "+text[i+173])
              # print(text[i])
               #print text[i+1]
               #print text[i+2]
                #with own childre under 18
              # print text[i+6]
                #values
              # print text[i+7]
              # print text[i+8]

             i=1+i












