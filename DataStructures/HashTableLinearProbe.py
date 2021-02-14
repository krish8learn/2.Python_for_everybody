#creating hash table using probing as to solve collision
class Hash_Table:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range (self.Max)]

    def get_hash(self,key):
        hash =0
        for char in key:
            hash+=ord(char)
        return hash % self.Max

    def __setitem__(self,key,val):
        loc = self.get_hash(key)
        if self.arr[loc] is None:
            self.arr[loc] = (key,val)
        else:
            new_loc = self.find_slot(key,loc)
            self.arr[new_loc] = (key,val)
        print(self.arr)

    def get_prob_range(self,index):
        return [*range(index,len(self.arr))]+[*range(0,index)]

    def find_slot(self,key,loc):
        prob_range = self.get_prob_range(loc)
        for i in prob_range:
            if self.arr[i] is None:
                return i
            if self.arr[i][0] == key:
                return i
        raise Exception("hashmap full")

    def __getitem__(self,key):
        loc = self.get_hash(key)
        if self.arr[loc] is None:
            return
        prob_range = self.get_prob_range(loc)
        for i in prob_range:
            if self.arr[i] is None:
                return
            if self.arr[i][0] == key:
                return self.arr[i][1]

    def __delitem__(self,key):
        loc = self.get_hash(key)
        prob_range = self.get_prob_range(loc)
        for i in prob_range:
            if self.arr[i] is None:
                return "data not present"
            if self.arr[i][0] == key:
                self.arr[i] = None
        print(self.arr)        

t = Hash_Table()
t['march 17'] = 22
t['march 6'] = 17
t["april 2"] = 989
t["march 33"] = 234
t["dec 3"] = 45
print(t['march 33'])
del t["april 2"]
