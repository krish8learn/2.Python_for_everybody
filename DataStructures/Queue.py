from collections import deque
import threading
import time
class Queue:

    def __init__(self):
        self.buffer = deque()


    def enqueue(self,val):
        self.buffer.appendleft(val)


    def dequeue(self):
        return self.buffer.pop()


    def size(self):
        return len(self.buffer)


    def is_empty(self):
        return len(self.buffer)==0


    def insert_list(self,data_list):
        for data in data_list:
            #time.sleep(0.5)
            self.buffer.appendleft(data)


    def Print_elements(self):
        print(self.buffer)


    def front_val(self):
        return self.buffer[-1]


Q = Queue()
Q.insert_list(['CHELSEA','LIVERPOOL','MANCHESTER CITY','WEST HAM','EVERTON'])
Q.Print_elements()
print(Q.dequeue())

"""
food = Queue()
def place_order(orders):
    for item in orders:
        print("placing order:",item)
        food.enqueue(item)
        time.sleep(0.5)

def serve_order():
    #time.sleep(2)
    while True:
        print("serving:",food.dequeue())
        time.sleep(1)
orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order,)

t1.start()
t2.start()
"""

def binary_number(num):
    bin = Queue()
    bin.enqueue("1")

    for i in range(num):
        front = bin.front_val()
        print(" ",front)
        bin.enqueue(front + "0")
        bin.enqueue(front + "1")
        bin.dequeue()

binary_number(16)
