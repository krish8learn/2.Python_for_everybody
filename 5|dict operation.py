#Dict operation ---adding element 
fname=input("Enter texts ")
wordslist=fname.split()
print("Words "wordslist)
count=dict()
for word in wordslist:
    count[word]=count.get(word,0)+1
print("Count ",count)
print(count.values())
print(count.items())
