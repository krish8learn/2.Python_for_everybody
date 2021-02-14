#Arrays
#n python array known as List[] which is Dynamic array and it can store heterogenous elements, though java has two different arrays
#Static -----------int [] arr = new int[];
#Dynamic------ArrayList<> obj = new ArraYList<>(); and stored elements are must be homogenous.
exp = [2200,2350,2600,2130,2190]
print("extra dollar spent in feb compare to january:",exp[1]-exp[0])
print("total expenses:",exp[0]+exp[1]+exp[2])
print("spent 2000 ? ",2000 in exp)
exp.append(1980)
print("at the end",exp)
for i in range(len(exp)):
    if(i==5):
        exp[i]+=200
print("after correction",exp)

animals = ['spider-man','thor','hulk','iron-man','captain-america']
print(len(animals))
animals.append('black panther')
animals.remove(animals[len(animals)-1])
animals.insert(3,'black panther')
animals.sort()
print(animals)
