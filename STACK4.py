
# design a stack which in addition to push and pop has a
# function min which returns the minimum element. Push pop amd min should all operate in 0(1) time.

class Stack():

    def __init__(self):
        self.element_stack = []
        self.min_element_stack = []

    def push(self, item):
        if self.size() == 0:
            self.min_element_stack.append(item)
        else:
            self.min_element_stack.append(min(self.min_element_stack[self.size() - 1], item))
        self.element_stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        self.min_element_stack.pop()
        return self.element_stack.pop()

    def minimum(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        return self.min_element_stack[self.size() - 1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.element_stack)


def main():
    stack = Stack()
    stack.push(3)
    print(stack.minimum())
    stack.push(5)
    print(stack.minimum())
    stack.push(1)
    print(stack.minimum())
    stack.pop()
    print(stack.minimum())

if __name__ == "__main__":
    main()