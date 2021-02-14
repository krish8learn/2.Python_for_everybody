number = input("enter the number")
odd = []
for i in range(int(number)):
    if(i%2!=0):
        odd.append(i)

print(odd)
