#  File: TestLinkedList.py

#  Description: Python script creating all the methods involved in a linked list class
#               This script then tests all such methods

#  Student Name: Mehul Gupta

#  Student UT EID: mdg3739

#  Partner Name: Ginger Hudson

#  Partner UT EID: gsh628

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/29/2022

#  Date Last Modified: 10/31/2022

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    current = self.first
    counter = 0
    while current != None:
      counter += 1
      current = current.next
    return counter
  
  # add an item at the beginning of the list
  def insert_first (self, data): 
    item_node = Link(data)
    item_node.next = self.first   
    self.first = item_node
    return 

  # add an item at the end of a list
  def insert_last (self, data): 
    item_node = Link(data)
    if (self.first == None):
      self.first = item_node
      return
    current = self.first
    while (current.next != None):
      current = current.next
    current.next = item_node
    return

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    item_node = Link(data)
    if (self.first == None):
      self.first = item_node
      return
    if (data <= self.first.data):
      self.insert_first(data)
      return
    elif (data > self.first.data):
      current = self.first
      while data > current.data:
          if current.next == None:
              self.insert_last(data)
              return
          else:
              previous = current
              current = current.next
      previous.next = item_node
      item_node.next = current
      return

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    current = self.first
    while current != None:
      if current.data == data:
        return current.data
      else:
        current = current.next
    return None

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    current = self.first
    while current != None:
      if current.data == data:
        return current.data
      elif current.data > data:
        return None
      else:
        current = current.next
    return None


  # Delete and return the first occurrence of a Link containing data
  
  def delete_link (self, data):
    current = self.first
    previous = self.first
    while current != None:
      if current.data == data:
        if current == self.first:
          self.first = self.first.next
        else:
            previous.next = current.next
            return current
      else:
        previous = current
        current = current.next
    return None



  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    current = self.first
    counter = 0
    string = ''
    while current != None:
      string += str(current.data) + '  '
      counter += 1
      if counter == 10:
        string += "\n"
      current = current.next
    return string


  # Copy the contents of a list and return new list

  def copy_list (self):
    copy = LinkedList()
    current = self.first
    while current != None:
      copy.insert_last(current.data)
      current = current.next
    return copy


  # Reverse the contents of a list and return new list
  # do not change the original list

  def reverse_list (self): 
    previous=None
    current=self.first
    while current != None:
      next = current.next
      current.next = previous
      previous = current
      current = next
    self.first = previous
    return self

  # Sort the contents of a list in ascending order and return new list

  def sort_list (self): 
    current = self.first
    while current != None:
      minimum = current
      next = current.next
      while next != None:
        if next.data < minimum.data:
          minimum = next
        next = next.next
      temp = current.data
      current.data = minimum.data
      minimum.data = temp
      current = current.next
    return self 

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    if self.is_empty():
      return True
    current = self.first
    while current.next != None:
      if current.data <= current.next.data:
        current = current.next
        continue
      else:
        return False
    return True


  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    if self.first == None:
      return True
    else:
      return False

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    merged = self.copy_list()
    if self.is_empty():
      if other.is_empty():
        return merged
      else:
        merged = other.copy_list()
        return merged
    elif other.is_empty():
      return merged.sort_list()
    current = other.first
    i = 0
    while i < other.get_num_links():
      merged.insert_in_order(current.data)
      current = current.next
      i+=1
    return merged

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    if self.is_empty() and other.is_empty():
      return True
    if self.get_num_links() != other.get_num_links():
      return False
    first_current = self.first
    second_current = other.first
    i = 0
    while i < self.get_num_links():
      i+=1
      if first_current.data != second_current.data:
        return False
      first_current = first_current.next
      second_current = second_current.next
    return True


  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    copy = self.copy_list()
    current = copy.first
    previous = copy.first
    single_occurance = []
    i = 0
    while i < copy.get_num_links():
      i+=1
      if current.data in single_occurance:
        current = current.next
        previous.next = current
      else:
        single_occurance.append(current.data)
        previous = current
        current = current.next
    return bool(single_occurance)


def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  myTest = LinkedList()
  i = 0
  while i < 10:
    myTest.insert_first(i)
    i+=1
    print(myTest)
    print("--------------------")

  # Test method insert_last()
  myTest.insert_last(12)
  print(myTest)
  print("--------------------")

  # Test method insert_in_order()
  myTest.insert_in_order(11)
  print(myTest)
  print("--------------------")

  # Test method get_num_links()
  print(myTest.get_num_links())
  print("--------------------")

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 
  print(myTest.find_unordered(10))
  print(myTest.find_unordered(13))
  print("--------------------")

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  print(myTest.find_ordered(10))
  print(myTest.find_ordered(13))
  print("--------------------")

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  print(myTest.delete_link(12))
  print(myTest.delete_link(15))
  print("--------------------")

  # Test method copy_list()
  print(myTest.copy_list())
  print("--------------------")

  # Test method reverse_list()
  print(myTest.reverse_list())
  print("--------------------")

  # Test method sort_list()
  myTest.insert_first(50)
  print(myTest.sort_list())
  print("--------------------")
  myTest.delete_link(50)

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print(myTest.is_sorted())
  myTest.insert_first(50)
  print(myTest.is_sorted())
  myTest.delete_link(50)
  print("--------------------") 

  # Test method is_empty()
  print(myTest.is_empty)
  print("--------------------") 

  # Test method merge_list()
  myTest2 = LinkedList()
  myTest2.insert_first(50)
  myTest2.insert_last(15)
  merged = myTest.merge_list(myTest2)
  print(merged)
  print("--------------------") 

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print(myTest.is_equal(myTest)) 
  print(myTest.is_equal(myTest2))
  print("--------------------") 

  # Test remove_duplicates()
  myTest.insert_first(1)
  print(myTest)
  myTest.remove_duplicates()
  print(myTest)
  print("--------------------") 

if __name__ == "__main__":
  main()
