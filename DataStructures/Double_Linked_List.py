#double Linked_List
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Double_Linked_List:
    #creating a head which indicate to the 1st data
    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data,self.head,None)
        self.head.prev = node
        self.head = node


    def insert_at_end(self,data):
        if(self.head == None):
            self.head = Node(data,None,None)
            return

        itr = self.head
        while(itr.next):
            itr = itr.next
        itr.next = Node(data,None,itr)


    def Linked_length(self):
        count =0
        itr = self.head
        while(itr):
            count+=1
            itr = itr.next
        return count


    def insert_at(self, index, data):
        if(index>self.Linked_length() or index<0):
            raise Exception("Not valid Index")
            return

        if(index == 0):
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while(itr):
            if(count==index-1):
                node = Node(data,itr.next,itr)
                if(node.next):
                    node.next.prev = node
                itr.next = node
                break
            count+=1
            itr = itr.next


    def last_node(self):
        itr = self.head
        while(itr.next):
            itr = itr.next
        return itr

    def insert_all(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def Remove_at(self,index):
        if(index>self.Linked_length() or index<0):
            raise Exception("Not valid Index")
            return

        if(index == 0):
            self.head = self.head.next
            self.prev = None
            return

        count =0
        itr = self.head
        while(itr):
            if(count == index):
                itr.prev.next = itr.next
                if(itr.next):
                    itr.next = itr.prev
                break
            itr = itr.next
            count+=1

    def print_forward(self):
        if(self.head is None):
            print("Empty Double_Linked_List")
            return

        itr = self.head
        dstr = " "
        while(itr):
            dstr +=str(itr.data)+"--->"
            itr = itr.next
        print("forward direction:",dstr)


    def print_backward(self):
        if(self.head is None):
            print("Empty Double Linked_List")
            return

        last_node = self.last_node()
        itr = last_node
        dstr = " "
        while(itr):
            dstr +=str(itr.data)+"--->"
            itr = itr.prev
        print("Backward direction: ",dstr)




if __name__== '__main__':
    ll = Double_Linked_List()
    ll.insert_all(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.insert_at_begining("ozile")
    ll.print_forward()
