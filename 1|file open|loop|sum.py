#performing file open opertion then finding the desired data then finding sum
fhand=input("enter file name")
data=open(fhand)
total=0
count=0
for x in data:
    if x.startswith("X-DSPAM-Confidence:"):
        count+=1
        start=x.find(":")
        st=x[start+1:]
        sum=float(st)
        total=total+sum
out=total/count
print(out)
