input1 = int(input("enter number of days:"))
input2 = int(input("enter starting amount"))

esum = []
osum = []
elemento=0
elemente=0
for i in range (1,input1+1):
    if(i==1):
        osum.append(input2)
        elemento+=1
    elif(i==2):
        esum.append(int(input2/2))
        elemente+=1
    elif(i%2!=0):
        osum.append(osum[elemente-1]*2)
        elemento+=1
    elif(i%2==0):
        esum.append(int((osum[elemento-2] + osum[elemento-1])/2))
        elemente+=1

print(len(osum),len(esum))
print(osum)
print(esum)
print(sum(osum),sum(esum))
