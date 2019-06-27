# implement a stack



class Stack (object):
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items ==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return  len(self.items)



## testing the stack
s= Stack()



s.push(1)
s.push('two')
s.peek()
print(s.size())

print(s.isEmpty())


s.pop()

s.pop()


print(s.isEmpty())






    



