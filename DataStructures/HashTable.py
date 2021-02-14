#creating a Hash_Table which function is similar to the dictionary
class Hash_Table:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range (self.Max)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.Max

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        #self.arr[h] = val      #next code will try to solve the collision
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] ==key:
                self.arr[h][idx]= (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))   # here no element was present, it is storing the 1st value at this hash index

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h][idx]



t = Hash_Table()
t['march 6'] = 17
#t['march 7']  = 45
t['march 8'] = 14
t['march 9'] = 41
t['march 17'] = 998
#t['mambo'] = 48
#march 6 and march 17 generate same index to store value through get_hash function
print(t.arr)
print(t['march 6'])
print(t['march 17'])
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))
#print(t['krish'])
#del t['chayan']
#print(t.arr)
