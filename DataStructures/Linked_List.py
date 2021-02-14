#creating node
class Node:
    def __init__(self,data=None,next=None):
        self.data =data
        self.next = next #pointer to the next element

#creating class for linked_list where we would perform methods
class Linked_List:
    #creating head which would point to the 1st Node
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        #creating node inside the class which would be added at the begining
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self,data):
        if(self.head == None):  #checking Whether the linked list is empty or not
            self.head = Node(data,None)  #if it is null then head must point to the newly created node
            return

        itr = self.head        #for an active linked list iterator must take the value of overhead
        while(itr.next):       #it must keep increasing until it's reach the last element
            itr = itr.next
        itr.next = Node(data,None)    #last node is pointing to the newly created node


    def insert_new_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def Linked_length(self):
        count =0
        if(self.head is None):
            print ("Linked List is empty")
            return
        itr = self.head
        while(itr):
            count+=1
            itr = itr.next
        return count



    def Remove_at(self,pos):
        if(self.head is None or pos>self.Linked_length() or pos<0):
            print("Linked List is empty or not valid position entered")

        if (pos == 0 ):
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while(itr):                #iterate through the linked list until it reach pos-1
            if(count == pos-1):
                itr.next = itr.next.next           #the itr node must point to the node which is ahead of deleting node
                break
            count+=1
            itr = itr.next


    def insert_at(self, index, data):
        if(index>=self.Linked_length() or index<0):
            #raise Exception("invalid index")
            print("invalid index")
        if(index==0):
            insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while(itr):
            if(count==index-1):
                node = Node(data,itr.next)       #creating node and that new node must point to the next node
                itr.next = node                  #itr which is at the the previous node of new node, now must point to the new node
                break
            count+=1
            itr=itr.next

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while(itr):
            if(itr.data == data_after):
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data_to_remove):
        itr = self.head
        count = 0;
        while(itr):
            count+=1
            if(itr.data == data_to_remove):
                self.Remove_at(count-1)
                break
            itr = itr.next


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        lstr = " "
        while itr:
            lstr +=str(itr.data) + '--->'
            itr = itr.next
        print(lstr)


if __name__== '__main__':
    ll = Linked_List()
    ll.insert_at_begining(12)
    ll.insert_at_begining(45)
    ll.insert_at_begining(78)
    ll.insert_at(2,86)
    ll.insert_after_value(45,22)
    #ll.insert_at(2,19)
    ll.insert_at_end(75)
    ll.print()
    ll.remove_by_value(78)
    print("length:",ll.Linked_length())
    ll.print()
    #ll.insert_at_end(66)
    #ll.insert_at_end(42)
    #ll.insert_at(5,86)
    #print("length:",ll.Linked_length())
    #ll.print()
    ll.insert_new_values(["krish","avik","sayak","arghya"])
    #ll.Remove_at(4)
    #print("length:",ll.Linked_length())
    ll.print()
