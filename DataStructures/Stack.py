from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def every_element(self):
        print(self.container)

def reverse_string(st):
    stack = Stack()
    for ch in st:
        stack.push(ch)
    rstr = " "
    while(stack.size()!=0):
        rstr = rstr + stack.pop()
    return rstr

def is_balanced(st):
    stack = Stack()

    for ch in st:
        if(ch=='[' or ch=='{' or ch=='(' or ch==')' or ch=='}' or ch==']'):
            if(ch=='{'or ch=='(' or ch=='['):
                stack.push(ch)
            if(ch=='}'or ch==')' or ch==']'):
                if(stack.size()==0):
                    stack.push(ch)
                if(stack.size()!=0):
                    if((ch=='}' and stack.peek()=='{') or (ch==')' and stack.peek()=='(') or (ch==']' and stack.peek()=='[')):
                        stack.pop()
        else:
            continue


    if(stack.is_empty() is True):
        print("True")
    else:
        print("False")

s = Stack()
s.push(5)
s.push(78)
s.push(98)
s.push(45)
print(s.peek())
#print(s.pop())
#print(s.peek())
print(s.size())
s.every_element()
print(reverse_string("I am the king"))
is_balanced("({a+b})")
is_balanced("))((a+b}{")
is_balanced("((a+b))")
is_balanced("))")
is_balanced("[a+b]*(x+2y)*{gg+kk}")
