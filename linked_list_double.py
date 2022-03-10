import random
import merge_sort

"""An exercise building on the singly linked list program"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class LL_double:
    def __init__(self):
        self.head = None
        self.tail = None
        self.list = []

    def __repr__(self):
        #print(self.head.data, end =" INBETWEEN STUFF ")
        #print(self.tail.data)
        return "will return list later"

    def isEmpty(self):
        return self.head == None

    def add(self,data):
        self.list.append(data)
        new_node = Node(data)
        current = self.head
        last = current

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        #Should find rightmost node and append to the list
        while current.right != None:
            last = current
            current = current.right

        if current.right == None:
            current.left = last
            current.right = new_node
            self.tail = new_node


    def printList(self):
        """Prints the list in order of left to right"""
        current = self.head
        while current != None:
            print(current.data)
            current = current.right

    def lengthList(self):
        """Returns length of the list"""
        count = 1
        current = self.head
        while current.right != None:
            count+=1
            current = current.right

        return count



    def returnIndex(self,index):
        """Returns index that was input"""

        if index > self.lengthList()-1:
            return "Index input is over the length of the list"

        current = self.head
        for i in range(0,index,1):
            current = current.right
        return current.data

    def printArray(self):
        print(self.list)



l = LL_double()
l.add(10)
l.add(12)
l.add(15)
l.add(22)
l.add(25)
l.printList()
print("length: ",l.lengthList())
val = 3
print("index at ",val," = ",l.returnIndex(val))

print("\nRepr function \n",l)

