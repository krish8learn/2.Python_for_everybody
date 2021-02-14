#operation of list, dict and their methods and how interchange the key and value of a dictionary
#opening file using a dialogue box
fname=input("Enter the file name ")
handle=open(fname)
#here the program goes through line by line looking for "From", if "Form" present then split that line and check if the generated list length whether greater than 2 or not, if it is greater than 2, go to the time(5) element and split that element by ":" then create a dictionary for the 1st element of 2nd list
count=dict()
for line in handle:
    if line.startswith("From"):
        lst=line.split()
        if len(lst)>2:
            lst2=lst[5].split(':')
            count[lst2[0]]=count.get(lst2[0],0)+1
#we convert the dictionary into list in form of tuples as example----(key,val)
lst3=list()
for key,val in count.items():
    newtup=(key,val)
    lst3.append(newtup)
#sort the list
lst3.sort()
for key,val in lst3[:]:
    print(key,val)
