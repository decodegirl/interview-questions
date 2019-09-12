
# 1) Creates unsorted linked list
# 2) Prints the list
# 3) remove duplicates from the unsorted linked list
# 4) Prints the new linked list
# Write code to remove duplicates from an unsorted linked list
# Define a Node class that holds the following:
#    => data: store the value of the current list element
#    => next_node: stores the next Node in the Linked List. 

class Node(object):
    def __init__(self,data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node = new_next

    def printNode(self):
        print(self.data)
        print (" ===> ")

# Define a LinkedList class the holds the following:
#    => head  : pointer to the head of the Linked List. Head is the 1st node

class SinglyLinkedList:
    # Note when list is first initialized it has no nodes so head is set to None
  def __init__(self,head=None):
        self.head = head
    
  def insert(self,data):
       new_node = Node(data)
       new_node.set_next(self.head)
       self.head = new_node

  def size(self):
      current = self.head
      count = 0 
      while current:
          count += 1
          current = current.get_next()
      return count

  def printList(self):
      current = self.head
      #print ( "the value of the head is %s" %(current.data) ) 
      count = 0 
      while current:
          count += 1
          if current.data is not None:
              current.printNode()
              current = current.get_next()
          else:
              return

  def search(self,data):
      current = self.head
      found = False
      while current and found is False:
          if current.get_data() == data:
              found = True
          else:
              current = current.get_next()
          if current is None:
              raise ValueError("Data not in list")
      return current
  
  # this function will delete ALL occurances of a value from the LL
  def delete(self,data):
      current = self.head
      previous = None
      found = False
      while current and found is False:
          if current.get_data() == data:
              found = True
          else:
              previous = current
              current = current.get_next()
      if current is None:
          raise ValueError("Data not in list")
      if previous is None:
          self.head = current.get_next()
      else:
          previous.set_next(current.get_next())
 
  # use 2 pointers current which iterates through the Linked List
  # and runner which checks all subsequent nodes for duplicates 
  # current.next_node is not an iterator it is simply a property of the Node and does not change
  # if we find a duplicate(s) in the LL we want to keep the 1st occurance but remove any others
  def remove_duplicates(self):
      current = self.head
      #print ( "the value of head is ==> %s" %(self.head.data) ) 
      while current is not None:
          runner = current

          while runner.next_node is not None:
              if runner.next_node.data == current.data:
                  #print ( "about to delete %s" %(runner.next_node.data) )
                  runner.next_node = runner.next_node.next_node
              else:
                  runner = runner.next_node
                  #print ( "I didnt delete anything move to next node %s" %(runner.data) ) 
          current = current.next_node
               
