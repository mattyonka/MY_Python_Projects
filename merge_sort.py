import math

def merge_sort(list):
    """
    Sorts a list in ascending order, and returns a new sorted list.
    Divide: find midpoint of a list and divide into sublists
    Conquer: recursively sorts the sublists created in previous step
    combine: merge the sorted sublists created in previous step

    O k*n log(n)
    """
    if len(list) <= 1:
        return(list)

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide unsorted list at midpoint into sublists left and right
    O k log(n)
    """
    left = []
    right = []
    mid = len(list)//2         #Floor of len(list) divided by two
    """
    Could change this slice operation to not use python's built in program to reduce time complexity
    
    """
    left = list[:mid]       #from blank to midpoint( aka 0 to mid)
    right = list[mid:]
    return left,right

def merge(left,right):
    """
    merges two lists or arrays, sorting them in the process
    Returns a new merged list
    O (n)
    """

    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    #accounts for situations where list is odd
    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    """
    Checks
    """
    size = len(list)
    if size == 0 or size == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

"""For testing Purposes

test_array = [1,6,2,4,8,23,12,65]
new_array = merge_sort(test_array)


print(test_array)
print(new_array)

print(verify_sorted(test_array))
print(verify_sorted(new_array))

"""