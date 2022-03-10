import random
import math


"""This is THE working binary search tree that I have created. This is mostly just a learning exercise. 

    it's not completely functional for any operation you would want but it lays out as a tree should"""

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.head = None
        self.list = []

    #adds data to the normal list to build later
    def add(self,data):
        self.list.append(data)

    #adds the node value to any position in the list
    def addNode(self,data,pos = -1):
        if pos == -1:
            pos = len(self.list)
        self.list.insert(pos,data)
        self.buildList()

    def removeNodeIndex(self,pos):
        #removes node at any given index
        self.list.pop(pos)
        self.buildList()

    def removeNodeValue(self,data):
        #removes all instances of a node's value at given data
        for i in range(0,len(self.list),1):
            if self.list[i] == data:
                self.list.pop(i)
        self.buildList()


    #builds a node-based structure of this list
    def buildList(self):
        for i in range(0,len(self.list),1):
            if i ==0:
                current = Node(self.list[i])
                self.head = current
            else:
                new_node = Node(self.list[i])
                current.nextNode = new_node
                current = new_node

    def searchValue(self,key):
        """
        Search for the first node that matches the key
        Returns the node or None if not found
        Takes 0(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.nextNode
        return None

    def searchIndex(self,index):
        """
        Linear search for indexed node.
        Returns the node or None if not found.
        Takes 0(n) time
        """
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            else:
                count+=1
                current = current.nextNode
        return None

    def searchLast(self):
        """Returns last node in the tree"""

        current = self.head
        while current:
            if current.nextNode == None:
                return current
            else:
                current = current.nextNode
        return None

    def printAllValues(self,node):
        """Returns string with all relevant node's data
        For testing purposes
        """
        #If no node return
        if node == None:
            return("No Node")

        #prints node's data
        print("Node data:",node.data)

        #print's next node's data
        if node.nextNode != None:
            print("Next Node's data:",node.nextNode.data)
        else:
            print("No next Node")

        #prints left node's data
        if node.left != None:
            print("Left Node's data:",node.left.data)
        else:
            print("No left Node")

        #print right note's data
        if node.right != None:
            print("Right Node's data:",node.right.data)
        else:
            print("No right Node")

        return""

    def printData(self,node):
        return node.data

##GONNA CHANGE THIS LATER

    def buildTree(self):
        current = self.head
        #finds max index that has children,assigns them
        max = math.floor(len(self.list)/2)
        for i in range(0,max,1):
            nextLeft = (i*2)+1
            nextRight = (i*2)+2
            current.left = self.searchIndex(nextLeft)
            current.right = self.searchIndex(nextRight)
            current = current.nextNode



    def __repr__(self):
        return("Will fix later")


    def printTree(self):
        """Prints based on the python standard list-version of the tree"""
        count = 0
        depth = 0
        for i in range(0, len(self.list), 1):

            # if is power of two then new line

            # changes the depth of the heap to show order of the heap, right now the whole thing is simply visual
            # but I will have to build a node-based binary tree soonTM

            print(self.list[i], end=" ")
            count += 1
            if count == depth * 2:
                print("\n")
                depth *= 2
                count = 0
            elif depth == 0:
                print("\n")
                depth += 1
                count = 0

    def getBranches(self,index):
        #Only works with head for now
        current = self.head
        return(current.left.data,current.right.data)



"""Test values to create a tree"""
tree = BST()
val = 0
for i in range(0,15,1):
    #val = random.randrange(0,100,1)
    tree.add(i)

tree.buildList()
tree.buildTree()
print(tree.printData(tree.searchIndex(5)))

for j in range(0,len(tree.list),1):

    print(tree.printAllValues(tree.searchIndex(j)))