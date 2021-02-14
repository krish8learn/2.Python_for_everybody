#list dict operation and interchange 
#opening the files
#fname=input("Enter file name ")
handle=open('file1.txt')
#iterating through text files line by line using list and dict
count=dict()
for line in handle:
    lsit=line.split()
    if len(lsit)>2:
        for word in lsit:
            count[word]=count.get(word,0)+1
#converting the dict into an list in form tuples
lst=list()
for key,value in count.items():
    newtup=(value,key)
    lst.append(newtup) #dict structure element inside list
#sorting the list which has items in form of tuples
lst=sorted(lst,reverse=True)
#printing values
for val,key in lst[:10]:
    print(key,val)
