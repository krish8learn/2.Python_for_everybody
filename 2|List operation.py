#learn how to use list in python
#fname=input("Enter the file name ")
fhandle=open('file2.txt')
res=[]
for line in fhandle:
    res=res+line.rstrip().split()
res.sort()
print(res)
