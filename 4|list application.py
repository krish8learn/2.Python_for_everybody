#finding number of lines strt with 'from' by using list, split, if, for, strtswith
fname=input("Enter file name ")
fhandle=open(fname)
count =0
lst=[]
for line in fhandle:
    if line.startswith("From"):
        lst=line.split()
        if(len(lst)>2):
            count+=1
            print(lst[1])
print("There were", count, "lines in the file with From as the first word")
