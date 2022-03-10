import copy
import random
from linked_list import LinkedList


"""
Merge_sort, divide, merge
"""
def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    Resursively divide the linked list ino sublists containing a single node
    Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.size() == None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):

    """
    Divide unsorted list at midpoint
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)     # -1 because size returns one value higher
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None


        return left_half,right_half

def merge(left,right):
    """
    Function merges two linked lists, sorting by data in the nodes
    Returns a new merged list
    """

    #create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    #adds fake head that's discarded later
    merged.add(0)

    #set current = head
    current = merged.head

    #obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    #iterate over left and right as until they reach the tail node of either
    while left_head or right_head:
        #if head node of left is none, past tail
        #add node from right to merged linked list
        if left_head == None:
            current.next_node = right_head
            #call next on right to set loop condition to false
            right_head = right_head.next_node

        #if head node at right is none, we're past the tail
        #add tail from left to merged linked list
        elif right_head == None:
            current.next_node = left_head
            #call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            #not at either tail node, obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            #if data on left is less than right, set current to left node

            if left_data < right_data:
                current.next_node = left_head
                #move left head to next node
                left_head = left_head.next_node
            #opposite happens here
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        #move current to next node
        current = current.next_node

    #discard fake head, set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

#uses copy.deepcopy() to create an entirely new object because this function uses the .remove() operator
#in order to parse through the list. A non-destructive version of this operation is likely(almost certainly)
#possible
def verify_sorted_ll(linked_list):
    test_list = copy.deepcopy(linked_list)
    size = test_list.size()
    if size == None or size == 0 or size == 1:
        return True

    current = test_list.head
    cur_data = current.data
    next = test_list.head.next_node
    next_data = next.data

    #print("cur data",cur_data)
   # print(next_data)

    #if current data is less than next data then its true, move current up one node
    if cur_data <= next_data:
        test_list.remove(cur_data)
        return verify_sorted_ll(test_list)
    else:
        return False


l = LinkedList()
for i in range(1,10,1):
    l.add(random.randrange(1,100))
q = copy.deepcopy(l)

print(l)
print(l.size())
print("Is sorted?", verify_sorted_ll(l))

q = merge_sort(q)
print(q)
print(q.size())
print("Is sorted?", verify_sorted_ll(q))



