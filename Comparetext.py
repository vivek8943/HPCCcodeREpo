old_lines = set((line.strip() for line in open(r'/Users/Vivekanand/HPCCcodeREpo/listofvars', 'r+')))
file_new = open(r'/Users/Vivekanand/HPCCcodeREpo/dummy', 'r+')
file_diff = open(r'file_diff.txt', 'w')

file_new_set=set(line.strip() for line in file_new)

decodedvars_old_lines=[];
decodedvars_new_lines=[];
target1 = open('decodedvars_old', 'w');
for var1 in old_lines:
    temp=((var1).replace('u\'',''))

    temp=temp.replace('\'','')

    temp=temp.replace('\"','')
    target1.write(temp+"\n")
    decodedvars_old_lines.append(temp)

target = open('decodedvars_new', 'w');
for var2 in file_new_set:
    temp1=((var2).replace('u\'',''))
    temp1=temp1.replace('\'','')
    temp1=temp1.replace('\"','')
    decodedvars_new_lines.append(temp1)
    target.write(temp1+"\n")

for i in decodedvars_new_lines:
    print(i)

print('//////////')


varsrequired=[];

for str1 in decodedvars_new_lines :
    if str1 not in decodedvars_old_lines:

        varsrequired.append(str1)


print len(varsrequired)

print((varsrequired))

print decodedvars_old_lines.__contains__('EducationIndex')