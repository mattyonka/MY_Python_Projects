import random
#import string

"""I'm going to be testing graph (dict) algorithms to find path of least or highest values when adding all nodes.
Ex. 1 - 2 - 3 
     \     /
        4   
        
    Highest val from 1 to 3 would be 1, 4,3 for 8 and lowest = 1,2,3 for 6 
    
    This program should also be able to report distance (aka number of hops) from point of origin
    """

class Node:
    def __repr__(self):
        #returns values of the node in string format
        return str(self.data)

    #name for diagraming purposes
    def __init__(self,data,name):
        self.data = data
        self.name =name

    def value(self):
        #returns integer value of node data
        return self.data




def addThenNext(graph,count,numSteps,current,desired,path):

    """This function takes the parameters graph, count,numSteps,current,desired and iterates from
    current to desired nodes, then prints out (could return if want) count and numSteps"""

    if current!= desired:
        #if branch, pick a branch and push back through this function
        if type(graph.get(current)) == None:
            return
        elif type(graph.get(current)) == list:
            #print("Length = ", len(graph[current]))
            #used to assign branching paths where tempCurrent is the branching point
            #ex a-b
            #   \-c
            #    \-d
            #
            #In this case a would be the branching(tempCurrent) point to b, c and d
            #same applies to tempSteps and tempCount
            tempCurrent = current

            for i in range(0, len(graph[current]), 1):
                #have to use copy assignment when reassigning lists, otherwise it just counts as a pointer
                tempPath = path.copy()
                tempCount = count
                tempSteps = numSteps

                #handling exemptions
                tempNode = graph.get(tempCurrent)
                if tempNode == None:
                    return

                current = tempNode[i]
                tempPath.append(current.name)
                tempCount += current.data
                tempSteps += 1
                addThenNext(graph,tempCount,tempSteps,current,desired,tempPath)

        else:
            current = graph.get(current)
            if current == None:
                return
            count+=current.data
            numSteps +=1
            path.append(current.name)
            addThenNext(graph,count,numSteps,current,desired,path)
    else:
        print("Count:",count,"\n NumSteps:",numSteps)
        print("Path:",path)



def simpleTest():
    ####This is a test path for a simple branching graph with NO dead ends
    #a-b-c
    # \ /
    #  d
    a = Node(1,"a")
    b = Node(2,"b")
    c = Node(3,"c")
    d = Node(4,"d")
    graph = {a:[b,d],b:c,d:c}

    #Assigned start and stop points
    head = a
    desired = c

    #necessary pre-assignments
    current = head
    count = head.data
    numSteps = 0
    path = [current.name]

    #execution
    addThenNext(graph,count,numSteps,current,desired,path)

def deadEndTest():
    ####This is a test path for a simple branching graph with a dead end
    #a-b-c
    # \
    #  d
    a = Node(1,"a")
    b = Node(2,"b")
    c = Node(3,"c")
    d = Node(4,"d")
    graph = {a:[b,d],b:c}

    #Assigned start and stop points
    head = a
    desired = c

    #necessary pre-assignments
    current = head
    count = head.data
    numSteps = 0
    path = [current.name]

    #execution
    addThenNext(graph,count,numSteps,current,desired,path)

def moreValuesTest():
    ####This is a test path for a two-branch graph with 3 possible paths and NO dead ends
    #a-b-c
    # \ \  \
    #  e----d
    a = Node(1,"a")
    b = Node(2,"b")
    c = Node(3,"c")
    d = Node(4,"d")
    e = Node(5,"e")
    graph = {a:[b,e],b:[c,d],c:d,e:d}

    #Assigned start and stop points
    head = a
    desired = d

    #necessary pre-assignments
    current = head
    count = head.data
    numSteps = 0
    path = [current.name]

    #execution
    addThenNext(graph,count,numSteps,current,desired,path)



print("*** Simple test ***")
simpleTest()
print("\n*** Dead-end test ***")
deadEndTest()
print("\n*** More Values test ***")
moreValuesTest()
"""


a = Node(1,"a")
b = Node(2,"b")
c = Node(3,"c")
d = Node(4,"d")
graph = {a:[b,d],b:c}

graph.get(d)
"""