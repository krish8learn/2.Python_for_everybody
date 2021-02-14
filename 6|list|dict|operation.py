# dict list operation highest sender, highest times
fname=input("Enter file name ")
handle=open(fname)
count=dict()

for line in handle:
    if line.startswith("From"):
        lst=line.split()
        if len(lst)>2:
            count[lst[1]]=count.get(lst[1],0)+1

bignum=None
bigsender=None
for sender,num in count.items():
    if bignum is None or num>bignum:
        bigsender=sender
        bignum=num

print(bigsender,bignum)
