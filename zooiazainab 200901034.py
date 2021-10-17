#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#zooia zainab
#200901034
#bscs-01-b


class Stack:

    def _init_(self):
        self.container = deque()
        
    def push(self, x):
        self.container.append(x)
        
    def pop(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

    def top(self):
        return self.container[-1]

s= Stack()
p= input("enter your equation ")
check = True
y = 0
#program start
try:
    for j in p :
        if j =='[' or j=='(' or j=='{':
            stack.push(j)
        elif j==']' or j==')' or j=='}':
            stack.pop()
    if stack.size()==0:
        for j in range(0, len(p)):
            if p[j] == '"':
                if y % 2 == 0:
                    y += 1
                    if p[j+1] ==')'or p[j+1] ==']'or p[j+1] =='}'or p[j+1] =='"':
                        check = False
                    else:
                        check = True
                else:
                    check = True
                    y += 1

    if y % 2 == 0:
        check= True
    else:
        check= False
    if chech:
        print("your equation is true")
    else:
        print("your equation is wrong")
except:
    print("error")

