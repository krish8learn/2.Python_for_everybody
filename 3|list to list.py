#open file, sending one item of list to another list 
fname=input("Enter the file name ")
fhandle=open(fname)
res=[]
for line in fhandle:
    lst=line.split()
    for item in lst:
        if item in res:
            continue
        res.append(item)    
res.sort()
print(res)
