
file_new = open(r'/Users/Vivekanand/HPCCcodeREpo/decodedvarsdummy.txt', 'r+')
file_new_set=set(line.strip() for line in file_new)
file_sep = open(r'/Users/Vivekanand/HPCCcodeREpo/decodedvarsseperated.txt', 'r+')
file_sep_set=set(line.strip() for line in file_sep)


print(set(file_new_set) - set(file_sep_set))
print(len(set(file_sep_set)))

