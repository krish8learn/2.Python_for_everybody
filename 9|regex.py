# python regular expressions
import re
fname = input("File name ")
numlist = list()
fhandle = open(fname)
for line in fhandle:
    line = line.strip()
    stuff = re.findall('[0-9]+',line)
    for element in range(0,len(stuff)):
        num = int(stuff[element])
        numlist.append(num)
tot =0
for element in range(0,len(numlist)):
    tot = tot + numlist[element]
print(tot)
