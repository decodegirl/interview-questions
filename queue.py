# queues work on a first in first out principle
# implement a stack


class Queue(object):

    def __init__(self):
        self.items =[]

    def isEmpty (self):
        return self.items == []

    def enqueue (self,item):
        self.items.insert(0,item)


    def dequeue(self):
        return self.items.pop()


    def size(self):
        return len(self.items)



## testing the queue
q = Queue()

print(q.isEmpty())


q.enqueue(1)

q.enqueue(2)

print(q.dequeue())